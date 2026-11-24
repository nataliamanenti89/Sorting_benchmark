from sortingbenchmark.algorithms.gnomesort import gnome_sort
from sortingbenchmark.algorithms.tournamentsort import tournament_sort
from sortingbenchmark.algorithms.pancakesort import pancake_sort
import json
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parents[2] / "data" / "raw"

with open(DATA_DIR / "names_100000.json", "r", encoding="utf-8") as file:
    lista = json.load(file)
    
resultado_gnome = gnome_sort(lista.copy()) 

resultado_tournament = tournament_sort(lista.copy())
resultado_pancake = pancake_sort(lista.copy())

print("Original:", lista)  
print("Gnome Sort:", resultado_gnome) 
print("Tournament Sort:", resultado_tournament)
