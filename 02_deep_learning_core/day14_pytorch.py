#The Multi-Layer Perceptron Structural Mapper
import torch
import torch.nn as nn

class TextEmbeddingClassifier(nn.Module):
    def __init__(self):
        super().__init__()
        
        # TODO: Step 1 - Build a sequential network architecture pipeline using nn.Sequential().
        # Inside the block, stack three consecutive operations:
        # 1. An nn.Linear layer mapping 4 input dimensions to 8 hidden layer nodes.
        # 2. An nn.ReLU() activation step.
        # 3. An nn.Linear layer mapping those 8 hidden nodes down to 2 output target classes.
        self.pipeline = nn.Sequential(
            nn.Linear(4,8),
            nn.ReLU(),
            nn.Linear(8,2)
        )
        
    def forward(self, x):
        # TODO: Step 2 - Stream the input tensor 'x' through your structural self.pipeline property
        return self.pipeline(x) # Fix this return value

# --- INFERENCE VERIFICATION ENVIRONMENT ---
if __name__ == "__main__":
    print("🔥 Activating PyTorch Deep Learning Graph Module...")
    
    # Instantiate your custom deep learning network model structure
    model = TextEmbeddingClassifier()
    print(model)
    
    # Generate mock tensor inputs representing a batch of 5 records, each with 4 features
    # (Similar to 5 document token embeddings)
    mock_input_tensor = torch.randn(5, 4)
    print(f"\n📥 Ingested Input Tensor Shape: {mock_input_tensor.shape}")
    
    # Run a forward inference calculation pass
    # Calling model(inputs) automatically triggers the underlying forward() function code
    output_predictions = model(mock_input_tensor)
    print(f"📤 Resulting Output Tensor Shape: {output_predictions.shape}")
    
    # Structural network configuration assertions
    assert output_predictions.shape == (5, 2), "Output matrix shape mismatch! Check your Linear dimensions."
    print("\n🎉 Success! Your deep learning topology mapped and executed tensor transformations correctly.")