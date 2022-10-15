# JANETH ALEJANDRA MORALES MENDOZA 203445 VERIFICADOR DE RMU 
from tkinter.messagebox import NO
import PyPDF2
import tkinter	as tk
from tkinter import *
from tkinter import CENTER, Label,ttk, Button
from io import open
from tkinter import filedialog as fd
from tkinter import messagebox as Message

alfR= ['0','1','2','3','4','5','6','7','8','9','X','A','C','F','E', ' ', '-']
alfP= ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E', 'F', 'G','I','J','L','M','N','O','P','R','S','T','U','V','-', ' ',':']
alfE= ['0','1','2','3','4','5','6','7','8','9', ',', ' ']
alfT = ['0','1','2','3','4','5','6','7','8','9','$']

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
           
        return new_states              
        
    def evaluate(self, string,alfabeto): #string
        """
            returns:
                0 -> Match
                1 -> No match
        """
        states = self.__initial_states.copy()
        self.__get_new_states_e(states)
        for c in string:
            if c in alfabeto:
                new_states = self.__get_new_states(states, c)
                self.__get_new_states_e(new_states)
                print(c)
                states = new_states
            else:
                Message.showerror("Error", "No pertenece al alfabeto") 
                print(string)
                print("----No pertenece al alfabeto-----")
                return False
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
 
rmu = FSM()
prd = FSM()
kwh = FSM()
total = FSM()

rmu.add_initial_states("q0")
 
#CÓDIGO POSTAL 
rmu.add_transition("q0", "0", "q1")
rmu.add_transition("q0", "1", "q1")
rmu.add_transition("q0", "2", "q1")
rmu.add_transition("q0", "3", "q1")
rmu.add_transition("q0", "4", "q1")
rmu.add_transition("q0", "5", "q1")
rmu.add_transition("q0", "6", "q1")
rmu.add_transition("q0", "7", "q1")
rmu.add_transition("q0", "8", "q1")
rmu.add_transition("q0", "9", "q1")

rmu.add_transition("q1", "0", "q2")
rmu.add_transition("q1", "1", "q2")
rmu.add_transition("q1", "2", "q2")
rmu.add_transition("q1", "3", "q2")
rmu.add_transition("q1", "4", "q2")
rmu.add_transition("q1", "5", "q2")
rmu.add_transition("q1", "6", "q2")
rmu.add_transition("q1", "7", "q2")
rmu.add_transition("q1", "8", "q2")
rmu.add_transition("q1", "9", "q2")

rmu.add_transition("q2", "0", "q3")
rmu.add_transition("q2", "1", "q3")
rmu.add_transition("q2", "2", "q3")
rmu.add_transition("q2", "3", "q3")
rmu.add_transition("q2", "4", "q3")
rmu.add_transition("q2", "5", "q3")
rmu.add_transition("q2", "6", "q3")
rmu.add_transition("q2", "7", "q3")
rmu.add_transition("q2", "8", "q3")
rmu.add_transition("q2", "9", "q3")

rmu.add_transition("q3", "0", "q4")
rmu.add_transition("q3", "1", "q4")
rmu.add_transition("q3", "2", "q4")
rmu.add_transition("q3", "3", "q4")
rmu.add_transition("q3", "4", "q4")
rmu.add_transition("q3", "5", "q4")
rmu.add_transition("q3", "6", "q4")
rmu.add_transition("q3", "7", "q4")
rmu.add_transition("q3", "8", "q4")
rmu.add_transition("q3", "9", "q4")

rmu.add_transition("q4", "0", "q5")
rmu.add_transition("q4", "1", "q5")
rmu.add_transition("q4", "2", "q5")
rmu.add_transition("q4", "3", "q5")
rmu.add_transition("q4", "4", "q5")
rmu.add_transition("q4", "5", "q5")
rmu.add_transition("q4", "6", "q5")
rmu.add_transition("q4", "7", "q5")
rmu.add_transition("q4", "8", "q5")
rmu.add_transition("q4", "9", "q5")

rmu.add_transition("q5", " ", "q6")

#--------------- AÑOS----------------
rmu.add_transition("q6", "0", "q7")
rmu.add_transition("q6", "1", "q7")
rmu.add_transition("q6", "2", "q7")
rmu.add_transition("q6", "3", "q7")
rmu.add_transition("q6", "4", "q7")
rmu.add_transition("q6", "5", "q7")
rmu.add_transition("q6", "6", "q7")
rmu.add_transition("q6", "7", "q7")
rmu.add_transition("q6", "8", "q7")
rmu.add_transition("q6", "9", "q7")

