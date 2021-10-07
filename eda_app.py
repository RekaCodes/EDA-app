import numpy as np
from numpy.random import sample
import pandas as pd
import pandas_profiling
import streamlit as st
st.set_page_config(layout="wide")
from streamlit import uploaded_file_manager
from pandas_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report

def main():   

    # sidebar
    st.sidebar.header('File Uploader')
    # st.sidebar.write('---')
    data_file = st.sidebar.file_uploader('Upload a file or select the sample dataset below.')

    
    # app
    st.write('''
        # EDA Web App

        Built in `Python` + `Streamlit` by [Derrick Green](https://derrickhudsongreen.wordpress.com/)
        
        ---''')

    
    if data_file is not None:
        @st.cache
        def load_data():
            csv = pd.read_csv(data_file)
            return csv
        df = load_data()
        report = ProfileReport(df, explorative=True)        
        st.write('### Input Data')
        st.dataframe(df)
        st.write('### EDA Report')
        st_profile_report(report)

    elif st.sidebar.button('Click for sample dataset.'):
        @st.cache
        def load_data():
            sample_df = pd.read_csv('titanic_sample_data.csv')
            return sample_df
        df = load_data()
        report = ProfileReport(df, explorative=True) 
        st.write('### Input Data')
        st.dataframe(df)
        st.write('---')
        st.write('### EDA Report')
        st_profile_report(report)

    else:
        st.info('Upload data to begin.')



if __name__ == "__main__":
    main()
