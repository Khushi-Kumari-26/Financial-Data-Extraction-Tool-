import streamlit as st
import pandas as pd
import helper

st.title("Financial Extractor Tool")
financial_data_df = pd.DataFrame({
    "Measure":["Company Name", "Stock Symbol", "Revenue", "Net Income", "EPS"],"Value":["","","","",""]
})
# article = st.text_area("Paste your article here")

col1,spacer,col2 = st.columns([3,0.5,2])

with col1:
    st.header("Extracter Tool")
    article = st.text_area("Paste your article here",height=300)
    if st. button("Extract"):
        financial_data_df = helper.extract_financial_info(article)

with col2:
    st.header("Result")
   
    st.dataframe(
        financial_data_df,
        column_config={
            "Measure": st.column_config.Column(width=150),
            "Value": st.column_config.Column(width=150)
        },
        hide_index=True
    )


