MKDOCS=mkdocs # python3 -m mkdocs

serve:
	$(MKDOCS) serve

build:
	$(MKDOCS) build

publish:
	rsync -ru site /var/www/html/kyzjnbk