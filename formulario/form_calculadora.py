# Importar los módulos requeridos
from tkinter import font
import tkinter as tk
from config import constantes as cons
from util.util_ventana import centrar_ventana 

class FormularioCalculadora(tk.Tk):
    def __init__(self):
        super().__init__()
        self.crear_ventana()
        self.crear_widget()
    
    # Crear ventana de la app
    def crear_ventana(self):
        self.title('by Paco Ruiz')
        self.config(bg=cons.color_1_negro)
        self.attributes('-alpha',0.96)
        self.resizable(False,False)
        w, h = 362, 450
        centrar_ventana(self,w,h)

    # Crear un label o ventanita de prueba
    def crear_widget(self):
        self.oper_label = tk.Label(self, text='BPR',font=('Arial',16),bd=1,
        bg=cons.color_1_negro,fg=cons.color_2_blanco,justify='center')
        self.oper_label.grid(row=0,column=3,padx=10,pady=10)
        
        # Pantalla de operación
        self.entry = tk.Entry(self, width=12, font=('Arial',35),bd=1,
        bg=cons.color_3_celeste,fg=cons.color_1_negro,justify='right')
        self.entry.grid(row=1,column=0,columnspan=4,padx=10,pady=10)

        # Crear botones de calculadora
        buttons = ['AC','<','%','÷',
                   '7','8','9','*',
                   '4','5','6','-',
                   '1','2','3','+',
                   '0','.','=']
        row_val = 2
        col_val = 0
        roboto_font = font.Font(family='Roboto', size=16)
        # Estructura de los botones
        for button in buttons:
            if button == '=':
                tk.Button(self,width=10,height=2,text=button,font=font.Font(size=16,weight='bold'),
                command= lambda b=button: self.click_button(b),
                bg=cons.color_3_celeste,fg=cons.color_1_negro).grid(row=row_val,
                column=col_val,columnspan=2, padx=0.5,pady=0.5)
            elif button in ['AC','<','%','÷','*','-','+','.']:
                tk.Button(self,width=4,height=2,text=button,font=font.Font(size=16),
                command= lambda b=button: self.click_button(b),
                bg=cons.color_3_celeste,fg=cons.color_1_negro).grid(row=row_val,
                column=col_val,padx=0.5,pady=0.5)
                button_font = roboto_font
            else:
                tk.Button(self,width=4,height=2,text=button,font=font.Font(size=16),
                command= lambda b=button: self.click_button(b),
                bg=cons.color_3_celeste,fg=cons.color_1_negro).grid(row=row_val,
                column=col_val,padx=0.5,pady=0.5)
                button_font = roboto_font
            col_val +=1
            if col_val > 3:
                col_val = 0
                row_val += 1
    
    # Operaciones lógicas 
    def click_button(self, value):
        if value == '=':
            try:
                expression = self.entry.get().replace('%', '/ 100')
                result = eval(expression)
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, str(result))
                operation = expression + ' ' + value
                self.oper_label.config(text=operation)
            except Exception:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, 'Error')
                self.oper_label.config(text='')
        elif value == 'AC':
            self.entry.delete(0, tk.END)
            self.oper_label.config(text='')
        elif value == '<':
            current_text = self.entry.get()
            new_text = current_text[:-1]
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, new_text)
            self.oper_label.config(text=new_text + '')
        else:
            current_text = self.entry.get()
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, current_text + value)
            if value == '=':
                self.entry.config(text='')



            










    
