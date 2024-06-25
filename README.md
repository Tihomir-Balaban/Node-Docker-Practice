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
docker build .                                               // Build image
docker build -t [name_the_image] .                           // Build image and name it
docker build -t [name_the_image:tag] .                       // Build image and name it and add tag

// Remove Image
docker rmi [image_id_name_name:tag]                          // Delete image
docker image prune                                           // Deletes all unused images

// Image
docker images                                                // Show a list of all images
docker image inpect [image_id_name_name:tag]                 // Image detailed information

// Push & Pull
docker push [image_id_name]                                  // Push docker image to docker hub repo
docker push [host]:[image_id_name]                           // Push docker image to 3de party host repo
docker pull [image_id_name]                                  // Pull docker image from docker hub repo
docker pull [host]:[image_id_name]                           // Pull docker image from 3de party host repo

```
### Containers:
#### Run Container Commands
```
// Run (can also be run with given image [name] or [name:tag] combo instead [of image_id])
docker run [image_id]                                        // Start a new container based on image id
docker run -p [external_port:internal_port] [image_id]       // Start a new container based on image id and expose some ports
docker run -d [image_id]                                     // Start a new container based on image id and expose some ports detached mode 
docker run -it [image_id]                                    // Start a new container based on image id and uses interactive mode and terminal mode
docker run --rm [image_id]                                   // Start a new container based on image id and container will be remove automatically
docker run --name [image_id]                                 // Start a new container based on image id and name it

// Start
docker start [container_id_name]                             // Start a container based on container id or name and expose some ports if in the orignal run command -p flag was used
docker start -a [container_id_name]                          // Start a container based on container id or name in attach mode and expose some ports if in the orignal run command -p flag was used
docker start -i [container_id_name]                          // Start a container based on container id or name and uses interactive mode

// Attach
docker attach [container_id_name]                            // Attach terminal to a running container based on container id or name and expose some ports if in the orignal run command -p flag was used

// Copy
docker cp [path] [container_name:/path]                      // Copy path to container path
docker cp [container_name:/path] [path]                      // Copy container path to path

// Logs
docker logs [container_id_name]                              // Check logs of container
docker logs -f [container_id_name]                           // Check logs of container and turn on follow mode to attach / keep listing to the logs

// Remove
docker rm [container_id_name]                                // Delete container that isn't running

```
#### Stop Container Commands
```
docker stop [container_id_name]  // Stop container with given name (name found in process state)

```
