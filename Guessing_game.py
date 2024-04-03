import random
from tkinter import *
from tkinter import messagebox


root =Tk()
root.title("Guessing Game")
root.geometry('800x600')
root.resizable('false','false')
root.configure(bg='black')


attempts=0 
    
#FUNCTION
def guess():
    global attempts   
    try:
        user =User.get()
        user =int(user)
        attempts+=1
            
        
        Computer =random.randint(30,41)
        print(Computer)

        if user == Computer:
            messagebox.showinfo('',f'YOU GUESSED CORRECTLY!!!!!!!! \n {Computer}  IS EQUAL TO {user}')
            computerguess.config(text=f"COMPUTER GUESS :{Computer}\n\n YOU GUESSED {attempts} TIMES",font=('Calibri',29),fg='green',bg='black')
        
                

        elif user > Computer:
            messagebox.showerror('',' YOUR GUESS IS HIGHER THAN THE COMPUTER GUESS')
            User.delete(0,END)
            
    

        elif user < Computer:
            messagebox.showerror('',' YOUR GUESS IS LOWER THAN THE COMPUTER GUESS')
            User.delete(0,END)
        
    
                
    except ValueError :
            messagebox.showerror('','INSERT ONLY INTEGER NUMBER IN THE WIDGET!!!!')
            User.delete(0,END)
        

#RESET FUNCTION
        

def reset():
    User.delete(0,END)
    messagebox.showinfo('','Entry Widget Clearing...........')
    global computerguess
    computerguess.config(text='')
    
                
    



#Title

Title =Label(root,text="Guessing Game",font=('Calibri',27),fg='red',bg='black')
Title.place(x=300,y=0)



#Instruction
Instruction =Label(root,text="Guessing Number is between Range 30 -  40",font=('Calibri',27),fg='white',bg='black')
Instruction.place(x=100,y=100)



Userlabel =Label(root,text="USER GUESS:",font=('Calibri',27),fg='white',bg='black')
Userlabel.place(x=50,y=230)

User =Entry(root,bd=3,width=30,font={'Helvetica',12})
User.place(x=260,y=240)


#Computer Guess
computerguess =Label(root,text="",font=('Calibri',29),fg='green',bg='black')
computerguess.place(x=100,y=330)
             




#Button

button =Button(root,text="CLICK",width=13,height=2,font=("Heletica",12),bg='green',command=guess)

button.place(x=260,y=500)



#Clear Entry Widget
clear=Button(root,text="RESET",width=13,height=2,font=("Heletica",12),bg='red',command=reset)

clear.place(x=450,y=500)




























root.mainloop()





