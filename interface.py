import customtkinter as ctk


janela = ctk.CTk()

ctk.set_appearance_mode("system")

janela.title("EduAnalytics | Desempenho Aluno")

janela.geometry("1000x650")

janela.minsize(800, 500)


painel = ctk.CTkFrame(
    janela,
    width = 200,
    height = 500
)

painel.pack(side ="left" , fill ="y")

conteudo = ctk.CTkFrame(
    janela,
    width= 700,
    height = 300

)
conteudo.pack(side = "right", fill = 'both',expand=True)

titulo = ctk.CTkLabel(painel,
                      text="EduAnalytics",
                      font=("Arial", 22, "bold")
                      )


titulo.pack(padx=15, pady=10, anchor="nw")

botao_alunos = ctk.CTkButton(
    painel,
    text="Alunos",
    fg_color = "#2563EB",
    text_color = "#FFFFFF",
    corner_radius = 10
)

botao_alunos.pack(padx=15, pady=8, fill = "x")

botao_desempenho = ctk.CTkButton(
    painel,
    text="Desempenho"
)

botao_desempenho.pack(padx=15, pady=8, fill = "x")


botao_relatorios = ctk.CTkButton(
    painel,
    text="Relatorios"
)

botao_relatorios.pack(padx=15, pady=8, fill = "x")




janela.mainloop()




