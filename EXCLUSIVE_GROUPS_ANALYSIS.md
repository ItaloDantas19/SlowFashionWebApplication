# Análise de Grupos Mutuamente Exclusivos

## Grupos Identificados

### 1. Ornamento ✅ MUTUAMENTE EXCLUSIVO
- `ornamento_baixo`
- `ornamento_alto`

**Justificativa**: Um calçado não pode ter ornamentação baixa e alta simultaneamente. São níveis opostos de ornamentação.

**Comportamento**: Ao ativar um, desativar o outro automaticamente.

---

### 2. Forma ✅ MUTUAMENTE EXCLUSIVO
- `forma_organica`
- `forma_tradicional`
- `forma_anatomica`
- `forma_basica`

**Justificativa**: A forma/silhueta do calçado é uma característica única. Um calçado tem uma forma predominante, não pode ser simultaneamente orgânico e tradicional.

**Comportamento**: Ao ativar uma forma, desativar todas as outras.

---

### 3. Cor ⚠️ ANÁLISE NECESSÁRIA
- `cor_vibrante`
- `cor_sobria`
- `cor_neutra`
- `cor_terrosa`

**Justificativa**: Um calçado pode ter múltiplas cores, mas as características cromáticas tendem a ser mutuamente exclusivas (não pode ser vibrante e sóbrio ao mesmo tempo).

**Comportamento Proposto**: Mutuamente exclusivo - ao ativar uma característica cromática, desativar as outras.

---

### 4. Costura ✅ MUTUAMENTE EXCLUSIVO
- `costura_aparente`
- `costura_discreta`
- `costura_oculta`

**Justificativa**: A visibilidade da costura é uma característica única do acabamento. As costuras não podem ser simultaneamente aparentes e ocultas.

**Comportamento**: Ao ativar um tipo, desativar os outros.

---

### 5. Material ❌ NÃO EXCLUSIVO
- `mat_decorativa`
- `mat_fosca`
- `mat_crua`
- `mat_sintetica`

**Justificativa**: Um calçado pode combinar diferentes tipos de materiais (ex: couro fosco + detalhe sintético).

**Comportamento**: Permitir múltiplas seleções.

---

### 6. Acabamento ⚠️ ANÁLISE NECESSÁRIA
- `acabamento_rustico`
- `acabamento_polido`

**Justificativa**: O nível de refinamento tende a ser uma característica global, mas um calçado pode ter áreas rústicas e áreas polidas.

**Comportamento Proposto**: Permitir múltiplas seleções (um calçado pode ter acabamento misto).

---

## Decisão Final

### Grupos Mutuamente Exclusivos (implementar):
1. **Ornamento**: ornamento_baixo ↔ ornamento_alto
2. **Forma**: forma_organica ↔ forma_tradicional ↔ forma_anatomica ↔ forma_basica
3. **Cor**: cor_vibrante ↔ cor_sobria ↔ cor_neutra ↔ cor_terrosa
4. **Costura**: costura_aparente ↔ costura_discreta ↔ costura_oculta

### Grupos Não Exclusivos (permitir múltiplas seleções):
- Material (mat_decorativa, mat_fosca, mat_crua, mat_sintetica)
- Acabamento (acabamento_rustico, acabamento_polido)
- Superfície (estampa_floral - único atributo, não aplicável)
