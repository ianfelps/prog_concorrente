import matplotlib.pyplot as plt
import numpy as np
import random
import os
import threading
import time

# Configuração para salvar as imagens na área de trabalho
DESKTOP_PATH = os.path.join(os.path.expanduser("~"), "Desktop")

# Função para gerar fractais usando um Sistema de Funções Iteradas (IFS)
def gerar_fractal(transformacoes, probabilidades, iteracoes=100000):
    if not abs(sum(probabilidades) - 1.0) < 1e-6:
        raise ValueError("As probabilidades devem somar 1.")
    
    x, y = 0.0, 0.0
    pontos = []

    for _ in range(iteracoes):
        r = random.random()
        acumulado = 0.0
        for i, prob in enumerate(probabilidades):
            acumulado += prob
            if r < acumulado:
                transformacao = transformacoes[i]
                break
        
        x, y = transformacao(x, y)
        pontos.append((x, y))
    
    return pontos

# Função para salvar a figura com timestamp
def save_fig(fig, name):
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    filename = f"{name}_{timestamp}.png"
    filepath = os.path.join(DESKTOP_PATH, filename)
    fig.savefig(filepath, bbox_inches='tight', dpi=300)
    plt.close(fig)
    print(f"Saved: {filepath}")

# Funções de geração de fractais (cada uma será executada em uma thread separada)

def sierpinski():
    print("Iniciando geração do Triângulo de Sierpinski...")
    start_time = time.time()
    
    transformacoes = [
        lambda x, y: (0.5 * x, 0.5 * y),
        lambda x, y: (0.5 * x + 0.5, 0.5 * y),
        lambda x, y: (0.5 * x + 0.25, 0.5 * y + 0.5)
    ]
    probabilidades = [1/3, 1/3, 1/3]
    pontos = gerar_fractal(transformacoes, probabilidades, iteracoes=100000)

    x_vals, y_vals = zip(*pontos)
    fig, ax = plt.subplots()
    ax.scatter(x_vals, y_vals, s=0.1, color='black', marker='.')
    ax.set_title("Triângulo de Sierpinski")
    ax.axis('off')
    save_fig(fig, "sierpinski")
    print(f"Triângulo de Sierpinski concluído em {time.time() - start_time:.2f} segundos")

def samambaia_barnsley():
    print("Iniciando geração da Samambaia de Barnsley...")
    start_time = time.time()
    
    transformacoes = [
        lambda x, y: (0.0, 0.16 * y),
        lambda x, y: (0.85 * x + 0.04 * y, -0.04 * x + 0.85 * y + 1.6),
        lambda x, y: (0.2 * x - 0.26 * y, 0.23 * x + 0.22 * y + 1.6),
        lambda x, y: (-0.15 * x + 0.28 * y, 0.26 * x + 0.24 * y + 0.44)
    ]
    probabilidades = [0.01, 0.85, 0.07, 0.07]
    pontos = gerar_fractal(transformacoes, probabilidades, iteracoes=100000)

    x_vals, y_vals = zip(*pontos)
    fig, ax = plt.subplots()
    ax.scatter(x_vals, y_vals, s=0.1, color='green', marker='.')
    ax.set_title("Samambaia de Barnsley")
    ax.axis('off')
    save_fig(fig, "samambaia_barnsley")
    print(f"Samambaia de Barnsley concluída em {time.time() - start_time:.2f} segundos")

def mandelbrot():
    print("Iniciando geração do Conjunto de Mandelbrot...")
    start_time = time.time()
    
    width, height = 800, 800
    max_iter = 100
    x_min, x_max = -2.0, 1.0
    y_min, y_max = -1.5, 1.5
    image = np.zeros((height, width))

    for row in range(height):
        for col in range(width):
            c = complex(x_min + (x_max - x_min) * col / width,
                        y_min + (y_max - y_min) * row / height)
            z = 0.0j
            n = 0
            while abs(z) <= 2 and n < max_iter:
                z = z * z + c
                n += 1
            image[row, col] = n

    fig, ax = plt.subplots()
    ax.imshow(image, extent=(x_min, x_max, y_min, y_max), cmap='hot', interpolation='bilinear')
    ax.set_title("Conjunto de Mandelbrot")
    ax.axis('off')
    save_fig(fig, "mandelbrot")
    print(f"Conjunto de Mandelbrot concluído em {time.time() - start_time:.2f} segundos")

