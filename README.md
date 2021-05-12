# dCampTokyo2020

## IMPORTANT UPDATE

A standalone app version has been released on [https://moodchecker.app/](https://moodchecker.app/).

Repo is open source [here](https://github.com/ideo/mood-checker)

## About

Workshop tools for d.camp Tokyo 2020

### Mood Checker

The campers can adjust the sliders any time during the day to show how they are feeling using the slider.

### Remote High Five

The campers can turn on the camera through this web app to show their location of their hand.
The location of other campers' hands are superimposed on the camera view, and if they are
aligned it creates a high five sound.

## How To Use

This app consists of a _facilitator view_ and a _participant view_.

### Facilitaor view

This is the server. Deploy this repo to Heroku (without the `/client` and `/log` directory). The [Socket.io](https://socket.io/) server would start when you access the page. You can also log the received sockets by locally running `/log/log.py`.

### Participant view

This is the client. Host the `/client` directory to a server of your choice. If the Facilitator view server is up and running, the Participant view would automatically connect to the server and start sending values. You can distribute the Participant view URL to your audience.
