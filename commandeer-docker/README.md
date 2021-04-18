# Running Commandeer on Docker

Commandeer seems to be GUI option for localstack.  

Commandeer has both open source and paid solution.  The open source solution seems to be not so much open source.  There are literally no proper tutorials to install them.
The only option is to do subscript for free trail and don't renew for full account.

Another alternate option is to do linux debian package installation.  This route is really painful.  If this is what you need use this notes as guidance.
Before you start, if you running environment is mac like me.  Just stop here and find alternative solution.  This is my conclusion after spending a day trying to make it work.


## linux option

1. Commandeer is available on linux/debina via Snap package only.  Go here and get the latest version.
https://snapcraft.io/commandeer

If you are running linux, awesome.  Install snap and get the commandeer installed.  Hope the app works for you out of the box.

I'm using mac, so this is not an option for me.

## mac option

I choose to install via Ubuntu docker.  On the outset it might look simple, reality is a different game.

1. Running snap on a ubuntu docker is not easy.  Its is a nightmare.  Read these articles will help you if you are lost.
    * Refer:
        * https://forum.snapcraft.io/t/snapd-in-docker/177 -- discussion
        * https://github.com/ogra1/snapd-docker -- took the above version and cleaned up a bit
1. After you have a docker with snap that is working, you have to manually install commandeer.  No way to automate this at this time.
1. Last part, running gui application docker wont work with mac easily.
    * Need to install something call socal(connects between docker container to mac's Xwindows client) & xquartz(Xwindows client).
    * This solution is too slow
    * I was not able to seen see proper gui after spending a day on this.
    * Refer:
        1. https://cntnr.io/running-guis-with-docker-on-mac-os-x-a14df6a76efc?gi=75286c1ee84c#:~:text=We%20are%20very%20familiar%20with,with%20Docker%E2%80%A6%20on%20OS%20X!
        1. https://medium.com/@dimitris.kapanidis/running-gui-apps-in-docker-containers-3bd25efa862a

If you are desparate to try this method.  Start from my version should be better than both the articles.

### 1. Running snap on ubuntu docker container

1. Use the files under commandeer-docker folder.  Dockerfile use ubuntu image and installs snap.
1. Add this section to the docker container.  This enables mac to connect to snap based ubuntu.  After this step only you'd be allowed to installed apps.
    ```
    commandeer-ui:
        container_name: "commandeer-base"
        build:
          context: ./commandeer-docker
        image: localstack/commandeer-base
        # hostname: commandeer
        networks:
          - localstack-net
        # ports:
        environment:
          - DISPLAY=${DOCKER_GATEWAY_HOST:-192.168.1.10}:0
          # - DISPLAY=$$(ifconfig en0 | grep "inet " | cut -d " " -f2):0  # HOST IP -- Too bad compose does not all scripts
        cap_add: 
          - SYS_ADMIN
          # - NET_ADMIN
        ipc: host
        privileged: true
        stdin_open: true
        tty: true
        devices:
          - /dev/fuse
        security_opt:
          - seccomp:unconfined
          - apparmor:unconfined
        volumes:
          - "/var/run/docker.sock:/var/run/docker.sock"
          - "/sys/fs/cgroup:/sys/fs/cgroup:ro"
          - "/lib/modules:/lib/modules:ro"
        tmpfs: 
          - /run
          - /run/lock
          - /tmp
    ```
1. Start the compose.  This will start the docker with snap installed.  

    Run this command to see if snap install is working for you.  If not triage before proceeding further.  Refer the docs above if needed.
    ```
    make up
    (or)
    docker compose up

    docker exec -ti commandeer-base snap version
    ```


### 2. Manually install Commandeer on Linux
1. Install the commandeer
    ```
    docker exec -ti commandeer-base snap install commandeer
    ```
1. Confirm the package is installed in your docker container
    ```
    docker exec -ti commandeer-base snap list
    ```
1. Check the docker environment has your mac's ip address.  Compare with mac by running command ==> `echo $(ifconfig en0 | grep "inet " | cut -d " " -f2):0`
    ```
    docker exec -ti commandeer-base env | grep DISPLAY
    ```


### 3. Enable docker container to display gui app in mac
1. Need to install 2 applications
    ```
    brew install socat
    brew install xquartz
    ```
1. Run the pipe app to run in background
    ```
    socat TCP-LISTEN:6000,reuseaddr,fork UNIX-CLIENT:\"$DISPLAY\" &
    ```
1. Change XWindows security options.  Run the command.  Go to Xquartz->Preference->Security->Enable option: Allow connections from clients.
    ```
    open -a Xquartz
    ```
1. Last step, run the commandeer ui tool
    ```
    docker exec -ti commandeer-base commandeer
    ```

### 4. Other info
I also stumbled on another direct link to install via debian package.  Unfortunately these do not work with ubuntu 20.04.  It may work in older instances, did not get a chance to test this.
```
wget https://commander-releases.s3-us-west-1.amazonaws.com/Commandeer_0.3.3_amd64.deb
wget https://commander-releases.s3-us-west-1.amazonaws.com/Commandeer_1.0.0_amd64.deb
dpkg -i Commandeer_1.0.0_amd64.deb -- install failed pkg conflicts; try older version of ubuntu
```


## Additional References:
1. https://docs.docker.com/compose/compose-file/compose-file-v3/#compose-documentation
1. https://docs.getcommandeer.com/blog/latest/commandeer-version-1-0-available-now-on-the-linux-snap-store/
1. https://www.apress.com/gp/blog/all-blog-posts/developing-for-aws-docker/18515442
1. https://anthony-f-tannous.medium.com/using-commandeer-as-a-front-end-console-for-aws-local-resources-32c26b290d39
