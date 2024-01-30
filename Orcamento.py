
from fpdf import FPDF

projeto = input("Digite a descrição do projeto: ")
horas_estimadas = input("Digite o total de horas estimadas: ")
valor_hora = input("Digite o valor da hora trabalhada: ")
prazo_estipulado = input("Digite o prazo estipulado: ")

valor_total_estimado = int(horas_estimadas) * int(valor_hora)




pdf = FPDF()
pdf.add_page()
pdf.set_font("arial")

pdf.image("template.png", x=0, y=0)

pdf.text(115, 145, projeto)
pdf.text(115, 160, horas_estimadas)
pdf.text(115, 175, valor_hora)
pdf.text(115, 190, prazo_estipulado)
pdf.text(115, 205, str(valor_total_estimado))

pdf.output("Orçamento.pdf")
print("Orçamento gerado com sucesso!")