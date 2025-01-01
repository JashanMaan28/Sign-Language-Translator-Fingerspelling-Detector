from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"E:\Sign Language Translator\gui\build\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("1024x720")
window.configure(bg = "#121826")


canvas = Canvas(
    window,
    bg = "#121826",
    height = 720,
    width = 1024,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    0.0,
    0.0,
    1024.0,
    45.0,
    fill="#000000",
    outline="")

canvas.create_text(
    10.0,
    10.5,
    anchor="nw",
    text="Sign Language Translator",
    fill="#FFFFFF",
    font=("Montserrat ExtraBold", 20 * -1)
)

canvas.create_rectangle(
    46.0,
    83.0,
    456.0,
    283.0,
    fill="#FFFFFF",
    outline="")

canvas.create_rectangle(
    557.0,
    83.0,
    967.0,
    283.0,
    fill="#FFFFFF",
    outline="")

canvas.create_rectangle(
    46.0,
    331.0,
    456.0,
    376.0,
    fill="#FFFFFF",
    outline="")

canvas.create_text(
    47.0,
    301.0,
    anchor="nw",
    text="Translated Output",
    fill="#FFFFFF",
    font=("Montserrat ExtraBold", 20 * -1)
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    762.0,
    353.5,
    image=entry_image_1
)

entry_1 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)

entry_1.place(
    x=557.0,
    y=331.0,
    width=410.0,
    height=43.0
)

canvas.create_text(
    558.0,
    301.0,
    anchor="nw",
    text="Enter text to translate ",
    fill="#FFFFFF",
    font=("Montserrat ExtraBold", 20 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)

button_1.place(
    x=151.0,
    y=403.0,
    width=179.0,
    height=43.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)

button_2.place(
    x=673.0,
    y=403.0,
    width=179.0,
    height=43.0
)

window.resizable(False, False)
window.mainloop()