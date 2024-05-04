# -*- coding: utf-8 -*-
"""
Created on Fri May  3 22:38:35 2024

@author: Marcelo Melo
"""
# exemplo do site
import gradio as gr
import numpy as np    

def escolhas(input_img,filtro):
#sepia
    if filtro == "Sepia" :     
        sepia_filter = np.array([ #matriz que armazena as coordenadas das cores
            [0.393, 0.769, 0.189], 
            [0.349, 0.686, 0.168], 
            [0.272, 0.534, 0.131]  
        ])
        sepia_img = input_img.dot(sepia_filter.T) # o que é isso? .dot e .T
        sepia_img /= sepia_img.max() # o que é isso? divisão e .max
        final_img = sepia_img # passa o resultado da imagem com o filtro aplicado para a imagem final
        
#preto e branco      
    if filtro == "Preto e branco" : 
        black_white_filter = np.array([
            [0.1, 0.1, 0.1],
            [0.1, 0.1, 0.1], 
            [0.1, 0.1, 0.1]  
        ])
        black_white_img = input_img.dot(black_white_filter.T)
        black_white_img /= black_white_img.max()
        final_img = black_white_img

    return final_img #retorna a imagem com o filtro aplicado

demo = gr.Interface(escolhas,
                    [gr.Image(),
                     gr.Dropdown(["Sepia","Preto e branco"], label="Filtros", info="mais filtros no futuro")],
                    "image",
                    allow_flagging=False
                    )
  
if __name__ == "__main__":
    demo.launch()

	