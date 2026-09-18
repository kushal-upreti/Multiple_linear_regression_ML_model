# Multiple Linear Regression (From Scratch)

A simple implementation of multiple linear regression using the Normal Equation method, built with plain Python (no NumPy/scikit-learn) — matrix operations are implemented manually.

## Files

- **`main.py`** – Entry point. Loads the dataset, trains the model, takes user input for prediction, and prints results.
- **`model_class.py`** – Contains the `MultipleLinearRegression` class (`fit`, `predict`, `mse_r2_score`).
- **`calculation.py`** – Helper functions for matrix operations (transpose, multiplication, inverse) and data preparation.

## How It Works

1. **Data Preparation**: Reads a CSV of student data (`hours_studied`, `classes_attended`, `past_score`, `exam_score`) and splits it into 80% training / 20% testing sets.
2. **Model Fitting**: Solves for regression coefficients (`beta`) using the Normal Equation:

   ```
   beta = (XᵀX)⁻¹ XᵀY
   ```

3. **Prediction**: Takes user-entered feature values and predicts the exam score.
4. **Evaluation**: Computes Mean Squared Error (MSE) and R² score on the test set.

## Requirements

- Python 3
- pandas

```bash
pip install pandas
```

## Usage

1. Update the CSV path in `main.py`:
   ```python
   student_df = pd.read_csv("path/to/your/dataset.csv")
   ```
2. Run the script:
   ```bash
   python main.py
   ```
3. Enter the requested feature values when prompted (e.g., hours studied, classes attended, past score).
4. View the predicted exam score, MSE, and R² score.

## Dataset Format

The CSV should contain at least these columns:

| hours_studied | classes_attended | past_score | exam_score |
|---|---|---|---|

## Notes

- All matrix math (transpose, multiplication, inverse) is implemented manually in `calculation.py` for educational purposes.
- The model assumes the feature matrix `XᵀX` is invertible (non-singular).