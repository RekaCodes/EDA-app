import numpy as np
from numpy.random import sample
import pandas as pd
import streamlit as st
st.set_page_config(layout="wide")
from streamlit import uploaded_file_manager
from pandas_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report

def main():   

    # data
    sample_data = pd.DataFrame(
        np.random.rand(100,8),
        columns=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    )

    # sidebar

    st.sidebar.header('File Uploader')
    st.sidebar.write('---')
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
        st.dataframe(df)
        st_profile_report(report)

    else:
        st.info('To get started, use the File Uploader in the Sidebar.')
        if st.sidebar.button('Click for sample dataset.'):
            @st.cache
            def load_data():
                sample_df = pd.DataFrame(
                    np.random.rand(100,8),
                    columns=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
                )
                return sample_df
            df = load_data()
            report = ProfileReport(df, explorative=True) 
            st.dataframe(df)
            st_profile_report(report)



if __name__ == "__main__":
    main()