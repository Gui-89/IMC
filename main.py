import tkinter as tk


def calc_imc():
    altura = float(entry_altura.get())
    peso = float(entry_peso.get())

    IMC = peso / (altura/100)**2

    if IMC < 18.5:
        label_result["text"] = f'Seu IMC é de {IMC:.2f}, e é classificado como Magreza!'
    elif IMC >= 18.5 and IMC < 24.9:
        label_result["text"] = f'Seu IMC é de {IMC:.2f}, e é classificado como Normal!'
    elif IMC >= 25 and IMC < 29.9:
        label_result["text"] = f'Seu IMC é de {IMC:.2f}, e é classificado como Sobrepeso!'
    elif IMC >= 30 and IMC < 39.9:
        label_result["text"] = f'Seu IMC é de {IMC:.2f}, e é classificado como Obesidade!'
    else:
        label_result["text"] = "Pode para de comer e começar a malhar pois o negócio está feio! Obesidade Grave!!!"


root = tk.Tk()
root.title("Calculadora de IMC")
root.geometry("530x160")


label_altura = tk.Label(root, text="Altura (cm)")
label_altura.pack()

entry_altura = tk.Entry(root)
entry_altura.pack()

label_peso = tk.Label(root, text="Peso (kg)")
label_peso.pack()

entry_peso = tk.Entry(root)
entry_peso.pack()

calc_button = tk.Button(root, text="Calcular IMC", command=calc_imc)
calc_button.pack()

label_result = tk.Label(root, text="")
label_result.pack()

root.mainloop()
