#!/usr/bin/env python3
"""
Replace hardcoded MODEL_COEFFICIENTS, MODEL_INTERCEPTS, QUANTILE_THRESHOLDS, SCALER_MEAN, SCALER_STD
in model_inference.ts with values from model_params.json
"""
import json

# Load model params
with open('server/ml/model_params.json', 'r') as f:
    params = json.load(f)

# Read the TypeScript file
with open('server/ml/model_inference.ts', 'r') as f:
    content = f.read()

# Format coefficients as TypeScript array
def format_array(arr):
    return '[' + ', '.join(f'{x:.6f}' for x in arr) + ']'

def format_2d_array(arr):
    lines = []
    target_names = ['Exclusividade', 'Autenticidade', 'Funcionalismo', 'Localismo']
    for i, row in enumerate(arr):
        comment = f'  // {target_names[i]}'
        formatted_row = format_array(row)
        lines.append(f'{comment}\n  {formatted_row}')
    return ',\n'.join(lines)

# Build replacement strings
coefficients_str = f"""// Model coefficients extracted from the trained ElasticNet model
// Shape: [4 targets x 20 features]
export const MODEL_COEFFICIENTS: number[][] = [
{format_2d_array(params['coefficients'])}
];"""

intercepts_str = f"""// Model intercepts for each target
export const MODEL_INTERCEPTS: number[] = {format_array(params['intercepts'])};"""

quantiles = params['quantile_thresholds']
quantiles_str = f"""// Quantile thresholds for discretization (33rd and 67th percentiles from training data)
export const QUANTILE_THRESHOLDS: Record<string, {{ low: number; high: number }}> = {{
  Exclusividade: {{ low: {quantiles['Exclusividade']['low']:.4f}, high: {quantiles['Exclusividade']['high']:.4f} }},
  Autenticidade: {{ low: {quantiles['Autenticidade']['low']:.4f}, high: {quantiles['Autenticidade']['high']:.4f} }},
  Funcionalismo: {{ low: {quantiles['Funcionalismo']['low']:.4f}, high: {quantiles['Funcionalismo']['high']:.4f} }},
  Localismo: {{ low: {quantiles['Localismo']['low']:.4f}, high: {quantiles['Localismo']['high']:.4f} }}
}};"""

scaler_mean_str = f"""// StandardScaler parameters from training data
export const SCALER_MEAN: number[] = {format_array(params['scaler_mean'])};"""

scaler_std_str = f"""export const SCALER_STD: number[] = {format_array(params['scaler_std'])};"""

# Replace in content
import re

# Replace MODEL_COEFFICIENTS
content = re.sub(
    r'// Model coefficients.*?\n// Shape:.*?\nexport const MODEL_COEFFICIENTS:.*?\n\[[\s\S]*?\n\];',
    coefficients_str,
    content,
    flags=re.MULTILINE
)

# Replace MODEL_INTERCEPTS
content = re.sub(
    r'// Model intercepts.*?\nexport const MODEL_INTERCEPTS:.*?;',
    intercepts_str,
    content,
    flags=re.MULTILINE
)

# Replace QUANTILE_THRESHOLDS
content = re.sub(
    r'// Quantile thresholds.*?\nexport const QUANTILE_THRESHOLDS:.*?\{[\s\S]*?\n\};',
    quantiles_str,
    content,
    flags=re.MULTILINE
)

# Replace SCALER_MEAN
content = re.sub(
    r'// StandardScaler parameters.*?\nexport const SCALER_MEAN:.*?;',
    scaler_mean_str,
    content,
    flags=re.MULTILINE
)

# Replace SCALER_STD
content = re.sub(
    r'export const SCALER_STD:.*?;',
    scaler_std_str,
    content,
    flags=re.MULTILINE
)

# Write back
with open('server/ml/model_inference.ts', 'w') as f:
    f.write(content)

print('✓ model_inference.ts updated with values from model_params.json')
print(f'✓ Coefficients shape: {len(params["coefficients"])} targets x {len(params["coefficients"][0])} features')
