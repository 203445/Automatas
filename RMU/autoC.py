
# from PyPDF2 import PdfReader
import PyPDF2
from tkinter.font import Font
import tkinter	as tk
from tkinter import ttk


mypdf = open('ReciboAgosto.pdf',mode='rb')
# Llame a la función PdfFileReader
pdf_document = PyPDF2.PdfFileReader(mypdf)

# Utilice las variables del objeto PdfFileReader 
# para obtener información diversa, como el atributo numPages para obtener el número de páginas del documento PDF
pdf_document.numPages  

first_page = pdf_document.getPage(0)

text = first_page.extractText()

separator = text.split('\n')

ora = []

# lineas = 

for i in separator:
    ora.append(i)

str_1 = [s for s in ora if "RMU" in s]
rm = str(str_1)[7:41]

str_match = [s for s in ora if "PAGAR" in s]
new = str(str_match).split('TOTAL A PAGAR:')
n2 =" ".join(new)[2:42]


# for j in ora: 
l = ora.index('-1-')+1
print(ora[l])

ventana = tk.Tk()
ventana.title("Verificador de RMU")
ventana.config(width=400, height=400,background="#DCF5D1")

label2 = ttk.Label(text="I'm at (75, 75)", font=Font(size=15))
label2.place(x=30, y=30)

etiqueta_rmu = ttk.Label(text="Verificar RMU: ",background="#DCF5D1",style="BW.TLabel")
etiqueta_rmu.place(x=50,y=50)
ventana.mainloop()

class FSM:
    def __init__(self):
        self.__table = {}
        self.__initial_states = set()
        self.__final_states = set()
 
    def add_transition(self, state, symbol, new_states):
        """
            state = string
            symbol = string, len = 1
            new_states = list
        """
        try:
            self.__table[state]
        except:
            self.__table[state] = {}
            
        if type(new_states) == str:
            self.__table[state][symbol] = set([new_states])
        else:
            self.__table[state][symbol] = set(new_states)
 
    def add_initial_states(self, states):
        """
            state = list or str
        """
        if type(states) == str:
            self.__initial_states.update([states])
        else:
            self.__initial_states.update(states)
 
    def add_final_states(self, states):
        """
            states = list or str
        """
        if type(states) == str:
            self.__final_states.update([states])
        else:
            self.__final_states.update(states)
 
    def __get_new_states_e(self, states):
        visited_states_a = states.copy()
        visited_states_b = set()
        current_states = visited_states_a.difference(visited_states_b)
        while current_states:
            visited_states_b.update(visited_states_a)
            for state in current_states:
                try:
                    self.__table[state][""]
                except KeyError:
                    pass
                else:
                    visited_states_a.update(self.__table[state][""])
            current_states = visited_states_a.difference(visited_states_b)
        states.update(visited_states_a)
 
    def __get_new_states(self, states, symbol):
        new_states = set()
        for state in states:
            try:
                self.__table[state][symbol]
            except KeyError:
                pass
            else:
                new_states.update(self.__table[state][symbol])
            # print (new_states, "aqui")
        return new_states
                
        
    def evaluate(self, string): #string
        """
            returns:
                0 -> Match
                1 -> No match
        """
        states = self.__initial_states.copy()
        self.__get_new_states_e(states)
        for c in string:
            new_states = self.__get_new_states(states, c)
            self.__get_new_states_e(new_states)
            # print(string)
            # print(c)
            states = new_states
            # print(states.intersection(self.__final_states))
        return bool(states.intersection(self.__final_states))
 
    def print_fsm(self):
        print ("Table:")
        for state in self.__table:
            for symbol in self.__table[state]:
                print ("(%s, '%s') -> %s" % (state, symbol, self.__table[state][symbol]))
                
        print ("\nFinal States:")
        print (self.__final_states)
        print ("\nInitial_states")
        print (self.__initial_states)
        print ("")
 
fsm = FSM()
prd = FSM()
kwh = FSM()

fsm.add_initial_states("q0")
 
#CÓDIGO POSTAL 

