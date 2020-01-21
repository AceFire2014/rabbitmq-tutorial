.PHONY: bash build build-img clean run test

IMG=andytsai/rabbitmq-tutorial-2-work-queues
export TAG ?= $(shell git rev-parse --abbrev-ref HEAD)

RUNDOCKER=docker run --rm --network=rabbitmq-tutorial_default -v $(shell pwd):/app

run: build-img
	$(RUNDOCKER) $(IMG):$(TAG) /app/run --reload

test: COV_REPORT ?= html
test: build-dev
	$(RUNDOCKER) -e COV_REPORT=$(COV_REPORT) $(IMG):$(TAG)

bash: build-img
	$(RUNDOCKER) -it $(IMG):$(TAG) "bash"

# https://www.technovelty.org/tips/the-stamp-idiom-with-make.html
build: build-img

build-img: build/build-img-stamp
build/build-img-stamp: build/Dockerfile requirements.txt
	docker build -t $(IMG):$(TAG) -f build/Dockerfile .
	@touch $@

push: build/push-stamp
build/push-stamp: build/build-img-stamp
	docker push $(IMG):$(TAG)
	@touch $@

clean:
	@docker rmi -f $(IMG):$(TAG) || true
	@rm -f build/build-img-stamp build/push-stamp
