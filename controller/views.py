from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from controller.models import SonosBox, MusicCategory, MusicItem


def index(request):
    return HttpResponse("Hello World. This is the index.")


def box(request, box_slug):
    box_object = get_object_or_404(SonosBox, slug=box_slug)

    category = request.session.get('category')
    sub_category_list = MusicCategory.objects.filter(parent=category)
    music_item_list = MusicItem.objects.filter(category=category).order_by('episode_no')

    return render(request, 'controller/box.html', {'box': box_object, 'category_list': sub_category_list,
                                                   'item_list': music_item_list})


def box_category(request, box_slug, category_id):
    if category_id == 0:
        request.session['category'] = None
    else:
        category = get_object_or_404(MusicCategory, pk=category_id)
        request.session['category'] = category.id

    return HttpResponseRedirect(reverse('controller:box', args=(box_slug,)))


def action(request, box_slug, cmd):
    box_object = get_object_or_404(SonosBox, slug=box_slug)

    if cmd == 'play':
        box_object.play()
    elif cmd == 'pause':
        box_object.pause()
    elif cmd == 'stop':
        box_object.stop()
    elif cmd == 'vol_up':
        box_object.increase_volume()
    elif cmd == 'vol_down':
        box_object.decrease_volume()

    return HttpResponseRedirect(reverse('controller:box', args=(box_object.slug,)))


def item(request, box_slug, item_id):
    box_object = get_object_or_404(SonosBox, slug=box_slug)
    item_object = get_object_or_404(MusicItem, pk=item_id)

    if request.POST['action'] == 'play':
        box_object.play_item(item_object)
    elif request.POST['action'] == 'queue':
        box_object.queue_item(item_object)

    return HttpResponseRedirect(reverse('controller:box', args=(box_object.slug,)))


def item_play(request, box_slug, item_id):
    box_object = get_object_or_404(SonosBox, slug=box_slug)
    item_object = get_object_or_404(MusicItem, pk=item_id)

    box_object.play_item(item_object)

    return HttpResponseRedirect(reverse('controller:box', args=(box_object.slug,)))


def item_queue(request, box_slug, item_id):
    box_object = get_object_or_404(SonosBox, slug=box_slug)
    item_object = get_object_or_404(MusicItem, pk=item_id)

    box_object.queue_item(item_object)

    return HttpResponseRedirect(reverse('controller:box', args=(box_object.slug,)))