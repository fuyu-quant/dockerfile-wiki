import streamlit as st
import pandas as pd
import numpy as np


left_col, right_col = st.columns(2)


left_col.title('Sample App')

right_col.title('Hello')




st.sidebar.title('sidebar')




# 文章を書く
st.write('あいうえお')
"Hellow World"



# markdown
st.markdown('# 見出し1')
st.markdown('## 見出し2')

st.markdown("""
- 箇条書き
- 箇条書き
- 箇条書き
"""

)

st.code("""
import numpy as np
import pandas as pd
a = 123

df = pd.DataFrame()

"""
)

st.latex("\int a x^2")


if st.button('Click'):
    st.write('Click')


if st.checkbox('Click'):
    st.write('Click')


options = st.multiselect(
    'what are your favorite colors',
    ['Green', 'Yellow', 'Red', 'Blue'],
    ['Yellow', 'Red']
)

# 引数は最小値，最大値，初期値
number = st.sidebar.slider('Pick a Num',0,100,40)
st.sidebar.write(f'number:{number}')


# dataframe 
df = pd.DataFrame(
   np.random.randn(10, 20),
   columns=('col %d' % i for i in range(20)))

st.dataframe(df.style.highlight_max(axis=0))

# jsonの可視化
st.json({
    'data':{
        'name1': 'a',
        'name2': 'b'
    }
})


df = pd.DataFrame(
    np.random.randn(20,3),
    columns=['a', 'b','c']
)

st.line_chart(df)
st.area_chart(df)