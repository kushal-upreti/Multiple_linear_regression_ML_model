def mean_calculate(data):
    sum = 0

    for i in range(len(data)):
        for j in range(len(data[0])):
            sum += data[i][j]

    mean = sum/(len(data))
    return mean

def sum_of_y_diff_mean_y(y_test):

    mean_y_test = mean_calculate(y_test)
    sum_y_diff_mean_y_squared = 0

    for i in range(len(y_test)):
        for j in range(len(y_test[0])):
            sum_y_diff_mean_y_squared += ((y_test[i][j] - mean_y_test) **2)

    return sum_y_diff_mean_y_squared


def matrix_transpose(colum_len, train_length, matrix_A):

    x_train_transpose = []
    for i in range(colum_len):
        row= []
        for j in range(train_length):
            row.append(matrix_A[j][i])
        x_train_transpose.append(row)

    return x_train_transpose

def data_preparation(student_df):

    length = len(student_df)
    train_length =int( 0.8 * length)
    colum_len = int(student_df.shape[1])

    x_train = []
    y_train = []
    x_test = []
    y_test = []

    for i in range(length):
        row = [
            1,
            student_df['hours_studied'][i],
            student_df['classes_attended'][i],
            student_df['past_score'][i]
        ]

        target_output = [student_df['exam_score'][i]]

        if i < train_length:
            x_train.append(row)
            y_train.append(target_output)
        else:
            x_test.append(row)
            y_test.append(target_output)

    x_train_transpose = matrix_transpose(colum_len, train_length, x_train)

    return x_train_transpose, x_train, y_train, x_test, y_test

def swap_pivot_row(square_matrix):
    for i in range(len(square_matrix)):
            first_pivot = square_matrix[0][0]
            if first_pivot != 0:
                break
            else:
                for j in range(len(square_matrix)):
                    if i != j:
                        if square_matrix[j][i] != 0:
                            for k in range(len(square_matrix)):
                                temp = square_matrix[j][k]
                                square_matrix[j][k] = square_matrix[i][k]
                                square_matrix[i][k] = temp
                            if square_matrix[0][0] != 0:
                                break
                            return square_matrix

def make_pivot_one(square_matrix, result, row_index, pivot_num):
    if pivot_num != 0:
        for i in range(len(square_matrix)):
            square_matrix[row_index][i] /= pivot_num
            result[row_index][i] /= pivot_num
    else:
        print("Matrix has pivot elemtn 0 so inverse doesn't exit")

def matrix_multiplication(matrix_A, matrix_B):
    result= []

    for i in range(len(matrix_A)):
        row =[]
        for j in range(len(matrix_B[0])):
            row.append(0)
        result.append(row)
    
    for i in range(len(matrix_A)):
        for j in range(len(matrix_B[0])):
            for k in range(len(matrix_B)):
                result[i][j] += (matrix_A[i][k] * matrix_B[k][j])

    return result

def matrix_inverse(square_matrix):
    result = []

    for i in range(len(square_matrix)):
        row = []
        for j in range(len(square_matrix[0])):
            row.append(0)
        result.append(row)
        result[i][i] += 1

    for i in range(len(square_matrix)):
        pivot_num = square_matrix[i][i]
        row_index = i
        make_pivot_one(square_matrix,result, row_index, pivot_num)
        for j in range(len(square_matrix)):
                if i != j:
                    factor = square_matrix[j][i]
                    for k in range(len(square_matrix)):
                        square_matrix[j][k] -= (factor*(square_matrix[i][k]))
                        result[j][k] -= (factor*(result[i][k]))    
    return result

