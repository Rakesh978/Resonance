import streamlit as st 
st.title("Resonance - 2205A21027")
import math
def output(R,L,C):
    Fr=1/(2*math.pi*math.sqrt(L*C))
    Bw=R/(2*math.pi*L)
    Q=Fr/Bw
    Fl=Fr-(Bw/2)
    Fu=Fr+(Bw/2)
    return Fr,Bw,Q,Fl,Fu

col1,col2=st.columns(2)
with col1:
    R=st.number_input("enter the Resistance(Ohm)",value=100.0)
    L=st.number_input("enter the Inductance(H)",value=100.0)
    C=st.number_input("enter theCapictance(F)",value=100.0)
    compute=st.button("comput")

with col2:
    with st.container(border=True):
        if compute:
            Fr,Bw,Q,Fl,Fu=output(R,L,C)
            st.write(f"**Resonance Freqency (Fr):**{Fr:.2f}Hz")
            st.write(f"**Bandwidth (Bw):**{Bw:.2f}Hz")
            st.write(f"**Quality Factor (Q):**{Q:.2f}")
            st.write(f"**Upper Cutoff Frequency (Fu):**{Fu:.2f}Hz")
            st.write(f"**Lower Cutoff Frequency (Fl):**{Fl:.2f}Hz")
        else:
            st.error("Inductance(L) and Capictance (C) must be greater than 0.")  