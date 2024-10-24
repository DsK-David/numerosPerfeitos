# Gerador de Números Perfeitos

Este projeto é um programa em Python que encontra e exibe todos os números perfeitos até um limite especificado pelo usuário. Um número perfeito é um número inteiro positivo que é igual à soma de seus divisores próprios positivos, excluindo ele mesmo.

## Funcionalidades

- **Identificação de Números Perfeitos:** O programa verifica se um número é perfeito através da função `eh_numero_perfeito`.
- **Limite Personalizável:** O usuário pode definir um limite até onde deseja encontrar números perfeitos.

## Como Funciona

### Funções Principais

1. **`eh_numero_perfeito(n)`**
   - **Descrição:** Verifica se o número `n` é um número perfeito.
   - **Parâmetro:** `n` (int) - O número a ser verificado.
   - **Retorno:** Retorna `True` se `n` for um número perfeito e `False` caso contrário.
   - **Lógica:**
     - Inicializa a soma dos divisores com 1, pois 1 é divisor de qualquer número.
     - Itera sobre os números de 2 até a raiz quadrada de `n`.
     - Para cada divisor encontrado, adiciona tanto o divisor quanto seu par (n // i) à soma dos divisores, evitando contagem duplicada.
     - No final, compara a soma dos divisores com o número `n`.

2. **`encontrar_numeros_perfeitos(limite)`**
   - **Descrição:** Encontra todos os números perfeitos até um determinado limite.
   - **Parâmetro:** `limite` (int) - O limite superior para a busca.
   - **Retorno:** Uma lista de números perfeitos encontrados até o limite.
   - **Lógica:**
     - Cria uma lista vazia para armazenar números perfeitos.
     - Itera através de todos os números de 2 até o limite e usa a função `eh_numero_perfeito` para verificar se cada número é perfeito.

### Execução do Programa

Para executar o programa, siga os seguintes passos:

1. **Instalação do Python:** Certifique-se de que o Python está instalado em seu sistema.
2. **Execução do Script:**
   - Salve o código em um arquivo chamado `numeros_perfeitos.py`.
   - Execute o script no terminal:
     ```bash
     python numeros_perfeitos.py
     ```
3. **Insira o Limite:** Quando solicitado, digite o limite até onde deseja encontrar números perfeitos.

### Exemplo de Uso

```
Digite o limite para encontrar números perfeitos: 10000
Números perfeitos até 10000: [6, 28, 496, 8128]
```

## Conclusão

Esse programa é uma forma interessante de explorar a matemática dos números perfeitos e pode ser expandido para incluir mais funcionalidades, como a pesquisa de números perfeitos em intervalos maiores ou a visualização gráfica dos resultados.

## Contato

Para mais informações ou sugestões, entre em contato
