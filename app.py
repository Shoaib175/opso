from re import T
import streamlit as st
import streamlit.components.v1 as components
import time
import requests
from bs4 import BeautifulSoup

def main():
    st.title('On-Page SEO Optimizer')
    st.subheader('Combining data science with SEO to get better results!')
    city = st.text_input("Enter your target keyword")
    button = st.button("Scrape")
    if(button==T):
        url = "https://www.google.com/search?q=baby+shark"
        req = requests.get(url)
        soup = BeautifulSoup(req.text, "html.parser")
        st.write(req.text)
        st.write(soup.title.text)   



if __name__ == '__main__':
    main()
