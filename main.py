"""
Para inserir os valores no programa, você pode seguir o formato esperado para cada entrada. Vou explicar como você deve inserir os valores para cada campo:

Horário de Entrada (HH:MM):

Insira o horário de entrada no formato de 24 horas, separando as horas e os minutos por dois pontos. Exemplo: "08:30" para 8 horas e 30 minutos.
Duração do Expediente (em horas):

Insira a duração do expediente em horas, usando um número decimal se necessário. Exemplo: "8.5" para 8 horas e 30 minutos.
Intervalo para Almoço (em minutos):

Insira a duração do intervalo para o almoço em minutos. Exemplo: "60" para uma hora de intervalo.
Depois de inserir os valores nos campos correspondentes, clique no botão "Calcular". O programa calculará o horário de saída e exibirá o resultado na parte inferior da janela.

"""
import customtkinter as tk
from datetime import datetime, timedelta
from PIL import Image,ImageTk
class CalculadoraHoras(tk.CTk):
    def __init__(self):
        super().__init__()
        #Imagem do tempo
        img = (Image.open("desenho_tempo1.png"))
        resized_image= img.resize((280,300))
        my_img=ImageTk.PhotoImage(resized_image)

        #colocando a imagem em Label e customizando Logo Corporate
        label= tk.CTkLabel(self, image=my_img,text="")
        label.pack()
        label.place(x=240, y=20)


        font_text_label = ("Artifakt Element Heavy", 13, 'bold')
        font_text_result = ("Artifakt Element Heavy", 16,'bold')

        self.resizable(False, False)#Congelando a tela do App
        self.title("Banco de Horas")# Titulo do App
        self.geometry("500x400")# Altura e Largura da tela
        self.iconbitmap('relogio.ico')# Icone Relogio
        self._set_appearance_mode('darkgreen')# Tema do App

        self.label_entrada = tk.CTkLabel(self, text="Horário de Entrada (em horas):",font=font_text_label)
        self.label_entrada.pack()
        self.label_entrada.place(x=10,y=10)
        

        self.entrada_horario = tk.CTkEntry(self,placeholder_text="(HH:MM)",width=200,height=40)
        self.entrada_horario.pack()
        self.entrada_horario.place(x=10,y=40)

        self.label_duracao = tk.CTkLabel(self, text="Duração do Expediente (em horas):",font=font_text_label)
        self.label_duracao.pack()
        self.label_duracao.place(x=10,y=80)
        

        self.entrada_duracao = tk.CTkEntry(self,placeholder_text='(HH:MM)',width=200,height=40)
        self.entrada_duracao.pack()
        self.entrada_duracao.place(x=10,y=120)

        self.label_intervalo = tk.CTkLabel(self, text="Intervalo para Almoço (em minutos):",font=font_text_label)
        self.label_intervalo.pack()
        self.label_intervalo.place(x=10,y=160)
        

        self.entrada_intervalo = tk.CTkEntry(self,placeholder_text="60 minutos",width=200,height=40)
        self.entrada_intervalo.pack()
        self.entrada_intervalo.place(x=10, y=200)

        self.botao_calcular = tk.CTkButton(self, text="Calcular",
                                        command=self.calcular_horario_saida,
                                        width=200,
                                        height=40,
                                        border_width=0,
                                        corner_radius=8)
        
        self.botao_calcular.pack()
        self.botao_calcular.place(x=10, y=260)

        self.label_resultado = tk.CTkLabel(self, text="",font= font_text_result)
        self.label_resultado.pack()
        self.label_resultado.place(x=70,y=310)

    def calcular_horario_saida(self):
        horario_entrada_str = self.entrada_horario.get()
        duracao_str = self.entrada_duracao.get()
        intervalo_str = self.entrada_intervalo.get()
        

        try:
            horario_entrada = datetime.strptime(horario_entrada_str, "%H:%M")
            duracao = timedelta(hours=float(duracao_str.split(':')[0]), minutes=float(duracao_str.split(':')[1]))
            intervalo = timedelta(minutes=float(intervalo_str))
            

            horario_saida = horario_entrada + duracao + intervalo
            horario_extra = horario_entrada + duracao + intervalo + timedelta(hours=2)

            resultado_str = f"Você deve sair às: {horario_saida.strftime('%H:%M')},\n Podendo sair até às: {horario_extra.strftime('%H:%M')} \n ATENÇÃO APÓS ISSO SERÁ HORA IRREGULAR"
            self.label_resultado.configure(text=resultado_str)

        except ValueError:
            self.label_resultado.configure(text="Valores incorretos, preencha-os novamente.")


if __name__ == "__main__":
    app = CalculadoraHoras()
    app.mainloop()
