#: The Multi-Head Self-Attention Simulator
import torch
import torch.nn as nn

# Set seed for layer weight reproducibility
torch.manual_seed(42)

class SelfAttentionBlock(nn.Module):
    def __init__(self, embedding_dim, number_of_heads):
        super().__init__()
        
        # TODO: Step 1 - Initialize the PyTorch MultiheadAttention module.
        # Set embed_dim to embedding_dim, and num_heads to number_of_heads.
        # CRITICAL: Always remember to pass batch_first=True to match our standard batch shape layouts!
        self.multihead_attn = nn.MultiheadAttention(embed_dim=embedding_dim, num_heads=number_of_heads, batch_first=True)
        
    def forward(self, x):
        # TODO: Step 2 - Stream your input tensor 'x' through your self.multihead_attn block.
        # In a standard Self-Attention layout, the Query, Key, and Value inputs are all identical.
        # Hint: pass query=x, key=x, and value=x into the module call.
        # This layer returns a tuple: (attn_output, attn_output_weights). Return both of them!
        
        attn_output, attn_weights = self.multihead_attn(query=x, key=x, value=x)
        return attn_output, attn_weights

# --- ATTENTION MAP TEST RUNNER ---
if __name__ == "__main__":
    print("⚡ Activating PyTorch Transformer Self-Attention Core...")
    
    # Define structural layout sizes:
    # Word Embedding Dimension = 16, Parallel Attention Heads = 2
    model = SelfAttentionBlock(embedding_dim=16, number_of_heads=2)
    print(model)
    
    # Simulate an input batch of 3 prompt logs, each exactly 5 tokens long
    # Shape: [Batch Size=3, Sequence Length=5, Embedding Dim=16]
    mock_prompt_embeddings = torch.randn(3, 5, 16)
    print(f"\n📥 Ingested Prompt Tensor Shape: {mock_prompt_embeddings.shape}")
    
    # Execute global parallel attention mapping
    context_embeddings, attention_matrix = model(mock_prompt_embeddings)
    
    print("\n📈 Shape Analytics Extraction Completed:")
    print(f"   -> Contextualized Output Embedding Shape: {context_embeddings.shape}")
    print(f"   -> Extracted Attention Weight Map Shape:  {attention_matrix.shape}")

    # Architectural structure validation assertions
    assert context_embeddings.shape == (3, 5, 16), "Output feature projection space shape mismatch!"
    assert attention_matrix.shape == (3, 5, 5), "Attention weight distribution grid shape mismatch!"
    print("\n🎉 Success! Your attention engine calculated global token contexts completely in parallel.")