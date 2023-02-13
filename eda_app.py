# import libraries
import pandas as pd
import streamlit as st
st.set_page_config(layout="wide")
from pandas_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report

# main app
def main():   

    # sidebar
    st.sidebar.header('File Uploader')
    data_file = st.sidebar.file_uploader('Upload a file or select the sample dataset below.')

    
    # app
    st.write('''
        # EDA Web App

        Built in `Python` + `Streamlit` by [Derrick Green](https://derrickhudsongreen.wordpress.com/)
        
        ---''')

    df = None

    if data_file is not None:
        @st.cache
        def load_data():
            csv = pd.read_csv(data_file)
            return csv
        df = load_data()

    elif st.sidebar.button('Click for sample dataset.'):
        @st.cache
        def load_data():
            sample_df = pd.read_csv('titanic_sample_data.csv')
            return sample_df
        df = load_data()

    if df is not None:
        report = ProfileReport(df, explorative=True) 
        st.write('### Input Data')
        st.dataframe(df)
        st.write('---')
        st.write('### EDA Report')
        st_profile_report(report)

        def download_report():
            report.to_file('EDA_report.html')

        st.sidebar.write('---')
        st.sidebar.button('Download Report',on_click=download_report)

    else:
        st.info('To begin, upload data or select Sample Data from the sidebar.')
    
   

if __name__ == "__main__":
    main()