fsm.add_transition("q0", "0", "q1")
fsm.add_transition("q0", "1", "q1")
fsm.add_transition("q0", "2", "q1")
fsm.add_transition("q0", "3", "q1")
fsm.add_transition("q0", "4", "q1")
fsm.add_transition("q0", "5", "q1")
fsm.add_transition("q0", "6", "q1")
fsm.add_transition("q0", "7", "q1")
fsm.add_transition("q0", "8", "q1")
fsm.add_transition("q0", "9", "q1")

fsm.add_transition("q1", "0", "q2")
fsm.add_transition("q1", "1", "q2")
fsm.add_transition("q1", "2", "q2")
fsm.add_transition("q1", "3", "q2")
fsm.add_transition("q1", "4", "q2")
fsm.add_transition("q1", "5", "q2")
fsm.add_transition("q1", "6", "q2")
fsm.add_transition("q1", "7", "q2")
fsm.add_transition("q1", "8", "q2")
fsm.add_transition("q1", "9", "q2")

fsm.add_transition("q2", "0", "q3")
fsm.add_transition("q2", "1", "q3")
fsm.add_transition("q2", "2", "q3")
fsm.add_transition("q2", "3", "q3")
fsm.add_transition("q2", "4", "q3")
fsm.add_transition("q2", "5", "q3")
fsm.add_transition("q2", "6", "q3")
fsm.add_transition("q2", "7", "q3")
fsm.add_transition("q2", "8", "q3")
fsm.add_transition("q2", "9", "q3")

fsm.add_transition("q3", "0", "q8")
fsm.add_transition("q3", "1", "q8")
fsm.add_transition("q3", "2", "q8")
fsm.add_transition("q3", "3", "q8")
fsm.add_transition("q3", "4", "q8")
fsm.add_transition("q3", "5", "q8")
fsm.add_transition("q3", "6", "q8")
fsm.add_transition("q3", "7", "q8")
fsm.add_transition("q3", "8", "q8")
fsm.add_transition("q3", "9", "q8")

fsm.add_transition("q8", "0", "q9")
fsm.add_transition("q8", "1", "q9")
fsm.add_transition("q8", "2", "q9")
fsm.add_transition("q8", "3", "q9")
fsm.add_transition("q8", "4", "q9")
fsm.add_transition("q8", "5", "q9")
fsm.add_transition("q8", "6", "q9")
fsm.add_transition("q8", "7", "q9")
fsm.add_transition("q8", "8", "q9")
fsm.add_transition("q8", "9", "q9")

# ESPACIO
fsm.add_transition("q9", " ", "q10")

#--------------- AÑOS----------------

fsm.add_transition("q10", "0", "q11")
fsm.add_transition("q10", "1", "q11")
fsm.add_transition("q10", "2", "q11")
fsm.add_transition("q10", "3", "q11")
fsm.add_transition("q10", "4", "q11")
fsm.add_transition("q10", "5", "q11")
fsm.add_transition("q10", "6", "q11")
fsm.add_transition("q10", "7", "q11")
fsm.add_transition("q10", "8", "q11")
fsm.add_transition("q10", "9", "q11")

fsm.add_transition("q11", "0", "q12")
fsm.add_transition("q11", "1", "q12")
fsm.add_transition("q11", "2", "q12")
fsm.add_transition("q11", "3", "q12")
fsm.add_transition("q11", "4", "q12")
fsm.add_transition("q11", "5", "q12")
fsm.add_transition("q11", "6", "q12")
fsm.add_transition("q11", "7", "q12")
fsm.add_transition("q11", "8", "q12")
fsm.add_transition("q11", "9", "q12")

# MEJORANDO
fsm.add_transition("q12", "-", "q13")


#------------- MES ------------------

fsm.add_transition("q13", "0", "q14")

fsm.add_transition("q14", "1", "q15")
fsm.add_transition("q14", "2", "q15")
fsm.add_transition("q14", "3", "q15")
fsm.add_transition("q14", "4", "q15")
fsm.add_transition("q14", "5", "q15")
fsm.add_transition("q14", "6", "q15")
fsm.add_transition("q14", "7", "q15")
fsm.add_transition("q14", "8", "q15")
fsm.add_transition("q14", "9", "q15")