rmu.add_transition("q7", "0", "q8")
rmu.add_transition("q7", "1", "q8")
rmu.add_transition("q7", "2", "q8")
rmu.add_transition("q7", "3", "q8")
rmu.add_transition("q7", "4", "q8")
rmu.add_transition("q7", "5", "q8")
rmu.add_transition("q7", "6", "q8")
rmu.add_transition("q7", "7", "q8")
rmu.add_transition("q7", "8", "q8")
rmu.add_transition("q7", "9", "q8")

rmu.add_transition("q8", "-", "q9")

#------------- MES ------------------
rmu.add_transition("q9", "0", "q10")

rmu.add_transition("q10", "1", "q11")
rmu.add_transition("q10", "2", "q11")
rmu.add_transition("q10", "3", "q11")
rmu.add_transition("q10", "4", "q11")
rmu.add_transition("q10", "5", "q11")
rmu.add_transition("q10", "6", "q11")
rmu.add_transition("q10", "7", "q11")
rmu.add_transition("q10", "8", "q11")
rmu.add_transition("q10", "9", "q11")

rmu.add_transition("q9", "1", "q12")

rmu.add_transition("q12", "0", "q13")
rmu.add_transition("q12", "1", "q13")
rmu.add_transition("q12", "2", "q13")

rmu.add_transition("q11", "-", "q14")
rmu.add_transition("q13", "-", "q14")

# -----------DIAS-----------------
rmu.add_transition("q14", "0", "q15") 

rmu.add_transition("q15", "1", "q16")
rmu.add_transition("q15", "2", "q16")
rmu.add_transition("q15", "3", "q16")
rmu.add_transition("q15", "4", "q16")
rmu.add_transition("q15", "5", "q16")
rmu.add_transition("q15", "6", "q16")
rmu.add_transition("q15", "7", "q16")
rmu.add_transition("q15", "8", "q16")
rmu.add_transition("q15", "9", "q16")

rmu.add_transition("q14", "1", "q17")
rmu.add_transition("q14", "2", "q17")  

rmu.add_transition("q17", "0", "q18")
rmu.add_transition("q17", "1", "q18")
rmu.add_transition("q17", "2", "q18")
rmu.add_transition("q17", "3", "q18")
rmu.add_transition("q17", "4", "q18")
rmu.add_transition("q17", "5", "q18")
rmu.add_transition("q17", "6", "q18")
rmu.add_transition("q17", "7", "q18")
rmu.add_transition("q17", "8", "q18")
rmu.add_transition("q17", "9", "q18")

rmu.add_transition("q14", "3", "q19")

rmu.add_transition("q19", "0", "q20")
rmu.add_transition("q19", "1", "q20")

rmu.add_transition("q16", " ", "q21")
rmu.add_transition("q18", " ", "q21")
rmu.add_transition("q20", " ", "q21")

# -----CADENA DE XAXX-010101 ----rmu
rmu.add_transition("q21", "X", "q22")
rmu.add_transition("q22", "A", "q23")
rmu.add_transition("q23", "X", "q24")
rmu.add_transition("q24", "X", "q25")

rmu.add_transition("q25", "-", "q26") 

rmu.add_transition("q26", "0", "q27")
rmu.add_transition("q27", "1", "q28")
rmu.add_transition("q28", "0", "q29")
rmu.add_transition("q29", "1", "q30")
rmu.add_transition("q30", "0", "q31")
rmu.add_transition("q31", "1", "q32")

rmu.add_transition("q32", " ", "q33")

# --- FOLIO DE 000-999 ----
rmu.add_transition("q33", "0", "q34")
rmu.add_transition("q33", "1", "q34")
rmu.add_transition("q33", "2", "q34")
rmu.add_transition("q33", "3", "q34")
rmu.add_transition("q33", "4", "q34")
rmu.add_transition("q33", "5", "q34")
rmu.add_transition("q33", "6", "q34")
rmu.add_transition("q33", "7", "q34")
rmu.add_transition("q33", "8", "q34")
rmu.add_transition("q33", "9", "q34")

rmu.add_transition("q34", "0", "q35")
rmu.add_transition("q34", "1", "q35")
rmu.add_transition("q34", "2", "q35")
rmu.add_transition("q34", "3", "q35")
rmu.add_transition("q34", "4", "q35")
rmu.add_transition("q34", "5", "q35")
rmu.add_transition("q34", "6", "q35")
rmu.add_transition("q34", "7", "q35")
rmu.add_transition("q34", "8", "q35")
rmu.add_transition("q34", "9", "q35")

