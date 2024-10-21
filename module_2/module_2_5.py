def get_matrix (n, m, value):
    matrix = []
    for i in range(n):
        matrix.append([]) # добавляем список в список
        for j in range(m):
            matrix[i].append(value) #добавляем в список m раз значение value
    print(matrix)
get_matrix(7, 3, 10)