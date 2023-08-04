# Estudos sobre State of charge de baterias
Esse repositório aprensenta um compilado de conceitos referentes ao uso de baterias. Esse estudo foi realizado com o objetivo de melhor entender como é metrificado o uso da bateria, atualmente e como podemos melhorar seu uso a partir dessas métricas

## O que é SoC (State of Charge)?
"State of Charge", que em português pode ser traduzido como "Estado de Carga", também é chamado de SOC.
O SOC de uma bateria é uma medida que indica a quantidade de energia armazenada disponível em uma bateria em relação à sua capacidade total. É expresso como uma porcentagem, onde 0% representa uma bateria totalmente descarregada e 100% representa uma bateria totalmente carregada.

O SOC é uma informação crucial para muitas aplicações, pois permite aos usuários ou sistemas monitorar o nível de carga da bateria e tomar decisões informadas sobre o uso ou recarga dela. Em veículos elétricos, sistemas de energia renovável e dispositivos eletrônicos portáteis, o SOC é monitorado para garantir uma utilização adequada da bateria e prolongar sua vida útil.

## O que é SoH (State of Health) e como essa métrica influencia o SoC?

O SoH (State of Health), ou Estado de Saúde, de uma bateria é outra métrica importante que representa a capacidade atual da bateria em relação à sua capacidade original quando era nova. Em outras palavras, o SoH é uma medida da degradação ou desgaste da bateria ao longo do tempo devido a ciclos de carga e descarga repetidos, idade, temperatura e outros fatores ambientais.

O SoH é uma importante para um melhor cálculo do SOC (State of Charge) da bateria, pois a degradação da bateria pode afetar a precisão das estimativas do SOC. O SoH influencia o cálculo do SOC de duas maneiras principais:

1. **Capacidade Efetiva da Bateria**: O SoH reflete a capacidade atual da bateria. À medida que a capacidade diminui devido ao envelhecimento, o SOC total disponível também diminui. Por exemplo, se uma bateria tinha uma capacidade de 100 Wh quando nova, mas seu SoH é de 80% devido à degradação, a capacidade efetiva da bateria agora é de 80 Wh. Portanto, mesmo que a bateria esteja totalmente carregada, o SOC será de 80%.

2. **Precisão dos Métodos de Cálculo**: Alguns métodos de cálculo do SOC dependem de modelos matemáticos que incluem informações sobre a capacidade da bateria, que é frequentemente representada pelo SoH. Se o SoH não for levado em conta ou for mal estimado, os cálculos do SOC podem ser imprecisos. Portanto, um SoH preciso é importante para melhorar a precisão dos métodos de cálculo do SOC.

Em resumo, o SoH e o SOC são duas métricas inter-relacionadas. O SoH afeta a quantidade de energia disponível em uma bateria e a capacidade de fornecer uma carga completa. Para obter estimativas precisas do SOC, é fundamental levar em consideração o SoH da bateria ao usar qualquer método de cálculo do SOC. Medir o SoH periodicamente é essencial para monitorar a saúde da bateria ao longo do tempo e tomar decisões informadas sobre sua utilização e possível substituição.

## Como obter o SoC de uma bateria?
Existem várias formas de calcular o SOC de uma bateria, e a escolha do método depende do tipo de bateria, da disponibilidade de sensores e dos requisitos de precisão. Algumas das formas mais comuns de calcular o SOC de uma bateria incluem:

1. **Método de Coulomb Counting:** Este é um método simples que envolve a integração da corrente que entra ou sai da bateria ao longo do tempo. Ele calcula o SOC com base no princípio de que a quantidade de carga que entra ou sai da bateria é proporcional ao SOC.

2. **Método de Tensão:** Esse método utiliza a tensão da bateria para estimar o SOC. É importante observar que a tensão da bateria nem sempre é uma medida precisa do SOC, pois pode haver variações na tensão devido a diferentes condições de carga e descarga. Ou melhor falando, vai depender do SoH (State of Health) da bateria.

3. **Método de Resistência Interna:** Neste método, mede-se a resistência interna da bateria e, em seguida, utiliza-se para calcular o SOC a partir da variação da tensão em relação à corrente.

4. **Métodos Baseados em Modelos:** Estes métodos utilizam modelos matemáticos ou algoritmos para estimar o SOC com base no comportamento conhecido da bateria. Modelos como o modelo de circuito elétrico equivalente e modelos de regressão podem ser utilizados para estimar o SOC.

5. **Métodos de Aprendizado de Máquina:** Algoritmos de aprendizado de máquina, como redes neurais, podem ser treinados com base em dados históricos de carga e descarga da bateria para prever o SOC com maior precisão.

6. **Método de Amperímetro-horímetro:** Este método utiliza um dispositivo chamado amperímetro-horímetro para medir a quantidade de carga que entra e sai da bateria, permitindo calcular o SOC.

7. **Métodos Combinados:** Em muitos sistemas, uma combinação de métodos é usada para obter estimativas mais precisas do SOC. Por exemplo, o método de Coulomb Contagem pode ser combinado com um método baseado em modelo para melhorar a precisão.

> ⚠️ É importante notar que cada método tem suas vantagens e desvantagens, e a precisão do cálculo do SOC pode variar dependendo das condições de operação da bateria. A seleção do método adequado para calcular o SOC deve levar em consideração a aplicação específica e as limitações técnicas do sistema em que a bateria está sendo usada.

# Artigos interessantes
* [The State Of Charge estimating methods for rechargeable Lead-acid batteries](Docs/The_State_Of_Charge_estimating_methods_for_rechargeable_Lead-acid_batteries.pdf)
* [State of charge estimation of lead acid battery using a kalman filter](Docs/State_of_charge_estimation_of_lead_acid_battery_using_a_Kalman_filter.pdf)
* [The SOC Prediction of Lead-Acid Battery Based on MIV-OSELM Algorithm](Docs/The_SOC_Prediction_of_Lead-Acid_Battery_Based_on_MIV-OSELM_Algorithm.pdf) 
* [State of Charge (SOC) Estimation on Lead-Acid Batteries Using the Coulomb Counting Method](Docs/State_of_Charge_SOC_Estimation_on_Lead-Acid_Batteries_Using_the_Coulomb_Counting_Method.pdf)