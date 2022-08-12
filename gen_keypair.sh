#!/bin/sh
openssl genrsa -des3 -out .private.pem 2048
openssl rsa -in .private.pem -outform PEM -pubout -out .public.pem
cp .public.pem ./includes
nuitka3  --standalone  --onefile --include-data-dir=./includes stockholm.py
# tar -czvf stockholm.tar.gz ./stockholm_src
