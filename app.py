from re import T
import streamlit as st


def showpositiveprompt():
    st.success('Success')

def shownegprompt():
    st.error('Failed!')

def validation(username):
    if (username=='shoaib'):
        showpositiveprompt()
    else:
        shownegprompt()


def main():
    st.title('On-Page SEO Optimizer')
    st.subheader('Combining data science with SEO to get better results!')
    st.subheader('Automatic Deployment')
    username = st.text_input("Enter your name")
    butt = st.button("button")
    if(butt==T):
        validation(username)


if __name__ == '__main__':
    main()
