from tkinter import *
import random
import datetime
from tkinter import filedialog, messagebox

operador = ''
precios_comidas = [3.35, 2.55, 3.95, 5.00, 3.35, 3.20, 3.00, 4.65]
precios_bebidas = [1.35, 1.55, 1.95, 1.00, 1.50, 2.20, 2.00, 2.65]
precios_postres = [2.00, 3.25, 2.95, 3.20, 3.55, 3.40, 3.20, 2.80]


def click_boton(numero):
    global operador
    operador = operador + numero
    visor_calculadora.delete(0, END)
    visor_calculadora.insert(END, operador)


def borrar():
    global operador
    operador = ''
    visor_calculadora.delete(0, END)


def obtener_resultado():
    global operador
    resultado = str(eval(operador))
    visor_calculadora.delete(0, END)
    visor_calculadora.insert(0, resultado)
    operador = ''


def revisar_check():
    x = 0
    for c in cuadros_comida:
        if variables_comida[x].get() == 1:
            cuadros_comida[x].config(state=NORMAL)
            if cuadros_comida[x].get() == 0:
                cuadros_comida[x].delete(0, END)
            cuadros_comida[x].focus()
        else:
            cuadros_comida[x].config(state=DISABLED)
            texto_comida[x].set('0')
        x += 1

    x = 0

    for c in cuadros_bebida:
        if variables_bebida[x].get() == 1:
            cuadros_bebida[x].config(state=NORMAL)
            if cuadros_bebida[x].get() == 0:
                cuadros_bebida[x].delete(0, END)
            cuadros_bebida[x].focus()
        else:
            cuadros_bebida[x].config(state=DISABLED)
            texto_bebida[x].set('0')
        x += 1

    x = 0
    for c in cuadros_postre:
        if variables_postre[x].get() == 1:
            cuadros_postre[x].config(state=NORMAL)
            if cuadros_postre[x].get() == 0:
                cuadros_postre[x].delete(0, END)
            cuadros_postre[x].focus()
        else:
            cuadros_postre[x].config(state=DISABLED)
            texto_comida[x].set('0')
        x += 1


def total():
    subtotal_comida = 0
    p = 0
    for cantidad in texto_comida:
        subtotal_comida = subtotal_comida + (float(cantidad.get()) * precios_comidas[p])
        p += 1

    subtotal_bebida = 0
    p = 0
    for cantidad in texto_bebida:
        subtotal_bebida = subtotal_bebida + (float(cantidad.get()) * precios_bebidas[p])
        p += 1

    subtotal_postre = 0
    p = 0
    for cantidad in texto_postre:
        subtotal_postre = subtotal_postre + (float(cantidad.get()) * precios_postres[p])
        p += 1

    sub_total = subtotal_comida + subtotal_bebida + subtotal_postre
    impuestos = sub_total * 0.07
    total = sub_total + impuestos

    var_costo_comida.set(f'${round(subtotal_comida, 2)}')
    var_costo_bebida.set(f'${round(subtotal_bebida, 2)}')
    var_costo_postre.set(f'${round(subtotal_postre, 2)}')
    var_subtotal.set(f'${round(sub_total, 2)}')
    var_impuestos.set(f'${round(impuestos, 2)}')
    var_total.set(f'${round(total, 2)}')


def recibo():
    texto_recibo.delete(1.0, END)
    numero_recibo = f'N# - {random.randint(1000, 9999)}'
    fecha = datetime.datetime.now()
    fecha_recibo = f'{fecha.day}/{fecha.month}/{fecha.year} - {fecha.hour}: {fecha.minute}'
    texto_recibo.insert(END, f'Datos: \t{numero_recibo}\t\t{fecha_recibo}\n')
    texto_recibo.insert(END, f'*' * 57 + '\n')
    texto_recibo.insert(END, 'Items\t\tCant.\tPrecio Items\n')
    texto_recibo.insert(END, f'-' * 57 + '\n')

    x = 0
    for comida in texto_comida:
        if comida.get() != '0':
            texto_recibo.insert(END, f'{lista_comidas[x]}\t\t{comida.get()}\t'
                                     f'${int(comida.get())} * {precios_comidas[x]}\n')
        x += 1

    x = 0
    for bebida in texto_bebida:
        if bebida.get() != '0':
            texto_recibo.insert(END, f'{lista_bebidas[x]}\t\t{bebida.get()}\t'
                                     f'${int(bebida.get())} * {precios_bebidas[x]}\n')
        x += 1

    x = 0
    for postre in texto_postre:
        if postre.get() != '0':
            texto_recibo.insert(END, f'{lista_postres[x]}\t\t{postre.get()}\t'
                                     f'${int(postre.get())} * {precios_postres[x]}\n')
        x += 1

    texto_recibo.insert(END, f'-' * 57 + '\n')
    texto_recibo.insert(END, f'Precio de la comida: \t\t\t{var_costo_comida.get()}\n')
    texto_recibo.insert(END, f'Precio de la bebida: \t\t\t{var_costo_bebida.get()}\n')
    texto_recibo.insert(END, f'Precio de la postre: \t\t\t{var_costo_postre.get()}\n')
    texto_recibo.insert(END, f'-' * 57 + '\n')
    texto_recibo.insert(END, f'Subtotal: \t\t\t{var_subtotal.get()}\n')
    texto_recibo.insert(END, f'Impuestos: \t\t\t{var_impuestos.get()}\n')
    texto_recibo.insert(END, f'Total: \t\t\t{var_total.get()}\n')
    texto_recibo.insert(END, f'*' * 57 + '\n')
    texto_recibo.insert(END, 'Muchísimas gracias y os esperamos pronto.')


