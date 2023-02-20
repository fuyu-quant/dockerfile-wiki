option=$1

if [ $option = up ]; then
    # start container
    docker compose -f /Users/tanakatouma/vscode/ds_mlops/docker-compose.yml up -d
elif [ $option = force ]; then
    # rebuild the docker image and start container
    docker compose -f /Users/tanakatouma/vscode/ds_mlops/docker-compose.yml up -d --force-recreate
elif [ $option = down ]; then
    # stop container
    docker compose -f /Users/tanakatouma/vscode/ds_mlops/docker-compose.yml down -v
elif [ $option = rm ]; then
    # stop the container and delete the image
    docker compose -f /Users/tanakatouma/vscode/ds_mlops/docker-compose.yml down -v --rmi all
else
    echo "Command is wrong"
fi