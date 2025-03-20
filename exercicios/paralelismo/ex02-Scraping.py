import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import threading

class WebScraper:
    def __init__(self, url_inicial, palavra, profundidade_maxima=3, max_threads=10):
        self.url_inicial = url_inicial
        self.palavra = palavra.lower()
        self.profundidade_maxima = profundidade_maxima
        self.urls_visitados = set()
        self.resultados = {}
        self.lock = threading.Lock()
        self.semaforo = threading.Semaphore(max_threads)  # Limita o número de threads simultâneas
    
    def buscar_recursivo(self, url_atual, profundidade_atual):
        if profundidade_atual > self.profundidade_maxima:
            return

        with self.lock:
            if url_atual in self.urls_visitados:
                return
            self.urls_visitados.add(url_atual)
        
        try:
            with self.semaforo:  # Controla o número de threads ativas
                print(f"Buscando em: {url_atual} (Profundidade: {profundidade_atual})")
                response = requests.get(url_atual, timeout=10)
                response.raise_for_status() # Lança exceção para erros HTTP

                # Analisa o conteúdo HTML
                soup = BeautifulSoup(response.text, 'html.parser')

                # Verifica se a palavra está no conteúdo da página
                conteudo = soup.get_text().lower()
                palavra_encontrada = self.palavra in conteudo
                
                with self.lock:
                    self.resultados[url_atual] = palavra_encontrada
                
                # Extrai todos os links da página
                links = [urljoin(self.url_inicial, link['href']) for link in soup.find_all('a', href=True)]
                threads = []
                for link in links:
                    # Garante que só navegamos dentro do mesmo domínio
                    if link.startswith(self.url_inicial):
                        thread = threading.Thread(target=self.buscar_recursivo, args=(link, profundidade_atual + 1))
                        thread.start()
                        threads.append(thread)
                
                for thread in threads:
                    thread.join()

        except requests.exceptions.RequestException as e:
            print(f"Erro ao acessar {url_atual}: {e}")

    # Inicia a busca recursiva
    def iniciar_busca(self):
        self.buscar_recursivo(self.url_inicial, profundidade_atual=1)
        return self.resultados

# Exemplo de uso
if __name__ == "__main__":
    url_inicial = input("Digite a URL inicial do site (ex.: https://www.exemplo.com): ")
    palavra = input("Digite a palavra a ser buscada: ")
    
    scraper = WebScraper(url_inicial, palavra)
    resultados = scraper.iniciar_busca()
    
    print("\nResultados da busca:")
    for url, encontrada in resultados.items():
        status = "Encontrada" if encontrada else "Não encontrada"
        print(f"{url}: Palavra '{palavra}' {status}")