# voice-assistant
Developing voice assistant using python to make day to day life easy like creating architecture diagram, sending emails, write notes , listen news and many more

# create any directory <dir name>
# do cd <dir name>

# First install git 
# git clone https://github.com/nigamreetesh84/voice-assistant.git 
# cd voice-assistant
# 

#Open command terminal and type

python -m venv git_env

git_env\Scripts\activate

#should be look like below
# (git_env) C:\mydev\test\voice-assistant>

#Install pipwin first for pyaudio
python -m pip install pipwin

#Install pyaudio 
pipwin install PyAudio==0.2.11

#install module 
python -m pip install -r requirements.txt

# if pyaudio fails then please follow below steps:
find your Python version by python --version mine is 3.7.3 for example
PyAudio-0.2.11-cp37-cp37m-win_amd64
find the appropriate .whl file from here, for example mine is PyAudio‑0.2.11‑cp37‑cp37m‑win_amd64.whl, and download it.
