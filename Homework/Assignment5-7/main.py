from ui.ui import UI


def read_settings():
    f = open("settings.properties", "r")
    s = f.read()
    lines = s.split("\n")
    settings = {}
    for line in lines:
        keyValue = line.split("=")
        settings[keyValue[0].strip()] = keyValue[1].strip()
    return settings


def main():
    settings = read_settings()
    _ui = UI(settings)
    _ui.main_loop()


main()
