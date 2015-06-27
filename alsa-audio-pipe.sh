#!/bin/sh

SOURCE_DEVICE=imic
DESTINATION_DEVICE=soundsticks

arecord -f S16_LE -r48000 -c2 -D ${SOURCE_DEVICE} -F0 --period-size=1024 -B0 --buffer-size=4096 | aplay -D ${DESTINATION_DEVICE}

