import tkinter as tk

ventana =tk.TK()

marco = tk.Frame(ventana)


#DNI NIE
tk.Label(marco,text ="introduce el dni/nie del cliente").pack(padx=20,pady=20)
dninie= tk.Entry(marco)
dninie.pack (padx=10,pady=10)

#Nombre del cliente
tk.Label(marco,text ="introduce el nombre del cliente").pack(padx=20,pady=20)
nombre= tk.Entry(marco)
nombre.pack (padx=10,pady=10)

#Apellidos 
tk.Label(marco,text ="introduce los apellidos del cliente").pack(padx=20,pady=20)
apellidos= tk.Entry(marco)
apellidos.pack (padx=10,pady=10)

#Email del cliente
tk.Label(marco,text ="introduce el email del cliente").pack(padx=20,pady=20)
email= tk.Entry(marco)
email.pack(padx=10,pady=10)




marco.pack (padx=20,pady=20)

ventana.mainloop()