import json

# Load model params
with open('/home/ubuntu/fashion-design-support/server/ml/model_params.json', 'r') as f:
    params = json.load(f)

features = params['features']
scaler_mean = params['scaler_mean']
scaler_std = params['scaler_std']
coefficients = params['coefficients']
intercepts = params['intercepts']

# Test: ornamento_alto = 1, all others = 0
ornamento_alto_idx = features.index('ornamento_alto')

# Build feature vector
feature_vector = [0.0] * len(features)
feature_vector[ornamento_alto_idx] = 1.0

print("="*60)
print("DEBUGGING PREDICTION FOR ornamento_alto=1")
print("="*60)

# Normalize
normalized = []
for i, (f, mean, std) in enumerate(zip(feature_vector, scaler_mean, scaler_std)):
    norm = (f - mean) / std
    normalized.append(norm)
    if i == ornamento_alto_idx:
        print(f"\nornamento_alto normalization:")
        print(f"  Raw value: {f}")
        print(f"  Mean: {mean}, Std: {std}")
        print(f"  Normalized: ({f} - {mean}) / {std} = {norm}")

# Compute prediction for Exclusividade
target_idx = 0  # Exclusividade
intercept = intercepts[target_idx]
coefs = coefficients[target_idx]

print(f"\nExclusividade prediction:")
print(f"  Intercept: {intercept}")

contribution = sum(c * n for c, n in zip(coefs, normalized))
print(f"  Total contribution from features: {contribution}")
print(f"    (ornamento_alto contribution: {coefs[ornamento_alto_idx]} * {normalized[ornamento_alto_idx]} = {coefs[ornamento_alto_idx] * normalized[ornamento_alto_idx]})")

# Check contributions from WPPP and PI (they default to 0.5)
wppp_idx = features.index('WPPP')
pi_idx = features.index('PI')
print(f"\n  WPPP contribution: {coefs[wppp_idx]} * {normalized[wppp_idx]} = {coefs[wppp_idx] * normalized[wppp_idx]}")
print(f"  PI contribution: {coefs[pi_idx]} * {normalized[pi_idx]} = {coefs[pi_idx] * normalized[pi_idx]}")

prediction = intercept + contribution
print(f"\nFinal prediction: {intercept} + {contribution} = {prediction}")

# Compare with expected behavior
print(f"\n{'='*60}")
print("EXPECTED BEHAVIOR:")
print(f"  ornamento_alto coefficient: {coefs[ornamento_alto_idx]} (positive)")
print(f"  When ornamento_alto=1, Exclusividade should INCREASE")
print(f"  Baseline (all zeros): Let's calculate...")

# Baseline: all zeros
baseline_vector = [0.0] * len(features)
baseline_normalized = [(f - m) / s for f, m, s in zip(baseline_vector, scaler_mean, scaler_std)]
baseline_prediction = intercept + sum(c * n for c, n in zip(coefs, baseline_normalized))
print(f"  Baseline prediction (all 0): {baseline_prediction}")
print(f"  With ornamento_alto=1: {prediction}")
print(f"  Difference: {prediction - baseline_prediction}")
print(f"\n  Result: {'✓ CORRECT - ornamento_alto INCREASES Exclusividade' if prediction > baseline_prediction else '✗ INCORRECT - ornamento_alto DECREASES Exclusividade'}")
