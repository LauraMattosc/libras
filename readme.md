# Reconhecimento de Gestos de Mão com MediaPipe e Keras

Este código demonstra como realizar o reconhecimento de gestos de mão em imagens utilizando a biblioteca MediaPipe e um modelo de aprendizado profundo carregado com o Keras. O objetivo é identificar gestos de mão específicos em imagens e exibir os resultados visualmente.

## Pré-requisitos

Antes de executar o código, você precisará ter os seguintes pré-requisitos instalados:

- Python (versão utilizada: 3.7+)
- Bibliotecas Python: cv2, mediapipe, keras, numpy, PIL (Pillow)
- TensorFlow (versão utilizada: 2.9.1)
- Jupyter Notebook (ou ambiente equivalente)

## Como usar

1. **Código Fonte**: Certifique-se de que você tenha o código fonte em mãos.

2. **Imagens de Entrada**: Você precisa fornecer imagens de gestos de mão como entrada para o código. No exemplo fornecido, uma lista de nomes de arquivos de imagem é usada (por exemplo, 'B2.jpg'). Certifique-se de que suas imagens estejam no mesmo diretório ou atualize o caminho dos arquivos de imagem conforme necessário.

3. **Modelo Keras**: Você também precisa ter treinado um modelo de aprendizado profundo para o reconhecimento de gestos de mão usando o Keras. Certifique-se de carregar o modelo corretamente no código (por exemplo, 'keras_model.h5').

4. **Execução**: Execute o código em um ambiente Python compatível (como o Jupyter Notebook). Ele processará as imagens de entrada, identificará gestos de mão e exibirá os resultados visualmente usando OpenCV.

5. **Resultados**: Os resultados do reconhecimento de gestos de mão serão exibidos na tela, com rótulos indicando o gesto identificado.

## Melhorando o Modelo

Para melhorar o modelo de reconhecimento de gestos de mão, considere as seguintes estratégias:

- Aumentar o tamanho do conjunto de dados de treinamento.
- Aumentar o número de classes de gestos de mão.
- Ajustar hiperparâmetros do modelo.
- Experimentar diferentes arquiteturas de rede.
- Aumentar a quantidade de dados de treinamento sintético.
- Ajustar os critérios de pós-processamento dos resultados.
