# \033[<style>;<text_color>;<background_color>m\e[0;39m
# python ./AlphaVersion/formatting.py
class Format:
    black = '\033[0;30m'
    red = '\033[0;31m'
    green = '\033[0;32m'
    yellow = '\033[0;33m'
    blue = '\033[0;34m'
    purple = '\033[0;35m'
    cyan = '\033[0;36m'
    white = '\033[0;37m'
    default = '\033[0;39m'
    #formatting
    bold = '\033[0;1m'
    italic = '\033[0;3m'
    #backgrounds
    back_black = '\033[0;40m'
    back_red = '\033[0;41m'
    back_green = '\033[0;42m'
    back_yellow = '\033[0;43m'
    back_blue = '\033[0;44m'
    back_magenta = '\033[0;45m'
    back_cyan = '\033[0;46m'
    back_white = '\033[0;47m'
    back_default = '\033[0;49m'
    #bright colours
    bright_black = '\033[0;90m'
    bright_red = '\033[0;91m'
    bright_green = '\033[0;92m'
    bright_yellow = '\033[0;93m'
    bright_blue = '\033[0;94m'
    bright_magenta = '\033[0;95m'
    bright_cyan = '\033[0;96m'
    bright_white = '\033[0;97m'

def ansi_format(text, code):
    return code + text + Format.default

def embolden(text):
    return ansi_format(text, Format.bold)

def italicize(text):
    return ansi_format(text, Format.italic)
