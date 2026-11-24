import csv
import time 
from pathlib import Path 
from gnome_sort import gnome_sort
from tournament_sort import tournament_sort
from pancake_sort import pancake_sort

def executar_benchmark(lista, repeticoes=10): 
    resultados = [] 
    lista_esperada = sorted(lista)
    algoritmos = [
        ("gnome Sort", gnome_sort), 
        ("tournament Sort", tournament_sort)
    ]
    for repeticao in range(1, repeticoes + 1): 
        for nome, algoritmo in algoritmos: 
            dados = lista.copy()
            inicio = time.perf_counter() 
            resultado = algoritmo(dados)
            fim = time.perf_counter() 
            tempo_execucao 
            if resultado is None: 
                resultado = dados
            if resultado != lista_esperada: 
                raise ValueError( 
                    f"{nome} não ordenou corretamente os dados."
                ) 
            resultados.append({
                "algoritmo": nome,
                "tamanho": len(lista),
                "repeticao": repeticao,
                "tempo_segundos": tempo_execucao
            })
    pasta = Path("resultados")
    pasta.mkdir(exist_ok=True) 
    arquivo = pasta / "benchmark.csv" 
    with open(arquivo, "w", newline="", encoding="utf-8") as csvfile:
        campos = [
            "algoritmo",
            "tamanho",
            "repeticao",
            "tempo_segundos"
        ] 
        escritor = csv.DictWriter(
            csvfile,
            fieldnames=campos
        )
        escritor.writeheader() #escreve a primeira linha do CSV.
        escritor.writerows(resultados) #escreve várias linhas.
    print(f"Benchmark concluído! Resultados salvos em: {arquivo}") 
