# BrainRot Gen

This is a simple BrainRot generator. It currently is designed to make those weird videos. You supply videos to it and text to it and it will generate an output video from it.

Currently it is functioning at: [Firebase](). ***Please*** try to be soft with my server, it's not free for me.

## Run for yourself:
The following will work in Linux, and should work pretty similarly in Windows (I am using a VPS so other people can use it):
Requires:
    - Docker


```bash
cd Backend
docker build -t brainrotgen .
docker run -d -p 5000:5000 brainrotgen # -d is optional, it runs everything "detached" so you can close the terminal
```
You can then find a webserver of your liking (I've been using the built in WebStorm webserver) and open the index.html file

To spin down the docker container, if you didn't run with `-d`, then you can just close the terminal. If you did, then you can run `docker ps` to find the container id and then `docker stop <container id>` to stop it.






### Currently it does not support the AI features, as I'm having problem with my credits, but it will when I fix those. On my computer the AI works.