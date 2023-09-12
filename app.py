import streamlit as st
from annotated_text import annotated_text
import random
import os
# import keras

def get_text(path, categ, num):
    # print('Loading', num)
    if categ == 'pos':
        filename = f'hackathon_{num}.txt'
    else:
        filename = f'{num}.txt'

    filename = os.path.join(path, filename)
    with open(filename) as f:
        text = f.read()

    return text

def get_sorted_files():
    ret=[]
    filename='/Users/akashmeesa/desktop/aihackathon/generated_data/sorted_files.txt'
    with open(filename, 'r') as readfile:
        for line in readfile:
            if 'Bad' in line:
                ret.append(line)
    return ret   

if __name__ == '__main__':

    st.markdown("<h1 style='text-align: center; color: white;'>Loan Analyzer</h1>", unsafe_allow_html=True)
    result = st.button("Load new file")
    if result:
        num = random.randint(1,100)
        categ = random.choice(['pos','neg'])
        train_path = os.path.join('generated_data', 'generated_data', 'train', categ)
        # st.markdown("<em>Loading Analyzer</em>", unsafe_allow_html=True)
        text = get_text(train_path, categ, num)
        st.write(f'Loaded {num}!')
        st.write(text)
        
#     my_list = [
#         get_sorted_files(),
#         ("dear", "Adj"),
#         ("world", "Noun"),
#         ".",
#     ]

#     annotated_text(my_list)

    # print(text)
# new_Path = os.path.join('generated_data', 'new_data', categ)
