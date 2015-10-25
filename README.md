# alsa-audio-pipe
Brain dead simple audio piper with ALSA

# What do I do with this?

This is simply my set up on a Raspberry Pi running Raspbian that allows
me to pipe in the audio in from a Griffin iMic USB audio dongle to a USB
Harmon Kardon Soundsticks speaker system.

Included is a python script that depends on python-alsasound that does the
equivalent of piping audio data from one device to another.

# Requirements

python-alsasound 0.8.2

```
sudo apt-get install python-dev libasound2-dev
git clone https://github.com/larsimmisch/pyalsaaudio
cd pyalsaaudio
python setup.py build
sudo python setup.py install
```

# Setup

```
cd ~
git clone https://github.com/liquidx/alsa-audio-pipe.git
cd alsa-audio-pipe
sudo make install  # installs script in to /etc/init.d/alsa-audio-pipe
sudo chkconfig --add alsa-audio-pipe
```

# Starting and stopping the service

```
# start the alsa-audio-pipe
sudo service alsa-audio-pipe start
# Stop the alsa-audio-pipe
sudo service alsa-audio-pipe stop
```

# Audio Setup

ALSA just works straight out of the box once you install everything, I made some additional changes to ```/etc/asound.conf``` to point to alias the devices to order-independent names:

```
# This will create an ALSA card named 'soundsticks' that maps to the SoundSticks card's PCM
pcm.soundsticks {
  type hw
  card "SoundSticks"
  device 0
}

# This will create an ALSA card named 'imic' that maps to the Griffin iMic PCM
pcm.imic {
  type hw
  card "system"
  device 0
}

# Default to SoundSticks as the default audio device.
defaults.pcm.!card "SoundSticks"
defaults.ctl.!card "SoundSticks"
```

Adjust volume

```
alsamixer
```

Store and copy volume for next restart

```
sudo alsactl store
sudo cp /var/lib/alsa/asound.state /etc/asound.state
```
