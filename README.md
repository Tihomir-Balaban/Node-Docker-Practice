# Node Docker Practice

## Docker commands
### General Docker Commands
#### Process State Commands
```
docker ps                                                    // Show all active containers
docker ps -a                                                 // Show all containers

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
docker run -v [internal_path] [image_id]                     // Start a new container based on image id and add an Anonymous Volume
docker run -v [external_folder:internal_path] [image_id]     // Start a new container based on image id and add a Named Volume
docker run -v [ext_absolute_patj:internal_path] [image_id]   // Start a new container based on image id and add a Bind Mount

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
docker stop [container_id_name]                              // Stop container with given name (name found in process state)

```

#### Volume Commands
```
docker volume ls                                             // Lists all volumes
```

## Dockerfile
### FROM Keyword
```
FROM baseImage                                               // Base image like node for example
FROM baseImage:tag                                           // Base image with a version tag
FROM baseImage@digest                                        // Base image with a immutable version
FROM baseImage AS stage                                      // Base image given an allias for later FROM commands
FROM baseImage:tag AS stage                                  // Base image combineing tags and allias
FROM baseImage@digest AS stage                               // Base image combineing digest and allias

```
### COPY Keyword
```
COPY [source_path] [dest_path]                               // Copy file or directory from a external path to and internal container path
COPY --chown=user:group [source_path] [dest_path]            // Copy file or directory with flag for setting user and/or group permission
COPY --from=stage [source_path] [dest_path]                  // Copy file or directory with flag for coping file from a different stage aswell

```
### RUN Keyword
```
RUN [command]                                                // Run a shell command
RUN [command] [parameters]                                   // Run a shell command with a parameter
RUN [command] -[flags] [parameters]                          // Run a shell command with a parameter and flag

```
### EXPOSE Keyword
```
EXPOSE [port]                                                // Listen to port at runtime
EXPOSE [port]/[protocol]                                     // Listen to port at runtime and set protocol

```

### CMD Keyword
```
CMD [ "executable", "parameter", ... ]                       // Set the default executable and parameters for this executing container.
CMD [ "parameter", "parameter2", ... ]                       // Set the default parameters for this executing container. An ENTRYPOINT instruction must also be specified.
CMD [executable] [parameter] ...                             // The default executable for this executing container. Set the default executable and parameters for this executing container.

```
### VOLUME Keyword
```
# VOLUME [ "internal/path" ]                                 // Create anonymous volume

```