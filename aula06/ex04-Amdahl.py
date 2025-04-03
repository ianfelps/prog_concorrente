import matplotlib.pyplot as plt

# função para calcular o speedup
def speedup(f, p_values):
    results = [(p, 1 / ((1 - f) + f / p)) for p in p_values]
    return results

f = 0.6 # 60% do código paralelizável
p_values = [1, 2, 4, 8, 16, 32]
speedups = speedup(f, p_values)

# exibindo os resultados
print("p\tSpeedup")
for p, speedup in speedups:
    print(f"{p}\t{speedup:.2f}")

# gráfico
plt.plot(p_values, [s[1] for s in speedups], marker='o')
plt.xlabel("Número de Processadores (p)")
plt.ylabel("Speedup (S(p))")
plt.title(f"Speedup vs Processadores para f = {f}")
plt.grid()
plt.show()