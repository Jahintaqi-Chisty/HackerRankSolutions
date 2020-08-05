# matrix = []
#
# for i in range(5):
#
#     # Append an empty sublist inside the list
#     matrix.append([])
#
#     for j in range(2):
#         matrix[i].append(j)
#
# print(matrix)
if __name__ == '__main__':
    matrix = []
    l = []
    for i in range(int(input())):
        name = input()
        score = float(input())
        matrix.append([name, score])


    second_lowest_matrix = sorted(matrix, key=lambda x: x[::-1])

    for name, score in matrix:
        if score == second_lowest_matrix[-1]:
            l.append([name, score])

    for name in l:
        print(name[0], end='\n')
