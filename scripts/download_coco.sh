#!/usr/bin/env bash
set -e

mkdir -p data/images data/annotations tmp
cd tmp

wget -c http://images.cocodataset.org/zips/val2017.zip
wget -c http://images.cocodataset.org/annotations/annotations_trainval2017.zip

unzip -o val2017.zip -d ../data/images/
unzip -o annotations_trainval2017.zip -d ../data/

rm -rf ../tmp
