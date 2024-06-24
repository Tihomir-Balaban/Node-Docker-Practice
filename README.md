# Node Docker Practice

## Docker commands
#### Process State Commands
```
  docker ps       // Show all active containers
  docker ps -a    // Show all containers
```
#### Build Image Commands
```
  docker build .                         // Build image
  docker build --tag [name_the_image] .  // Build image and name it
```
#### Run Container Commands
```
  docker run [image_hash]                                   // Start a container based on image hash id
  docker run -p [external_port:internal_port] [image_hash]  // Start a container based on image hash id and expose some ports
```
#### Stop Container Commands
```
  docker stop [container_name]  // Stop container with given name (name found in process state)
```
