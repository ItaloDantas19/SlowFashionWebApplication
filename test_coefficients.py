import json

# Load model params
with open('/home/ubuntu/fashion-design-support/server/ml/model_params.json', 'r') as f:
    params = json.load(f)

features = params['features']
targets = params['targets']
coefficients = params['coefficients']

# Test case: only ornamento_alto = 1, all others = 0
test_features = {
    'ornamento_alto': 1.0
}

# Find index of ornamento_alto
ornamento_alto_idx = features.index('ornamento_alto')
print(f"ornamento_alto index: {ornamento_alto_idx}")

# Check coefficient for Exclusividade (target index 0)
excl_coef = coefficients[0][ornamento_alto_idx]
print(f"\nCoefficient for ornamento_alto → Exclusividade: {excl_coef}")
print(f"Expected: 0.408")
print(f"Match: {abs(excl_coef - 0.408) < 0.001}")

# Manual prediction for Exclusividade with only ornamento_alto=1
# All features start at 0 except ornamento_alto
feature_vector = [0.0] * len(features)
feature_vector[ornamento_alto_idx] = 1.0

# Normalize (mean=0.5, std=0.5 for binary features)
normalized = [(f - 0.5) / 0.5 for f in feature_vector]

# Compute prediction
intercept = params['intercepts'][0]  # Exclusividade intercept
prediction = intercept + sum(c * n for c, n in zip(coefficients[0], normalized))

print(f"\nManual prediction for Exclusividade with ornamento_alto=1:")
print(f"Intercept: {intercept}")
print(f"Contribution from ornamento_alto: {coefficients[0][ornamento_alto_idx]} * {normalized[ornamento_alto_idx]} = {coefficients[0][ornamento_alto_idx] * normalized[ornamento_alto_idx]}")
print(f"Final prediction: {prediction}")
print(f"\nIf ornamento_alto has positive coefficient (0.408), prediction should be > intercept ({intercept})")
print(f"Actual result: {'CORRECT ✓' if prediction > intercept else 'INCORRECT ✗'}")
