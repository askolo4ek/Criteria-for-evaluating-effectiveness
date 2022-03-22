import numpy as np


def matrix_of_risks(matrix):
    maxlist = matrix.max(axis=0)

    R = maxlist - matrix
    return R


def criteria_of_vald(matrix, f=-1):
    matrix_f = matrix.copy()
    if f == -1:
        matrix_f = matrix.copy()
    else:
        matrix_f = matrix_f[:, :, f]

    minlist = []

    for i in range(len(list(matrix_f))):
        minlist.append(min(matrix_f[i]))

    maximin = max(minlist)
    return maximin


def criteria_of_sevij(matrix, f=-1):
    matrix_f = matrix.copy()
    if f == -1:
        matrix_f = matrix.copy()
    else:
        matrix_f = matrix_f[:, :, f]

    R = matrix_of_risks(matrix_f)
    maxlist = []

    for i in range(len(list(R))):
        maxlist.append(max(R[i]))

    minimax = min(maxlist)

    return minimax


def criteria_of_gurvits(matrix, alpha, f=-1):
    matrix_f = matrix.copy()

    if f == -1:
        matrix_f = matrix.copy()
    else:
        matrix_f = matrix_f[:, :, f]

    gurvits_list = []

    for i in range(len(list(matrix_f))):
        gurvits_list.append(round((alpha * min(matrix_f[i]) + (1 - alpha) * max(matrix_f[i])), 2))

    # print(gurvits_list)
    gurvits_koef = max(gurvits_list)
    return gurvits_koef


def criteria_of_laplas(matrix, f=-1):
    matrix_f = matrix.copy()
    if f == -1:
        matrix_f = matrix.copy()
    else:
        matrix_f = matrix_f[:, :, f]
    avg_win_list = []

    for i in range(len(list(matrix_f))):
        avg_win_list.append(round((sum(matrix_f[i]) / len(list(matrix_f[i]))), 2))

    # print(avg_win_list)
    max_avg_win = max(avg_win_list)
    return max_avg_win


def criteria_of_bayes(matrix, list_koefs, f=-1):
    matrix_f = matrix.copy()
    if f == -1:
        matrix_f = matrix.copy()
    else:
        matrix_f = matrix_f[:, :, f]

    bayes_win_list = []
    list_of_wins = []

    if sum(list_koefs) != 1:
        print("Error! The sum of the probabilities should be equal to 1!")
        return None

    else:
        for i in range(len(list(matrix_f))):
            bayes_win_list.append((matrix_f[i]) * list_koefs)

        for elem in bayes_win_list:
            list_of_wins.append(round((sum(elem)), 2))

        max_bayes_win = max(list_of_wins)

        return max_bayes_win


def vector_maximin(matrix):
    dots_of_pessimism = np.array([])

    dots = []

    for k in range(len(list(matrix[0][0]))):
        for i in range(len(list(matrix[::]))):
            dots.append(min(matrix[i, :, k]))

    for i in range(int(len(dots))):
        dots_of_pessimism = np.append(dots_of_pessimism, dots[i])

    dots_of_pessimism.shape = (8, 2)
    dots_of_pessimism = dots_of_pessimism.astype(int)

    max_dot = []

    dots_of_pessimism = np.hstack(dots_of_pessimism)

    dots_of_pessimism = np.hsplit(dots_of_pessimism, 2)

    dots_of_pessimism = np.vstack(dots_of_pessimism)

    dots = dots_of_pessimism.transpose()

    #print(dots)
    index = 0
    for i in range(len(list(dots_of_pessimism))):
        flag = index
        line_max = dots_of_pessimism[i][0]
        #print(line_max)
        for j in range(len(list(dots_of_pessimism[i]))):
            if line_max < dots_of_pessimism[i][j]:
                line_max = dots_of_pessimism[i][j]
                index = j
        if flag == index:
            continue
        max_dot.append(list(dots[index]))
        flag = index

    return max_dot


def vector_minimax(matrix):
    perfect_dots = matrix.max(axis=0)

    risks = perfect_dots - matrix
    #print(perfect_dots)
    dots = []

    for k in range(len(list(risks[0][0]))):
        for i in range(len(list(risks[::]))):
            dots.append(max(risks[i, :, k]))

    dots_of_pessimism = np.array(dots)

    dots_of_pessimism = dots_of_pessimism.reshape(2, 8).transpose()
    dots = dots_of_pessimism.copy()
    print(dots)





Q = np.array([8, 5, 4, 12, 2, 6, 3, 9, 1, 2, 3, 4, 5, 3, 4, 6, 2, 5, 3, 9, 9, 6, 4, 11, 4, 5, 6, 14, 6, 7, 8, 9])


#Q = np.array([8, 2, 5, 2, 4, 3, 12, 4, 2, 2, 6, 4, 3, 3, 9, 4, 1, 3, 2, 2, 3, 6, 4, 1, 5, 1, 3, 5, 4, 1, 6, 3,
              #2, 6, 5, 7, 3, 8, 9, 10, 9, 4, 6, 5, 4, 6, 11, 13, 4, 10, 5, 6, 6, 5, 14, 11, 6, 8, 7, 9, 8, 7, 9, 9])

p = np.array([0.1, 0.4, 0.4, 0.1])

Q.shape = (8, 4)
#Q.shape = (8, 4, 2)


#vector_minimax(Q)


print(matrix_of_risks(Q))
print(criteria_of_vald(Q))
print(criteria_of_sevij(Q))
print(criteria_of_gurvits(Q, 0.6))
print(criteria_of_laplas(Q))
#print(criteria_of_bayes(Q, p))
#print(vector_maximin(Q))
