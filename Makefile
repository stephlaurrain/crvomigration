all: build

PROJECT=crvo
CONTAINER_NAME=prj_crvomigration_ctn
IMAGE_NAME=prj_crvomigration_img
DOCKER_USER=docker
REMOTE_ROOT=-w '/root'

start: 
	sudo service docker start

listctn: 
	docker container ls --all

listimg:
	docker image ls

rembash:
	docker exec -ti $(CONTAINER_NAME) bash

getip:
	docker inspect $(CONTAINER_NAME) | grep "IPAddress"

stop:
	docker stop $(CONTAINER_NAME)

stopall:
	docker stop $$(docker ps -q -a)

##cleaning
dri:
	docker rmi $$(docker images -q)

drmf: 
	docker rm -f $$(docker ps -q -a)

clnall: stopall drmf dri 
# prune

clnright:
	docker exec  $(REMOTE_ROOT) $(CONTAINER_NAME) bash -c '/root/install/clnright.sh'

reinit:
	docker exec  $(REMOTE_ROOT) $(CONTAINER_NAME) bash -c '/root/install/reinit.sh'

startbe:
	docker exec $(CONTAINER_NAME) bash -c "cd /root/backend && yarn start"

prune:
	docker builder prune -a

prunecache:	
	docker builder prune

erase: stopall
##	docker container rm ${CONTAINER_NAME} && docker rmi $(docker images "*${CONTAINER_NAME}*" -q)
	docker container rm ${CONTAINER_NAME} && docker image prune -a --filter "dangling=false"

#	docker container rm $(CONTAINER_NAME) && docker image rm $$(docker images '*$(CONTAINER_NAME)*')

# runmain:
# 	docker exec -ti $(REMOTE_ROOT)/code $(CONTAINER_NAME) 'npm run rest'
#
# launch
build:
	docker-compose build

up: clnright
	docker-compose up
upd: 
	docker-compose up -d

setpsswd:
	docker exec  $(REMOTE_ROOT)  $(CONTAINER_NAME) passwd docker

buildraw:
	docker build -t $(CONTAINER_NAME) ./docker/build
 

.FORCE: