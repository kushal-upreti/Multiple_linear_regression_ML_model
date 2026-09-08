from calculation import matrix_multiplication, matrix_inverse, sum_of_y_diff_mean_y

class MultipleLinearRegression:

    def __init__(self):
        self.beta = None
        self.matrix_mult_XTY = None
        self.matrix_mult_XTX = None
        self.inverse_matrix = None
        self.predicted_value = None
        self.mean_squared_error = None
        self.r2_score = None

    def fit(self, x_train_transpose, x_train, y_train):
        self.matrix_mult_XTY = matrix_multiplication(x_train_transpose, y_train)
        self.matrix_mult_XTX = matrix_multiplication(x_train_transpose, x_train)
        self.inverse_matrix = matrix_inverse(self.matrix_mult_XTX)
        self.beta = matrix_multiplication(self.inverse_matrix, self.matrix_mult_XTY)
        return self

    def predict(self, x_input):

        self.predicted_value  = matrix_multiplication(x_input, self.beta)

        return self

    def mse_r2_score(self, x_test, y_test):

        sum_squared_error = 0
        y_predict = matrix_multiplication(x_test, self.beta)

        for i in range(len(y_test)):
            for j in range(len(y_test[0])):
                sum_squared_error += ((y_test[i][j] - y_predict[i][j]) **2)

        self.mean_squared_error = sum_squared_error/(len(y_test))

        sum_y_diff_mean_y_squared = sum_of_y_diff_mean_y(y_test)

        self.r2_score = 1 - (sum_squared_error/sum_y_diff_mean_y_squared)

        return self


