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
// Build
docker build .                         // Build image
docker build --tag [name_the_image] .  // Build image and name it
docker build -t [name_the_image] .     // Build image and name it

// Remove Image
docker rmi [name_the_image]            // Delete image
docker image prune                     // Deletes all unused images

// Image
docker images                          // Show a list of all images
docker image inpect [image_id_name]    // Image detailed information

```
### Containers:
#### Run Container Commands
```
// Run
docker run [image_hash]                                      // Start a new container based on image hash id
docker run -p [external_port:internal_port] [image_hash]     // Start a new container based on image hash id and expose some ports
docker run -p [external_port:internal_port] -d [image_hash]  // Start a new container based on image hash id and expose some ports detached mode
docker run -i -t [image_hash]                                // Start a new container based on image hash id and uses interactive mode and terminal mode
docker run -it [image_hash]                                  // Start a new container based on image hash id and rest same as above
docker run -rm [image_hash]                                  // Start a new container based on image hash id and container will be remove automatically

// Start
docker start [container_id_name]                             // Start a container based on container id or name and expose some ports if in the orignal run command -p flag was used
docker start -a [container_id_name]                          // Start a container based on container id or name in attach mode and expose some ports if in the orignal run command -p flag was used
docker start -i [container_id_name]                          // Start a container based on container id or name and uses interactive mode

// Attach
docker attach [container_id_name]                            // Attach terminal to a running container based on container id or name and expose some ports if in the orignal run command -p flag was used

// Logs
docker logs [container_id_name]                              // Check logs of container
docker logs -f [container_id_name]                           // Check logs of container and turn on follow mode to attach / keep listing to the logs

// Remove
docker rm [container_id_name]                               // Delete container that isn't running

```
#### Stop Container Commands
```
docker stop [container_id_name]  // Stop container with given name (name found in process state)

```
