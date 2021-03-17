tag=$1
image_name="coinrising/cryptobridge:$tag"

docker -H hkgw.uranome.com:2375 build -t $image_name .
docker -H hkgw.uranome.com:2375 push $image_name
