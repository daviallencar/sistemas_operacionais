# Sistema Operacional - Filósofos Jantando

Este repositório contém a implementação do **Problema dos Filósofos Jantando**, um problema clássico de sincronização de processos em sistemas operacionais. A solução foi desenvolvida em **Python**, utilizando conceitos de **concurrency** (concorrência) e **threads** para simular o comportamento dos filósofos.

## O Problema

O **Problema dos Filósofos Jantando** é um exemplo clássico utilizado para estudar como gerenciar recursos compartilhados de forma eficaz e evitar condições indesejáveis como **deadlocks** e **starvation**. 

Em um cenário simplificado, temos **5 filósofos** sentados à mesa, onde cada um possui dois garfos à sua disposição (um à esquerda e outro à direita). Eles alternam entre **pensar** e **comer**, mas para comer, precisam de dois garfos simultaneamente. O desafio é garantir que os filósofos possam comer sem que o sistema entre em deadlock ou starvation.

## Objetivos do Projeto

- **Sincronização de Threads**: Utilizando `threading` para simular a execução simultânea dos filósofos.
- **Evitar Deadlocks**: Implementação de controle de concorrência para garantir que os filósofos não bloqueiem uns aos outros de forma indefinida.
- **Gestão de Recursos**: Uso de mutexes para garantir que apenas um filósofo utilize um garfo por vez, evitando conflitos.

## Como Funciona a Implementação

- Cada filósofo é representado como uma thread que alterna entre dois estados: **pensando** e **comendo**.
- Para comer, o filósofo precisa pegar dois garfos, e para evitar deadlocks, a estratégia de sincronização garante que um filósofo só possa pegar os garfos quando ambos estiverem disponíveis.
- Após terminar de comer, o filósofo devolve os garfos para que outros possam usá-los.