fsm.add_transition("q13", "1", "q16")

fsm.add_transition("q16", "0", "q17")
fsm.add_transition("q16", "1", "q17")
fsm.add_transition("q16", "2", "q17")


fsm.add_transition("q15", "-", "q18")
fsm.add_transition("q17", "-", "q18")


# -----------DIAS-----------------

fsm.add_transition("q18", "0", "q19") 

fsm.add_transition("q19", "1", "q20")
fsm.add_transition("q19", "2", "q20")
fsm.add_transition("q19", "3", "q20")
fsm.add_transition("q19", "4", "q20")
fsm.add_transition("q19", "5", "q20")
fsm.add_transition("q19", "6", "q20")
fsm.add_transition("q19", "7", "q20")
fsm.add_transition("q19", "8", "q20")
fsm.add_transition("q19", "9", "q20")

fsm.add_transition("q18", "1", "q21")
fsm.add_transition("q18", "2", "q21")  

fsm.add_transition("q21", "0", "q22")
fsm.add_transition("q21", "1", "q22")
fsm.add_transition("q21", "2", "q22")
fsm.add_transition("q21", "3", "q22")
fsm.add_transition("q21", "4", "q22")
fsm.add_transition("q21", "5", "q22")
fsm.add_transition("q21", "6", "q22")
fsm.add_transition("q21", "7", "q22")
fsm.add_transition("q21", "8", "q22")
fsm.add_transition("q21", "9", "q22")


fsm.add_transition("q18", "3", "q23")

fsm.add_transition("q23", "0", "q24")
fsm.add_transition("q23", "1", "q24")

fsm.add_transition("q20", " ", "q25")
fsm.add_transition("q22", " ", "q25")
fsm.add_transition("q24", " ", "q25")


# -----CADENA DE XAXX-010101 -------

fsm.add_transition("q25", "X", "q26")
fsm.add_transition("q26", "A", "q27")
fsm.add_transition("q27", "X", "q28")
fsm.add_transition("q28", "X", "q29")

fsm.add_transition("q29", "-", "q30") 

fsm.add_transition("q30", "0", "q31")
fsm.add_transition("q31", "1", "q32")
fsm.add_transition("q32", "0", "q33")
fsm.add_transition("q33", "1", "q34")
fsm.add_transition("q34", "0", "q35")
fsm.add_transition("q35", "1", "q36")

fsm.add_transition("q36", " ", "q37")
# --- FOLIO DE 000-999 ----

fsm.add_transition("q37", "0", "q38")
fsm.add_transition("q37", "1", "q38")
fsm.add_transition("q37", "2", "q38")
fsm.add_transition("q37", "3", "q38")
fsm.add_transition("q37", "4", "q38")
fsm.add_transition("q37", "5", "q38")
fsm.add_transition("q37", "6", "q38")
fsm.add_transition("q37", "7", "q38")
fsm.add_transition("q37", "8", "q38")
fsm.add_transition("q37", "9", "q38")


fsm.add_transition("q38", "0", "q39")
fsm.add_transition("q38", "1", "q39")
fsm.add_transition("q38", "2", "q39")
fsm.add_transition("q38", "3", "q39")
fsm.add_transition("q38", "4", "q39")
fsm.add_transition("q38", "5", "q39")
fsm.add_transition("q38", "6", "q39")
fsm.add_transition("q38", "7", "q39")
fsm.add_transition("q38", "8", "q39")
fsm.add_transition("q38", "9", "q39")

fsm.add_transition("q39", "0", "q40")
fsm.add_transition("q39", "1", "q40")
fsm.add_transition("q39", "2", "q40")
fsm.add_transition("q39", "3", "q40")
fsm.add_transition("q39", "4", "q40")
fsm.add_transition("q39", "5", "q40")
fsm.add_transition("q39", "6", "q40")
fsm.add_transition("q39", "7", "q40")
fsm.add_transition("q39", "8", "q40")
fsm.add_transition("q39", "9", "q40")

