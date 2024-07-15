import tkinter as tk

main_window = tk.Tk()
main_window.title('Cleytin')
main_window.geometry('600x600')
main_window.grid()

frame = tk.Frame(main_window, background='#000000')
frame.grid()

label = tk.Label(
    frame, text="Essa é a primeira label!", 
    foreground='#3E77B6', # Cor da fonte 
    background='black', # Cor do fundo
    font='48px' # Tamanho da fonte
    )
label.grid(row=0, column=0)

label2 = tk.Label(
    frame, text="Essa é a segunda label!", 
    foreground='#3E77B6', # Cor da fonte 
    background='red', # Cor do fundo
    font='48px' # Tamanho da fonte
    )
label2.grid(row=0, column=1)

label3 = tk.Label(
    frame, text="Essa é a terceira label!", 
    foreground='#3E77B6', # Cor da fonte 
    background='lightgreen', # Cor do fundo
    font='48px' # Tamanho da fonte
    )
label3.grid(row=1, column=0)

label4 = tk.Label(
    frame, text="Essa é a quarta label!", 
    foreground='#3E77B6', # Cor da fonte 
    background='yellow', # Cor do fundo
    font='48px' # Tamanho da fonte
    )
label4.grid(row=1, column=1)

main_window.mainloop()