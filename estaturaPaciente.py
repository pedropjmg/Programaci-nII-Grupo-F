import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime

ventana_principal = tk.Tk()
ventana_principal.title("Libro de Pacientes y Doctores")
ventana_principal.geometry("800x620")

edadVar = tk.StringVar()

def enmascarar_fecha(texto):
    limpio = ''.join(filter(str.isdigit, texto))
    formato_final = ""

    if len(limpio) > 8:
        limpio = limpio[:8]
    if len(limpio) > 4:
        formato_final = f"{limpio[:2]}-{limpio[2:4]}-{limpio[4:]}"
    elif len(limpio) > 2:
        formato_final = f"{limpio[:2]}-{limpio[2:]}"
    else:
        formato_final = limpio

    if fechaN.get() != formato_final:
        fechaN.delete(0, tk.END)
        fechaN.insert(0, formato_final)

    if len(fechaN.get()) == 10:
        fecha_nacimiento = datetime.strptime(fechaN.get(), "%d-%m-%Y").date()
        fecha_actual = datetime.now().date()
        edad = fecha_actual.year - fecha_nacimiento.year - ((fecha_actual.month, fecha_actual.day) < (fecha_nacimiento.month, fecha_nacimiento.day))
        edadVar.set(edad)
    else:
        edadVar.set("")
    return True

def guardar_en_archivo():
    with open("pacienteEstatura.txt", "w", encoding="utf-8") as archivo:
        for paciente in paciente_data:
            archivo.write(f"{paciente['Nombre']} | {paciente['Fecha de Nacimiento']} | {paciente['Edad']} | "
                          f"{paciente['Grupo Sanguineo']} | {paciente['Tipo de Seguro']} | {paciente['Centro Medico']} | "
                          f"{paciente['Estatura']}\n")

def cargar_desde_archivo_paciente():
    try:
        with open("pacienteEstatura.txt", "r", encoding="utf-8") as archivo:
            paciente_data.clear()
            for linea in archivo:
                datos = linea.strip().split("|")
                if len(datos) == 7:
                    paciente = {
                        "Nombre": datos[0].strip(),
                        "Fecha de Nacimiento": datos[1].strip(),
                        "Edad": datos[2].strip(),
                        "Grupo Sanguineo": datos[3].strip(),
                        "Tipo de Seguro": datos[4].strip(),
                        "Centro Medico": datos[5].strip(),
                        "Estatura": datos[6].strip()
                    }
                    paciente_data.append(paciente)
        cargar_treeview()
    except FileNotFoundError:
        open("pacienteEstatura.txt", "w", encoding="utf-8").close()

pestañas = ttk.Notebook(ventana_principal)
frame_pacientes = ttk.Frame(pestañas)
pestañas.add(frame_pacientes, text="Pacientes")
frame_doctores = ttk.Frame(pestañas)
pestañas.add(frame_doctores, text="Doctores")
pestañas.pack(expand=True, fill="both")

# formulario
tk.Label(frame_pacientes, text="Nombre Completo:").grid(row=0, column=0, sticky="w", pady=5, padx=5)
nombreP = tk.Entry(frame_pacientes)
nombreP.grid(row=0, column=1, sticky="w", padx=5, pady=5)

tk.Label(frame_pacientes, text="Fecha de Nacimiento:").grid(row=1, column=0, sticky="w", padx=5, pady=5)
validacion_fecha = ventana_principal.register(enmascarar_fecha)
fechaN = ttk.Entry(frame_pacientes, validate="key", validatecommand=(validacion_fecha, '%P'))
fechaN.grid(row=1, column=1, sticky="w", padx=5, pady=5)

tk.Label(frame_pacientes, text="Edad:").grid(row=2, column=0, sticky="w", padx=5, pady=5)
edadentry = tk.Entry(frame_pacientes, textvariable=edadVar, state="readonly")
edadentry.grid(row=2, column=1, sticky="w", padx=5, pady=5)

tk.Label(frame_pacientes, text="Grupo Sanguíneo:").grid(row=3, column=0, sticky="w", padx=5, pady=5)
entrygruposanguineo = tk.Entry(frame_pacientes)
entrygruposanguineo.grid(row=3, column=1, sticky="w", padx=5, pady=5)

tk.Label(frame_pacientes, text="Tipo de Seguro:").grid(row=4, column=0, sticky="w", padx=5, pady=5)
tipo_seguro = tk.StringVar()
combotseguro = ttk.Combobox(frame_pacientes, values=("Publico", "Privado", "Ninguno"), textvariable=tipo_seguro)
combotseguro.grid(row=4, column=1, sticky="w", padx=5, pady=5)
tipo_seguro.set("Publico")

