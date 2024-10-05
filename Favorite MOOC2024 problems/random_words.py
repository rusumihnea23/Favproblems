from random import sample
def words(n: int, beginning: str) -> list:
    cuvinte = []
    with open('words.txt') as fisier:
        for line in fisier:
            cuv = line.replace('\n', '')
            if cuv.startswith(beginning):
                cuvinte.append(cuv)
    if len(cuvinte) < n:
        raise ValueError(f'Could not find {n} words that start with {beginning}. Only found {len(cuvinte)} words.')
    
    return sample(cuvinte, n)

# if __name__ == "__main__":
#     lista_cuv = words(3, "ty")
#     for cuv in lista_cuv:
#         print(cuv)