def guardar():
    info_recibo = texto_recibo.get(1.0, END)
    archivo = filedialog.asksaveasfile(mode='w', defaultextension='.txt')
    archivo.write(info_recibo)
    archivo.close()
    messagebox.showinfo('Información', 'Su recibo ha sido guardado.')


def resetear():
    texto_recibo.delete(0.1, END)
    for texto in texto_comida:
        texto.set('0')
    for texto in texto_bebida:
        texto.set('0')
    for texto in texto_postre:
        texto.set('0')

    for cuadro in cuadros_comida:
        cuadro.config(state=DISABLED)
    for cuadro in cuadros_bebida:
        cuadro.config(state=DISABLED)
    for cuadro in cuadros_postre:
        cuadro.config(state=DISABLED)

    for check in variables_comida:
        check.set(0)
    for check in variables_bebida:
        check.set(0)
    for check in variables_postre:
        check.set(0)

    var_costo_comida.set('')
    var_costo_bebida.set('')
    var_costo_postre.set('')
    var_subtotal.set('')
    var_impuestos.set('')
    var_total.set('')





# Activar ventana
tk = Tk()

# Titulo
tk.title('My Restaurant')

# Tamaño
tk.geometry('1020x630+0+0')

# Evitar maximizar tamaño
tk.resizable(False, False)

# Color fondo pantalla
tk.config(bg='burlywood')

# Panel Superior
panel_superior = Frame(tk, bd=2, relief=FLAT)
panel_superior.pack(side=TOP)

# Etiqueta Título panel superior
etiqueta_panel_superior = Label(panel_superior, text="Sistema de facturación", fg='azure4',
                                font=('Dosis', 58), bg='burlywood', width=27)
etiqueta_panel_superior.grid(row=0, column=0)

# Panel izquierdo
panel_izquierdo = Frame(tk, bd=2, relief=FLAT, bg='azure4')
panel_izquierdo.pack(side=LEFT)

# Panel costos
panel_costos = Frame(panel_izquierdo, bd=2, relief=FLAT, bg='azure4', padx=60)
panel_costos.pack(side=BOTTOM)

# Panel Comida
panel_comida = LabelFrame(panel_izquierdo, text='Comida', font=('Dosis', 19, 'bold'),
                          bd=2, relief=FLAT, fg='azure4')
panel_comida.pack(side=LEFT)

# Panel bebidas
panel_bebida = LabelFrame(panel_izquierdo, text='Bebidas', font=('Dosis', 19, 'bold'),
                          bd=2, relief=FLAT, fg='azure4')
panel_bebida.pack(side=LEFT)

# Panel postres
panel_postre = LabelFrame(panel_izquierdo, text='Postres', font=('Dosis', 19, 'bold'),
                          bd=2, relief=FLAT, fg='azure4')
panel_postre.pack(side=LEFT)

# Panel Derecha
panel_derecha = Frame(tk, bd=2, relief=FLAT)
panel_derecha.pack(side=RIGHT)

# Panel Calculadora
panel_calculadora = Frame(panel_derecha, bd=2, relief=FLAT, bg='burlywood')
panel_calculadora.pack()

# Panel recibo
panel_recibo = Frame(panel_derecha, bd=2, relief=FLAT, bg='burlywood')
panel_recibo.pack()

# Panel botones
panel_botones = Frame(panel_derecha, bd=2, relief=FLAT, bg='burlywood')
panel_botones.pack()

# Lista comidas
lista_comidas = ['pollo al curry', 'Merluza al pesto', 'Tortilla de patatas', 'Croquetas',
                 'pisto', 'salmorejo', 'Flamenquín Cordobés', 'Raviolis de setas']

# Lista bebidas
lista_bebidas = ['Agua', 'Coca-Cola', 'Fanta de Naranja', 'Fanta de Limón', 'Cerveza', 'Vino tinto',
                 'Vino blanco', 'Vino rosado']
