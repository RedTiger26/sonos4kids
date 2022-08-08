# sonos4kids
A simple webinterface for Sonos music boxes. Give your kids control over their personal box with selected music files and fine-grained control.

## Project idea
The idea of this project is to provide a simple webinterface for controlling Sonos music boxes. Placing one of them in your child's room together with Spotify premium gives them a ton of music and stories to listen and laugh. But the official Sonos app is not suitable for children: Neither do you want them to access all the Spotify music database nor should they be able to select any Sonos box in your home (given that you have more than one).

So this projects offers a webinterface that allows the control of one predefined box and only gives access to a preselected libary of music or stories.

## Architecture
The project is build with Django and Django templates. In addition Bootstrap 5 is used to do most of the styling work. The soco python libary is used to control the Sonos box. Everything is put together in docker image for easy deployment on a local raspberry pi, NAS or other home server you have at hand. For your kids just take an old Android tablet and put it in kiosk mode and place the fixed link on the home screen, and you're done.

## Status
This project is not yet fully functional, but as the creation of the docker image needs a GitHub repo, the first steps are already pushed here. Stay tuned for updates in the future.
