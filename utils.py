from decouple import config

USERNAME = config('USER')
BOTNAME = config('BOTNAME')

opening_text = [
    f"Cool, I'm on it {USERNAME}.",
    f"Okay {USERNAME}, I'm working on it.",
    f"Just a second {USERNAME}.",
]
