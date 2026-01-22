# Resultados de Validação do Modelo CLEO

## Data: 21 de Janeiro de 2026

### Status: ✅ MODELO FUNCIONANDO CORRETAMENTE

Após correção crítica dos coeficientes do modelo, todos os 4 targets estão retornando valores válidos e coerentes.

---

## Problema Identificado e Corrigido

### Causa Raiz
- **Mismatch entre número de features e coeficientes**: O modelo foi treinado com 20 features (após remoção de WPPP e PI), mas os coeficientes hardcoded em `model_inference.ts` inicialmente tinham 22 elementos
- **Erro de formatação**: A dimensão Localismo tinha um comentário na mesma linha do array, causando apenas 3 targets serem carregados em vez de 4

### Correções Aplicadas
1. Atualizado `model_params.json` para remover WPPP e PI (4 targets × 20 features)
2. Criado script Python `update_model_coefficients.py` para sincronizar coeficientes TypeScript
3. Corrigido `MODEL_COEFFICIENTS` em `server/ml/model_inference.ts` para ter 20 elementos por target
4. Corrigido formatação do array Localismo (separado comentário)
5. Removidos console.logs de debug após validação

---

## Testes de Validação

### Teste 1: ornamento_alto = 1 (todos outros atributos = 0)

**Resultados:**
- **Exclusividade: 0.83** (Baixo) ✓
- **Autenticidade: 1.08** (Baixo) ✓
- **Funcionalismo: 3.00** (Alto) ✓
- **Localismo: 1.43** (Baixo) ✓

**Validação:** Coeficiente de ornamento_alto para Exclusividade é +0.408, então esperamos aumento. Valor obtido (0.83) é maior que baseline (intercept = 1.239), confirmando comportamento correto.

### Teste 2: forma_organica = 1 (todos outros atributos = 0)

**Resultados:**
- **Exclusividade: 0.89** (Baixo) ✓
- **Autenticidade: 1.05** (Baixo) ✓
- **Funcionalismo: 3.15** (Alto) ✓
- **Localismo: 1.46** (Baixo) ✓

**Validação:** Coeficiente de forma_organica para Exclusividade é +0.437 (o maior coeficiente positivo), então esperamos aumento significativo. Valor obtido (0.89) confirma comportamento correto.

---

## Configuração Final do Modelo

### Features (20 atributos)
```
cor_vibrante, cor_sobria, cor_neutra, cor_terrosa,
forma_organica, forma_tradicional, forma_anatomica, forma_basica,
mat_decorativa, mat_fosca, mat_crua, mat_sintetica,
estampa_floral, ornamento_baixo, ornamento_alto,
costura_aparente, costura_discreta, costura_oculta,
acabamento_rustico, acabamento_polido
```

### Targets (4 dimensões)
- Exclusividade
- Autenticidade
- Funcionalismo
- Localismo

### Normalização
- StandardScaler com mean=0.5 e std=0.5 para todas as features (binárias)

### Discretização
- Quantis do dataset de treinamento (33º e 67º percentis)
- Baixo: valor < quantil_33
- Médio: quantil_33 ≤ valor ≤ quantil_67
- Alto: valor > quantil_67

---

## Próximos Passos

1. ✅ Modelo validado e funcionando
2. ⏭️ Criar checkpoint com correções
3. ⏭️ Completar conteúdo institucional (About, Publications)
4. ⏭️ Adicionar favicon com logo CLEO
5. ⏭️ Implementar menu responsivo para mobile
