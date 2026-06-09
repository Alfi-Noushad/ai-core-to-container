#The Weight Convergence Optimizer
import torch
import torch.nn as nn
import torch.optim as optim

# Seed for reproducibility
torch.manual_seed(42)

# Create a mock training sample dataset: 100 inputs (X) and matching targets (y)
X_train = torch.randn(100, 1)
# The true relationship we want our network to discover is y = 3.5 * X
y_true = X_train * 3.5

# --- SYSTEM INITIALIZATION ---
# A single layer network with 1 input and 1 output node
model = nn.Linear(1, 1, bias=False) 

# Print the starting random weight value assigned by the computer
print(f"🎲 Starting Initial Model Weight Parameter: {model.weight.item():.4f}")

# --- YOUR GRADIENT OPTIMIZATION SETUP ---

# TODO: Step 1 - Define your Loss Criterion and Optimizer instances.
# Use nn.MSELoss() for the criterion.
# Use optim.SGD() for your optimizer, passing `model.parameters()` and a learning rate (lr) of 0.1.
criterion = nn.MSELoss()
optimizer = optim.SGD(model.parameters(),lr=0.1)

# --- THE INTERACTIVE TRAINING LOOP ---
print("\n🏋️ Training the neural network...")

for epoch in range(1, 41): # Train for 40 epochs
    # TODO: Step 2 - Forward Pass: pass X_train into your model instance to generate predictions
    predictions = model(X_train)
    
    # TODO: Step 3 - Loss Computation: pass your predictions and y_true into your criterion instance
    loss = criterion(predictions,y_true)
    
    # TODO: Step 4 - Reset parameters, calculate gradients, and update weights.
    # 1. Clear previous historical storage markers using optimizer.zero_grad()
    # 2. Trigger backpropagation by calling loss.backward()
    # 3. Step forward with your optimization adjustments using optimizer.step()
    # Add those 3 execution lines here...
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    if epoch % 10 == 0:
        print(f"   -> Epoch {epoch:02d} | Current Loss: {loss.item():.6f} | Current Weight: {model.weight.item():.4f}")

# --- FINAL QUALITY VALUATION ---
print(f"\n🎯 Final Learned Optimization Weight Parameter: {model.weight.item():.4f}")

# Integrity assertions to confirm the convergence loop executed correctly
assert loss.item() < 0.001, "The network did not converge! Verify your training loop step sequence."
assert abs(model.weight.item() - 3.5) < 0.05, "The weight coefficient failed to settle near the target 3.5 value."
print("\n🎉 Success! Your optimization loop successfully trained the network parameter via backpropagation.")