def julia():
    print("Iniciando geração do Conjunto de Julia...")
    start_time = time.time()
    
    c = -0.7 + 0.27015j
    width, height = 800, 800
    max_iter = 100
    x_min, x_max = -1.5, 1.5
    y_min, y_max = -1.5, 1.5
    image = np.zeros((height, width))

    for row in range(height):
        for col in range(width):
            z = complex(x_min + (x_max - x_min) * col / width,
                        y_min + (y_max - y_min) * row / height)
            n = 0
            while abs(z) <= 2 and n < max_iter:
                z = z * z + c
                n += 1
            image[row, col] = n

    fig, ax = plt.subplots()
    ax.imshow(image, extent=(x_min, x_max, y_min, y_max), cmap='twilight_shifted', interpolation='bilinear')
    ax.set_title("Conjunto de Julia")
    ax.axis('off')
    save_fig(fig, "julia")
    print(f"Conjunto de Julia concluído em {time.time() - start_time:.2f} segundos")

def koch_curve():
    print("Iniciando geração da Curva de Koch...")
    start_time = time.time()
    
    def koch_curve_recursive(points, order):
        if order == 0:
            return points
        new_points = []
        for i in range(len(points) - 1):
            p1, p2 = points[i], points[i + 1]
            dx, dy = p2[0] - p1[0], p2[1] - p1[1]
            new_points.append(p1)
            new_points.append((p1[0] + dx / 3, p1[1] + dy / 3))
            new_points.append((p1[0] + dx / 2 - dy * np.sqrt(3) / 6, p1[1] + dy / 2 + dx * np.sqrt(3) / 6))
            new_points.append((p1[0] + 2 * dx / 3, p1[1] + 2 * dy / 3))
        new_points.append(points[-1])
        return koch_curve_recursive(new_points, order - 1)

    points = [(0, 0), (300, 0)]
    points = koch_curve_recursive(points, 4)

    x_vals, y_vals = zip(*points)
    fig, ax = plt.subplots()
    ax.plot(x_vals, y_vals, color='blue', linewidth=1)
    ax.set_title("Curva de Koch")
    ax.axis('equal')
    ax.axis('off')
    save_fig(fig, "koch_curve")
    print(f"Curva de Koch concluída em {time.time() - start_time:.2f} segundos")

def fractal_tree():
    print("Iniciando geração da Árvore Fractal...")
    start_time = time.time()
    
    def draw_tree(ax, x, y, length, angle, depth):
        if depth == 0:
            return
        x_end = x + length * np.cos(np.radians(angle))
        y_end = y + length * np.sin(np.radians(angle))
        ax.plot([x, x_end], [y, y_end], color='brown', linewidth=1)
        draw_tree(ax, x_end, y_end, length * 0.7, angle - 30, depth - 1)
        draw_tree(ax, x_end, y_end, length * 0.7, angle + 30, depth - 1)

    fig, ax = plt.subplots()
    draw_tree(ax, 0, 0, 100, 90, 8)
    ax.set_title("Árvore Fractal")
    ax.axis('equal')
    ax.axis('off')
    save_fig(fig, "fractal_tree")
    print(f"Árvore Fractal concluída em {time.time() - start_time:.2f} segundos")

def sierpinski_carpet():
    print("Iniciando geração do Tapete de Sierpinski...")
    start_time = time.time()
    
    def recursive_remove(grid, x, y, size, iteration):
        if iteration == 0:
            return
        sub_size = size // 3
        for i in range(3):
            for j in range(3):
                if i == 1 and j == 1:
                    grid[x + sub_size:x + 2 * sub_size, y + sub_size:y + 2 * sub_size] = 0
                else:
                    recursive_remove(grid, x + i * sub_size, y + j * sub_size, sub_size, iteration - 1)

    size = 3**4
    carpet = np.ones((size, size))
    recursive_remove(carpet, 0, 0, size, 4)

    fig, ax = plt.subplots()
    ax.imshow(carpet, cmap='gray_r')
    ax.set_title("Tapete de Sierpinski")
    ax.axis('off')
    save_fig(fig, "sierpinski_carpet")
    print(f"Tapete de Sierpinski concluído em {time.time() - start_time:.2f} segundos")

# Função principal para executar todos os fractais em threads separadas
def gerar_todos_fractais():
    # Lista de funções de geração de fractais
    fractal_functions = [
        sierpinski,
        samambaia_barnsley,
        mandelbrot,
        julia,
        koch_curve,
        fractal_tree,
        sierpinski_carpet
    ]

    # Criar e iniciar threads para cada fractal
    threads = []
    for fractal_func in fractal_functions:
        thread = threading.Thread(target=fractal_func)
        threads.append(thread)
        thread.start()

    # Aguardar todas as threads terminarem
    for thread in threads:
        thread.join()

    print("Todos os fractais foram gerados com sucesso!")

if __name__ == "__main__":
    gerar_todos_fractais()