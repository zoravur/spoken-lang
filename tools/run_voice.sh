#!/usr/bin/env bash

BASEDIR=$(dirname "$0")
cd $BASEDIR
python ../whisper_streaming/whisper_online_server.py & \
arecord -f S16_LE -c1 -r 16000 -t raw -D default | nc localhost 43007 | python ../spock/main.py