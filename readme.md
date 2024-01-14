# Reconhecimento de Gestos de Mão em Vídeo com MediaPipe e Keras

Este código demonstra como realizar o reconhecimento de gestos de mão em um vídeo utilizando a biblioteca MediaPipe e um modelo de aprendizado profundo carregado com o Keras. O objetivo é identificar gestos de mão específicos em cada quadro do vídeo e exibir os resultados visualmente em um novo vídeo de saída.

## Pré-requisitos

Antes de executar o código, você precisará ter os seguintes pré-requisitos instalados:

- Python (versão utilizada: 3.7+)
- Bibliotecas Python: cv2, mediapipe, keras, numpy
- TensorFlow (versão utilizada: 2.9.1)
- Jupyter Notebook (ou ambiente equivalente)

## Como usar

1. **Código Fonte**: Certifique-se de que você tenha o código fonte em mãos.

2. **Vídeo de Entrada**: Você precisa fornecer um vídeo como entrada para o código. No exemplo fornecido, o caminho para o vídeo é definido como 'V.mp4'. Certifique-se de que seu vídeo esteja no mesmo diretório ou atualize o caminho do arquivo de vídeo conforme necessário.

3. **Modelo Keras**: Você também precisa ter treinado um modelo de aprendizado profundo para o reconhecimento de gestos de mão usando o Keras. Certifique-se de carregar o modelo corretamente no código (por exemplo, 'keras_model.h5').

4. **Execução**: Execute o código em um ambiente Python compatível (como o Jupyter Notebook). Ele processará cada quadro do vídeo de entrada, identificará gestos de mão e exibirá os resultados visualmente em um novo vídeo de saída.

5. **Resultados**: O vídeo de saída conterá os quadros do vídeo de entrada com os rótulos indicando o gesto de mão identificado.

## Melhorando o Modelo

Para melhorar o modelo de reconhecimento de gestos de mão, considere as seguintes estratégias:

- Aumentar o tamanho do conjunto de dados de treinamento.
- Aumentar o número de classes de gestos de mão.
- Ajustar hiperparâmetros do modelo.
- Experimentar diferentes arquiteturas de rede.
- Aumentar a quantidade de dados de treinamento sintético.
- Ajustar os critérios de pós-processamento dos resultados.
