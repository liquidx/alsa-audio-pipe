#!/usr/bin/python
#
# Equivalent to:
#
# arecord -f S16_LE -r48000 -c2 -F0 --period-size=1024 -B0 --buffer-size=4096 \
#    -D ${SOURCE_DEVICE} | aplay -D ${DESTINATION_DEVICE}
#
# But instead, this will run as a single executable that is not the same as
# aplay.

import alsaaudio
import argparse


def pipe(in_card, out_card, channels=2, rate=48000, periodsize=128):
  format = alsaaudio.PCM_FORMAT_S16_LE
  in_device = alsaaudio.PCM(alsaaudio.PCM_CAPTURE, alsaaudio.PCM_NORMAL, card=in_card)
  in_device.setchannels(channels)
  in_device.setrate(rate)
  in_device.setformat(format)
  in_device.setperiodsize(periodsize)

  out_device = alsaaudio.PCM(alsaaudio.PCM_PLAYBACK, card=out_card)
  out_device.setchannels(channels)
  out_device.setrate(rate)
  out_device.setformat(format)
  out_device.setperiodsize(periodsize)

  while True:
    length, buf = in_device.read()
    if length:
      out_device.write(buf)


if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument('--input', '-i', help='Input card name')
  parser.add_argument('--output', '-o', help='Output card name')
  args = parser.parse_args()

  pipe(args.input, args.output)