rmu.add_transition("q35", "0", "q36")
rmu.add_transition("q35", "1", "q36")
rmu.add_transition("q35", "2", "q36")
rmu.add_transition("q35", "3", "q36")
rmu.add_transition("q35", "4", "q36")
rmu.add_transition("q35", "5", "q36")
rmu.add_transition("q35", "6", "q36")
rmu.add_transition("q35", "7", "q36")
rmu.add_transition("q35", "8", "q36")
rmu.add_transition("q35", "9", "q36")

rmu.add_transition("q36", " ", "q37")

# ---DIGÍTOS NECES. TERMINALES CFE---
rmu.add_transition("q37", "C", "q38")
rmu.add_transition("q38", "F", "q39")
rmu.add_transition("q39", "E", "q40")

rmu.add_final_states(("q40"))

# -----PERIODO DE FACTURA------ AUTOMATA 2
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
prd.add_transition("q26", "E", "q27")
prd.add_transition("q27", "N", "q28")
prd.add_transition("q28", "E", "q46")#FINAL

prd.add_transition("q26", "F", "q29")
prd.add_transition("q29", "E", "q30")
prd.add_transition("q30", "B", "q46")#FINAL

prd.add_transition("q26", "M", "q31")
prd.add_transition("q31", "A", "q32")
prd.add_transition("q32", "R", "q46")#FIN
prd.add_transition("q32", "Y", "q46")#FIN

prd.add_transition("q26", "A", "q33")
prd.add_transition("q33", "B", "q34")
prd.add_transition("q34", "R", "q46")# FINAL

prd.add_transition("q33", "G", "q35")
prd.add_transition("q35", "O", "q46")# FINAL

prd.add_transition("q26", "J", "q36")
prd.add_transition("q36", "U", "q37")
prd.add_transition("q37", "N", "q46") #FINAL
prd.add_transition("q37", "L", "q46") #FINAL

prd.add_transition("q26", "S", "q38")
prd.add_transition("q38", "E", "q39")
prd.add_transition("q39", "P", "q46")#FINAL

prd.add_transition("q26", "O", "q40")
prd.add_transition("q40", "C", "q41")
prd.add_transition("q41", "T", "q46")#FINAL

prd.add_transition("q26", "N", "q42")
prd.add_transition("q42", "O", "q43")
prd.add_transition("q43", "V", "q46")#FINAL

prd.add_transition("q26", "D", "q44")
prd.add_transition("q44", "I", "q45")
prd.add_transition("q45", "C", "q46")#FINAL

prd.add_transition("q46", " ", "q47")

# ----------AÑO---------------------
prd.add_transition("q47", "0", "q48")
prd.add_transition("q47", "1", "q48")
prd.add_transition("q47", "2", "q48")
prd.add_transition("q47", "3", "q48")
prd.add_transition("q47", "4", "q48")
prd.add_transition("q47", "5", "q48")
prd.add_transition("q47", "6", "q48")
prd.add_transition("q47", "7", "q48")
prd.add_transition("q47", "8", "q48")
prd.add_transition("q47", "9", "q48")

prd.add_transition("q48", "0", "q49")
prd.add_transition("q48", "1", "q49")
prd.add_transition("q48", "2", "q49")
prd.add_transition("q48", "3", "q49")
prd.add_transition("q48", "4", "q49")
prd.add_transition("q48", "5", "q49")
prd.add_transition("q48", "6", "q49")
prd.add_transition("q48", "7", "q49")
prd.add_transition("q48", "8", "q49")
prd.add_transition("q48", "9", "q49")
prd.add_transition("q48", "9", "q49")
prd.add_transition("q49", " ", "q50")
prd.add_transition("q50", "-", "q51")
prd.add_transition("q51", " ", "q52")

# --------SEGUNDA FECHA----------------
prd.add_transition("q52", "0", "q53") #inicio

prd.add_transition("q53", "1", "q54")
prd.add_transition("q53", "2", "q54")
prd.add_transition("q53", "3", "q54")
prd.add_transition("q53", "4", "q54")
prd.add_transition("q53", "5", "q54")
prd.add_transition("q53", "6", "q54")
prd.add_transition("q53", "7", "q54")
prd.add_transition("q53", "8", "q54")
prd.add_transition("q53", "9", "q54") #final

prd.add_transition("q52", "1", "q55")
prd.add_transition("q52", "2", "q55")  

