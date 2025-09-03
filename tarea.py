import tkinter as tk
from tkinter import ttk
#crear ventana principal

ventana_Principal= tk.Tk()
ventana_Principal.title("Libro de pacientes y Doctores")
ventana_Principal.geometry("700x600")
#crear contenedores

pestañas= ttk.Notebook(ventana_Principal)
#crear frames (uno por pestañas)

frame_Pacientes= ttk.Frame(pestañas)
pestañas.add(frame_Pacientes, text="Pacientes")
#mostrar las pestañas

pestañas.pack(expand=True, fill="both")
#añadir doctores

frame_Doctores= ttk.Frame(pestañas)
pestañas.add(frame_Doctores, text="Doctores")

#NOMBRE

labelNombre= tk.Label(frame_Pacientes, text="Nombre completo: ")
labelNombre.grid(row=0, column=0, sticky="w", pady=5, padx=5)
nombreP=tk.Entry(frame_Pacientes)
nombreP.grid(row=0, column=1, sticky="w", padx=5, pady=5)
#fecha de nacimiento

labelFechaN=tk.Label(frame_Pacientes, text="fecha de Nacimiento: ")
labelFechaN.grid(row=1, column=0, sticky="w", pady=5, padx=5)
FechaN=tk.Entry(frame_Pacientes)
FechaN.grid(row=1, column=1, sticky="w", padx=5, pady=5)
#edad

