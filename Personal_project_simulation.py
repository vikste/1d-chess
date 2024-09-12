#If you wish to start the simulation, click the "F5" key.

#Importing tkinter as tk allows me to use commands that are not normally available in default Python
import tkinter as tk
from tkinter import ttk

menu=tk.Tk()
menu.title('1D Chess')
menu.geometry('700x500')
menu.minsize(700,500)
menu.maxsize(700,500)

board=tk.Canvas(height=500, width=700)
board.pack(fill=tk.BOTH)

def draw_msg(text, font=('aerial 18 bold'), x=200, y=100):
    label = ttk.Label(text = text, font = font)
    label.place(x=x, y=y)

    restart = ttk.Button(height = 4, width = 8, text = 'Play again', command = lambda:[Wrook.configure(command = movestart_Wrook),
                                                                                      Wknight.configure(command = movestart_Wknight),
                                                                                      Wking.place(x=35, y=175, bordermode=tk.OUTSIDE),
                                                                                      Wknight.place(x=115, y=175, bordermode=tk.OUTSIDE),
                                                                                      Wrook.place(x=195, y=175, bordermode=tk.OUTSIDE),
                                                                                      Brook.place(x=435, y=175, bordermode=tk.OUTSIDE),
                                                                                      Bknight.place(x=515, y=175, bordermode=tk.OUTSIDE),
                                                                                      Bking.place(x=595, y=175, bordermode=tk.OUTSIDE),
                                                                                      label.place_forget(),
                                                                                      restart.place_forget()])
    restart.place(x=300, y = 300)



color='white'

for i in range(8):
    x1 = i*80 + 30
    x2 = x1+80
    board.create_rectangle((x1, 170, x2, 250), fill=color)

    color = 'brown' if color =='white' else 'white'
        

def movestart_Wrook():
    
    m1=tk.Button(height=1, width=1, bg="grey", command = lambda:[Wrook.place(x=275, y=175, bordermode=tk.OUTSIDE),
                                                                 Wrook.configure(command = errormessage),
                                                                 m1.destroy(),
                                                                 m2.destroy(),
                                                                 m3.destroy(),
                                                                 Bmove.configure(command = lambda:[Bknight.place(x=355, y=175, bordermode=tk.OUTSIDE),
                                                                                                   Bmove.place_forget(),
                                                                                                   Wrook.configure(command = movestart4_2_Wrook)]),
                                                                 Bmove.place(x=300, y=400, bordermode = tk.OUTSIDE)])
    m1.place(x=295, y=195, bordermode=tk.OUTSIDE)


    m2=tk.Button(height=1, width=1, bg="grey", command = lambda:[Wrook.place(x=355, y=175, bordermode=tk.OUTSIDE),
                                                                 Wrook.configure(command = errormessage),
                                                                 m1.destroy(),
                                                                 m2.destroy(),
                                                                 m3.destroy(),
                                                                 Bmove.configure(command = lambda:[Brook.place(x=355, y=175, bordermode=tk.OUTSIDE),
                                                                                                   Wrook.place_forget(),
                                                                                                   Wknight.configure(command = movestart_Wknight_loss1),
                                                                                                   Bmove.place_forget()]),
                                                                 Bmove.place(x=300, y=400, bordermode = tk.OUTSIDE)])
    m2.place(x=380, y=195, bordermode=tk.OUTSIDE)

    
    m3=tk.Button(height=1, width=1, bg="grey", command = lambda: [Wrook.place(x=435, y=175, bordermode=tk.OUTSIDE),
                                                                  Wrook.configure(command = errormessage),
                                                                  Brook.place_forget(),
                                                                  m1.destroy(),
                                                                  m2.destroy(),
                                                                  m3.destroy(),
                                                                  draw_msg(text='Draw by stalemate, try again!')])
    m3.place(x=460, y=195, bordermode=tk.OUTSIDE)

    
    Wrook.configure(command = lambda:[
        Wrook.configure(command = movestart_Wrook),
        Wknight.configure(command = movestart_Wknight),
        m1.destroy(),
        m2.destroy(),
        m3.destroy()])
    Wknight.configure(command = errormessage)


def movestart4_2_Wrook():
    m1=tk.Button(height=1, width=1, bg="grey", command = lambda:[Wrook.place(x=195, y=175, bordermode=tk.OUTSIDE),
                                                                 m1.destroy(),
                                                                 m2.destroy(),
                                                                 Bmove.configure(command = lambda:[Bknight.place(x=195, y=175, bordermode=tk.OUTSIDE),
                                                                                                   Wrook.place_forget(),
                                                                                                   Bmove.place_forget(),
                                                                                                   draw_msg(text = 'Black wins by checkmate, try again!', x=150),
                                                                                                   Bmove.place_forget()]),
                                                                 Bmove.place(x=300, y=400, bordermode = tk.OUTSIDE)])

        
    m1.place(x=220, y=195, bordermode = tk.OUTSIDE)

    m2=tk.Button(height=1, width=1, bg="grey", command = lambda:[Wrook.place(x=355, y=175, bordermode=tk.OUTSIDE),
                                                                 m1.destroy(),
                                                                 m2.destroy(),
                                                                 Bknight.place_forget(),
                                                                 Bmove.configure(command = lambda:[Brook.place(x=355, y=175, bordermode=tk.OUTSIDE),
                                                                                                   Wrook.place_forget(),
                                                                                                   Wknight.configure(command = movestart_Wknight_loss1),
                                                                                                   Bmove.place_forget()]),
                                                                 Bmove.place(x=300, y=400, bordermode = tk.OUTSIDE)])
    m2.place(x=380, y=195, bordermode=tk.OUTSIDE)

    Wrook.configure(command = lambda:[Wrook.configure(command = movestart4_2_Wrook),
                                      m1.destroy(),
                                      m2.destroy()])

def movestart_Wknight_loss1():
    m1=tk.Button(height=1, width=1, bg="grey", command = lambda:[Wknight.place(x=275, y=175, bordermode=tk.OUTSIDE),
                                                                 m1.destroy(),
                                                                 Bmove.configure(command = lambda:[Brook.place(x=275, y=175, bordermode=tk.OUTSIDE),
                                                                                                   Wknight.place_forget(),
                                                                                                   draw_msg(text = 'Black wins by checkmate, try again!', x=150),
                                                                                                   Bmove.place_forget()]),
                                                                 Bmove.place(x=300, y=400, bordermode = tk.OUTSIDE)])
    m1.place(x=300, y=195, bordermode=tk.OUTSIDE)
    
    Wknight.configure(command = lambda:[Wknight.configure(command = movestart_Wknight_loss1),
                                        m1.destroy()])
    
def movestart_Wknight():
    m1=tk.Button(height=1, width=1, bg="grey", command = lambda:[Wknight.place(x=275, y=175, bordermode=tk.OUTSIDE),
                                                                 Wknight.configure(command = errormessage),
                                                                 m1.destroy(),
                                                                 Bmove.configure(command = lambda:[Bknight.place(x=355, y=175, bordermode=tk.OUTSIDE),
                                                                                                   Wking.configure(command = movestart_Wking1_2),
                                                                                                   Wrook.configure(command = movestart_Wrook3_2),
                                                                                                   Wknight.configure(command = movestart_Wknight4_2),
                                                                                                   Bmove.place_forget()]),
                                                                 Bmove.place(x=300, y=400, bordermode = tk.OUTSIDE)])
    m1.place(x=300, y=195, bordermode=tk.OUTSIDE)
    Wknight.configure(command = lambda:[Wknight.configure(command = movestart_Wknight),
                                        m1.destroy()])

    Wknight.configure(command = lambda:[Wknight.configure(command = movestart_Wknight),
                                      Wrook.configure(command = movestart_Wrook),
                                      m1.destroy()])
    
    Wrook.configure(command = errormessage)

def movestart_Wking1_2():
    m1=tk.Button(height=1, width=1, bg="grey", command = lambda:[Wking.place(x=115, y=175, bordermode=tk.OUTSIDE),
                                                                 Wking.configure(command = errormessage),
                                                                 m1.destroy(),
                                                                 Bmove.configure(command = lambda:[Bknight.place(x=195, y=175, bordermode=tk.OUTSIDE),
                                                                                                   Wrook.place_forget(),
                                                                                                   Bmove.place_forget(),
                                                                                                   Wking.configure(command = movestart_Wking_2_3),
                                                                                                   Wknight.configure(command = movestart_Wknight_4_3_1)]),
                                                                 Bmove.place(x=300, y=400, bordermode = tk.OUTSIDE)])
    m1.place(x=140, y=195, bordermode=tk.OUTSIDE)

    Wking.configure(command = lambda:[Wking.configure(command = movestart_Wking1_2),
                                      Wrook.configure(command = movestart_Wrook3_2),
                                      Wknight.configure(command = movestart_Wknight4_2),
                                      m1.destroy()])
    Wrook.configure(command = errormessage)

    Wknight.configure(command = errormessage)

def movestart_Wking_2_3():
    m1=tk.Button(height=1, width=1, bg="grey", command = lambda:[Wking.place(x=195, y=175, bordermode=tk.OUTSIDE),
                                                                 Wking.configure(command = errormessage),
                                                                 Bknight.place_forget(),
                                                                 m1.destroy(),
                                                                 Bmove.configure(command = lambda: [Brook.place(x=355, y=175, bordermode=tk.OUTSIDE),
                                                                                                    Wknight.configure(command = errormessage),
                                                                                                    Wking.configure(command = movestart_Wking_3_4),
                                                                                                    Bmove.place_forget()]),
                                                                 Bmove.place(x=300, y=400, bordermode = tk.OUTSIDE)])
    m1.place(x=220, y=195, bordermode=tk.OUTSIDE)

    Wking.configure(command = lambda:[Wking.configure(command = movestart_Wking_2_3),
                                      Wknight.configure(command = movestart_Wknight_4_3_1),
                                      m1.destroy()])
    
    Wknight.configure(command = errormessage)

def movestart_Wking_3_4():
    m1=tk.Button(height=1, width=1, bg="grey", command = lambda:[Wking.place(x=115, y=175, bordermode=tk.OUTSIDE),
                                                                 Wking.configure(command = errormessage),
                                                                 m1.destroy(),
                                                                 Bmove.configure(command = lambda:[Brook.place(x = 275, y = 175, bordermode=tk.OUTSIDE),
                                                                                                   Wknight.place_forget(),
                                                                                                   Bmove.place_forget(),
                                                                                                   draw_msg(text = 'Black wins by checkmate, try again!')]),
                                                                 Bmove.place(x=300, y=400, bordermode = tk.OUTSIDE)])
    m1.place(x=140, y=195, bordermode=tk.OUTSIDE)

    Wking.configure(command = lambda:[Wking.configure(command = movestart_Wking_3_4),
                                      m1.destroy()])

def movestart_Wknight_4_3_1():
    m1=tk.Button(height=1, width=1, bg="grey", command = lambda:[Wknight.place(x=435, y=175, bordermode=tk.OUTSIDE),
                                                                 Wknight.configure(command = errormessage),
                                                                 Brook.place_forget(),
                                                                 Bmove.configure(command = lambda:[Bking.place(x=515, y=175, bordermode=tk.OUTSIDE),
                                                                                                   Wknight.configure(command = errormessage),
                                                                                                   draw_msg(text = 'Draw by insufficient material, try again!',
                                                                                                            x = 150),
                                                                                                   Bmove.place_forget()]),
                                                                 Bmove.place(x=300, y=400, bordermode = tk.OUTSIDE),
                                                                 m1.destroy()])
    m1.place(x=460, y=195, bordermode=tk.OUTSIDE)

    Wknight.configure(command = lambda:[Wking.configure(command = movestart_Wking_2_3),
                                      Wknight.configure(command = movestart_Wknight_4_3_1),
                                      m1.destroy()])

    Wking.configure(command = errormessage)

def movestart_Wrook3_2():
    m1=tk.Button(height=1, width=1, bg="grey", command = lambda:[Wrook.place(x=115, y=175, bordermode=tk.OUTSIDE),
                                                                 Wrook.configure(command = errormessage),
                                                                 Bmove.configure(command = lambda:[Brook.place(x=515, y=175, bordermode=tk.OUTSIDE),
                                                                                                   Wrook.configure(command = movestart_Wrook2_3),
                                                                                                   Wknight.configure(command = movestart_Wknight4_3),
                                                                                                   Bmove.place_forget()]),
                                                                 Bmove.place(x=300, y=400, bordermode = tk.OUTSIDE),
                                                                 m1.destroy()])
    m1.place(x=140, y=195, bordermode=tk.OUTSIDE)

    Wrook.configure(command = lambda:[Wking.configure(command = movestart_Wking1_2),
                                      Wrook.configure(command = movestart_Wrook3_2),
                                      Wknight.configure(command = movestart_Wknight4_2),
                                      m1.destroy()])
    Wking.configure(command = errormessage)

    Wknight.configure(command = errormessage)

def movestart_Wrook2_3():
    m1=tk.Button(height=1, width=1, bg="grey", command = lambda:[Wrook.place(x=195, y=175, bordermode=tk.OUTSIDE),
                                                                 Wrook.configure(command = errormessage),
                                                                 Bmove.configure(command = lambda:[Bknight.place(x=195, y=175, bordermode=tk.OUTSIDE),
                                                                                                   Wrook.place_forget(),
                                                                                                   Bmove.place_forget(),
                                                                                                   Wking.configure(command = movestart_king1_4)]),
                                                                 Bmove.place(x=300, y=400, bordermode = tk.OUTSIDE),
                                                                 m1.destroy()])
    m1.place(x=220, y=195, bordermode=tk.OUTSIDE)

    Wrook.configure(command = lambda:[Wrook.configure(command = movestart_Wrook2_3),
                                      Wknight.configure(command = movestart_Wknight4_3),
                                      m1.destroy()])
    Wknight.configure(command = errormessage)

def movestart_Wknight4_3():
    m1=tk.Button(height=1, width=1, bg="grey", command = lambda:[Wknight.place(x=435, y=175, bordermode=tk.OUTSIDE),
                                                                 Wknight.configure(command = errormessage),
                                                                 Bmove.configure(command = lambda:[Brook.place(x=435, y=175, bordermode=tk.OUTSIDE),
                                                                                                   Wknight.place_forget(),
                                                                                                   Wrook.configure(command = movestart_Wrook2_4_1),
                                                                                                   Bmove.place_forget()]),
                                                                 Bmove.place(x=300, y=400, bordermode = tk.OUTSIDE),
                                                                 m1.destroy()])
    m1.place(x=460, y=195, bordermode=tk.OUTSIDE)

    Wknight.configure(command = lambda:[Wrook.configure(command = movestart_Wrook2_3),
                                      Wknight.configure(command = movestart_Wknight4_3),
                                      m1.destroy()])
    Wrook.configure(command = errormessage)

def movestart_Wrook2_4_1():
    m1=tk.Button(height=1, width=1, bg="grey", command = lambda:[Wrook.place(x=195, y=175, bordermode=tk.OUTSIDE),
                                                                 Wrook.configure(command = errormessage),
                                                                 Bmove.configure(command = lambda:[Bknight.place(x=195, y=175, bordermode=tk.OUTSIDE),
                                                                                                   Wrook.place_forget(),
                                                                                                   Wking.configure(command = movestart_Wking1_5_1),
                                                                                                   Bmove.place_forget()]),
                                                                 Bmove.place(x=300, y=400, bordermode = tk.OUTSIDE),
                                                                 m1.destroy(),
                                                                 m2.destroy(),
                                                                 m3.destroy()])
    m1.place(x=220, y=195, bordermode=tk.OUTSIDE)
    
    m2=tk.Button(height=1, width=1, bg="grey", command = lambda:[Wrook.place(x=275, y=175, bordermode=tk.OUTSIDE),
                                                                 Wrook.configure(command = errormessage),
                                                                 Bmove.configure(command = lambda:[Bknight.place(x=195, y=175, bordermode=tk.OUTSIDE),
                                                                                                   Wrook.configure(command = movestart_Wrook4_5),
                                                                                                   Wking.configure(command = movestart_Wking1_5_2),
                                                                                                   Bmove.place_forget()]),
                                                                 Bmove.place(x=300, y=400, bordermode = tk.OUTSIDE),
                                                                 m1.destroy(),
                                                                 m2.destroy(),
                                                                 m3.destroy()])
    m2.place(x=300, y=195, bordermode=tk.OUTSIDE)


    m3=tk.Button(height=1, width=1, bg="grey", command = lambda:[Wrook.place(x=355, y=175, bordermode=tk.OUTSIDE),
                                                                 Wrook.configure(command = errormessage),
                                                                 Bknight.place_forget(),
                                                                 Bmove.configure(command = lambda:[Brook.place(x=355, y=175, bordermode=tk.OUTSIDE),
                                                                                                   Wrook.place_forget(),
                                                                                                   draw_msg(text = 'Black wins by checkmate, try again!', x=150),
                                                                                                   Bmove.place_forget()]),
                                                                 Bmove.place(x=300, y=400, bordermode = tk.OUTSIDE),
                                                                 m1.destroy(),
                                                                 m2.destroy(),
                                                                 m3.destroy()])

    m3.place(x=380, y=195, bordermode=tk.OUTSIDE)

    Wrook.configure(command = lambda:[Wrook.configure(command = movestart_Wrook2_4_1),
                                      m1.destroy(),
                                      m2.destroy(),
                                      m3.destroy()])

def movestart_Wking1_5_1():
    m1=tk.Button(height=1, width=1, bg="grey", command = lambda:[Wking.place(x=115, y=175, bordermode=tk.OUTSIDE),
                                                                 Wking.configure(command = errormessage),
                                                                 Bmove.configure(command = lambda:[Bknight.place(x=35, y=175, bordermode=tk.OUTSIDE),
                                                                                                   draw_msg(text = 'Black wins by checkmate! Try again!', x=150),
                                                                                                   Bmove.place_forget()]),
                                                                 Bmove.place(x=300, y=400, bordermode = tk.OUTSIDE),
                                                                 m1.destroy()])
    m1.place(x=140, y=195, bordermode=tk.OUTSIDE)
    
    Wking.configure(command = lambda:[Wking.configure(command = movestart_Wking1_5_2),
                                      m1.destroy()])

    
def movestart_Wrook4_5():
    m1=tk.Button(height=1, width=1, bg="grey", command = lambda:[Wrook.place(x=195, y=175, bordermode=tk.OUTSIDE),
                                                                 Bknight.place_forget(),
                                                                 Wrook.configure(command = errormessage),
                                                                 Bmove.configure(command = lambda:[Brook.place(x=195, y=175, bordermode=tk.OUTSIDE),
                                                                                                   Wrook.place_forget(),
                                                                                                   draw_msg(text = 'Black wins by checkmate, try again!', x=150),
                                                                                                   Bmove.place_forget()]),
                                                                 Bmove.place(x=300, y=400, bordermode = tk.OUTSIDE),
                                                                 m1.destroy()])
    m1.place(x=220, y=195, bordermode=tk.OUTSIDE)

    Wking.configure(command = errormessage)
    Wrook.configure(command = lambda:[Wking.configure(command = movestart_Wking1_5_2),
                                      Wrook.configure(command = movestart_Wrook4_5),
                                      m1.destroy()])

def movestart_Wking1_5_2():
    m1=tk.Button(height=1, width=1, bg="grey", command = lambda:[Wking.place(x=115, y=175, bordermode=tk.OUTSIDE),
                                                                 Wking.configure(command = errormessage),
                                                                 Bmove.configure(command = lambda:[Brook.place(x=275, y=175, bordermode=tk.OUTSIDE),
                                                                                                   Wrook.place_forget(),
                                                                                                   draw_msg(text = 'Draw by stalemate! Try again!'),
                                                                                                   Bmove.place_forget()]),
                                                                 Bmove.place(x=300, y=400, bordermode = tk.OUTSIDE),
                                                                 m1.destroy()])
    m1.place(x=140, y=195, bordermode=tk.OUTSIDE)
    Wrook.configure(command = errormessage)
    Wking.configure(command = lambda:[Wking.configure(command = movestart_Wking1_5_2),
                                      Wrook.configure(command = movestart_Wrook4_5),
                                      m1.destroy()])

def movestart_king1_4():
    m1=tk.Button(height=1, width=1, bg="grey", command = lambda:[Wking.place(x=115, y=175, bordermode=tk.OUTSIDE),
                                                                 Wking.configure(command = errormessage),
                                                                 Bmove.configure(command = lambda:[Brook.place(x=275, y=175, bordermode=tk.OUTSIDE),
                                                                                                  Wknight.place_forget(),
                                                                                                  draw_msg(text='Draw by stalemate, try again!'),
                                                                                                  Bmove.place_forget()]),
                                                                 Bmove.place(x=300, y=400, bordermode = tk.OUTSIDE),
                                                                 m1.destroy()])
    m1.place(x=140, y=195, bordermode=tk.OUTSIDE),

    Wking.configure(command = lambda:[Wking.configure(command = movestart_king1_4),
                                      m1.destroy()])

def movestart_Wknight4_2():
    m1=tk.Button(height=1, width=1, bg="grey", command = lambda:[Wknight.place(x=115, y=175, bordermode=tk.OUTSIDE),
                                                                 Wknight.configure(command = errormessage),
                                                                 m1.destroy(),
                                                                 m2.destroy(),
                                                                 Bmove.configure(command = lambda:[Bknight.place(x=195, y=175, bordermode=tk.OUTSIDE),
                                                                                                   Wrook.place_forget(),
                                                                                                   draw_msg(text = 'Black wins by checkmate, try again!', x=150),
                                                                                                   Bmove.place_forget()]),
                                                                 Bmove.place(x=300, y=400, bordermode = tk.OUTSIDE)])
    m1.place(x=140, y=195, bordermode=tk.OUTSIDE)

    m2=tk.Button(height=1, width=1, bg="grey", command = lambda:[Wknight.place(x=435, y=175, bordermode=tk.OUTSIDE),
                                                                 Wknight.configure(command = errormessage),
                                                                 Brook.place_forget(),
                                                                 m1.destroy(),
                                                                 m2.destroy(),
                                                                 Bmove.configure(command = lambda:[Bking.place(x=515, y=175, bordermode=tk.OUTSIDE),
                                                                                                   Wking.configure(command = movestart_Wking1_3),
                                                                                                   Wrook.configure(command = movestart_Wrook3_3),
                                                                                                   Wknight.configure(command = movestart_Wknight6_3),
                                                                                                   Bmove.place_forget()]),
                                                                 Bmove.place(x=300, y=400, bordermode = tk.OUTSIDE)])
    m2.place(x=460, y=195, bordermode=tk.OUTSIDE)

    Wknight.configure(command = lambda:[Wking.configure(command = movestart_Wking1_2),
                                        Wrook.configure(command = movestart_Wrook3_2),
                                        Wknight.configure(command = movestart_Wknight4_2),
                                        m1.destroy(),
                                        m2.destroy()])
    Wrook.configure(command = errormessage)

    Wking.configure(command = errormessage)

def movestart_Wking1_3():
    m1=tk.Button(height=1, width=1, bg="grey", command = lambda:[Wking.place(x=115, y=175, bordermode=tk.OUTSIDE),
                                                                 Wking.configure(command = errormessage),
                                                                 m1.destroy(),
                                                                 Bmove.configure(command = lambda:[Bknight.place(x=195, y=175, bordermode=tk.OUTSIDE),
                                                                                                   Wrook.place_forget(),
                                                                                                   draw_msg(text = 'Draw by insufficient material, try again!', x = 150),
                                                                                                   Bmove.place_forget()]),
                                                                 Bmove.place(x=300, y=400, bordermode = tk.OUTSIDE)])
    m1.place(x=140, y=195, bordermode=tk.OUTSIDE)
    
    Wking.configure(command = lambda:[Wking.configure(command = movestart_Wking1_3),
                                      Wrook.configure(command = movestart_Wrook3_3),
                                      Wknight.configure(command = movestart_Wknight6_3),
                                      m1.destroy()])
    Wrook.configure(command = errormessage)
    Wknight.configure(command = errormessage)

