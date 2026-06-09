#The Fraudulent Transaction Classifier
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
import xgboost as xgb

# --- MOCK SECURITY TELEMETRY SIMULATION ---
np.random.seed(42)
# Feature 1: Request Frequency (per minute), Feature 2: Data Payload Volume (MB)
X_legit = np.random.normal(loc=[20, 5], scale=[5, 2], size=(800, 2))      # Normal user behavior
X_fraud = np.random.normal(loc=[180, 85], scale=[30, 15], size=(200, 2))  # Attack behavior

X = np.vstack([X_legit, X_fraud])
y = np.array([0] * 800 + [1] * 200) # 0 = Legit, 1 = Fraud

# Split into training (80%) and test (20%) evaluation blocks
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# --- YOUR GRADIENT BOOSTING ENGINE ---

def train_security_classifier(X_tr, X_te, y_tr):
    """
    Instantiates an XGBClassifier, fits it to the dataset, and generates predictions.
    """
    # TODO: Step 1 - Initialize the XGBClassifier model object.
    # Set n_estimators to 50, max_depth to 3, and learning_rate to 0.1.
    model = xgb.XGBClassifier(
        n_estimators=50,
        max_depth=3,
        learning_rate =0.1
    ) 
    
    # TODO: Step 2 - Train the model using your training features and target arrays.
    # Hint: Call model.fit()
    model.fit(X_tr, y_tr)
    # TODO: Step 3 - Predict the binary outcomes for the test feature matrix.
    # Hint: Call model.predict()
    preds = model.predict(X_test) # Fix this line
    
    return model, preds

# --- PIPELINE RUNNER & EVALUATION ---
if __name__ == "__main__":
    print("🛡️ Initializing Cyber-Security XGBoost Gateway...")
    
    # Execute the machine learning script
    trained_model, y_pred = train_security_classifier(X_train, X_test, y_train)
    
    # Calculate performance metrics
    acc = accuracy_score(y_test, y_pred)
    
    print("\n📊 Model Performance Summary:")
    print(f"   -> Global Model Accuracy: {acc * 100:.2f}%")
    
    print("\n📋 Detailed Structural Classification Report:")
    print(classification_report(y_test, y_pred, target_names=["LEGIT", "FRAUD"]))

    # Verification protection assertions
    assert acc > 0.95, "Classification performance is below production security thresholds!"
    print("🎉 Success! Your XGBoost engine has mapped the threat boundary perfectly.")