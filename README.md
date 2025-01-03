# jlgenerator
JLSpeech package generator

## Installation:
Use whatever python package manager you want, but don't ask me to support it.

Make sure you've got an appropriate virtualenv tool installed (as for package manager, same rules apply).

### Using vanilla virtualenv and pip:
```shell
user@machine ~ $ virtualenv -p python3 .venvs/jlsgenerator/
user@machine ~ $ source .venvs/jlsgenerator/bin/activate
(jlsgenerator) user@machine ~ $ git clone https://github.com/bitswalk/jlsgenerator.git
(jlsgenerator) user@machine ~ $ cd jlsgenerator
(jlsgenerator) user@machine ~/jlgenerator/ $ chmod +x ./jlsgenerator.py
(jlsgenerator) user@machine ~/jlgenerator/ $ pip install -r requirements.txt
```

## Usage:
This dirty script comes with a self explanatory CLI helper, if you wanna know which options are available use `jlsgenerator.py -h` command.
