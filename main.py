import flet as ft
import matplotlib.pyplot as plt
import tempfile

plt.switch_backend('Agg')

# Função para criar o gráfico
def create_plot():
    # Criando o gráfico com os valores de result_1 e result_2
    fig, ax = plt.subplots()
    fig.patch.set_facecolor('none')
    ax.set_facecolor('none')
    ax.bar([1, 2], [50, 70], tick_label=["Produto 1", "Produto 2"],
           color=['#bc8d27', '#976f17'], )  # Plotando os dois resultados (produto 1 e 2)
    ax.set_xticks([1, 2])  # Definindo as posições no eixo X
    ax.set_xticklabels(["Produto 1", "Produto 2"], fontsize=15, color='white')  # Nomeando os pontos do eixo X
    ax.get_yaxis().set_visible(False)
    ax.tick_params(axis='y', labelcolor='white')

    for spine in ax.spines.values():
        spine.set_visible(False)

    # Salvando o gráfico diretamente em um arquivo temporário
    img_path = "/tmp/plot.png"
    plt.savefig(img_path, format='png')  # Salvando diretamente no caminho
    plt.close()  # Fechar o gráfico para liberar os recursos

    return img_path


# Função para atualizar o gráfico no Flet
def update_plot(result_1_value, result_2_value, flet_img):
    # Gerando o gráfico e obtendo o caminho da imagem
    img_path = create_plot(result_1_value, result_2_value)

    # Atualizando o caminho da imagem no Flet
    flet_img.src = img_path
    flet_img.update()


# Função principal do Flet
def main(page: ft.Page):
    page.title = 'Comparador de Preços com Gráfico'
    page.vertical_alignment = ft.MainAxisAlignment.START

    img_path = create_plot()

    # Imagem para exibir o gráfico
    flet_img = ft.Image(src=img_path, width=300, height=200)

    # Layout
    page.add(

        flet_img
    )


# Inicializando o aplicativo Flet
ft.app(target=main)
