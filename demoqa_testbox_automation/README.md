### Run tests

```sh
pip install -r requirements.txt
python -m unittest tests/test_text_box.py -v

```


### Docker for Jenkins

```sh
docker network create jenkins-net

docker volume create jenkins_home

docker run -d \
  --name jenkins \
  --restart unless-stopped \
  --network jenkins-net \
  -p 8080:8080 -p 50000:50000 \
  -v jenkins_home:/var/jenkins_home \
  -v /var/run/docker.sock:/var/run/docker.sock \
  jenkins/jenkins:lts

  docker exec jenkins cat /var/jenkins_home/secrets/initialAdminPassword

```
### Setup node on macbook due to some issues on M series chip

```sh 

 docker exec -it jenkins -u root bash 

 pip install -r requirements.txt --break-system-packages

 apt-get install -y python3 python3-pip

apt-get update && apt-get install -y \
    chromium chromium-driver curl unzip git \
    && pip install selenium pytest
    
```