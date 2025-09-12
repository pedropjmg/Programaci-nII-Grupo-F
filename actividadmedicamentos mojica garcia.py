import tkinter as tk
from tkinter import ttk, messagebox

# -------------------------
# Función para enmascarar fecha
# -------------------------
def formato_fecha_keyrelease(event):
    s = entry_fecha_var.get()
    # conservar solo dígitos y limitar a 8 (DDMMYYYY)
    digits = ''.join(ch for ch in s if ch.isdigit())[:8]

    if len(digits) > 4:
        formatted = f"{digits[:2]}-{digits[2:4]}-{digits[4:]}"
    elif len(digits) > 2:
        formatted = f"{digits[:2]}-{digits[2:]}"
    else:
        formatted = digits

    if formatted != s:
        entry_fecha_var.set(formatted)

    entry_fecha.icursor(tk.END)

def guardar_en_archivo():
    with open("medicamento.txt","w",encoding="utf-8") as archivo:
            for medicamento in medicamentos_data:
                archivo.write(f"{medicamento['Nombre']}|{medicamento['Presentacion']}|{medicamento['Dosis']}|{medicamento['Fecha']}\n")

#lista de medicamentos
medicamentos_data=[]
#funcion para registrar medicamentos
def registrar_medicamento():
    #crear un diccionario con los datos ingresados
    medicamento={
        "Nombre":entry_nombre.get(),
        "Presentacion":combo_presentacion.get(),
        "Dosis":entry_dosis.get(),
        "Fecha":entry_fecha_var.get()
    }
    #Agregar mediacamento a la lista
    medicamentos_data.append(medicamento)
    guardar_en_archivo()
    #Cargar el treeview
    cargar_treeview()

def cargar_treeview():
    #Limpiar el treeview
    for medicamento in treeview.get_children():
        treeview.delete(medicamento)
    #Insertar cada medicamento
    for i, item in enumerate(medicamentos_data):
        treeview.insert(
            "","end",iid=str(i),
            values=(
                item["Nombre"],
                item["Presentacion"],
                item["Dosis"],
                item["Fecha"],
            )
        )
def cargar_desde_archivo_medicamento():
    try:
        with open("medicamento.txt","r",encoding="utf-8")as archivo:
            medicamentos_data.clear()
            for linea in archivo:
                datos=linea.strip().split("|")
                if len(datos)==4:
                    medicamento={
                        "Nombre":datos[0],
                        "Presentacion":datos[1],
                        "Dosis":datos[2],
                        "Fecha":datos[3]
                    }
                    medicamentos_data.append(medicamento)
        cargar_treeview()
    except FileNotFoundError:
        open("medicamento.txt","w",encoding="utf-8").close()
#Funcion para eliminar medicamento
def Eliminar_medicamento():
    seleccionado=treeview.selection()
    if seleccionado:
        indice=int(seleccionado[0])
        id_item=seleccionado[0]
        if messagebox.askyesno("Eliminar Medicamento",f"¿Está seguro de aliminar el medicamento'{treeview.item(id_item,'values')[0]}'?"):
            del medicamentos_data[indice]
            guardar_en_archivo()
            cargar_treeview()
            messagebox.showinfo("Eliminar Medicamento","Medicamento eliminado exitosamente")
    else:
        messagebox.showwarning("Eliminar Medicamento","No se ha seleccionado ningun medicamento")
        return
# Interfaz gráfica
ventana = tk.Tk()
ventana.title("Gestión de Medicamentos")
ventana.geometry("800x520")
ventana.minsize(700, 450)

# Frame formulario
form_frame = ttk.Frame(ventana, padding=(12, 10))
form_frame.grid(row=0, column=0, sticky="ew")
form_frame.columnconfigure(0, weight=0)
form_frame.columnconfigure(1, weight=1)

# Nombre
lbl_nombre = ttk.Label(form_frame, text="Nombre:")
lbl_nombre.grid(row=0, column=0, sticky="w", padx=6, pady=6)
entry_nombre = ttk.Entry(form_frame)
entry_nombre.grid(row=0, column=1, sticky="ew", padx=6, pady=6)

# Presentación
lbl_present = ttk.Label(form_frame, text="Presentación:")
lbl_present.grid(row=1, column=0, sticky="w", padx=6, pady=6)
combo_presentacion = ttk.Combobox(form_frame, values=["Tabletas", "Jarabe", "Inyectable", "Cápsulas", "Otro"])
combo_presentacion.grid(row=1, column=1, sticky="ew", padx=6, pady=6)

# Dosis
lbl_dosis = ttk.Label(form_frame, text="Dosis:")
lbl_dosis.grid(row=2, column=0, sticky="w", padx=6, pady=6)
entry_dosis = ttk.Entry(form_frame)
entry_dosis.grid(row=2, column=1, sticky="w", padx=6, pady=6)

# Fecha Vencimiento con enmascarado
lbl_fecha = ttk.Label(form_frame, text="Fecha Vencimiento (dd-mm-yyyy):")
lbl_fecha.grid(row=3, column=0, sticky="w", padx=6, pady=6)
entry_fecha_var = tk.StringVar()
entry_fecha = ttk.Entry(form_frame, textvariable=entry_fecha_var)
entry_fecha.grid(row=3, column=1, sticky="w", padx=6, pady=6)
entry_fecha.bind("<KeyRelease>", formato_fecha_keyrelease)

# Boton
btn_frame = ttk.Frame(form_frame)
btn_frame.grid(row=4, column=0, columnspan=2, sticky="ew", padx=6, pady=(10, 2))
btn_frame.columnconfigure((0, 1, 2, 3), weight=1)  # columnas equitativas

btn_registrar = ttk.Button(btn_frame, text="Registrar",command=registrar_medicamento)
btn_registrar.grid(row=0, column=0, padx=5, pady=5, sticky="ew")

btn_eliminar = ttk.Button(btn_frame, text="Eliminar",command=Eliminar_medicamento)
btn_eliminar.grid(row=0, column=1, padx=5, pady=5, sticky="ew")


# Frame lista
list_frame = ttk.Frame(ventana, padding=(12, 6))
list_frame.grid(row=1, column=0, sticky="nsew")
ventana.rowconfigure(1, weight=1)
ventana.columnconfigure(0, weight=1)
list_frame.rowconfigure(0, weight=1)
list_frame.columnconfigure(0, weight=1)

treeview = ttk.Treeview(list_frame,
                        columns=("nombre", "presentacion", "dosis", "fecha"),
                        show="headings")
treeview.grid(row=0, column=0, sticky="nsew")
treeview.heading("nombre", text="Nombre")
treeview.heading("presentacion", text="Presentación")
treeview.heading("dosis", text="Dosis")
treeview.heading("fecha", text="Fecha Vencimiento")
treeview.column("nombre", width=220)
treeview.column("presentacion", width=120, anchor="center")
treeview.column("dosis", width=100, anchor="center")
treeview.column("fecha", width=120, anchor="center")

scroll_y = ttk.Scrollbar(list_frame, orient="vertical", command=treeview.yview)
scroll_y.grid(row=0, column=1, sticky="ns")
treeview.configure(yscrollcommand=scroll_y.set)
#cargar los datos desde archivo medicamento
cargar_desde_archivo_medicamento()
# Ejecutar
ventana.mainloop()
