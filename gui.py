import tkinter as tk
from tkinter import messagebox
from tkinter import scrolledtext

from src.services.weather_service import obtener_clima_completo
from src.utils.formatter import formatear_clima_completo


def consultar_clima():
    ciudad = entrada_ciudad.get().strip()

    if not ciudad:
        messagebox.showwarning("Aviso", "Ingresa una ciudad")
        return

    resultado = obtener_clima_completo(ciudad)
    texto = formatear_clima_completo(resultado)

    output.delete("1.0", tk.END)
    output.insert(tk.END, texto)


# ------------------------
# Ventana principal
# ------------------------
ventana = tk.Tk()
ventana.title("Weather App")
ventana.geometry("600x450")
ventana.configure(bg="#f4f6f7")
ventana.bind("<Return>", lambda event: consultar_clima())

# ------------------------
# Título
# ------------------------
titulo = tk.Label(
    ventana,
    text="🌤️ Weather App",
    font=("Arial", 18, "bold"),
    bg="#f4f6f7",
    fg="#2c3e50"
)
titulo.pack(pady=10)

# ------------------------
# Frame de entrada
# ------------------------
frame_input = tk.Frame(ventana, bg="#f4f6f7")
frame_input.pack(pady=10)

tk.Label(
    frame_input,
    text="Ciudad:",
    font=("Arial", 12),
    bg="#f4f6f7"
).grid(row=0, column=0, padx=5)

entrada_ciudad = tk.Entry(frame_input, width=30, font=("Arial", 12))
entrada_ciudad.grid(row=0, column=1, padx=5)

# ------------------------
# Botón
# ------------------------
boton = tk.Button(
    ventana,
    text="Consultar clima",
    font=("Arial", 12, "bold"),
    bg="#3498db",
    fg="white",
    padx=10,
    pady=5,
    command=consultar_clima
)
boton.pack(pady=10)

# ------------------------
# Área de salida con scroll
# ------------------------
output = scrolledtext.ScrolledText(
    ventana,
    width=70,
    height=15,
    font=("Consolas", 10),
    bg="#ffffff",
    fg="#2c3e50"
)
output.pack(pady=10)

# ------------------------
# Ejecutar
# ------------------------
ventana.mainloop()