prd.add_transition("q55", "0", "q56")
prd.add_transition("q55", "1", "q56")
prd.add_transition("q55", "2", "q56")
prd.add_transition("q55", "3", "q56")
prd.add_transition("q55", "4", "q56")
prd.add_transition("q55", "5", "q56")
prd.add_transition("q55", "6", "q56")
prd.add_transition("q55", "7", "q56")
prd.add_transition("q55", "8", "q56")#final

prd.add_transition("q52", "3", "q57")

prd.add_transition("q57", "0", "q58")
prd.add_transition("q57", "1", "q58")#final

prd.add_transition("q54", " ", "q59")
prd.add_transition("q56", " ", "q59")
prd.add_transition("q58", " ", "q59") #final

prd.add_transition("q59", "E", "q60")
prd.add_transition("q60", "N", "q61")
prd.add_transition("q61", "E", "q79")#FINAL

prd.add_transition("q59", "F", "q62")
prd.add_transition("q62", "E", "q63")
prd.add_transition("q63", "B", "q79")#FINAL

prd.add_transition("q59", "M", "q64")
prd.add_transition("q64", "A", "q65")
prd.add_transition("q65", "R", "q79")#FIN
prd.add_transition("q65", "Y", "q79")#FIN

prd.add_transition("q59", "A", "q66")
prd.add_transition("q66", "B", "q67")
prd.add_transition("q67", "R", "q79")# FINAL

prd.add_transition("q66", "G", "q68")
prd.add_transition("q68", "O", "q79")# FINAL

prd.add_transition("q59", "J", "q69")
prd.add_transition("q69", "U", "q70")
prd.add_transition("q70", "N", "q79") #FINAL
prd.add_transition("q70", "L", "q79") #FINAL

prd.add_transition("q59", "S", "q71")
prd.add_transition("q71", "E", "q72")
prd.add_transition("q72", "P", "q79")#FINAL

prd.add_transition("q59", "O", "q73")
prd.add_transition("q73", "C", "q74")
prd.add_transition("q74", "T", "q79")#FINAL

prd.add_transition("q59", "N", "q75")
prd.add_transition("q75", "O", "q76")
prd.add_transition("q76", "V", "q79")#FINAL

prd.add_transition("q59", "D", "q77")
prd.add_transition("q77", "I", "q78")
prd.add_transition("q78", "C", "q79")#FINAL

prd.add_transition("q79", " ", "q80")

# ----------SEGUNDO AÑO------------
prd.add_transition("q80", "0", "q81")
prd.add_transition("q80", "1", "q81")
prd.add_transition("q80", "2", "q81")
prd.add_transition("q80", "3", "q81")
prd.add_transition("q80", "4", "q81")
prd.add_transition("q80", "5", "q81")
prd.add_transition("q80", "6", "q81")
prd.add_transition("q80", "7", "q81")
prd.add_transition("q80", "8", "q81")
prd.add_transition("q80", "9", "q81")

prd.add_transition("q81", "0", "q82")
prd.add_transition("q81", "1", "q82")
prd.add_transition("q81", "2", "q82")
prd.add_transition("q81", "3", "q82")
prd.add_transition("q81", "4", "q82")
prd.add_transition("q81", "5", "q82")
prd.add_transition("q81", "6", "q82")
prd.add_transition("q81", "7", "q82")
prd.add_transition("q81", "8", "q82")
prd.add_transition("q81", "9", "q82")
prd.add_transition("q81", "9", "q82")

prd.add_final_states("q82")

# ------ENERGIA KWH--------- AUTOMATA 3
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
kwh.add_transition("q0", " ", "q3")


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

# ----IMPORTE AUTOMATA 4-----
total.add_initial_states("q0")

total.add_transition("q0","$","q1")
total.add_transition("q1","0","q1")
total.add_transition("q1","1","q1")
total.add_transition("q1","2","q1")
total.add_transition("q1","3","q1")
total.add_transition("q1","4","q1")
total.add_transition("q1","5","q1")
total.add_transition("q1","6","q1")
total.add_transition("q1","7","q1")
total.add_transition("q1","8","q1")
total.add_transition("q1","9","q1")

total.add_final_states("q1")

def save_data(rm, periodo,imp, energ):
    periodo2 = str(periodo).split(":")
    energia2 = str(energ).split(' ')
    eng = energia2[2]
    perd = periodo2[1]
    data2 = []
   
    data2.append([rm, perd,eng,imp])
    print(data2)
    x = 1 
    for i in range(x):
        tv.insert(parent='', index=i,  values=(data2[i]))
           
