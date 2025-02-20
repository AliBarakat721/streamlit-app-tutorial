import streamlit as st
import pandas as pd 
import plotly.express as px
import numpy as np 

@st.cache_data
def load_data (file):
    return pd.read_csv(file)

# تحميل الملف
file = st.file_uploader("Upload File", type=['csv'])

# معالجة البيانات عند تحميل الملف
if file is not None:
    df = load_data(file)

    # اختيار عدد الصفوف لعرضها
    n_rows = st.slider("Choose number of rows", min_value=5, 
                       max_value=len(df), step=1)
    
    # اختيار الأعمدة لعرضها
    cols_to_show = st.multiselect("Select Columns To Show", df.columns.to_list(), 
                                  default=df.columns.to_list())
    
    # تحديد الأعمدة العددية
    numerical_columns = df.select_dtypes(include=np.number).columns.to_list()

    # عرض البيانات
    st.write(df[:n_rows][cols_to_show])

    # استخدام التابات
    tab_1, tab_2 = st.tabs(["Scatter plot", "Histogram"])
    
    with tab_1:
        col_1, col_2, col_3 = st.columns(3)
        
        # اختيار الأعمدة للرسم البياني
        with col_1:
            x_column = st.selectbox('Select column for X-axis', numerical_columns)
        with col_2:
            y_column = st.selectbox('Select column for Y-axis', numerical_columns)
        with col_3:
            color = st.selectbox("Select columns to color", df.columns)

        # رسم الرسم البياني التشتتي (scatter plot)
        fig_scatter = px.scatter(df, x=x_column, y=y_column, color=color)
    
        # عرض الرسم البياني
        st.plotly_chart(fig_scatter)

    with tab_2:
        # اختيار الأعمدة للرسم البياني الهيستوجرام
        hist_feature = st.selectbox("Select Feature to create histogram", numerical_columns)
        
        # رسم الهيستوجرام
        fig_hist = px.histogram(df, x=hist_feature)
        st.plotly_chart(fig_hist)

