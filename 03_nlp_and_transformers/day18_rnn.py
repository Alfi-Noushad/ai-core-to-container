#The Sequence Sentiment Classifier
import torch
import torch.nn as nn

# Set seed for reproducible layer initialization
torch.manual_seed(42)

class LSTMSentimentClassifier(nn.Module):
    def __init__(self, vocab_size, embedding_dim, hidden_dim):
        super().__init__()
        
        # 1. Embedding Layer: Maps word integer IDs into continuous dense vectors
        self.embedding = nn.Embedding(num_embeddings=vocab_size, embedding_dim=embedding_dim)
        
        # TODO: Step 1 - Initialize the structural nn.LSTM core module.
        # Pass input_size equal to your embedding_dim, and hidden_size equal to hidden_dim.
        # CRITICAL: Always set batch_first=True so inputs are evaluated as (Batch, Sequence, Features).
        self.lstm = nn.LSTM(input_size=embedding_dim,hidden_size=hidden_dim,batch_first=True)
        
        # 2. Dense Linear Output Layer: Maps the final hidden memory state to a single prediction class score
        self.classifier = nn.Linear(hidden_dim, 1)
        
    def forward(self, text_tensor):
        # Pass raw integer indices through the embedding matrix
        # Shape output: [Batch Size, Sequence Length, Embedding Dimension]
        embedded_text = self.embedding(text_tensor)
        
        # TODO: Step 2 - Stream the embedded text matrix straight through your self.lstm layer.
        # Hint: The LSTM module returns two outputs: output, (hn, cn). We only need 'hn'.
        # Set up your unpacking variable assignments accordingly.
        output, (hn,cn) = self.lstm(embedded_text) 
        
        # TODO: Step 3 - Extract the final terminal hidden layer slice from 'hn'.
        # In a standard single-layer LSTM, the final hidden state vector is located at hn[-1].
        last_hidden_state = hn[-1]
        
        # Pass the memory summary slice through the linear classifier mapping
        output_logits = self.classifier(last_hidden_state)
        return output_logits

# --- SEQUENTIAL TEST ENVIRONMENT ---
if __name__ == "__main__":
    print("⏳ Initializing PyTorch Recurrent LSTM Core Pipeline...")
    
    # Establish structural hyper-dimensions
    # Vocabulary size = 20 unique words, Embedding size = 16, Hidden state memory size = 32
    model = LSTMSentimentClassifier(vocab_size=20, embedding_dim=16, hidden_dim=32)
    print(model)
    
    # Simulate an encoded batch of 4 text logs, each exactly 6 tokens long
    mock_text_batch = torch.randint(low=0, high=19, size=(4, 6))
    print(f"\n📥 Ingested Mock Text Batch Matrix Shape: {mock_text_batch.shape} (4 sentences, 6 words each)")
    
    # Execute forward sequence tracking inference
    final_logits = model(mock_text_batch)
    print(f"📤 Resulting Logit Output Matrix Shape: {final_logits.shape}")
    
    # Architectural verification assertions
    assert final_logits.shape == (4, 1), "Output prediction matrix dimensions mismatch! Check your hn slicing."
    print("\n🎉 Success! Your LSTM pipeline safely tracks text state context across sequential dimensions.")