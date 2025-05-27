import joblib
from sklearn.ensemble import RandomForestClassifier
import numpy as np

# Example data (replace with your actual data)
# For now, I'm using random data for the sake of demonstration
X_train = np.random.rand(100, 3)  # 100 samples, 3 features
y_train = np.random.choice([0, 1], size=100)  # 100 labels (binary classification)

# Initialize and train the model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Save the trained model to a file
joblib.dump(model, 'model.pkl')

print("Model trained and saved as model.pkl")
