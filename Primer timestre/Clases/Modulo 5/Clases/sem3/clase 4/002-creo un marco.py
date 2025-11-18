import tkinter as tk

ventana =tk.TK()

marco = tk.Frame(ventana)
tk.Label(marco,text ="introduce el nombre del cliente").pack(padx=20,pady=20)

marco.pack (padx=20,pady=20)

ventana.mainloop()