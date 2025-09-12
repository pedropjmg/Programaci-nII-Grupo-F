import tkinter as tk
from tkinter import ttk, messagebox
medicamento_data = []
 
# -------------------------
# Función para enmascarar fecha
# -------------------------
 
def formato_fecha_keyrelease(event):
    s = entry_fecha_var.get()
    digits = ''.join(ch for ch in s if ch.isdigit())[:8]
 
    if len(digits) > 4:
        formatted = f"{digits[:2]}-{digits[2:4]}-{digits[4:]}"
    elif len(digits) > 2:
        formatted = f"{digits[:2]}-{digits[2:]}"
    else:
        formatted = digits
 
    entry_fecha_var.set(formatted)
    entry_fecha.icursor(tk.END)
 
# Guardar en archivo.txt
def guardar_en_archivo_medicamentos():
    with open("medicamento.txt", "w", encoding="utf-8") as archivo:
        for med in medicamento_data:
            archivo.write(
                f"{med['Nombre']}|{med['Presentación']}|{med['Dosis']}|{med['Fecha Vencimiento']}\n"
            )
 
# Registrar medicamento
def registrar_medicamento():
    nombre = entry_nombre.get().strip()
    presentacion = combo_presentacion.get().strip()
    dosis = entry_dosis.get().strip()
    fecha = entry_fecha_var.get().strip()
 
 
    medicamento = {
        "Nombre": nombre,
        "Presentación": presentacion,
        "Dosis": dosis,
        "Fecha Vencimiento": fecha
    }
 
    medicamento_data.append(medicamento)
    guardar_en_archivo_medicamentos()
    cargar_treeview_medicamentos()
 
    entry_nombre.delete(0, tk.END)
    combo_presentacion.set('')
    entry_dosis.delete(0, tk.END)
    entry_fecha_var.set('')
 
# Cargar Treeview
def cargar_treeview_medicamentos():
    for item in treeview.get_children():
        treeview.delete(item)
 
    for i, med in enumerate(medicamento_data):
        treeview.insert(
            "", "end", iid=str(i),
            values=(med["Nombre"], med["Presentación"], med["Dosis"], med["Fecha Vencimiento"])
        )
 
# Cargar archivo
def cargar_desde_archivo_medicamentos():
    try:
        with open("medicamento.txt", "r", encoding="utf-8") as archivo:
            medicamento_data.clear()
            for linea in archivo:
                datos = linea.strip().split("|")
                if len(datos) == 4:
                    medicamento = {
                        "Nombre": datos[0],
                        "Presentación": datos[1],
                        "Dosis": datos[2],
                        "Fecha Vencimiento": datos[3]
                    }
                    medicamento_data.append(medicamento)
        cargar_treeview_medicamentos()
    except FileNotFoundError:
        open("medicamento.txt", "w", encoding="utf-8").close()
 
# Eliminar medicamento
def eliminar_medicamento():
    seleccionado = treeview.selection()
    if not seleccionado:
        messagebox.showwarning("Eliminar", " seleccione un medicamento para eliminar.")
        return
 
    indice = int(seleccionado[0])
    nombre = treeview.item(seleccionado, "values")[0]
 
    if messagebox.askyesno("Eliminar", f"¿Desea eliminar '{nombre}'?"):
        del medicamento_data[indice]
        guardar_en_archivo_medicamentos()
        cargar_treeview_medicamentos()
        messagebox.showinfo("Eliminado", f"'{nombre}' ha sido eliminado.")

# Interfaz d la grafica

ventana = tk.Tk()
ventana.title("Gestión de Medicamentos")
ventana.geometry("820x520")
ventana.minsize(700, 450)
 
# Frame del formulario
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
combo_presentacion = ttk.Combobox(form_frame, values=["Tabletas", "Jarabe", "Inyectable", "Capsulas", "Otro"])
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
 
# Botones
btn_frame = ttk.Frame(form_frame)
btn_frame.grid(row=4, column=0, columnspan=2, sticky="ew", padx=6, pady=(10, 2))
btn_frame.columnconfigure((0, 1), weight=1)
 
btn_registrar = ttk.Button(btn_frame, text="Registrar", command=registrar_medicamento)
btn_registrar.grid(row=0, column=0, padx=5, pady=5, sticky="ew")
 
btn_eliminar = ttk.Button(btn_frame, text="Eliminar", command=eliminar_medicamento)
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
 
cargar_desde_archivo_medicamentos()
 
#ejecutar la ventana
ventana.mainloop()
 