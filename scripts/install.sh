#!/bin/bash
git clone https://github.com/iewnfod/ChatTTS-Web --depth 1 --recursive
cd ChatTTS-Web
python3 -m venv .venv

echo "Use ChatTTS-Web/scripts/run.sh to run the project."