def movestart_Wrook3_3():
    m1=tk.Button(height=1, width=1, bg="grey", command = lambda:[Wrook.place(x=115, y=175, bordermode=tk.OUTSIDE),
                                                                 Wrook.configure(command = errormessage),
                                                                 m1.destroy(),
                                                                 m2.destroy(),
                                                                 m3.destroy(),
                                                                 Bmove.configure(command = lambda:[Bknight.place(x=195, y=175, bordermode=tk.OUTSIDE),
                                                                                                   Wrook.configure(command = movestart_Wrook2_4_2),
                                                                                                   Bmove.place_forget()]),
                                                                 Bmove.place(x=300, y=400, bordermode = tk.OUTSIDE)])
    m1.place(x=140, y=195, bordermode=tk.OUTSIDE)
    
    m2=tk.Button(height=1, width=1, bg="grey", command = lambda:[Wrook.place(x=275, y=175, bordermode=tk.OUTSIDE),
                                                                 Wrook.configure(command = errormessage),
                                                                 m1.destroy(),
                                                                 m2.destroy(),
                                                                 m3.destroy(),
                                                                 Bmove.configure(command = lambda:[Bknight.place(x=195, y=175, bordermode=tk.OUTSIDE),
                                                                                                   Wrook.configure(command = movestart_Wrook4_4),
                                                                                                   Wking.configure(command = movestart_Wking1_4_2),
                                                                                                   Bmove.place_forget()]),
                                                                 Bmove.place(x=300, y=400, bordermode = tk.OUTSIDE)])
    m2.place(x=300, y=195, bordermode=tk.OUTSIDE)


    m3=tk.Button(height=1, width=1, bg="grey", command = lambda:[Wrook.place(x=355, y=175, bordermode=tk.OUTSIDE),
                                                                 Wrook.configure(command = errormessage),
                                                                 Bknight.place_forget(),
                                                                 m1.destroy(),
                                                                 m2.destroy(),
                                                                 m3.destroy(),
                                                                 draw_msg(text = 'Draw by stalemate, try again!')])
    m3.place(x=380, y=195, bordermode=tk.OUTSIDE)
    
    Wrook.configure(command = lambda:[Wking.configure(command = movestart_Wking1_3),
                                      Wrook.configure(command = movestart_Wrook3_3),
                                      Wknight.configure(command = movestart_Wknight6_3),
                                      m1.destroy(),
                                      m2.destroy(),
                                      m3.destroy()])
    Wking.configure(command = errormessage)
    Wknight.configure(command = errormessage)

def movestart_Wknight6_3():
    m1=tk.Button(height=1, width=1, bg="grey", command = lambda:[Wknight.place(x=275, y=175, bordermode=tk.OUTSIDE),
                                                                 Wknight.configure(command = errormessage),
                                                                 m1.destroy(),
                                                                 m2.destroy(),
                                                                 Bmove.configure(command = lambda:[Bknight.place(x=195, y=175, bordermode=tk.OUTSIDE),
                                                                                                   Wrook.place_forget(),
                                                                                                   Bmove.place_forget(),
                                                                                                   Wking.configure(command = movestart_Wking1_4)]),
                                                                 Bmove.place(x=300, y=400, bordermode = tk.OUTSIDE)])
    m1.place(x=300, y=195, bordermode=tk.OUTSIDE)

    m2=tk.Button(height=1, width=1, bg="grey", command = lambda:[Wknight.place(x=595, y=175, bordermode=tk.OUTSIDE),
                                                                 Wknight.configure(command = errormessage),
                                                                 m1.destroy(),
                                                                 m2.destroy(),
                                                                 Bmove.configure(command = lambda:[Bknight.place(x=195, y=175, bordermode=tk.OUTSIDE),
                                                                                                   Wrook.place_forget(),
                                                                                                   Bmove.place_forget(),
                                                                                                   Wking.configure(command = movestart_Wking1_4)]),
                                                                 Bmove.place(x=300, y=400, bordermode = tk.OUTSIDE)])
    m2.place(x=620, y=195, bordermode=tk.OUTSIDE)
    
    Wknight.configure(command = lambda:[Wking.configure(command = movestart_Wking1_3),
                                      Wrook.configure(command = movestart_Wrook3_3),
                                      Wknight.configure(command = movestart_Wknight6_3),
                                      m1.destroy(),
                                      m2.destroy()])
    Wrook.configure(command = errormessage)
    Wking.configure(command = errormessage)

def movestart_Wrook2_4_2():
    m1=tk.Button(height=1, width=1, bg="grey", command = lambda:[Wrook.place(x=195, y=175, bordermode=tk.OUTSIDE),
                                                                 Wrook.configure(command = errormessage),
                                                                 Bknight.place_forget(),
                                                                 draw_msg(text = 'Draw by stalemate, try again!'),
                                                                 m1.destroy()])
    m1.place(x=220, y=195, bordermode=tk.OUTSIDE)

    Wrook.configure(command = lambda:[Wrook.configure(command = movestart_Wrook2_4_2),
                                      m1.destroy()])

def movestart_Wrook4_4():
    m1=tk.Button(height=1, width=1, bg="grey", command = lambda:[Wrook.place(x=195, y=175, bordermode=tk.OUTSIDE),
                                                                 Wrook.configure(command = errormessage),
                                                                 Bknight.place_forget(),
                                                                 draw_msg(text = 'Draw by stalemate, try again!'),
                                                                 m1.destroy()])
    m1.place(x=220, y=195, bordermode=tk.OUTSIDE)

    Wrook.configure(command = lambda:[Wrook.configure(command = movestart_Wrook4_4),
                                      Wking.configure(command = movestart_Wking1_4_2),
                                      m1.destroy()])

    Wking.configure(command = errormessage)

