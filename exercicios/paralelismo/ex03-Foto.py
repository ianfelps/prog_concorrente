from PIL import Image
from tkinter import Tk, filedialog
import threading
import time


def processar_faixa(imagem, imagem_pb, inicio_y, fim_y):
    """Processa uma faixa horizontal da imagem"""
    largura = imagem.width
    for x in range(largura):
        for y in range(inicio_y, fim_y):
            r, g, b = imagem.getpixel((x, y))
            luminancia = int(0.299 * r + 0.587 * g + 0.114 * b)
            imagem_pb.putpixel((x, y), luminancia)


def converter_para_preto_e_branco_threaded():
    try:
        # Configuração inicial (seleção de arquivo)
        root = Tk()
        root.withdraw()
        caminho_imagem = filedialog.askopenfilename(
            title="Selecione uma imagem",
            filetypes=[("Imagens", "*.jpg *.jpeg *.png *.bmp *.gif"),
                       ("Todos os arquivos", "*.*")]
        )

        if not caminho_imagem:
            print("Nenhuma imagem foi selecionada.")
            return

        # Carrega a imagem
        imagem = Image.open(caminho_imagem)
        imagem = imagem.convert("RGB")
        largura, altura = imagem.size
        imagem_pb = Image.new("L", (largura, altura))

        # Configuração do threading
        num_threads = 4  # Pode ajustar conforme o número de núcleos do processador
        faixas_por_thread = altura // num_threads
        threads = []

        # Medição do tempo de execução
        inicio = time.time()

        # Cria e inicia as threads
        for i in range(num_threads):
            inicio_y = i * faixas_por_thread
            fim_y = (i + 1) * faixas_por_thread if i != num_threads - \
                1 else altura

            thread = threading.Thread(
                target=processar_faixa,
                args=(imagem, imagem_pb, inicio_y, fim_y)
            )
            threads.append(thread)
            thread.start()

        # Aguarda todas as threads terminarem
        for thread in threads:
            thread.join()

        tempo_total = time.time() - inicio
        print(
            f"Conversão concluída em {tempo_total:.2f} segundos usando {num_threads} threads")

        # Salva a imagem
        caminho_saida = filedialog.asksaveasfilename(
            title="Salvar imagem em preto e branco",
            defaultextension=".jpg",
            filetypes=[("JPEG", "*.jpg"), ("PNG", "*.png"),
                       ("Todos os arquivos", "*.*")]
        )

        if not caminho_saida:
            print("Operação de salvamento cancelada.")
            return

        imagem_pb.save(caminho_saida)
        print(f"Imagem convertida com sucesso! Salva em: {caminho_saida}")

    except Exception as e:
        print(f"Erro ao processar a imagem: {e}")


def main():
    inicio = time.time()
    converter_para_preto_e_branco_threaded()
    tempo_total = time.time() - inicio
    print(f"Tempo de execução com threads: {tempo_total:.2f} segundos")


if __name__ == "__main__":
    main()