# Lista postres
lista_postres = ['Tarta de abuela', 'Tarta de queso', 'Brownie de Nutella', 'Tarta de dulce de leche',
                 'Crepes caseros', 'Tortitas',
                 'Tarta de pionono', 'Tiramisú']

# Items comida
variables_comida = []
cuadros_comida = []
texto_comida = []
contador_comida = 0

for comida in lista_comidas:
    # Crear checkbuttons
    variables_comida.append('')
    variables_comida[contador_comida] = IntVar()
    comida = Checkbutton(panel_comida,
                         text=comida.title(),
                         font=('Dosis', 14),
                         onvalue=1,
                         offvalue=0,
                         variable=variables_comida[contador_comida],
                         command=revisar_check)
    comida.grid(row=contador_comida,
                column=0,
                sticky=W)

    # Crear cuadros de entrada
    cuadros_comida.append('')
    texto_comida.append('')
    texto_comida[contador_comida] = StringVar()
    texto_comida[contador_comida].set('0')
    cuadros_comida[contador_comida] = Entry(panel_comida,
                                            font=('Dosis', 12, 'bold'),
                                            bd=2,
                                            width=3,
                                            state=DISABLED,
                                            textvariable=texto_comida[contador_comida])
    cuadros_comida[contador_comida].grid(row=contador_comida,
                                         column=1)

    contador_comida += 1

# Items bebida
variables_bebida = []
cuadros_bebida = []
texto_bebida = []
contador_bebida = 0
for bebida in lista_bebidas:
    # crear checkbuttons
    variables_bebida.append('')
    variables_bebida[contador_bebida] = IntVar()
    bebida = Checkbutton(panel_bebida,
                         text=bebida.title(),
                         font=('Dosis', 14),
                         onvalue=1,
                         offvalue=0,
                         variable=variables_bebida[contador_bebida],
                         command=revisar_check)
    bebida.grid(row=contador_bebida,
                column=0,
                sticky=W)

    # Crear cuadros de entrada
    cuadros_bebida.append('')
    texto_bebida.append('')
    texto_bebida[contador_bebida] = StringVar()
    texto_bebida[contador_bebida].set('0')
    cuadros_bebida[contador_bebida] = Entry(panel_bebida,
                                            font=('Dosis', 12, 'bold'),
                                            bd=2,
                                            width=3,
                                            state=DISABLED,
                                            textvariable=texto_bebida[contador_bebida])
    cuadros_bebida[contador_bebida].grid(row=contador_bebida,
                                         column=1)

    contador_bebida += 1

# Items postre
variables_postre = []
cuadros_postre = []
texto_postre = []
contador_postre = 0
for postre in lista_postres:
    # crear checkbuttons
    variables_postre.append('')
    variables_postre[contador_postre] = IntVar()
    postre = Checkbutton(panel_postre,
                         text=postre.title(),
                         font=('Dosis', 14),
                         onvalue=1,
                         offvalue=0,
                         variable=variables_postre[contador_postre],
                         command=revisar_check)
    postre.grid(row=contador_postre,
                column=0,
                sticky=W)

    # Crear cuadros de entrada
    cuadros_postre.append('')
    texto_postre.append('')
    texto_postre[contador_postre] = StringVar()
    texto_postre[contador_postre].set('0')
    cuadros_postre[contador_postre] = Entry(panel_postre,
                                            font=('Dosis', 12, 'bold'),
                                            bd=2,
                                            width=3,
                                            state=DISABLED,
                                            textvariable=texto_postre[contador_postre])
    cuadros_postre[contador_postre].grid(row=contador_postre,
                                         column=1)

    contador_postre += 1

# variables
var_costo_comida = StringVar()
var_costo_bebida = StringVar()
var_costo_postre = StringVar()
var_subtotal = StringVar()
var_impuestos = StringVar()
var_total = StringVar()

# Etiquetas de costo y campos de entrada
# comida
etiqueta_costo_comida = Label(panel_costos,
                              text='Precio Comida',
                              font=('Dosis', 12, 'bold'),
                              bg='azure4',
                              fg='white')
etiqueta_costo_comida.grid(row=0, column=0)

texto_costo_comida = Entry(panel_costos,
                           font=('Dosis', 12, 'bold'),
                           bd=2,
                           width=10,
                           state='readonly',
                           textvariable=var_costo_comida)
texto_costo_comida.grid(row=0, column=1, padx=41)

# bebida
etiqueta_costo_bebida = Label(panel_costos,
                              text='Precio bebida',
                              font=('Dosis', 12, 'bold'),
                              bg='azure4',
                              fg='white')
etiqueta_costo_bebida.grid(row=1, column=0)

texto_costo_bebida = Entry(panel_costos,
                           font=('Dosis', 12, 'bold'),
                           bd=2,
                           width=10,
                           state='readonly',
                           textvariable=var_costo_bebida)
