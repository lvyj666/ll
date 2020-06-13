from runpy import run_path
from tkinter import *

def make_app():
    app = Tk()
    Button(text="run",command=run_script).pack()
    return app

def run_script():
    print("hi,there")
    run_path(r"F:\pythonwork\auto_test\cs.py")

app = make_app()
app.mainloop()
