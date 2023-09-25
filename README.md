## What is it?
A simple CLI program to convert your ***secret*** text to random letters and symbols, and convert this random text to normal using a randomly generated dictionary.

Let's say you wanna send a send something in your whatsapp group but only 1 person's allow to see it, you can **ecnrypt** your message using this program and send it to your partner and the partner can decrypt your message using this program and **the same data.json file**

## Requirements
This program works on Windows, Linux, Android (Using [Termux](https://termux.dev), iOS (using [iSH](https://ish.app/))

You need **Python** installed in your system to use it (maybe will compile it and submit directly the executable files later).
## Hot to use it?
```
python3 main.py [OPTION] """YOUR-TEXT""" 

Example:
* Encrypt a text
python3 main.py -en "Hello, World"

Options:
1: ['g', '-g', 'gen', '-gen', '--generate-key'] <-- Generate a new crypto alphabet

2: ['d', '-d', 'de', '-de', '--decrypt'] <-- Decrypt a text

3: ['e', '-e', 'en', '-en', '--encrypt'] <-- Encrypt a text

More:
- Module files can be run directly from terminal (using: python3 modules/[MODULE-FILE].py)

```

## Example, Screenshot

<br>
<p align="center">
<img src="images/example.png"/>
</p>


It is not a super program, cause it's CLI, and you need python to be installed to use it, but still, I think it's a cool script.

If you have a question about this project, you can ask me in [issue](https://github.com/1RaY-1/crypto/issues).
