## Used Commands

### To Build a docker image
`docker build .`

### To run/create the container
`docker run -p *PORT*:*PORT* *image-code*`
The second port means one mentioned in the docker file and our code, the first one is the port it is mapped to in the local machine.

### View all running docker processes/containers
`docker ps`
`docker ps -a` - all containers including stopped in the past

### To stop the container
`docker stop *docker-container-name*`

### To restart a stopped container
`docker start *name-or-id*`
However, this is different to that launched with docker run command. This container process runs in the background and does not obstruct the terminal. This means we do not see what we console logged in the terminal via the code. So, we're not listening at the console. This is detached mode that is default for `docker start` whereas attached mode in default for `docker run`

Can run detached mode with `docker run -d` as well.
Can run attached mode with `docker start -a` as well.

### Attach terminal to a running container
`docker attach *container-name*`

### Fetch logs printed by a container
`docker logs *container-name*`
Useful to see logs for a detached container.
`-f` flag with this command will allow logs viewed in real time, i.e. similar to attaching.


