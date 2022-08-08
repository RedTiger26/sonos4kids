from django.db import models
from soco import SoCo
from soco.plugins.sharelink import ShareLinkPlugin


class MusicCategory(models.Model):
    name = models.CharField(max_length=100)
    icon_url = models.URLField(blank=True, null=True)
    parent = models.ForeignKey('MusicCategory', on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.name

    def get_child_categories(self):
        return MusicCategory.objects.filter(parent=self)

    def get_child_items(self):
        return MusicItem.objects.filter(category=self)

    def get_child_count(self):
        return MusicCategory.objects.filter(parent=self).count() + MusicItem.objects.filter(category=self).count()


class MusicItem(models.Model):
    title = models.CharField(max_length=100)
    episode_no = models.PositiveIntegerField(blank=True)
    episode_count = models.PositiveSmallIntegerField(default=1)
    media_uri = models.CharField(max_length=100, blank=True, null=True)
    cover_url = models.URLField(blank=True, null=True)
    category = models.ForeignKey('MusicCategory', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.title


class SonosBox(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    ip_address = models.GenericIPAddressField()
    volume_max = models.PositiveSmallIntegerField()
    volume_step = models.PositiveSmallIntegerField()

    soco_device = None

    def __str__(self):
        return f"SONOS {self.name}"

    def init_soco(self):
        if self.soco_device is None:
            self.soco_device = SoCo(self.ip_address)

    def play(self):
        self.init_soco()
        self.soco_device.play()

    def pause(self):
        self.init_soco()
        self.soco_device.pause()

    def stop(self):
        self.init_soco()
        self.soco_device.stop()

    def change_volume(self, step):
        self.init_soco()
        if 0 <= self.soco_device.volume + step <= self.volume_max:
            self.soco_device.volume += step

    def increase_volume(self):
        self.change_volume(self.volume_step)

    def decrease_volume(self):
        self.change_volume(-self.volume_step)

    def get_current_volume(self):
        self.init_soco()
        return self.soco_device.volume

    def get_current_volume_pct(self):
        self.init_soco()
        return int(self.soco_device.volume / self.volume_max * 100)

    def get_current_track(self):
        self.init_soco()
        track_info = self.soco_device.get_current_track_info()
        return track_info['title']

    def get_current_artist(self):
        self.init_soco()
        track_info = self.soco_device.get_current_track_info()
        return track_info['artist']

    def play_item(self, music_item: MusicItem):
        self.init_soco()
        shp = ShareLinkPlugin(self.soco_device)
        self.soco_device.clear_queue()
        shp.add_share_link_to_queue(music_item.media_uri)
        self.play()

    def queue_item(self, music_item: MusicItem):
        self.init_soco()
        shp = ShareLinkPlugin(self.soco_device)
        shp.add_share_link_to_queue(music_item.media_uri)
        self.play()
