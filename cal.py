import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


st.title("2차 방정식 계산기")

st.write("---")


def space(num_lines):
    for _ in range(num_lines):
        st.write("")

def func(a,b,c):
    D=b**2-4*a*c
    if D>0:
        x1=round((-b-D**0.5)/2*a)
        x2=round((-b+D**0.5)/2*a)
        st.success(f"x ={x1},{x2}")
    elif D==0:
        x=round(-b/2*a)
        st.info("중근입니다")
        st.success(f"x ={x}")
    else:
        st.info("허근입니다")
        
def graph(a,b,c):
    x = np.array(range(-10, 11))
    
    fomula = f'''{a}x^2 { "+" if b >= 0 else ""}{b}x {"+" if c >= 0 else ""}{c}'''
    
    plt.figure(figsize=(10,10))
    
    fig, ax = plt.subplots()
    ax.grid(color = "gray", alpha=.5, linestyle="--")
    
    ax.axvline(x=0, color = 'black')  # draw x =0 axes
    ax.axhline(y=0, color = 'black')   # draw y =0 axes
    
    ax.plot(x, a*x**2+b*x+c, label = fomula)
    ax.legend()
    st.pyplot(fig)
        
def get_latex(a,b,c):
    return f'''$y = {a}x^2 {"+" if b >= 0 else ""}{b}x {"+" if c >= 0 else ""}{c}$'''
        
def main():
    a = st.number_input(label="2차 항의 계수를 작성하시오")
    b = st.number_input(label="1차 항의 계수를 작성하시오")
    c = st.number_input(label="상수 항의 계수를 작성하시오")
    
    if st.button("result"):
        func(a,b,c)
        
        space(1)
        
        st.markdown(f"{get_latex(a,b,c)}")
        
        space(1)
        
        graph(a,b,c)
        
if __name__ == '__main__':
    main()