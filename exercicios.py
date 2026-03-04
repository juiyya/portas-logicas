### 6. Sistema de iluminação inteligente com Três Sensores

#contexto: Uma lâmpada inteligente acende SOMENTE quando:
# sensor de presença (A), detecta movimento;
# sensor de luminosidade (B), indica ambiente escuro (B=0)
# sensor de janela (C) detecta janela fechada (C=0);
# ou se o modo noturno (D) estiver ativado (D=1).

A = 1
B = 1
C= 1
D = 1
if (A and not (B) and not (C)) or D:
    print("ON")
else:
    print("OFF")

     