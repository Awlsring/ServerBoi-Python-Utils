#!/bin/bash
mkdir -p ./python/lib/python3.8/site-packages

pip3 install . -t ./python/lib/python3.8/site-packages

zip -r serverboi_utils.zip python/

rm -rf python

mv serverboi_utils.zip ../ServerlessBoi/lambdas/layers/serverboi_utils/serverboi_utils.zip