fsm.add_transition("q40", " ", "q41")


# -----DIGÍTOS NECESARIOS TERMINALES CFE------
fsm.add_transition("q41", "C", "q42")
fsm.add_transition("q42", "F", "q43")
fsm.add_transition("q43", "E", "q44")


fsm.add_final_states(("q44"))

# fsm.print_fsm()

print(fsm.evaluate(rm))

# if ora[23] == "Energía (kWh)":
#     print (fsm.evaluate(ora[27]))

# if  ora[22] == "Energía (kWh)" :  
#     print (fsm.evaluate(ora[26]))

# for x in ora:  
#     # print(x) 
#     prd.evaluate(x)

# if prd.evaluate == True:
#         print("El rum es valido")
# else:
#         print("No cumple")        



prd.add_initial_states("q0")

prd.add_transition("q0", "P", "q1")
prd.add_transition("q1", "E", "q2")
prd.add_transition("q2", "R", "q3")
prd.add_transition("q3", "I", "q4")
prd.add_transition("q4", "O", "q5")
prd.add_transition("q5", "D", "q6")
prd.add_transition("q6", "O", "q7")
prd.add_transition("q7", " ", "q8")
prd.add_transition("q8", "F", "q9")
prd.add_transition("q9", "A", "q10")
prd.add_transition("q10", "C", "q11")
prd.add_transition("q11", "T", "q12")
prd.add_transition("q12", "U", "q13")
prd.add_transition("q13", "R", "q14")
prd.add_transition("q14", "A", "q15")
prd.add_transition("q15", "D", "q16")
prd.add_transition("q16", "O", "q17")
prd.add_transition("q17", ":", "q18")
prd.add_transition("q18", " ", "q19")

# ------------FECHA------------------
prd.add_transition("q19", "0", "q20") 

prd.add_transition("q20", "1", "q21")
prd.add_transition("q20", "2", "q21")
prd.add_transition("q20", "3", "q21")
prd.add_transition("q20", "4", "q21")
prd.add_transition("q20", "5", "q21")
prd.add_transition("q20", "6", "q21")
prd.add_transition("q20", "7", "q21")
prd.add_transition("q20", "8", "q21")
prd.add_transition("q20", "9", "q21")

prd.add_transition("q19", "1", "q22")
prd.add_transition("q19", "2", "q22")  

prd.add_transition("q22", "0", "q23")
prd.add_transition("q22", "1", "q23")
prd.add_transition("q22", "2", "q23")
prd.add_transition("q22", "3", "q23")
prd.add_transition("q22", "4", "q23")
prd.add_transition("q22", "5", "q23")
prd.add_transition("q22", "6", "q23")
prd.add_transition("q22", "7", "q23")
prd.add_transition("q22", "8", "q23")
prd.add_transition("q22", "9", "q23")


prd.add_transition("q19", "3", "q24")

prd.add_transition("q24", "0", "q25")
prd.add_transition("q24", "1", "q25")

prd.add_transition("q21", " ", "q26")
prd.add_transition("q23", " ", "q26")
prd.add_transition("q25", " ", "q26")

# -------------MESES--------------
prd.add_transition("q26", "F", "q27")
prd.add_transition("q27", "E", "q28")
prd.add_transition("q28", "B", "q38")#FINAL

prd.add_transition("q26", "A", "q29")
prd.add_transition("q29", "B", "q30")
prd.add_transition("q30", "R", "q38")# FINAL

prd.add_transition("q29", "G", "q31")
prd.add_transition("q31", "O", "q38")# FINAL


prd.add_transition("q26", "J", "q32")
prd.add_transition("q32", "U", "q33")
prd.add_transition("q33", "N", "q38") #FINAL

prd.add_transition("q26", "O", "q34")
prd.add_transition("q34", "C", "q35")
prd.add_transition("q35", "T", "q38")#FINAL

