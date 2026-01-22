# Fashion Design Symbolic Reading Tool - TODO

## Backend FastAPI
- [x] Configurar servidor FastAPI separado para inferência do modelo
- [x] Carregar modelo ElasticNet (elasticnet_multitarget.joblib)
- [x] Implementar endpoint de inferência com 22 features de entrada
- [x] Implementar normalização usando StandardScaler com parâmetros do treinamento
- [x] Implementar discretização de outputs usando quantis do dataset de treinamento
- [x] Retornar predições contínuas para 4 dimensões simbólicas
- [x] Retornar coeficientes do modelo para explicabilidade

## Frontend - Tela 1 (Introdução)
- [x] Explicação do propósito interpretativo da ferramenta
- [x] Enfatizar papel exploratório e não prescritivo
- [x] Design educacional e acolhedor

## Frontend - Tela 2 (Configuração de Design)
- [x] Interface com sliders para atributos numéricos
- [x] Seletores para atributos categóricos
- [x] Organização lógica dos 22 atributos visuais
- [x] Botão de atualização em tempo real

## Frontend - Tela 3 (Leituras Simbólicas)
- [x] Visualização em barras para cada dimensão
- [x] Exibir score contínuo (ex: 0.63)
- [x] Exibir nível simbólico discreto (baixo/médio/alto)
- [x] Indicador visual de intensidade

## Frontend - Tela 4 (Insights de Design)
- [x] Visualização da contribuição relativa de cada atributo
- [x] Explicabilidade baseada em coeficientes do modelo
- [x] Opção de simular pequenas mudanças nos atributos
- [x] Apresentar significado cumulativo sem ranqueamento

## Integração e UX
- [x] Integração completa entre React e FastAPI
- [x] Tom interpretativo e não autoritário
- [x] Interface educacional para designers sem background técnico
- [x] Suporte a iteração e experimentação


## Novas Páginas Institucionais
- [x] Página Equipe com 2 membros (foto, nome, cargo, bio genérica)
- [x] Página Sobre com descrição do projeto
- [x] Página Publicações com lista de publicações acadêmicas
- [x] Atualizar navegação com links para as novas páginas


## Atualização de Conteúdo
- [x] Renomear ferramenta para CLEO — Slow Fashion
- [x] Adicionar nome completo institucional: CLEO — Códigos de Linguagem Estética Objetual para o Slow Fashion
- [x] Atualizar descrição da dimensão Autenticidade com definição correta
- [x] Atualizar descrição da dimensão Funcionalismo com definição correta
- [x] Atualizar descrição da dimensão Localismo com definição correta


## Identidade Visual e Branding
- [x] Adicionar logo CLEO no header substituindo ícone de bússola
- [x] Adicionar logo Universidade Feevale no footer
- [x] Criar footer com informações de autoria (Ítalo e Prof. Marcelo com links Lattes)
- [x] Adicionar informações de financiamento CAPES/PROSUC no footer
- [x] Alterar paleta de cores para tons de verde claro/pastel


## Correção do Modelo
- [x] Verificar coeficientes extraídos do modelo joblib
- [x] Comparar com coeficientes corretos fornecidos pelo usuário
- [x] Corrigir implementação se houver divergência
- [x] Validar predições com exemplo conhecido


## Atualização Página Equipe
- [x] Atualizar nome do Pesquisador 1 para "Ítalo José de Medeiros Dantas"
- [x] Atualizar cargo para "Doutorando - Bolsista PROSUC/CAPES"
- [x] Atualizar instituição para "Universidade Feevale"
- [x] Manter nome do Pesquisador 2 como "Marcelo Curth"
- [x] Atualizar cargo do Pesquisador 2 para "Professor orientador"


## Adicionar Fotos dos Pesquisadores
- [x] Copiar foto de Ítalo Dantas para o diretório public
- [x] Copiar foto de Marcelo Curth para o diretório public
- [x] Atualizar referências de imagem em Team.tsx


## Remover WPPP e PI
- [x] Remover WPPP e PI da interface de configuração (DesignConfiguration.tsx)
- [x] Remover WPPP e PI do contexto de design (DesignContext.tsx)
- [x] Atualizar modelo de inferência para não usar WPPP e PI
- [x] Testar se valores ficam mais realistas sem WPPP e PI


## Correção de Bug Crítico - Inferência NaN
- [x] Identificar causa raiz: mismatch entre 20 features e 22 coeficientes hardcoded
- [x] Atualizar model_params.json para remover WPPP e PI (4 targets x 20 features)
- [x] Criar script Python para sincronizar coeficientes TypeScript com model_params.json
- [x] Corrigir MODEL_COEFFICIENTS em model_inference.ts para ter 20 elementos por target
- [x] Corrigir erro de formatação na dimensão Localismo (comentário na mesma linha do array)
- [x] Reiniciar servidor e validar que todos os 4 targets retornam valores válidos


## Grupos Mutuamente Exclusivos
- [x] Analisar quais grupos de atributos devem ser mutuamente exclusivos
- [x] Implementar lógica no DesignContext para desativar atributos conflitantes
- [x] Atualizar interface DesignConfiguration.tsx para refletir comportamento exclusivo
- [x] Testar comportamento: ornamento (baixo/alto), forma (4 tipos), cor (4 tipos), costura (3 tipos)


## Bug: Botão Ajustar Atributos
- [ ] Investigar por que o botão "Ajustar Atributos" na página Leituras Simbólicas não volta para Configuração
- [ ] Corrigir navegação do botão
- [ ] Testar fluxo completo: Configuração → Leituras → Configuração
