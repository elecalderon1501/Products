from tkinter import ttk
from tkinter import *

import sqlite3 
# modulo para conexion

class Product:

    def __init__(self, window):
        self.wind =  window
        self.wind.title('Products Application')

#Frame Container
        frame = LabelFrame(self.wind, text = 'Register A new Product')
        frame.grid(row = 0, column = 0, columnspan = 3, pady = 20)
        #columnspan --> columnas vacias pady --> padding

        #Name Input
        Label(frame, text = 'Name:').grid(row = 1, column = 0)
        self.name = Entry(frame)
        self.name.focus()
        #focus --> posiciona el cursor en el input
        self.name.grid(row = 1, column = 1)

        #Price input
        Label(frame, text = 'Price: ').grid(row = 2, column = 0)
        self.price = Entry(frame)
        self.price.grid(row = 2, column = 1)

        #Button add product
        ttk.Button(frame, text = 'Save Product').grid(row = 3, columnspan = 2, sticky = W + E)
        #sticky = W + E --> asi ocupa todo el ancho, 'de este a oeste' 

        #Table
        self.tree = ttk.Treeview(height = 10, columns = 2)
        self.tree.grid(row = 4, column = 0, columnspan = 2)
        self.tree.heading('#0', text = 'Name', anchor = CENTER)
        #encabezado de la primer columna
        


        
if __name__== '__main__':
    window = Tk()
    application = Product(window)    
    window.mainloop()