def movestart_Wking1_4():
    m1=tk.Button(height=1, width=1, bg="grey", command = lambda:[Wking.place(x=115, y=175, bordermode=tk.OUTSIDE),
                                                                 Wking.configure(command = errormessage),
                                                                 m1.destroy(),
                                                                 draw_msg(text = 'Draw by insufficient material, try again!', x = 150)])
    m1.place(x=140, y=195, bordermode=tk.OUTSIDE)
    
    Wking.configure(command = lambda:[Wking.configure(command = movestart_Wking1_4),
                                      Wrook.configure(command = movestart_Wrook4_4),
                                      m1.destroy()])

def movestart_Wking1_4_2():
    m1=tk.Button(height=1, width=1, bg="grey", command = lambda:[Wking.place(x=115, y=175, bordermode=tk.OUTSIDE),
                                                                 Wking.configure(command = errormessage),
                                                                 Bmove.configure(command = lambda:[Bknight.place(x=355, y=175, bordermode=tk.OUTSIDE),
                                                                                                   Wrook.configure(command = movestart_Wrook4_5_2),
                                                                                                   Wknight.configure(command = movestart_Wknight6_5),
                                                                                                   Wking.configure(command = movestart_Wking2_5),
                                                                                                   Bmove.place_forget()]),
                                                                 Bmove.place(x=300, y=400, bordermode = tk.OUTSIDE),
                                                                 m1.destroy()])
    m1.place(x=140, y=195, bordermode=tk.OUTSIDE)
    
    Wking.configure(command = lambda:[Wrook.configure(command = movestart_Wrook4_4),
                                      Wking.configure(command = movestart_Wking1_4_2),
                                      m1.destroy()])

    Wrook.configure(command = errormessage)

def movestart_Wrook4_5_2():
    m1=tk.Button(height=1, width=1, bg="grey", command = lambda:[Wrook.place(x=195, y=175, bordermode=tk.OUTSIDE),
                                                                 Wrook.configure(command = errormessage),
                                                                 Bmove.configure(command = lambda:[Bknight.place(x=195, y=175, bordermode=tk.OUTSIDE),
                                                                                                   Wrook.place_forget(),
                                                                                                   draw_msg(text = 'Draw by insufficient material, try again!', x = 150),
                                                                                                   Bmove.place_forget()]),
                                                                 Bmove.place(x=300, y=400, bordermode = tk.OUTSIDE),
                                                                 m1.destroy(),
                                                                 m2.destroy()])
    m1.place(x=220, y=195, bordermode=tk.OUTSIDE)

    m2=tk.Button(height=1, width=1, bg="grey", command = lambda:[Wrook.place(x=355, y=175, bordermode=tk.OUTSIDE),
                                                                 Bknight.place_forget(),
                                                                 Wrook.configure(command = errormessage),
                                                                 draw_msg(text = 'Draw by stalemate, try again!'),
                                                                 m1.destroy(),
                                                                 m2.destroy()])
    m2.place(x=380, y=195, bordermode=tk.OUTSIDE)

    Wrook.configure(command = lambda:[Wrook.configure(command = movestart_Wrook4_5_2),
                                      Wknight.configure(command = movestart_Wknight6_5),
                                      Wking.configure(command = movestart_Wking2_5),
                                      m1.destroy(),
                                      m2.destroy()])

    Wknight.configure(command = errormessage)
    Wking.configure(command = errormessage)

def movestart_Wknight6_5():
    m1=tk.Button(height=1, width=1, bg="grey", command = lambda:[Wknight.place(x=595, y=175, bordermode=tk.OUTSIDE),
                                                                 Wknight.configure(command = errormessage),
                                                                 Bmove.configure(command = lambda:[Bking.place(x=595, y=175, bordermode=tk.OUTSIDE),
                                                                                                   Wknight.place_forget(),
                                                                                                   Wrook.configure(command = movestart_Wrook4_6),
                                                                                                   Wking.configure(command = movestart_Wking2_6),
                                                                                                   Bmove.place_forget()]),
                                                                 Bmove.place(x=300, y=400, bordermode = tk.OUTSIDE),
                                                                 m1.destroy()])
    m1.place(x=620, y=195, bordermode=tk.OUTSIDE)

    Wknight.configure(command = lambda:[Wrook.configure(command = movestart_Wrook4_5_2),
                                      Wknight.configure(command = movestart_Wknight6_5),
                                      Wking.configure(command = movestart_Wking2_5),
                                      m1.destroy()])

    Wrook.configure(command = errormessage)
    Wking.configure(command = errormessage)

