from tkinter import *
ventana =Tk()
ventana.title("Marcos Python")
ventana.geometry("700x700")
###############################
marco_padre = Frame(ventana, width=250, height=250)
marco_padre.config(bg="lightblue",
             bd=12,
             relief="raised" #solid
)
marco_padre.pack(side=BOTTOM, anchor=S,fill=X, expand=YES)
###############################
###Primer Marco
marco = Frame(marco_padre, width=250, height=250)
marco.config(bg="red",
             bd=12,
             relief="raised" #solid
)
marco.pack(side=LEFT, anchor=SW)

##############2do Marco
marco = Frame(marco_padre, width=250, height=250)
marco.config(bg="green",
             bd=12,
             relief="raised" #solid
)
marco.pack(side=RIGHT, anchor=SE)

################Tercer MArco
marco_padre = Frame(ventana, width=250, height=250)
marco_padre.config(bg="lightblue",
             bd=12,
             relief="raised" #solid
)
marco_padre.pack(side=TOP, anchor=N,fill=X, expand=YES)
#####################
marco = Frame(marco_padre, width=250, height=250)
marco.config(bg="blue",
             bd=12,
             relief="raised" #solid
)
marco.pack(side=LEFT)
marco = Frame(marco_padre, width=250, height=250)
marco.config(bg="orange",
             bd=12,
             relief="raised" #solid
)
marco.pack(side=RIGHT)
#####################
ventana.mainloop()