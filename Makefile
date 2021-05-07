MKDOCS=mkdocs # python3 -m mkdocs

serve:
	$(MKDOCS) serve
.PHONY: serve

build:
	$(MKDOCS) build
.PHONY: build

publish: build
	sudo rsync -ru site/ /var/www/html/kyzjnbk/
