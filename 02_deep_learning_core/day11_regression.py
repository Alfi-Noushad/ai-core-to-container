#The Cloud Infrastructure Cost Predictor
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# --- MOCK DATA SIMULATION ---
# Let's generate synthetic production logs for 1,000 virtual servers
np.random.seed(42)
X_raw = np.random.rand(1000, 2) * [100, 64] # Feature 1: CPU % (0-100), Feature 2: RAM GB (0-64)

# True underlying formula with some added random noise
y = (X_raw[:, 0] * 2.5) + (X_raw[:, 1] * 4.0) + 12.0 + np.random.randn(1000) * 5

# Split dataset: 80% for training data, 20% for validation testing
X_train, X_test, y_train, y_test = train_test_split(X_raw, y, test_size=0.2, random_state=42)

# --- YOUR ML PIPELINE ENGINE ---

def train_predictive_engine(X_tr, X_te, y_tr):
    """
    Scales features, initializes the model, and fits it on the training data.
    """
    # TODO: Step 1 - Initialize the StandardScaler and scale the training and testing matrices.
    # Hint: Use scaler.fit_transform(X_tr) for training data, 
    # and use scaler.transform(X_te) for testing data (never fit on test data!).
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_tr)
    X_test_scaled = scaler.transform(X_te)

    # TODO: Step 2 - Initialize a standard LinearRegression model instance and train it.
    # Hint: Call model.fit(X_train_scaled, y_tr)
    model = LinearRegression()
    # Fit the model here...
    model.fit(X_train_scaled, y_tr)
    # TODO: Step 3 - Generate predictions on the scaled testing features.
    # Hint: Call model.predict(X_test_scaled)
    preds = model.predict(X_test_scaled)
    
    return model, preds, X_test_scaled

# --- EXECUTION & EVALUATION ---
if __name__ == "__main__":
    print("🤖 Booting Scikit-Learn Regression Engine...")
    
    # Run the processing pipeline
    trained_model, y_pred, X_test_scaled = train_predictive_engine(X_train, X_test, y_train)
    
    # Calculate performance metrics
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    
    print("\n📈 Model Training Metrics Evaluation:")
    print(f"   -> Mean Squared Error (MSE): {mse:.4f}")
    print(f"   -> R-squared Score (Variance Explained): {r2:.4f}")
    
    print("\n🧠 Extracting Model Parameters:")
    print(f"   -> Learned Feature Weights (Slopes): {trained_model.coef_}")
    print(f"   -> Learned Bias (Intercept): {trained_model.intercept_:.4f}")

    # Safety assertions to guarantee your pipeline scaled and predicted correctly
    assert mse < 30.0, "MSE is too high! Verify your training steps."
    assert r2 > 0.90, "Model accuracy is lacking. Ensure you are using the scaled features."
    print("\n🎉 Success! Your predictive engine has accurately calculated server cost trends.")