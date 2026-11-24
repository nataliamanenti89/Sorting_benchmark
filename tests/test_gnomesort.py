from sortingbenchmark.algorithms.gnomesort import gnome_sort


def main():
    arr = [
        "Igor Oliveira",
        "Cecília da Mota",
        "Dra. Antonella da Costa",
        "Evelyn Rodrigues",
        "Gustavo Lima",
        "Sr. João Pedro Cavalcante",
        "Caleb Aparecida",
        "Larissa Freitas"
    ]

    print(f"Lista antes de ser ordenada: {arr}")
    arr = gnome_sort(arr)
    print(f"Lista ordenada do gnome: {arr}")


main()
