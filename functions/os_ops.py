import os
import subprocess as sp

paths = {
    'notes': "/System/Applications/Notes.app/Contents/MacOS/Notes",
    'discord': "/Applications/Discord.app/Contents/MacOS/Discord",
    'calculator': "/System/Applications/Calculator.app/Contents/MacOS/Calculator",
    'camera': "/System/Applications/Photo\ Booth.app/Contents/MacOS/Photo\ Booth:"
}


def open_camera():
    os.startfile(paths['camera'])


def open_notes():
    os.startfile(paths['notes'])


def open_discord():
    os.startfile(paths['discord'])


def open_calculator():
    sp.Popen(paths['calculator'])


def open_cmd():
    os.system('start cmd')