prd.add_transition("q26", "D", "q36")
prd.add_transition("q36", "I", "q37")
prd.add_transition("q37", "C", "q38")#FINAL

prd.add_transition("q38", " ", "q39")


# ----------AÑO---------------------
prd.add_transition("q39", "0", "q40")
prd.add_transition("q39", "1", "q40")
prd.add_transition("q39", "2", "q40")
prd.add_transition("q39", "3", "q40")
prd.add_transition("q39", "4", "q40")
prd.add_transition("q39", "5", "q40")
prd.add_transition("q39", "6", "q40")
prd.add_transition("q39", "7", "q40")
prd.add_transition("q39", "8", "q40")
prd.add_transition("q39", "9", "q40")

prd.add_transition("q40", "0", "q41")
prd.add_transition("q40", "1", "q41")
prd.add_transition("q40", "2", "q41")
prd.add_transition("q40", "3", "q41")
prd.add_transition("q40", "4", "q41")
prd.add_transition("q40", "5", "q41")
prd.add_transition("q40", "6", "q41")
prd.add_transition("q40", "7", "q41")
prd.add_transition("q40", "8", "q41")
prd.add_transition("q40", "9", "q41")
prd.add_transition("q40", "9", "q41")
prd.add_transition("q41", " ", "q42")
prd.add_transition("q42", "-", "q43")
prd.add_transition("q43", " ", "q44")

# --------SEGUNDA FECHA----------------
prd.add_transition("q44", "0", "q45") #inicio

prd.add_transition("q45", "1", "q46")
prd.add_transition("q45", "2", "q46")
prd.add_transition("q45", "3", "q46")
prd.add_transition("q45", "4", "q46")
prd.add_transition("q45", "5", "q46")
prd.add_transition("q45", "6", "q46")
prd.add_transition("q45", "7", "q46")
prd.add_transition("q45", "8", "q46")
prd.add_transition("q45", "9", "q46") #final

prd.add_transition("q44", "1", "q47")
prd.add_transition("q44", "2", "q47")  

prd.add_transition("q47", "0", "q48")
prd.add_transition("q47", "1", "q48")
prd.add_transition("q47", "2", "q48")
prd.add_transition("q47", "3", "q48")
prd.add_transition("q47", "4", "q48")
prd.add_transition("q47", "5", "q48")
prd.add_transition("q47", "6", "q48")
prd.add_transition("q47", "7", "q48")
prd.add_transition("q47", "8", "q48")#final

prd.add_transition("q44", "3", "q49")

prd.add_transition("q49", "0", "q50")
prd.add_transition("q49", "1", "q50")#final


prd.add_transition("q46", " ", "q51")
prd.add_transition("q48", " ", "q51")
prd.add_transition("q50", " ", "q51") #final

prd.add_transition("q51", "F", "q52")
prd.add_transition("q52", "E", "q53")
prd.add_transition("q53", "B", "q63")#FINAL

prd.add_transition("q51", "A", "q54")
prd.add_transition("q54", "B", "q55")
prd.add_transition("q55", "R", "q63")#FINAL

prd.add_transition("q51", "J", "q57")
prd.add_transition("q57", "U", "q58")
prd.add_transition("q58", "N", "q63")#FINAL

prd.add_transition("q54", "G", "q56")
prd.add_transition("q56", "O", "q63") #FINAL

prd.add_transition("q52", "O", "q59")
prd.add_transition("q59", "C", "q60")
prd.add_transition("q60", "T", "q63")#FINAL

prd.add_transition("q52", "D", "q61")
prd.add_transition("q61", "I", "q62")
prd.add_transition("q62", "C", "q63")#FINAL

prd.add_transition("q63", " ", "q64")

# ----------SEGUNDO AÑO------------
prd.add_transition("q64", "0", "q65")
prd.add_transition("q64", "1", "q65")
prd.add_transition("q64", "2", "q65")
prd.add_transition("q64", "3", "q65")
prd.add_transition("q64", "4", "q65")
prd.add_transition("q64", "5", "q65")
prd.add_transition("q64", "6", "q65")
prd.add_transition("q64", "7", "q65")
prd.add_transition("q64", "8", "q65")
prd.add_transition("q64", "9", "q65")