def movestart_Wking2_5():
    m1=tk.Button(height=1, width=1, bg="grey", command = lambda:[Wking.place(x=35, y=175, bordermode=tk.OUTSIDE),
                                                                 Wking.configure(command = errormessage),
                                                                 Bmove.configure(command = lambda:[Bknight.place(x=195, y=175, bordermode=tk.OUTSIDE),
                                                                                                   draw_msg(text = 'Draw by repetition, try again'),
                                                                                                   Bmove.place_forget()]),
                                                                 Bmove.place(x=300, y=400, bordermode = tk.OUTSIDE),
                                                                 m1.destroy()])
    m1.place(x=60, y=195, bordermode=tk.OUTSIDE)

    Wking.configure(command = lambda:[Wrook.configure(command = movestart_Wrook4_5_2),
                                      Wknight.configure(command = movestart_Wknight6_5),
                                      Wking.configure(command = movestart_Wking2_5),
                                      m1.destroy()])

    Wknight.configure(command = errormessage)
    Wrook.configure(command = errormessage)

def movestart_Wking2_6():
    m1=tk.Button(height=1, width=1, bg="grey", command = lambda:[Wking.place(x=35, y=175, bordermode=tk.OUTSIDE),
                                                                 Wking.configure(command = errormessage),
                                                                 draw_msg(text = 'You ran out of moves! Try again!', x = 150),
                                                                 m1.destroy()])
    m1.place(x=60, y=195, bordermode=tk.OUTSIDE)

    Wking.configure(command = lambda:[Wrook.configure(command = movestart_Wrook4_6),
                                      Wking.configure(command = movestart_Wking2_6),
                                      m1.destroy()])

    Wrook.configure(command = errormessage)

def movestart_Wrook4_6():
    m1=tk.Button(height=1, width=1, bg="grey", command = lambda:[Wrook.place(x=195, y=175, bordermode=tk.OUTSIDE),
                                                                 Wrook.configure(command = errormessage),
                                                                 draw_msg(text = 'You ran out of moves! Try again!', x = 150),
                                                                 m1.destroy(),
                                                                 m2.destroy()])
    m1.place(x=220, y=195, bordermode=tk.OUTSIDE)

    m2=tk.Button(height=1, width=1, bg="grey", command = lambda:[Wrook.place(x=355, y=175, bordermode=tk.OUTSIDE),
                                                                 Bknight.place_forget(),
                                                                 Wrook.configure(command = errormessage),
                                                                 draw_msg(text = 'You won by checkmate! Well played!', x = 150),
                                                                 m1.destroy(),
                                                                 m2.destroy()])
    m2.place(x=380, y=195, bordermode=tk.OUTSIDE)

    Wrook.configure(command = lambda:[Wrook.configure(command = movestart_Wrook4_6),
                                      Wking.configure(command = movestart_Wking2_6),
                                      m1.destroy(),
                                      m2.destroy()])

    Wking.configure(command = errormessage)
def errormessage():
    print("You can't move that piece.")

photo_Wknight = tk.PhotoImage(file = "./media/692-6922282_chess-knight-transparent-png-clipart-free-download-white.png")
photo_Wknight = photo_Wknight.subsample(2, 2)

photo_Bknight = tk.PhotoImage(file = "./media/chess-piece-knight-pin-clip-art-png-favpng-mtRQMZRbbHaYLuVXDxNbcUv9p.png")
photo_Bknight = photo_Bknight.subsample(2, 2)

photo_Wking = tk.PhotoImage(file = "./media/42-427843_chess-king.png")
photo_Wking = photo_Wking.subsample(2,2)

photo_Bking = tk.PhotoImage(file = "./media/3398_black-king.png")
photo_Bking = photo_Bking.subsample(2,2)

photo_Wrook = tk.PhotoImage(file = "./media/chess-piece-rook-king-chessboard-png-favpng-6q9QZnYbHbk7vfyQmK0wrgNdU.png")
photo_Wrook = photo_Wrook.subsample(2,2)

photo_Brook = tk.PhotoImage(file = "./media/png-clipart-chess-piece-rook-pawn-white-and-black-in-chess-chess-game-angle.png")
photo_Brook = photo_Brook.subsample(2,2)

Wking = tk.Button(height=60, width=60, text='wking',image = photo_Wking, command = errormessage)
Wking.place(x=35, y=175, bordermode=tk.OUTSIDE)

Wknight = tk.Button(height=60, width=60, image = photo_Wknight, command = movestart_Wknight)
Wknight.place(x=115, y=175, bordermode=tk.OUTSIDE)

Wrook = tk.Button(height=60, width=60, text='wrook', image = photo_Wrook, command = movestart_Wrook)
Wrook.place(x=195, y=175, bordermode=tk.OUTSIDE)

Brook = tk.Button(height=60, width=60, text='brook', image = photo_Brook, command = errormessage)
Brook.place(x=435, y=175, bordermode=tk.OUTSIDE)

Bknight = tk.Button(height=60, width=60, text='bknight',  image = photo_Bknight, command = errormessage)
Bknight.place(x=515, y=175, bordermode=tk.OUTSIDE)

Bking = tk.Button(height=60, width=60, text='bking', image = photo_Bking, command = errormessage)
Bking.place(x=595, y=175, bordermode=tk.OUTSIDE)


Bmove = tk.Button(height = 2, width = 9, text = 'Black moves')

menu.mainloop()
