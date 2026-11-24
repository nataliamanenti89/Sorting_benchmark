import json
from faker import Faker
from pathlib import Path

SEED = 23
SIZES = [100_000, 250_000, 500_000]

DATA_DIR = Path("data/raw")
DATA_DIR.mkdir(parents = True, exist_ok = True)

def generate_names(size):
    fake = Faker("pt_BR")
    fake.seed_instance(SEED + size)
    names = [fake.name() for _ in range(size)]
    return names

def main():
    for size in SIZES:
        names = generate_names(size)
        output_file = DATA_DIR/f"names_{size}.json"
        with output_file.open("w", encoding = "utf-8") as file:
            json.dump(names, file, ensure_ascii = False, indent = 2)

if __name__ == "__main__":
    main()
