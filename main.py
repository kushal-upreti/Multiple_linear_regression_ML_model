from model_class import MultipleLinearRegression
from calculation import data_preparation
import pandas as pd

student_df = pd.read_csv("/data/Files/Intern_Docs/multi_linreg_students.csv")       
x_train_transpose, x_train, y_train, x_test, y_test = data_preparation(student_df)

obj1 = MultipleLinearRegression()
obj1.fit(x_train_transpose, x_train, y_train)

x_input_num = student_df.shape[1]
x_input = [[0] * x_input_num]

print("------------------Multiple Regression ML Model--------------------------\n")

for i in range(len(x_input)):
    x_input[i][0] = 1
    for j in range(1, len(x_input[0])):
        x_input[i][j] = float(input(f"Enter the X{j} input: "))
          
obj1.predict(x_input)

print("The predicted output is: ", obj1.predicted_value)

obj1.mse_r2_score(x_test, y_test)

print(f"the mse of model is {obj1.mean_squared_error}\n the r2_score of model is {obj1.r2_score}")

