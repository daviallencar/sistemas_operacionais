import threading
import time
import random

# Número de filósofos
NUM_FILOSOFOS = 5

# Criação de um garfo (lock) para cada filósofo
garfos = [threading.Lock() for _ in range(NUM_FILOSOFOS)]

# Lock adicional para organizar a impressão na tela
print_lock = threading.Lock()

def filosofo(id):
    id += 1  # Ajuste para ID humano (começando em 1)

    # Definindo garfos à esquerda e à direita
    esquerda = garfos[(id - 1) % NUM_FILOSOFOS]
    direita = garfos[id % NUM_FILOSOFOS]

    # Estratégia para evitar deadlock:
    # O filósofo 1 pega primeiro o garfo da direita
    if id == 1:
        primeiro, segundo = direita, esquerda
    else:
        primeiro, segundo = esquerda, direita

    while True:
        # Pensando
        with print_lock:
            print(f"[Filósofo {id}] 💭 Está pensando...")
        time.sleep(random.uniform(0.5, 1.5))  # Tempo aleatório pensando

        # Tentando pegar os garfos
        with print_lock:
            print(f"[Filósofo {id}] 🥢 Tentando pegar os garfos.")

        # Pega primeiro garfo
        with print_lock:
            print(f"[Filósofo {id}] ✋ Esperando primeiro garfo...")
        primeiro.acquire()
        with print_lock:
            print(f"[Filósofo {id}] ✅ Pegou o primeiro garfo.")

        # Pega segundo garfo
        with print_lock:
            print(f"[Filósofo {id}] ✋ Esperando segundo garfo...")
        segundo.acquire()
        with print_lock:
            print(f"[Filósofo {id}] ✅ Pegou o segundo garfo.")

        # Comendo
        with print_lock:
            print(f"[Filósofo {id}] 🍝 Está comendo!")
        time.sleep(random.uniform(0.5, 1.5))  # Tempo aleatório comendo

        # Devolvendo os garfos
        primeiro.release()
        segundo.release()
        with print_lock:
            print(f"[Filósofo {id}] 🔄 Devolveu os garfos.")

def jantar():
    # Cria e inicia uma thread para cada filósofo
    filosofos = []
    for i in range(NUM_FILOSOFOS):
        t = threading.Thread(target=filosofo, args=(i,))
        filosofos.append(t)
        t.start()

    # Mantém o programa rodando (não encerramos as threads)
    for t in filosofos:
        t.join()

# Execução principal
if __name__ == "__main__":
    jantar()
