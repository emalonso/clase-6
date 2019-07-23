from calculadora import *
from Tkinter import *
from functools import partial
from tkFont import Font

class Interefaz():
	def __init__(self):
		self.valNumero = ""
		self.root = Tk()
		self.calc = Calculadora()
		self.frame = Frame(self.root)
		self.frame.pack(expand=True)
		self.root.geometry('300x500')
		self.comic=Font(family = 'Comic Sans MS',size=20)
		self.comic2=Font(family = 'Comic Sans MS',size=12,slant='italic')
		self.comic3=Font(family = 'Comic Sans MS',size=16)
		
		self.valor = StringVar()
		self.valor.set("0")
		self.display = Label(self.frame, textvariable = self.valor, width=18,height =3,relief = GROOVE,font =self.comic,bg="white")
		self.display.grid(row=0, column=0, columnspan=4)
		
		self.btn7 = Button(self.frame, text="7", command=partial(self.capturavalor, "7"),width=5,height =3,font=self.comic2,relief=GROOVE)
		#self.btn7.bind("<Button-1>", self.capturavalor)
		self.btn7.grid(row=1, column=0)
		        
		self.btn8 = Button(self.frame, text="8", command=partial(self.capturavalor, "8"), width=5,height =3,font=self.comic2,relief=GROOVE)
		#self.btn8.bind("<Button-1>", self.capturavalor)
		self.btn8.grid(row=1, column=1)
		        
		self.btn9 = Button(self.frame, text="9", command=partial(self.capturavalor, "9"), width=5,height =3,font=self.comic2,relief=GROOVE)
		#self.btn9.bind("<Button-1>", self.capturavalor)
		self.btn9.grid(row=1, column=2)
		
		self.btn4 = Button(self.frame, text="4", command=partial(self.capturavalor, "4"),width=5,height =3,font=self.comic2,relief=GROOVE)
		#self.btn4.bind("<Button-1>", self.capturavalor)
		self.btn4.grid(row=2, column=0)
		
		self.btn5 = Button(self.frame, text="5", command=partial(self.capturavalor, "5"),width=5,height =3,font=self.comic2,relief=GROOVE)
		#self.btn5.bind("<Button-1>", self.capturavalor)
		self.btn5.grid(row=2, column=1)		
		
		self.btn6 = Button(self.frame, text="6", command=partial(self.capturavalor, "6"),width=5,height =3,font=self.comic2,relief=GROOVE)
		#self.btn6.bind("<Button-1>", self.capturavalor)
		self.btn6.grid(row=2, column=2)
		
		self.btn1 = Button(self.frame, text="1", command=partial(self.capturavalor, "1"),width=5,height =3,font=self.comic2,relief=GROOVE)
		#self.btn1.bind("<Button-1>", self.capturavalor)
		self.btn1.grid(row=3, column=0)
		
		self.btn2 = Button(self.frame, text="2", command=partial(self.capturavalor, "2"),width=5,height =3,font=self.comic2,relief=GROOVE)
		#self.btn2.bind("<Button-1>", self.capturavalor)
		self.btn2.grid(row=3, column=1)
		
		self.btn3 = Button(self.frame, text="3", command=partial(self.capturavalor, "3"),width=5,height =3,font=self.comic2,relief=GROOVE)
		#self.btn3.bind("<Button-1>", self.capturavalor)
		self.btn3.grid(row=3, column=2)	
		
		self.btn0 = Button(self.frame, text="0", command=partial(self.capturavalor, "0"),width=5,height =3,font=self.comic2,relief=GROOVE)
		#self.btn0.bind("<Button-1>", self.capturavalor)
		self.btn0.grid(row=4, column=1)
		
		self.btnIniciar = Button(self.frame, text="CE",width=4,height =2,font=self.comic3,relief=GROOVE)
		self.btnIniciar.bind("<Button-1>", self.reiniciar)
		self.btnIniciar.grid(row=4, column=0)
		
		self.btnIgual = Button(self.frame, text="=",width=4,height =2,font=self.comic3,relief=GROOVE,bg="gray")
		self.btnIgual.bind("<Button-1>", self.resultado)
		self.btnIgual.grid(row=4, column=2)
		
		self.btnSuma = Button(self.frame, text="+", command=partial(self.operacion, "S"),width=4,height =2,font=self.comic3,relief=GROOVE)
		#self.btnSuma.bind("<Button-1>", self.resultado)
		self.btnSuma.grid(row=1, column=3)
		        
		self.btnResta = Button(self.frame, text="-", command=partial(self.operacion, "R"),width=4,height =2,font=self.comic3,relief=GROOVE)
		#self.btnResta.bind("<Button-1>", self.resultado)
		self.btnResta.grid(row=2, column=3)
		        
		self.btnMultiplicacion = Button(self.frame, text="*", command=partial(self.operacion, "M"),width=4,height =2,font=self.comic3,relief=GROOVE)
		#self.btnMultiplicacion.bind("<Button-1>", self.resultado)
		self.btnMultiplicacion.grid(row=3, column=3)
		
		self.btnDivision = Button(self.frame, text="/", command=partial(self.operacion, "D"),width=4,height =2,font=self.comic3,relief=GROOVE)
		#self.btnDivision.bind("<Button-1>", self.resultado)
		self.btnDivision.grid(row=4, column=3)

		
		self.root.mainloop()
		
	#@save_to_log
	
	def reiniciar(self, event):
		self.calc.iniciar()
		self.valNumero = ""
		self.imprimirValor("0")
	
	def resultado(self, event):
		resultado = self.calc.operacion(int(self.valNumero))
		self.valNumero = str(resultado)
		print str(resultado)
		self.imprimirValor(resultado)
	
	def operacion(self, operacion):
		self.calc.numero = int(self.valNumero)
		self.calc.tip_oper = operacion
		self.valNumero = ""
	
	def capturavalor(self, valor):
		self.valNumero = self.valNumero + str(valor)		
		print self.valNumero
		self.imprimirValor(self.valNumero)
	
	def imprimirValor(self, valor):
		self.valor.set(valor)

app = Interefaz()


