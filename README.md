# Node Docker Practice

## Docker commands
### General Docker Commands
#### Process State Commands
```
  docker ps       // Show all active containers
  docker ps -a    // Show all containers

```
### Images:
#### Build Image Commands
```
  docker build .                         // Build image
  docker build --tag [name_the_image] .  // Build image and name it

```
### Containers:
#### Run Container Commands
```
  docker run [image_hash]                                      // Start a new container based on image hash id
  docker run -p [external_port:internal_port] [image_hash]     // Start a new container based on image hash id and expose some ports
  docker run -p [external_port:internal_port] -d [image_hash]  // Start a new container based on image hash id and expose some ports detached mode
  docker start [container_id_name]                             // Start a container based on container id or name and expose some ports if in the orignal run command -p flag was used
  docker start -a [container_id_name]                          // Start a container based on container id or name in attach mode and expose some ports if in the orignal run command -p flag was used
  docker attach [container_id_name]                            // Attach terminal to a running container based on container id or name and expose some ports if in the orignal run command -p flag was used
  docker logs [container_id_name]                              // Check logs of container
  docker logs -f [container_id_name]                           // Check logs of container and turn on follow mode to attach / keep listing to the logs

```
#### Stop Container Commands
```
  docker stop [container_id_name]  // Stop container with given name (name found in process state)

```
