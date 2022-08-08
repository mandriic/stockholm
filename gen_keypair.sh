#!/bin/sh
openssl genrsa -des3 -out .private.pem 2048
openssl rsa -in .private.pem -outform PEM -pubout -out .public.pem
pyinstaller --onedir stockholm.py
mkdir ./stockholm_src
cp -r ./dist/stockholm/* ./stockholm_src/
cp ./.public.pem ./stockholm_src
cp ./.list_extenc_wannacry.txt ./stockholm_src
cp -r ./.src ./stockholm_src
tar -czvf stockholm.tar.gz ./stockholm_src
