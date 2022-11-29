from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

from random import *
from pint import UnitRegistry
ureg=UnitRegistry()
ureg.define('M_sun = (1.988435 *(10**33)) * g')


#print(450. * nm.to(pc))
#print((450. * nm).to(pc))

from sympy import *

x, y = symbols('x y')
f = Function('f')
#x=3
e=2.718281828
q_e=1.602E-19
G_Newton=6.67E-8
h_Planck=4.136E-15
c=2.99792E10
m_e=9.10938E-28
m_p=1.67262E-24
mu_mass=1.88353E-25
K_b=1.381E-16
N_A=6.022E23
Ste_Bol=5.6704E-5
Eps_0=8.85E-12
alpha=1.0/137.036
Mu_0=4*pi*10**-7
R=N_A*K_b

K_Wien=2.89777E-5
Thomson=6.652E-25
a_0=h_Planck/(2*pi*alpha*c*m_e)
Ry=2.1799E-18
phi=(1+sqrt(5))/2

def log10(Numero):
	return log(Numero,10)
def mean(lista):
	somma=float(sum(lista)) / max(len(lista), 1)
	if(somma>1):
		somma=round(somma,2)
	return somma
def Pythagoras(a,b):
	somma=sqrt(a**2+b**2)
	if(somma>1):
		somma=round(somma,2)
	return somma
def Quad_eq(a,b,c):
	if(b**2-4*a*c>=0):
		sol_p=(-b+sqrt(b**2-4*a*c))/(2*a)
		sol_m=(-b-sqrt(b**2-4*a*c))/(2*a)
		lista=[sol_p,sol_m]
	else:
		lista=["No solution"]
	return lista
def var(lista):
	m=mean(lista)
	somma=sum((xi - m) ** 2 for xi in lista) / len(lista)
	if(somma>1):
		somma=round(somma,2)
	return somma

def Unit_conv(a,sgn_1,sgn_2):
	Q_=ureg.Quantity
	home = Q_(a, eval("ureg."+sgn_1))
	conv_coeff=(home.to(sgn_2))
	sol=(conv_coeff.magnitude)
	if(sol>1):
		sol=round(sol,2)
	return sol

class MainApp(App):
	def build(self):
		self.operators = ["/", "*", "+", "-","**"]
		self.Num_layout=0
		self.Precisione=3
		self.last_was_operator = None
		self.last_button = None
		self.main_layout = BoxLayout(orientation="vertical")
		self.solution = TextInput(multiline=True,readonly=True,halign="right", font_size=55)
		self.main_layout.add_widget(self.solution)
		buttons1 = [
			["sin", "cos", "tan", "e","pi","Back"],
        	["sinh", "cosh", "tanh", "log","Mode-","Mode+"],
        	["random", "mean", "var", "[","]"],
        	["7", "8", "9", "(",")"],
        	["4", "5", "6", "*","/"],
        	["1", "2", "3", "+","-"],
        	[".", "0", "C", "**",","],
		]
		red = [1,0,0,1]
		green = [0,1,0,1]
		blue =  [0.2,0.3,1,1]
		purple = [1,0,1,1]
		colors=[red, green, blue, purple]
		cont=0
		for row in buttons1:
			h_layout = BoxLayout()
			cont2=0
			for label in row:
				if(cont<3):
					button = Button(text=label, pos_hint={"center_x": 0.5, "center_y": 0.5}, background_color=colors[0])
				else:
					if(cont2>2):
						button = Button(text=label, pos_hint={"center_x": 0.5, "center_y": 0.5}, background_color=colors[2])
					else:
						button = Button(text=label, pos_hint={"center_x": 0.5, "center_y": 0.5}, background_color=colors[1])
				button.bind(on_press=self.on_button_press)
				h_layout.add_widget(button)
				cont2+=1
			self.main_layout.add_widget(h_layout)
			cont+=1

			equals_button = Button(
			text="=", pos_hint={"center_x": 0.5, "center_y": 0.5}, background_color=colors[3]
		)
		equals_button.bind(on_press=self.on_solution)
		self.main_layout.add_widget(equals_button)

		return self.main_layout
	
	def Precision(self,Numero):
		self.Precisione=Numero	
	
	def build_buttons(self,mode):
		if mode==0:
			buttons1 = [
				["sin", "cos", "tan", "e","pi","Back"],
		    	["sinh", "cosh", "tanh", "log","Mode-","Mode+"],
		    	["random", "mean", "var", "[","]"],
		    	["7", "8", "9", "(",")"],
		    	["4", "5", "6", "*","/"],
		    	["1", "2", "3", "+","-"],
		    	[".", "0", "C", "**",","],
        	]
		if mode==1:
			buttons1= [["asin", "acos", "atan", "Quad_eq","factorial","Back"],
			["asinh", "acosh", "atanh", "log10","Mode-","Mode+"],
			["integrate","diff","x", "[","]"],
			["7", "8", "9", "(",")"],
			["4", "5", "6", "*","/"],
			["1", "2", "3", "+","-"],
			[".", "0", "C", "**",","],
			]
		if mode==2:
			buttons1= [
				["q_e", "Eps_0","Mu_0", "C","Back"],
				["Ste_Bol", "K_Wien", "a_0", "Mode-","Mode+"],
				["alpha","Thomson","Ry", "[","]"],
				["c", "G_Newton", "h_Planck", "(",")"],
				["m_e", "m_p", "mu_mass", "*","/"],
				["K_b", "N_A", "R", "+","-"],
				["Prec-", "0", "Prec+", "**",","],
			]
		if mode==3:
			buttons1= [
				["p", "n", "u", "m","c","d","Back","C"],
				["da", "h", "k", "M","G","T","Mode-","Mode+"],
				["s","h","d","yr","degF", "degC", "degR","K"],
				["J", "eV", "erg","cal","Wh","deg","rad"],
				["Pa","bar","atm", "torr","M_sun","g","lb"],
				["m", "pc", "ly", "au","inch","ft","mile"],
				["mps", "kph", "mph", "(",")","*","1",".to"],
			]
		if mode==4:
			buttons1= [["det", "eigenvals", "eigenvects", "Matrix","Back"],
			["limit", "series", "dsolve", "inv","Mode-","Mode+"],
			["oo","f","x", "[","]"],
			["7", "8", "9", "(",")"],
			["4", "5", "6", "*","/"],
			["1", "2", "3", "+","-"],
			[".", "0", "C", "**",","],
			]
		return buttons1
	def build_layout(self,mode):
		for child in self.main_layout.children[:]:
			self.main_layout.remove_widget(child)
		
		red = [1,0,0,1]
		green = [0,1,0,1]
		blue =  [0.2,0.3,1,1]
		purple = [1,0,1,1]
		yellow = [1,0.5,0.1,1]
		colors=[red, green, blue, purple,yellow]
		self.main_layout.add_widget(self.solution)
		buttons1 = self.build_buttons(mode)
		
		cont=0
		for row in buttons1:
			cont2=0
			h_layout = BoxLayout()
			for label in row:
				if(mode==0 or mode==1 or mode==4):
					if(cont<3):
						button = Button(text=label, pos_hint={"center_x": 0.5, "center_y": 0.5}, background_color=colors[0])
					else:
						if(cont2>2):
							button = Button(text=label, pos_hint={"center_x": 0.5, "center_y": 0.5}, background_color=colors[2])
						else:
							button = Button(text=label, pos_hint={"center_x": 0.5, "center_y": 0.5}, background_color=colors[1])	
				elif(mode==2):
					if(cont2>2 and cont<3):
						button = Button(text=label, pos_hint={"center_x": 0.5, "center_y": 0.5}, background_color=colors[0])
					else:
						if(cont2>2):
							button = Button(text=label, pos_hint={"center_x": 0.5, "center_y": 0.5}, background_color=colors[2])
						else:
							button = Button(text=label, pos_hint={"center_x": 0.5, "center_y": 0.5}, background_color=colors[1])
				elif(mode==3):
					if(cont2>5 and cont<2):
						button = Button(text=label, pos_hint={"center_x": 0.5, "center_y": 0.5}, background_color=colors[0])
					elif(cont>5 and cont2>2):
						button = Button(text=label, pos_hint={"center_x": 0.5, "center_y": 0.5}, background_color=colors[2])
					elif((cont>1 and cont<6) or (cont==6 and cont2<3)):
						button = Button(text=label, pos_hint={"center_x": 0.5, "center_y": 0.5}, background_color=colors[1])
					else:
						button = Button(text=label, pos_hint={"center_x": 0.5, "center_y": 0.5}, background_color=colors[4])
				button.bind(on_press=self.on_button_press)
				h_layout.add_widget(button)
				cont2+=1
			self.main_layout.add_widget(h_layout)
			cont+=1
		equals_button = Button(text="=", pos_hint={"center_x": 0.5, "center_y": 0.5}, background_color=colors[3])
		equals_button.bind(on_press=self.on_solution)
		self.main_layout.add_widget(equals_button)

		
	
	def on_button_press(self, instance):
		current = self.solution.text
		button_text = instance.text

		if button_text == "C":
			# Clear the solution widget
			self.solution.text = ""
		elif button_text == "Back":
			self.solution.text = current[:-1]
		elif button_text == "Mode+":
			if(self.Num_layout<4):
				self.Num_layout+=1
				self.build_layout(self.Num_layout)
			else:
				self.Num_layout=0
				self.build_layout(self.Num_layout)
		elif button_text=="Mode-":
			if(self.Num_layout>0):
				self.Num_layout-=1
				self.build_layout(self.Num_layout)
			else:
				self.Num_layout=4
				self.build_layout(self.Num_layout)
		elif button_text=="Prec+":
			self.Precisione+=1
		elif button_text=="Prec-":
			if(self.Precisione > 1):
				self.Precisione-=1
		else:
			if current and (
                self.last_was_operator and button_text in self.operators):
                # Don't add two operators right after each other
				return
			elif current == "" and button_text in self.operators:
                # First character cannot be an operator
				return
			else:
				new_text = current + button_text
				self.solution.text = new_text
			self.last_button = button_text
			self.last_was_operator = self.last_button in self.operators

	def on_solution(self, instance):
		text = self.solution.text
		if text:
			if(text.find('.to(') != -1):
				try:
					pos_per=text.find('*')
					a=float(text[:int(pos_per)])
					sgn_1_start=text.find('(')
					sgn_1_end=text.find(')')
					sgn_1=(text[int(sgn_1_start)+1:int(sgn_1_end)])
					sgn_2_start=text.find('(',sgn_1_end)
					sgn_2_end=text.find(')',sgn_2_start)
					sgn_2=(text[int(sgn_2_start)+1:int(sgn_2_end)])
					solution = str(N(Unit_conv(a,sgn_1,sgn_2),self.Precisione))
				except:
					solution = "Error"
			elif(text.find('Quad') == -1 and text.find('eigen')==-1):
				try:
					solution = str(eval("N("+self.solution.text+","+str(self.Precisione)+")"))
				except:
					solution = "Error"
					#solution = str(eval("N("+self.solution.text+","+str(self.Precisione)+")"))
			else:
				try:
					solution = str(eval(self.solution.text))
				except:
					#solution = "Error"
					solution = str(eval(self.solution.text))
			self.solution.text = solution

if __name__ == "__main__":
    app = MainApp()
    app.run()

