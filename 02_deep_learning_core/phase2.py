#Tabular Churn Prediction & Deep Embedding Representation
import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim
import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import roc_auc_score

# Set structural random seeds for matching evaluations
np.random.seed(42)
torch.manual_seed(42)

# --- 1. DATA GENERATION & SEPARATION ENGINE ---
# Features: [Total Tokens Consumed (K), Active Support Tickets Open]
X_clean = np.random.normal(loc=[50, 1], scale=[10, 0.5], size=(400, 2))  # Happy Users (Loyal)
X_churn = np.random.normal(loc=[10, 6], scale=[5, 1.5], size=(100, 2))   # Frustrated Users (Churning)

X_raw = np.vstack([X_clean, X_churn])
y_raw = np.array([0] * 400 + [1] * 100) # 0 = Retained, 1 = Churned (Target)

# Train-test splitting
X_train, X_test, y_train, y_test = train_test_split(X_raw, y_raw, test_size=0.2, random_state=42, stratify=y_raw)

# Scale continuous input space structures
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Convert arrays into matching PyTorch tensors for Layer B execution
X_train_tensor = torch.tensor(X_train_scaled, dtype=torch.float32)
X_test_tensor = torch.tensor(X_test_scaled, dtype=torch.float32)
y_train_tensor = torch.tensor(y_train, dtype=torch.float32).unsqueeze(1)

# ============================================
# 🔥 MODEL LANE A: CLASSICAL XGBOOST TREE
# ============================================
print("🌲 Training Lane A: XGBoost Engine...")
# TODO: Step 1 - Initialize an XGBClassifier (n_estimators=10, max_depth=3, random_state=42)
# Fit it to X_train_scaled and y_train, then extract positive class probabilities for the test set.
xgb_model = xgb.XGBClassifier(n_estimators=10, max_depth=3, random_state=42)
xgb_model.fit(X_train_scaled, y_train)
xgb_probs = xgb_model.predict_proba(X_test_scaled)[:, 1]

# ============================================
# 🔥 MODEL LANE B: DEEP PYTORCH NEURAL NETWORK
# ============================================
print("\n🧠 Training Lane B: Deep PyTorch Network...")

class ChurnDeepClassifier(nn.Module):
    def __init__(self):
        super().__init__()
        self.network = nn.Sequential(
            nn.Linear(2, 8),
            nn.ReLU(),
            nn.Linear(8, 1),
            nn.Sigmoid() # Squashes output layer values between 0.0 and 1.0 probability
        )
    def forward(self, x):
        return self.network(x)

pytorch_model = ChurnDeepClassifier()
# TODO: Step 2 - Initialize the BCELoss (Binary Cross Entropy) criterion 
# and an Adam optimizer tracking pytorch_model.parameters() with lr=0.05
criterion = nn.BCELoss()
optimizer = optim.SGD(pytorch_model.parameters(),lr=0.05)

# PyTorch Interactive Epoch Training Loop
for epoch in range(1, 101):
    # Forward Pass
    preds = pytorch_model(X_train_tensor)
    loss = criterion(preds, y_train_tensor)
    
    # TODO: Step 3 - Execute backpropagation mechanics:
    # 1. Zero out old gradients via optimizer
    # 2. Extract backward derivatives via loss
    # 3. Advance weights forward via optimizer step
    # Add your 3 lines of code here...
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
# Extract PyTorch continuous prediction probabilities without tracking gradients
with torch.no_grad():
    pytorch_probs = pytorch_model(X_test_tensor).numpy().flatten()

# ============================================
# 📈 SYSTEM EVALUATION AND THRESHOLD GATE
# ============================================
print("\n📊 Evaluating Cross-Network Analytics Profile Matrix...")

xgb_auc = roc_auc_score(y_test, xgb_probs)
torch_auc = roc_auc_score(y_test, pytorch_probs)
print(f"   -> Lane A (XGBoost) Area Under Curve Score: {xgb_auc:.4f}")
print(f"   -> Lane B (PyTorch) Area Under Curve Score: {torch_auc:.4f}")

# TODO: Step 4 - Implement a risk-averse threshold gate mapping of 0.25
# Convert pytorch_probs into integers (1 if prob >= 0.25 else 0)
risk_threshold = 0.25
final_risk_flags = (pytorch_probs >= 0.25).astype(int)

print(f"\n🛡️ High-Risk Flag Operations Triggered: {int(final_risk_flags.sum())} accounts identified as churn threats.")

# Validation protections
assert xgb_auc > 0.90 and torch_auc > 0.90, "Model optimizations fell below target accuracy benchmarks!"
assert final_risk_flags.dtype in [np.int32, np.int64, int] or final_risk_flags.max() <= 1, "Flags must be discrete binary values."
print("\n🎉 Graduation Complete! You have successfully orchestrated a dual-lane machine learning suite.")