def open_file(pth):
    mypdf = open("C:/Users/52961/Downloads/"+ pth ,mode='rb')
    pdf_document = PyPDF2.PdfFileReader(mypdf)
    pdf_document.numPages  
    first_page = pdf_document.getPage(0)

    text = first_page.extractText()
    separator = text.split('\n')
    mypdf.close()

    dataCFE = []

    for i in separator:
        dataCFE.append(i)

    cfe = [s for s in dataCFE if "RMU" in s]

    if not cfe:
        Message.showwarning("ADVERTENCIA", "Verfique que su documento sea un recibo")
    else:
        if dataCFE[0] == "TOTAL A PAGAR:":
            energia = dataCFE.index('Energía (kWh)X X')+1
            str_1 = [s for s in dataCFE if "RMU" in s]
            rm = str(str_1)[8:42]

            str_2 = [s for s in dataCFE if "PERIODO FACTURADO:" in s]
            new = str(str_2).split('TARIFA:')
            periodo =" ".join(new)[2:42]
            
            str_3 = [s for s in dataCFE if "$" in s]
            new = str(str_3[0]).split('(')
            importe = new[0]
        else:    
            str_1 = [s for s in dataCFE if "RMU" in s]
            rm = str(str_1)[7:41]
            impor = [s for s in dataCFE if "$" in s]
            importe = impor[1]

            str_2 = [s for s in dataCFE if "PAGAR" in s]
            new = str(str_2).split('TOTAL A PAGAR:')
            periodo =" ".join(new)[2:42]
            energia = dataCFE.index('-1-')+1

        if rmu.evaluate(rm,alfR):
            print("----La cadena es valida-------")
            if prd.evaluate(periodo,alfP):
                print("----La cadena es valida-------")
                print(periodo)
                if total.evaluate(importe,alfT):
                    print("----La cadena es valida-------")
                    energ = dataCFE[energia]
                    if kwh.evaluate(energ,alfE):
                        print("----La cadena es valida-------")
                        Message.showinfo("Aceptado", "Todos los datos son válidos")
                        save_data(rm, periodo,importe, energ)
                        tv.heading('#0', text='', anchor=CENTER)
                        tv.heading('RMU', text='RMU', anchor=CENTER)
                        tv.heading('Periodo', text='Periodo', anchor=CENTER)
                        tv.heading('kHw', text='kHw', anchor=CENTER)
                        tv.heading('Importe', text='Importe', anchor=CENTER)
                        tv.pack()
                        tv.place(x=50, y=200)
        else:
            print("----La cadena no es valida-------")
            Message.showerror("Error", "La cadena no es válida")    

def select_file():
    filetypes = (('pdf files', '*.pdf'),('All files', '*.*'))
    filename = fd.askopenfilename(title='Open a file',initialdir='/',filetypes=filetypes)
    
    path = filename.split('/',4)
    pth = path[4]

    open_file(pth)
    
ventana = tk.Tk()
ventana.title("Verificador de RMU")
ventana.config(bg="#B8C8C5")
ventana.geometry("700x500")

open_button = Button(ventana, text='Seleccionar archivo' ,command=select_file ,background='#189666', width=17, height=2 ,fg="white", font=('calibri', 12, 'bold'))
open_button.pack(expand=True)
open_button.place(x=280,y=120)

etiqueta_rmu = Label(text="Verificar RMU ",background="#189666", font=('Monserrat', 25, 'bold'), width=35 , height=2, fg='white')
etiqueta_rmu.place(x=0,y=0)

tv = ttk.Treeview(ventana, style="mystyle.Treeview")
tv['columns']=('RMU','Periodo', 'kHw', 'Importe')
tv.column('#0', width=0, stretch=NO )
tv.column('RMU', anchor=CENTER, width=250)
tv.column('Periodo', anchor=CENTER, width=150)
tv.column('kHw', anchor=CENTER, width=90)
tv.column('Importe', anchor=CENTER, width=90)

style = ttk.Style()
style.configure("mystyle.Treeview", highlightthickness=0, bd=0, font=('Calibri', 11)) # Modify the font of the body
style.configure("mystyle.Treeview.Heading", font=('Calibri', 13,'bold')) # Modify the font of the headings
style.layout("mystyle.Treeview", [('mystyle.Treeview.treearea', {'sticky': 'nswe'})]) # Remove the borders

ventana.mainloop()  