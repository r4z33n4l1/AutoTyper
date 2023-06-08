# Keyboard Automation Script

This Python script reads a file provided by the user as a command-line argument, and then types out the contents of the file using keyboard automation.

## Requirements
The script uses the following Python packages:
- `pynput`
- `time`
- `sys`

You can install `pynput` with pip:

```shell
pip install pynput
```

## Usage
To run the script, use the following command:

```shell
python autotyper.py <filename>
```

Replace `autotyper.py` with the name of your Python script and `filename` with the name of the text file you want to read from.

For example, if your script is named `keyboard_automation.py` and you want to read from a file named `text.txt`, you would use:

```shell
python keyboard_automation.py text.txt
```

## Warning
Please be careful with the use of `pynput.keyboard` as it directly interacts with your keyboard inputs, which could lead to unexpected behavior if not handled correctly. Also note that depending on your operating system and its security settings, you may need to provide additional permissions for the script to control your keyboard.

