from PIL import Image
from pathlib import PurePath
from tkinter import Tk, filedialog, IntVar, Label, Entry, Frame, Button, StringVar, NSEW, W

def main():
  root = Tk()
  var_width = IntVar(root)
  var_height = IntVar(root)
  var_path = StringVar(root)
  var_width.set(256)
  var_height.set(256)
  frame = Frame(root)
  lb_width = Label(frame, text="Width")
  lb_width.grid(column=0, row=0, sticky=W)
  lb_height = Label(frame, text="Height")
  lb_height.grid(column=0, row=1, sticky=W)
  lb_load = Label(frame, text="Load")
  lb_load.grid(column=0, row=2, sticky=W)
  et_width = Entry(frame, textvariable=var_width)
  et_width.grid(column=1, row=0, sticky=NSEW)
  et_height = Entry(frame, textvariable=var_height)
  et_height.grid(column=1, row=1, sticky=NSEW)
  bt_load = Button(frame, textvariable=var_path)
  bt_load.grid(column=1, row=2, sticky=NSEW)
  bt_load.bind("<Button-1>", lambda x, var_path=var_path: bt_load_command(var_path))
  bt_save = Button(frame, text="Save")
  bt_save.grid(column=1, row=3, sticky=NSEW)
  bt_save.bind("<Button-1>", lambda x, width=var_width, height=var_height, var_path=var_path: bt_save_command(var_width, var_height, var_path))
  frame.grid(padx=10, pady=10)
  root.mainloop()

def bt_load_command(var_path):
  result = open_dialog()
  if result and result.name:
    var_path.set(result.name)
  else:
    var_path.set("")
    
def bt_save_command(var_width, var_height, var_path):
  if var_path.get():
    path = PurePath(var_path.get())
    image = Image.open(path)
    image_resized = image.resize((var_width.get(), var_height.get()))
    image_resized.save(path.with_stem(f"{path.stem}_{var_width.get()}x{var_height.get()}"))
  
def open_dialog():
  result = filedialog.askopenfile()
  return result
main()
