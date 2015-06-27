# alsa-audio-pipe
Brain dead simple audio piper with ALSA

# What do I do with this?

This is simply my set up on a Raspberry Pi running Raspbian that allows
me to pipe in the audio in from a Griffin iMic USB audio dongle to a USB
Harmon Kardon Soundsticks speaker system.

Included is a simple shell script that uses the vanilla ALSA aplay and ALSA arecord to pipe the audio in user-space, and an rc-init script.

# Setup

```
cp alsa-audio-pipe.sh /home/pi/alsa-audio-pipe
sudo cp alsa-audio-pipe /etc/init.d/alsa-audio-pipe
sudo chkconfig on alsa-audio-pipe
```

# Audio Setup

ALSA just works straight out of the box once you install everything, I made some additional changes to ```/etc/asound.conf``` to point to alias the devices to order-independent names:

```
pcm.soundsticks {
  type hw
  card "SoundSticks"
  device 0
}

pcm.imic {
  type hw
  card "system"
  device 0
}

# Default to SoundSticks as the default audio device.
defaults.pcm.!card "SoundSticks"
defaults.ctl.!card "SoundSticks"
```