labelEdad= tk.Label(frame_Pacientes, text="edad: ")
labelEdad.grid(row=2, column=0, sticky="w", padx=5, pady=5)
edadP=tk.Entry(frame_Pacientes, state="readonly")
edadP.grid(row=2,column=1, sticky="w", padx=5, pady=5)
#genero
labelGenero=tk.Label(frame_Pacientes, text="Genero: ")
labelGenero.grid(row=3, column=0, sticky="W", pady=5,padx=5)
genero=tk.StringVar()
genero.set("Masculino")
radioMasculino=ttk.Radiobutton(frame_Pacientes, text="Masculino", variable=genero, value="Masculino")
radioMasculino.grid(row=3, column=1, sticky="w", padx=5)
radioFemenino=ttk.Radiobutton(frame_Pacientes, text="Femenino", variable=genero, value="Femenino")
radioFemenino.grid(row=4,column=1,sticky="w", padx=5)
#grupo sanguineo
labelGruposSanguineos=tk.Label(frame_Pacientes, text="Grupo Sanguineo: ")
labelGruposSanguineos.grid(row=5, column=0, sticky="w", padx=5, pady=5)
entryGrupoSanguineo= tk.Entry(frame_Pacientes)
entryGrupoSanguineo.grid(row=5, column=1, sticky="w", padx=5, pady=5)
#tipo de seguro
labelTipoSeguro=tk.Label(frame_Pacientes, text="Tipo de seguro:")
labelTipoSeguro.grid(row=5, column=0, sticky="w", pady=5, padx=5)
tipo_seguro=tk.StringVar()
tipo_seguro.set("Público") #valor por defecto
comboTipoSeguro=ttk.Combobox(frame_Pacientes, values=["Publico", "Privado", "Ninguno"], textvariable=tipo_seguro)
comboTipoSeguro.grid(row=5, column=1, sticky="w", pady=5, padx=5)
#centro medico
labelCentroMedico=tk.Label(frame_Pacientes, text="centro de salud:")
labelCentroMedico.grid(row=6, column=0, sticky="w", padx=5, pady=5)
centro_medico=tk.StringVar()
centro_medico.set("Hospital Central")
comboCentroMedico=ttk.Combobox(frame_Pacientes, values=["Hospital Central", "Clinica Norte", "Centro Sur"], textvariable=centro_medico)
comboCentroMedico.grid(row=6, column=1, sticky="w", padx=5, pady=5)
#Frame para los pacientes
btn_frame=tk.Frame(frame_Pacientes)
btn_frame.grid(row=8, column=0, columnspan=2, pady=5, sticky="w")
#Boton registrar
btn_registrar=tk.Button(btn_frame, text="Registar", command="")
btn_registrar.grid(row=0, column=0, padx=5)
#Boton eliminar
btn_eliminar=tk.Button(btn_frame, text="Eliminar", command="")
btn_eliminar.grid(row=0, column=1, padx=5)
#Creacion Treeview para mostrar pacientes
treeview=ttk.Treeview(frame_Pacientes, columns=("Nombre", "FechaN", "Edad", "Genero", "GrupoS", "TipoS", "CentroM"), show="headings")
#Definir encabezados
treeview.heading("Nombre", text="Nombre Completo")
treeview.heading("FechaN", text="Fecha de Nacimiento")
treeview.heading("Edad", text="Edad")
treeview.heading("Genero", text="Género")
treeview.heading("GrupoS", text="Grupo Sanguineo")
treeview.heading("TipoS", text="Tipo Seguro")
treeview.heading("CentroM", text="Centro Médico")
#Definir anchos de columnas
treeview.column("Nombre", width=120)
treeview.column("FechaN", width=120)
treeview.column("Edad", width=50, anchor="center")
treeview.column("Genero", width=60, anchor="center")
treeview.column("GrupoS", width=100, anchor="center")
treeview.column("TipoS", width=100, anchor="center")
treeview.column("CentroM", width=120)
#Ubicar el Treeview en la cuadricula
treeview.grid(row=7, column=0, columnspan=2, sticky="nsew", padx=5, pady=10)
#Scrollbar vertical
scroll_y=ttk.Scrollbar(frame_Pacientes, orient="vertical", command=treeview.yview)
treeview.configure(yscrollcommand=scroll_y.set)
scroll_y.grid(row=7, column=2, sticky="ns")
#Doctores
#Titulo
titulo=tk.Label(frame_Doctores, text="Registro de Doctores", font=("Arial", 14, "bold"))
titulo.grid(row=0,column=5, padx=220, pady=5, sticky="w")
# Nombre
labelNombreD = tk.Label(frame_Doctores, text="Nombre: ")
labelNombreD.grid(row=1, column=0, sticky="w", pady=5, padx=5)
nombreD = tk.Entry(frame_Doctores)
nombreD.grid(row=1, column=1, sticky="w", padx=5, pady=5)
# Especialidad
labelEspecialidad = tk.Label(frame_Doctores, text="Especialidad: ")
labelEspecialidad.grid(row=2, column=0, sticky="w", pady=5, padx=5)
especialidad = tk.StringVar()
comboEspecialidad = ttk.Combobox(frame_Doctores, textvariable=especialidad, values=["Cardiología", "Pediatría", "Neurología", "Ginecología", "Traumatología"])
comboEspecialidad.grid(row=2, column=1, sticky="w", padx=5, pady=5)
# Edad
labelEdadD = tk.Label(frame_Doctores, text="Edad: ")
labelEdadD.grid(row=3, column=0, sticky="w", pady=5, padx=5)
edadD = tk.Spinbox(frame_Doctores, from_=25, to=100)
edadD.grid(row=3, column=1, sticky="w", padx=5, pady=5)
# Teléfono
labelTelefono = tk.Label(frame_Doctores, text="Teléfono: ")
labelTelefono.grid(row=4, column=0, sticky="w", pady=5, padx=5)
telefonoD = tk.Entry(frame_Doctores)
telefonoD.grid(row=4, column=1, sticky="w", padx=5, pady=5)
# Botones
btn_frameD = tk.Frame(frame_Doctores)
btn_frameD.grid(row=5, column=0, columnspan=2, pady=10)
btn_registrarD = tk.Button(btn_frameD, text="Registrar", bg="lightgreen")
btn_registrarD.grid(row=5, column=0, padx=10)
btn_eliminarD = tk.Button(btn_frameD, text="Eliminar", bg="red")
btn_eliminarD.grid(row=5, column=1, padx=10)
# Tabla (Treeview)
treeviewD = ttk.Treeview(frame_Doctores, columns=("Nombre", "Especialidad", "Edad", "Telefono"), show="headings")
treeviewD.heading("Nombre", text="Nombre")
treeviewD.heading("Especialidad", text="Especialidad")
treeviewD.heading("Edad", text="Edad")
treeviewD.heading("Telefono", text="Teléfono")
treeviewD.column("Nombre", width=150)
treeviewD.column("Especialidad", width=150)
treeviewD.column("Edad", width=150, anchor="center")
treeviewD.column("Telefono", width=150, anchor="center")
treeviewD.grid(row=8, column=0, columnspan=2, sticky="nsew", padx=5, pady=10)
scroll_yD = ttk.Scrollbar(frame_Doctores, orient="vertical", command=treeviewD.yview)
treeviewD.configure(yscrollcommand=scroll_yD.set)
scroll_yD.grid(row=5, column=2, sticky="ns")
ventana_Principal.mainloop()
 