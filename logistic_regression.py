rom sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression as lr_sklearn
from concrete.ml.sklearn import LogisticRegression as lr_concrete

# Lets create a synthetic data-set
x, y = make_classification(n_samples=100, class_sep=2, n_features=30, random_state=42)

# Split the data-set into a train and test set
X_train, X_test, y_train, y_test = train_test_split(
            x, y, test_size=0.2, random_state=42
            )

# Now we train in the clear and quantize the weights
concrete_model = lr_concrete()
concrete_model.fit(X_train, y_train)

# We can simulate the predictions in the clear
y_pred_clear = concrete_model.predict(X_test)

# We then compile on a representative set
concrete_model.compile(X_train)

# Finally we run the inference on encrypted inputs
y_pred_fhe = concrete_model.predict(X_test, execute_in_fhe=True)

print("concrete-ml")
print("In clear  :", y_pred_clear)
print("In FHE    :", y_pred_fhe)
print(f"Similarity: {int((y_pred_fhe == y_pred_clear).mean()*100)}%")

# Output:
# In clear  : [0 0 0 0 1 0 1 0 1 1 0 0 1 0 0 1 1 1 0 0]
# In FHE    : [0 0 0 0 1 0 1 0 1 1 0 0 1 0 0 1 1 1 0 0]
# Similarity: 100%
#X_train, X_test, y_train, y_test = train_test_split(
#            x, y, test_size=0.2, random_state=42
#            )
scikit_model = lr_sklearn()
scikit_model.fit(X_train, y_train)
sk_y_pred_clear = scikit_model.predict(X_test)
sk_y_pred_fhe = scikit_model.predict(X_test)
print("\nscikit-learn")
print("In clear  :", sk_y_pred_clear)
print("In FHE    :", sk_y_pred_fhe)
print(f"Similarity: {int((y_pred_fhe == y_pred_clear).mean()*100)}%")
