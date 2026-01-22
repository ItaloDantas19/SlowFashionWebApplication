#!/usr/bin/env python3
import json
import re

# Load model_params.json
with open('server/ml/model_params.json', 'r') as f:
    params = json.load(f)

# Read the TypeScript file
with open('server/ml/model_inference.ts', 'r') as f:
    content = f.read()

# Format coefficients for TypeScript
def format_coef_array(arr):
    return '[' + ', '.join(f'{x:.6f}' for x in arr) + ']'

coef_lines = []
for i, coef in enumerate(params['coefficients']):
    target_name = ['Exclusividade', 'Autenticidade', 'Funcionalismo', 'Localismo'][i]
    coef_lines.append(f'  // {target_name}')
    coef_lines.append(f'  {format_coef_array(coef)},')

new_coefficients = 'export const MODEL_COEFFICIENTS: number[][] = [\n' + '\n'.join(coef_lines[:-1]) + coef_lines[-1][:-1] + '\n];'

# Replace MODEL_COEFFICIENTS
pattern = r'export const MODEL_COEFFICIENTS: number\[\]\[\] = \[[\s\S]*?\];'
content = re.sub(pattern, new_coefficients, content)

# Write back
with open('server/ml/model_inference.ts', 'w') as f:
    f.write(content)

print(f'✓ MODEL_COEFFICIENTS updated to {len(params["coefficients"])} x {len(params["coefficients"][0])}')
