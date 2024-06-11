DC = docker compose
API_FILE = api/docker_compose/app.yaml
MEDIA_FILE = media/docker_compose/media.yaml
S3_FILE = media/docker_compose/s3.yaml
STORAGE_FILE = api/docker_compose/storage.yaml

.PHONY: app
app-start:
	${DC} -f ${API_FILE} up -d

.PHONY: drop-app
drop-app:
	${DC} -f ${API_FILE} down


.PHONY: all
all:
	${DC} -f ${API_FILE} -f ${STORAGE_FILE} up --build -d
	${DC} -f ${MEDIA_FILE} -f ${S3_FILE} up --build -d


.PHONY: drop-all
drop-all:
	${DC} -f ${API_FILE} -f ${STORAGE_FILE} down
	${DC} -f ${MEDIA_FILE} -f ${S3_FILE} down

.PHONY: storage
storage:
	${DC} -f ${STORAGE_FILE} up -d

.PHONY: drop-storage
drop-storage:
	${DC} -f ${STORAGE_FILE} down

.PHONY: storage-init
storage-init:
	${DC} -f ${STORAGE_FILE} exec server alembic revision --autogenerate -m "Init"


.PHONY: storage-upgrade-head
storage-upgrade-head:
	${DC} -f ${STORAGE_FILE} exec  server alembic upgrade head