prd.add_transition("q65", "0", "q66")
prd.add_transition("q65", "1", "q66")
prd.add_transition("q65", "2", "q66")
prd.add_transition("q65", "3", "q66")
prd.add_transition("q65", "4", "q66")
prd.add_transition("q65", "5", "q66")
prd.add_transition("q65", "6", "q66")
prd.add_transition("q65", "7", "q66")
prd.add_transition("q65", "8", "q66")
prd.add_transition("q65", "9", "q66")
prd.add_transition("q65", "9", "q66")



prd.add_final_states(("q66"))

print(prd.evaluate(n2))
# print(prd.evaluate("PERIODO FACTURADO: 07 JUN 22 - 07 FEB 22"))
# print(prd.evaluate("PERIODO FACTURADO: 12 ABR 22 - 10 JUN 22"))
# print (prd.evaluate("PERIODO FACTURADO: 12 ABR 22 - 10 JUN 22TOTAL A PAGAR:"))


kwh.add_initial_states("q0")

kwh.add_transition("q0", "0", "q0")
kwh.add_transition("q0", "1", "q0")
kwh.add_transition("q0", "2", "q0")
kwh.add_transition("q0", "3", "q0")
kwh.add_transition("q0", "4", "q0")
kwh.add_transition("q0", "5", "q0")
kwh.add_transition("q0", "6", "q0")
kwh.add_transition("q0", "7", "q0")
kwh.add_transition("q0", "8", "q0")
kwh.add_transition("q0", "9", "q0")

kwh.add_transition("q0", ",", "q1")

kwh.add_transition("q1", "0", "q1")
kwh.add_transition("q1", "1", "q1")
kwh.add_transition("q1", "2", "q1")
kwh.add_transition("q1", "3", "q1")
kwh.add_transition("q1", "4", "q1")
kwh.add_transition("q1", "5", "q1")
kwh.add_transition("q1", "6", "q1")
kwh.add_transition("q1", "7", "q1")
kwh.add_transition("q1", "8", "q1")
kwh.add_transition("q1", "9", "q1")

kwh.add_transition("q1", " ", "q2")

kwh.add_transition("q2", "0", "q2")
kwh.add_transition("q2", "1", "q2")
kwh.add_transition("q2", "2", "q2")
kwh.add_transition("q2", "3", "q2")
kwh.add_transition("q2", "4", "q2")
kwh.add_transition("q2", "5", "q2")
kwh.add_transition("q2", "6", "q2")
kwh.add_transition("q2", "7", "q2")
kwh.add_transition("q2", "8", "q2")
kwh.add_transition("q2", "9", "q2")

kwh.add_transition("q2", ",", "q3")

kwh.add_transition("q3", "0", "q3")
kwh.add_transition("q3", "1", "q3")
kwh.add_transition("q3", "2", "q3")
kwh.add_transition("q3", "3", "q3")
kwh.add_transition("q3", "4", "q3")
kwh.add_transition("q3", "5", "q3")
kwh.add_transition("q3", "6", "q3")
kwh.add_transition("q3", "7", "q3")
kwh.add_transition("q3", "8", "q3")
kwh.add_transition("q3", "9", "q3")

kwh.add_transition("q3", " ", "q4")

kwh.add_transition("q4", "0", "q4")
kwh.add_transition("q4", "1", "q4")
kwh.add_transition("q4", "2", "q4")
kwh.add_transition("q4", "3", "q4")
kwh.add_transition("q4", "4", "q4")
kwh.add_transition("q4", "5", "q4")
kwh.add_transition("q4", "6", "q4")
kwh.add_transition("q4", "7", "q4")
kwh.add_transition("q4", "8", "q4")
kwh.add_transition("q4", "9", "q4")

kwh.add_final_states("q4")

# print(kwh.evaluate("9,456 1234 657898789789"))
print(kwh.evaluate(ora[l]))