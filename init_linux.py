#!/usr/bin/env python3

from PIL import Image
from os import system

name = input("Enter name for new app: ")

print(f'Creating {name}...')

system(f"mkdir {name}")

icon = Image.new('RGBA', (100, 100), (255, 255, 255, 0))
icon.save(f'{name}/icon.png', 'PNG')

app = open(f"{name}/{name}.pyw", "w+")

app.write(f"""import tkinter as tk

app = tk.Tk()
app.title("{name}")
icon = tk.PhotoImage(file = 'icon.png') #App's icon
app.iconphoto(False, icon)
app.geometry("800x600") #Window size

def main():
    #App's code goes here
    
    app.mainloop() #Start app

if __name__ == "__main__":
    main()
""")

app.close()

print(f'Project {name} has been created succesfully!')
input('Press enter to exit')