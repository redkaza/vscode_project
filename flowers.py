flowers = {
    "iris_setosa": {
        "sepal_length": [3.6, 4.9, 4.8, 4.7],
        "sepal_width": [2.9, 3.3, 3.2, 3.1],
        "petal_length": [1.3, 1.2, 1.5, 1.4],
    },
    "iris_virginica": {
        "sepal_length": [7.2, 7.0, 7.9],
         "sepal_width": [3.1, 2.7, 2.8],
        "petal_length": [5.5, 5.5, 6.5],
    },
    "iris_versicolor": {
        "sepal_length": [6.5, 6.0, 6.1, 6.2, 6.3],
         "sepal_width": [2.8, 2.9, 2.4, 2.7, 2.7],
        "petal_length": [4.8, 4.7, 5.0, 4.9, 4.8],
    },
}


sepal_lengths = [] 
sepal_widths = [] 
petal_lengths = [] 
for flower, data in flowers.items():
    for length in data['sepal_length']: 
        sepal_lengths.append(length)

    for width in data['sepal_width']: 
        sepal_widths.append(width)

    for length in data['petal_length']: 
        petal_lengths.append(length)


# общее среднее значение для sepal_length:
mean_sepal_length = sum(sepal_lengths) / len(sepal_lengths)
print(sepal_lengths)
print(mean_sepal_length)

# общее среднее значение для sepal_width:
mean_sepal_width = sum(sepal_widths) / len(sepal_widths)
print(sepal_widths)
print(mean_sepal_width)

# общее среднее значение для petal_length:
mean_petal_length = sum(petal_lengths) / len(petal_lengths)
print(petal_lengths)
print(mean_petal_length)