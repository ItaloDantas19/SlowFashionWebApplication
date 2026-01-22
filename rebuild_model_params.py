import json

# Feature names (20 features, sem WPPP e PI)
feature_names = [
    'cor_vibrante', 'cor_sobria', 'cor_neutra', 'cor_terrosa',
    'forma_organica', 'forma_tradicional', 'forma_anatomica', 'forma_basica',
    'mat_decorativa', 'mat_fosca', 'mat_crua', 'mat_sintetica',
    'estampa_floral', 'ornamento_baixo', 'ornamento_alto',
    'costura_aparente', 'costura_discreta', 'costura_oculta',
    'acabamento_rustico', 'acabamento_polido'
]

# Coeficientes fornecidos pelo usuário (sem Equidade)
# Ordem: Exclusividade, Autenticidade, Funcionalismo, Localismo
coefficients_dict = {
    'cor_vibrante': [0.171, 0.129, 0.024, 0.098],
    'cor_sobria': [-0.285, -0.006, 0.155, 0.016],
    'cor_neutra': [0.189, -0.081, -0.2, -0.082],
    'cor_terrosa': [-0.033, 0.1, 0.065, 0.107],
    'forma_organica': [0.437, 0.099, -0.213, 0.023],
    'forma_tradicional': [-0.103, -0.020, -0.023, -0.022],
    'forma_anatomica': [-0.146, -0.08, 0.146, 0.002],
    'forma_basica': [-0.057, -0.163, -0.072, -0.149],
    'mat_decorativa': [0.286, 0.132, -0.092, 0.028],
    'mat_fosca': [-0.271, -0.044, 0.105, 0.004],
    'mat_crua': [-0.068, 0.12, 0.125, 0.093],
    'mat_sintetica': [0.341, -0.021, -0.391, -0.107],
    'estampa_floral': [0.535, 0.191, -0.253, 0.105],
    'ornamento_baixo': [-0.312, -0.041, 0.309, 0.062],
    'ornamento_alto': [0.408, 0.111, -0.287, 0.006],
    'costura_aparente': [-0.068, 0.12, 0.125, 0.093],
    'costura_discreta': [-0.114, 0.058, 0.108, 0.077],
    'costura_oculta': [0.185, -0.011, -0.298, -0.117],
    'acabamento_rustico': [-0.123, 0.088, 0.091, 0.065],
    'acabamento_polido': [0.25, -0.050, -0.164, -0.068]
}

# Transpor: de {feature: [coefs]} para [[coefs_target0], [coefs_target1], ...]
num_targets = 4
coefficients = []
for target_idx in range(num_targets):
    target_coefs = [coefficients_dict[feat][target_idx] for feat in feature_names]
    coefficients.append(target_coefs)

# Load existing params to get intercepts and quantiles
with open('/home/ubuntu/fashion-design-support/server/ml/model_params.json', 'r') as f:
    old_params = json.load(f)

# Build new params
new_params = {
    'coefficients': coefficients,
    'intercepts': old_params['intercepts'],  # Keep existing intercepts
    'scaler_mean': [0.5] * 20,  # Binary features
    'scaler_std': [0.5] * 20,
    'quantile_thresholds': old_params['quantile_thresholds']  # Keep existing quantiles
}

# Save
with open('/home/ubuntu/fashion-design-support/server/ml/model_params.json', 'w') as f:
    json.dump(new_params, f, indent=2)

print("✓ model_params.json rebuilt successfully!")
print(f"✓ Features: {len(feature_names)}")
print(f"✓ Targets: {num_targets}")
print(f"✓ Coefficients shape: {len(coefficients)} targets x {len(coefficients[0])} features")
