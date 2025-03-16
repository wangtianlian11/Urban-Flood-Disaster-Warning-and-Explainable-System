import rand1
from rand1 import *

if __name__ == "__main__":
    try:
        main()
    except NameError:
        import streamlit as st
        st.title("Urban Flood Disaster Warning and Explainable System")
        st.write("系统已加载，请上传数据文件开始分析。")