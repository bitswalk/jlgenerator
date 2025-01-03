# jlgenerator
JLSpeech package generator

## Installation:
Use whatever python package manager you want, but don't ask me to support it.
Make sure you've got an appropriate virtualenv tool installed (as for package manager, same rules apply).

### Using vanilla virtualenv and pip:
```shell
user@machine ~ $ virtualenv -p python3 .venvs/jlgenerator/
user@machine ~ $ source .venvs/jlgenerator/bin/activate
(jlgenerator) user@machine ~ $ git clone https://github.com/bitswalk/jlgenerator.git
(jlgenerator) user@machine ~ $ cd jlgenerator
(jlgenerator) user@machine ~/jlgenerator/ $ chmod +x ./jlgenerator.py
(jlgenerator) user@machine ~/jlgenerator/ $ pip install -r requirements.txt
```

## Usage:
This dirty script comes with a self explanatory CLI helper, if you wanna know which options are available use `jlgenerator.py -h` command.
