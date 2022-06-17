import streamlit as st
import datetime as dt

def change(txt):
    encrypt = {'A':'.-', 'B':'-...', 'C':'-.-.',
               'D':'-..', 'E':'.', 'F':'..-.',
               'G':'--.', 'H':'....', 'I':'..',
               'J':'.---', 'K':'-.-', 'L':'.-..',
               'M':'--', 'N':'-.', 'O':'---',
               'P':'.--.', 'Q':'--.-', 'R':'.-.',
               'S':'...', 'T':'-', 'U':'..-',
               'V':'...-', 'W':'.--', 'X':'-..-',
               'Y':'-.--', 'Z':'--..', ' ':'.....'}
    decrypt = {v: k for k, v in encrypt.items()}
    
    if '-' in txt:
        return ''.join(decrypt[i] for i in txt.split())
    return ' '.join(encrypt[i] for i in txt.upper())

st.title("Morse Code Translator for you :P")

now = dt.datetime.now()

st.write(f"It is Currently {now}")

input_text = st.text_input("Enter text to tranlslate")

if st.button("Translate"):
	result = change(input_text)
	st.success(result)


