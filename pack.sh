#!/bin/bash
mkdir -p ./python/lib/python3.8/site-packages

pip3 install serverboi_utils -t ./python/lib/python3.8/site-packages

zip -r serverboi_utils.zip python/

rm -rf python
