#The Risk-Adjusted Threat Gate
import numpy as np
from sklearn.metrics import confusion_matrix, roc_auc_score

# --- MOCK SIMULATION DATA ---
# Ground truth labels: 0 = Safe Traffic, 1 = Active Attack
y_true = np.array([0, 0, 0, 0, 0, 1, 1, 1, 1, 1])

# Mock raw model probabilities (representing how confident the model is)
model_probabilities = np.array([0.05, 0.12, 0.45, 0.22, 0.18, 0.35, 0.78, 0.92, 0.88, 0.61])

# --- THRESHOLD EVALUATION ENGINE ---

def evaluate_custom_gate(true_labels, probs, threshold):
    """
    Converts continuous raw probabilities into binary flags based on a custom threshold,
    and returns the confusion matrix metrics.
    """
    # TODO: Step 1 - Convert probabilities into binary 0 or 1 integers using the threshold.
    # Hint: (probs >= threshold).astype(int)
    preds = (probs >= threshold).astype(int) # Fix this line
    
    # Generate a confusion matrix: [[TrueNeg, FalsePos], [FalseNeg, TruePos]]
    tn, fp, fn, tp = confusion_matrix(true_labels, preds).ravel()
    
    return tn, fp, fn, tp

# --- EXECUTION RUNNER ---
if __name__ == "__main__":
    print("📈 Extracting Global Model Performance...")
    
    # TODO: Step 2 - Compute the continuous ROC-AUC score using roc_auc_score()
    # Hint: Pass true_labels and model_probabilities
    auc_score = roc_auc_score(y_true, model_probabilities) # Fix this line
    print(f"   -> Model Area Under Curve (AUC): {auc_score:.4f}")
    
    print("\n🎛️ Running Run 1: Default Production Threshold (0.50)")
    tn1, fp1, fn1, tp1 = evaluate_custom_gate(y_true, model_probabilities, 0.50)
    print(f"   [!] Missed Attacks (False Negatives): {fn1}")
    print(f"   [!] Innocent Blocks (False Positives): {fp1}")
    
    print("\n🛡️ Running Run 2: High-Security Risk-Averse Threshold (0.30)")
    # TODO: Step 3 - Call evaluate_custom_gate using a strict threshold of 0.30
    tn2, fp2, fn2, tp2 = evaluate_custom_gate(y_true, model_probabilities, 0.30) # Fix this line
    print(f"   [!] Missed Attacks (False Negatives): {fn2}")
    print(f"   [!] Innocent Blocks (False Positives): {fp2}")

    # Integrity assertions to confirm correct threshold assignment logic
    assert fn1 == 1, "At 0.50 threshold, the system should have missed exactly 1 attack (index position 5)."
    assert fn2 == 0, "At 0.30 threshold, your security gate should have caught 100% of the active attacks!"
    print("\n🎉 Threshold configurations verified! You successfully zeroed out missed attacks.")