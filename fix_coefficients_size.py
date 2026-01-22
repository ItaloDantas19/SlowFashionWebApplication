import json

# Load current model_params.json
with open('/home/ubuntu/fashion-design-support/server/ml/model_params.json', 'r') as f:
    params = json.load(f)

# Remove last 2 columns from coefficients (WPPP and PI)
print("Original coefficients shape:")
for i, coefs in enumerate(params['coefficients']):
    print(f"  Target {i}: {len(coefs)} coefficients")

# Remove last 2 elements from each target's coefficients
params['coefficients'] = [coefs[:-2] for coefs in params['coefficients']]

print("\nUpdated coefficients shape:")
for i, coefs in enumerate(params['coefficients']):
    print(f"  Target {i}: {len(coefs)} coefficients")

# Save updated params
with open('/home/ubuntu/fashion-design-support/server/ml/model_params.json', 'w') as f:
    json.dump(params, f, indent=2)

print("\n✓ Coefficients updated successfully!")
print(f"✓ Each target now has {len(params['coefficients'][0])} coefficients (matching 20 features)")