tk.Label(frame_pacientes, text="Centro Médico:").grid(row=5, column=0, sticky="w", padx=5, pady=5)
centromedico = tk.StringVar()
combotcentromedico = ttk.Combobox(frame_pacientes, values=("Hospital Central", "Clinica Norte", "Centro Sur"), textvariable=centromedico)
combotcentromedico.grid(row=5, column=1, sticky="w", padx=5, pady=5)
centromedico.set("Hospital Central")

tk.Label(frame_pacientes, text="Estatura:").grid(row=6, column=0, sticky="w", padx=5, pady=5)
estaturaP = tk.Entry(frame_pacientes)
estaturaP.grid(row=6, column=1, sticky="w", padx=5, pady=5)

btn_frame = tk.Frame(frame_pacientes)
btn_frame.grid(row=7, column=0, columnspan=2, pady=10)

def limpiar_campos():
    nombreP.delete(0, tk.END)
    fechaN.delete(0, tk.END)
    edadVar.set("")
    entrygruposanguineo.delete(0, tk.END)
    tipo_seguro.set("Publico")
    centromedico.set("Hospital Central")
    estaturaP.delete(0, tk.END)

def registrarPaciente():
    paciente = {
        "Nombre": nombreP.get(),
        "Fecha de Nacimiento": fechaN.get(),
        "Edad": edadVar.get(),
        "Grupo Sanguineo": entrygruposanguineo.get(),
        "Tipo de Seguro": tipo_seguro.get(),
        "Centro Medico": centromedico.get(),
        "Estatura": estaturaP.get()
    }

    if not paciente["Nombre"] or not paciente["Fecha de Nacimiento"]:
        messagebox.showerror("Error", "Nombre y Fecha de Nacimiento son obligatorios.")
        return

    paciente_data.append(paciente)
    cargar_treeview()
    guardar_en_archivo()
    limpiar_campos()

def eliminar_paciente():
    seleccionado = treeview.selection()
    if not seleccionado:
        messagebox.showwarning("Aviso", "Selecciona un paciente para eliminar.")
        return
    confirmacion = messagebox.askyesno("Confirmar", "¿Estás seguro de eliminar al paciente seleccionado?")
    if confirmacion:
        idx = int(seleccionado[0])
        del paciente_data[idx]
        cargar_treeview()
        guardar_en_archivo()

btn_registrar = tk.Button(btn_frame, text="Registrar", bg="green", fg="white", command=registrarPaciente)
btn_registrar.grid(row=0, column=0, padx=5)
btn_eliminar = tk.Button(btn_frame, text="Eliminar",  bg="red", fg="white", command=eliminar_paciente)
btn_eliminar.grid(row=0, column=1, padx=5)

treeview = ttk.Treeview(frame_pacientes, columns=("Nombre", "Fecha", "Edad", "GrupoS", "TipoS", "CentroM", "Estatura"), show="headings")
treeview.heading("Nombre", text="Nombre")
treeview.heading("Fecha", text="Fecha de Nacimiento")
treeview.heading("Edad", text="Edad")
treeview.heading("GrupoS", text="Grupo Sanguíneo")
treeview.heading("TipoS", text="Tipo Seguro")
treeview.heading("CentroM", text="Centro Médico")
treeview.heading("Estatura", text="Estatura ")

treeview.column("Nombre", width=120)
treeview.column("Fecha", width=120)
treeview.column("Edad", width=50, anchor="center")
treeview.column("GrupoS", width=100, anchor="center")
treeview.column("TipoS", width=100, anchor="center")
treeview.column("CentroM", width=120)
treeview.column("Estatura", width=100, anchor="center")

treeview.grid(row=8, column=0, columnspan=2, sticky="nsew", padx=5, pady=10)
scroll_y = ttk.Scrollbar(frame_pacientes, orient="vertical", command=treeview.yview)
treeview.configure(yscrollcommand=scroll_y.set)
scroll_y.grid(row=8, column=2, sticky="ns")

paciente_data = []

def cargar_treeview():
    for paciente in treeview.get_children():
        treeview.delete(paciente)
    for i, item in enumerate(paciente_data):
        treeview.insert("", "end", iid=str(i),
            values=(
                item["Nombre"],
                item["Fecha de Nacimiento"],
                item["Edad"],
                item["Grupo Sanguineo"],
                item["Tipo de Seguro"],
                item["Centro Medico"],
                item["Estatura"]
            )
        )

# datos al iniciar
cargar_desde_archivo_paciente()

# Ejecutar la aplicación principal
ventana_principal.mainloop()