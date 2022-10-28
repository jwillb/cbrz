# cbrz
A dead simple Python script to convert .cbr book files to .cbz

## Information
I created this script because my eReader doesn't support .cbr files, because it isn't an open format. This terminal program (currently Linux only) decompresses the files and recompresses them using ```zip``` to create .cbz files. There are other scripts that do this but they are quite outdated and overcomplicated for the vast majority of use cases.

## Usage
- Download ```zip``` and ```unrar```, preferably through your package manager. NOTE: Debian users may have to download unrar-nonfree and change the command inside of the program (TODO: Make command changing simpler)
- Ensure Python is installed, customize the variables to your liking, and run the program with ```python3 main.py``` (No external libraries are needed).
