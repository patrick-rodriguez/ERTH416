import tkinter as tk
import ttkbootstrap as ttk
import customtkinter as ctk
import environment_gauges
from PIL import Image

images = ["images/calathea.png",
          "images/fiddle leaf.png",
          "images/monstera.png",
          "images/pineapple plant.png",
          "images/pothos.png",
          "images/sago palm.png",
          "images/zebra plant.png"]

names = ["Peacock Plant",
         "Fiddle Leaf Fig",
         "Monstera Deliciosa",
         "Pineapple Plant",
         "Pothos",
         "Sago Palm",
         "Zebra Plant"]

scientific_names = [
    "calathea makoyana",
    "fiddle leaf",
    "monstera deliciosa",
    "pineapple plant",
    "pothos",
    "sago palm",
    "zebra cactus",
]

photoimages = [

]


def create_ui():
    root = ttk.Window()
    root.geometry("500x900")
    root.resizable(False, False)

    frame = ttk.Frame(root)
    frame.pack(fill="both", expand="true")

    label = ttk.Label(frame, text="Plant Environment Optimizer", font=("Helvetica", 16))
    label.pack(pady=10)

    separator = ttk.Separator(frame, orient='horizontal')
    separator.pack(fill='x')

    canvas = ttk.Canvas(frame)
    canvas.pack(side="top", fill="both", expand="true")

    for image in images:
        photoimage = ctk.CTkImage(Image.open(image), size=(350, 200))
        photoimages.append(photoimage)

    scrollbar = ttk.Scrollbar(canvas, orient="vertical", command=canvas.yview)
    scrollbar.pack(side="right", fill="y")
    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    button_frame = tk.Frame(canvas)
    button_frame.pack(fill="both", expand="true")
    canvas.create_window((0, 0), window=button_frame, anchor="nw")

    def destroy_window():
        root.destroy()

    def open_gauges(plant_name):
        app = environment_gauges.create_gauges(plant_name)
        app.run_server(debug=False)

    for i in range(len(images)):
        button_image = ctk.CTkButton(button_frame, image=photoimages[i], text=names[i], font=("Times New Roman", 20),
                                     compound="top", height=255, width=385, fg_color="grey",
                                     command=lambda plant_name=scientific_names[i]: [destroy_window(),
                                                                                     open_gauges(plant_name)]
                                     )
        button_image.pack(padx=3, pady=5)

    return root