texto_costo_bebida.grid(row=1, column=1, padx=41)

# postres
etiqueta_costo_postre = Label(panel_costos,
                              text='Precio postre',
                              font=('Dosis', 12, 'bold'),
                              bg='azure4',
                              fg='white')
etiqueta_costo_postre.grid(row=2, column=0)

texto_costo_postre = Entry(panel_costos,
                           font=('Dosis', 12, 'bold'),
                           bd=2,
                           width=10,
                           state='readonly',
                           textvariable=var_costo_postre)
texto_costo_postre.grid(row=2, column=1, padx=41)

# subtotal
etiqueta_subtotal = Label(panel_costos,
                          text='Subtotal',
                          font=('Dosis', 12, 'bold'),
                          bg='azure4',
                          fg='white')
etiqueta_subtotal.grid(row=0, column=2)

texto_subtotal = Entry(panel_costos,
                       font=('Dosis', 12, 'bold'),
                       bd=2,
                       width=10,
                       state='readonly',
                       textvariable=var_subtotal)
texto_subtotal.grid(row=0, column=3, padx=41)

# impuestos
etiqueta_impuestos = Label(panel_costos,
                           text='impuestos',
                           font=('Dosis', 12, 'bold'),
                           bg='azure4',
                           fg='white')
etiqueta_impuestos.grid(row=1, column=2)

texto_impuestos = Entry(panel_costos,
                        font=('Dosis', 12, 'bold'),
                        bd=2,
                        width=10,
                        state='readonly',
                        textvariable=var_impuestos)
texto_impuestos.grid(row=1, column=3, padx=41)

# impuestos
etiqueta_total = Label(panel_costos,
                       text='TOTAL',
                       font=('Dosis', 14, 'bold'),
                       bg='azure4',
                       fg='white')
etiqueta_total.grid(row=2, column=2)

texto_total = Entry(panel_costos,
                    font=('Dosis', 12, 'bold'),
                    bd=2,
                    width=10,
                    state='readonly',
                    textvariable=var_total)
texto_total.grid(row=2, column=3, padx=41)

# Botones
botones = ['Total', 'Recibo', 'Guardar', 'Resetear']
botones_creados = []
columnas = 0
for boton in botones:
    boton = Button(panel_botones,
                   text=boton.title(),
                   font=('Dosis', 12, 'bold'),
                   fg='black',
                   bg='azure4',
                   bd=2,
                   width=4)
    botones_creados.append(boton)
    boton.grid(row=0, column=columnas)
    columnas += 1

botones_creados[0].config(command=total)
botones_creados[1].config(command=recibo)
botones_creados[2].config(command=guardar)
botones_creados[3].config(command=resetear)

# area de recibo
texto_recibo = Text(panel_recibo,
                    font=('Dosis', 12, 'bold'),
                    bd=2,
                    width=42,
                    height=10)
texto_recibo.grid(row=0, column=0)

# Calculadora
visor_calculadora = Entry(panel_calculadora,
                          font=('Dosis', 16, 'bold'),
                          width=22,
                          bd=2)
visor_calculadora.grid(row=0, column=0,
                       columnspan=4)

# Botones calculadora
botones_calculadora = ['7', '8', '9', '+',
                       '4', '5', '6', '-',
                       '1', '2', '3', 'x',
                       'CE', 'Borrar', '0', '/']

botones_guardados = []
fila = 1
columnas = 0
for boton in botones_calculadora:
    boton = Button(panel_calculadora,
                   text=boton.title(),
                   font=('Dosis', 16, 'bold'),
                   bd=2,
                   width=4)
    botones_guardados.append(boton)
    boton.grid(row=fila, column=columnas)

    if columnas == 3:
        fila += 1

    columnas += 1

    if columnas == 4:
        columnas = 0

botones_guardados[0].config(command=lambda: click_boton('7'))
botones_guardados[1].config(command=lambda: click_boton('8'))
botones_guardados[2].config(command=lambda: click_boton('9'))
botones_guardados[3].config(command=lambda: click_boton('+'))
botones_guardados[4].config(command=lambda: click_boton('4'))
botones_guardados[5].config(command=lambda: click_boton('5'))
botones_guardados[6].config(command=lambda: click_boton('6'))
botones_guardados[7].config(command=lambda: click_boton('-'))
botones_guardados[8].config(command=lambda: click_boton('1'))
botones_guardados[9].config(command=lambda: click_boton('2'))
botones_guardados[10].config(command=lambda: click_boton('3'))
botones_guardados[11].config(command=lambda: click_boton('*'))
botones_guardados[12].config(command=obtener_resultado)
botones_guardados[13].config(command=borrar)
botones_guardados[14].config(command=lambda: click_boton('0'))
botones_guardados[15].config(command=lambda: click_boton('/'))

tk.mainloop()
