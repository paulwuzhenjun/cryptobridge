tag=$1
image_name="coinrising/cryptobridge:$tag"

docker build -t $image_name .
docker push $image_name
