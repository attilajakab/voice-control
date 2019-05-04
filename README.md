# Simple voice control
This is a simple Python 3.6 project to try out speech recognition and text-to-speech libraries.   

## Prerequisites for Mac OS (Sierra)

 - Python3.6
 - [portaudio](http://www.portaudio.com/) (cross-platform, open-source, audio I/O library)
```
$ brew install portaudio
```

## Setup
In the root folder execute:   
```
$ python3.6 -m venv env   
$ source env/bin/activate   
$ pip3.6 install -r requirements.txt
```

## Run the program
```
$ python3.6 app.py
```
Currently the program listens to three commands listed in `io_text.py` under the `Input` section.   
To run the program in the background run it with `nohup` and `&`:
```
$ nohup python3.6 app.py &
```
