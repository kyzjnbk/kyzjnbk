MKDOCS=mkdocs # python3 -m mkdocs

serve:
	$(MKDOCS) serve
.PHONY: serve

build:
	$(MKDOCS) build
.PHONY: build

publish:
	sudo rsync -ruv site/ /var/www/html/kyzjnbk/
.PHONY: publish

