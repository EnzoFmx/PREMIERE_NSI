# Correction IE :

## Exercice 1 :

| a    | b    | ET   |
| ---- | ---- | ---- |
| 1    | 1    | 1    |
| 1    | 0    | 0    |
| 0    | 1    | 0    |
| 0    | 0    | 0    |

| a    | b    | OU   |
| ---- | ---- | ---- |
| 1    | 1    | 1    |
| 1    | 0    | 1    |
| 0    | 1    | 1    |
| 0    | 0    | 0    |

| A    | NOT A |
| ---- | ----- |
| 1    | 0     |
| 0    | 1     |

| A    | B    | C    | A&B  | A&B \| C |
| ---- | ---- | ---- | ---- | -------- |
| 1    | 1    | 1    | 1    | 1        |
| 1    | 1    | 0    | 1    | 1        |
| 1    | 0    | 1    | 0    | 1        |
| 1    | 0    | 0    | 0    | 0        |
| 0    | 1    | 1    | 0    | 1        |
| 0    | 1    | 0    | 0    | 0        |
| 0    | 0    | 1    | 0    | 1        |
| 0    | 0    | 0    | 0    | 0        |

| A    | B    | C    | !C   | !B   | !C\|A | !B\|C | (!C\|A) & (!B\|C) |
| ---- | ---- | ---- | ---- | ---- | ----- | ----- | ----------------- |
| 1    | 1    | 1    | 0    | 0    | 1     | 1     | 1                 |
| 1    | 1    | 0    | 1    | 0    | 1     | 0     | 0                 |
| 1    | 0    | 1    | 0    | 1    | 1     | 1     | 1                 |
| 1    | 0    | 0    | 1    | 1    | 1     | 1     | 1                 |
| 0    | 1    | 1    | 0    | 0    | 0     | 1     | 0                 |
| 0    | 1    | 0    | 1    | 0    | 1     | 0     | 0                 |
| 0    | 0    | 1    | 0    | 1    | 0     | 1     | 0                 |
| 0    | 0    | 0    | 1    | 1    | 1     | 1     | 1                 |

## Exercice 2 :

```python
>>> t[0]
>>> t[len(t)-1] # Ou t[2] ici
```

Caractéristiques :

- Taille
- Mutabilité
- Indexation
- Type d'éléments

Bonus :

Tableau python : Taille dynamique et tous types d'éléments

## Exercice 3

```python
def moyenne(t):
	somme =0
    for i in t:
        somme = somme + i
    return somme / len(t)
```

