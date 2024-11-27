import streamlit as st
import cv2
import numpy as np
from utils.graph_cut_segmentation import (
    graph_cut_segment, 
    graph_cut_withoutGB, 
    morpho_operations_with_GB, 
    morpho_operations_without_GB,
    ximgproc_graph_cut
)

import tempfile
import os

st.set_page_config(layout="wide")

st.title('🔍 Grain Boundary Detection')
st.markdown("""
    <style>
        .title {text-align: center}
        .stImage {display: block; margin: auto;}
        div.stButton > button {display: block; margin: auto;}
    </style>
    """, unsafe_allow_html=True)
st.write("Performs grain boundary detection using graph cut segmentation with morphological operations.")

uploaded_file = st.file_uploader("Choose an image...", type=['jpg', 'jpeg', 'png'])

# Add number inputs for morphological operations
erosion_iterations = st.number_input('Number of Erosion Iterations', min_value=1, max_value=10, value=1, 
                                   help="Controls how many times erosion is applied. Higher values create stronger erosion effect.")
dilation_iterations = st.number_input('Number of Dilation Iterations', min_value=1, max_value=10, value=1,
                                    help="Controls how many times dilation is applied. Higher values create stronger dilation effect.")

if uploaded_file is not None:
    # Create a progress bar
    with st.spinner('Processing image...'):
        progress_bar = st.progress(0)
        
        # Save uploaded file temporarily
    with tempfile.NamedTemporaryFile(delete=False, suffix='.jpg') as tmp_file:
        tmp_file.write(uploaded_file.getvalue())
        temp_path = tmp_file.name

        progress_bar.progress(10)
        result0 = morpho_operations_with_GB(temp_path, erosion_iter=erosion_iterations, dilation_iter=dilation_iterations)
        progress_bar.progress(20)
        result1 = morpho_operations_without_GB(temp_path, erosion_iter=erosion_iterations, dilation_iter=dilation_iterations)
        progress_bar.progress(30)
        result = graph_cut_segment(temp_path, erosion_iter=erosion_iterations, dilation_iter=dilation_iterations)
        progress_bar.progress(60)
        result2 = graph_cut_withoutGB(temp_path, erosion_iter=erosion_iterations, dilation_iter=dilation_iterations)
        progress_bar.progress(80)
        ximgproc_result = ximgproc_graph_cut(temp_path,erosion_iter=erosion_iterations, dilation_iter=dilation_iterations)
        progress_bar.progress(100)
    
    # Display images in a grid layout
    st.markdown("""
        <h2 style='text-align: center; color: #0066cc; margin-bottom: 30px;'>🔍 Image Processing Results</h2>
    """, unsafe_allow_html=True)
    
    # Original image in full width
    st.subheader("📸 Original Image")
    st.image(uploaded_file, use_column_width=True)
    
    # First row of processed images
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### 🔄 Morphological + Gaussian Blur")
        st.image(result0, use_column_width=True)
        st.caption("Morphological operations with Gaussian blur applied")
        
    with col2:
        st.markdown("### 🔄 Pure Morphological")
        st.image(result1, use_column_width=True)
        st.caption("Morphological operations without Gaussian blur")
    
    # Second row of processed images
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### ✨ Segmented + Gaussian")
        st.image(result, use_column_width=True)
        st.caption("Graph cut segmentation using felzenswab with Gaussian blur")
        
    with col2:
        st.markdown("### ✨ Pure Segmentation")
        st.image(result2, use_column_width=True)
        st.caption("Graph cut segmentation using felzenswab without Gaussian blur")
    
    # XImgProc result in full width
    st.markdown("### 🎯 XImgProc Graph Cut")
    st.image(ximgproc_result, use_column_width=True)
    st.caption("Graph-cut segmentation using cv2.ximgproc")
    
    # with col1:
    #     st.subheader("Original Image")
    #     st.image(uploaded_file, width=600)
    #     st.write("Original input image before processing")
    
    # with col2:
    #     st.subheader("Segmented Image")
    #     # st.image(result)
    #     # image size increase
    #     st.image(result, width=600)
    #     st.write("Processed image with grain boundaries detected")
    
    st.markdown("---")
    st.subheader("Current Settings")
    col1, col2 = st.columns(2)
    with col1:
        st.info(f"**Erosion Iterations:** {erosion_iterations}")
    with col2:
        st.info(f"**Dilation Iterations:** {dilation_iterations}")
    
    # Convert result to bytes for download
    
    # Download section
    st.markdown("---")
    st.markdown("""
        <h3 style='text-align: center; color: #0066cc;'>📥 Download Results</h3>
        <p style='text-align: center; color: #666666; margin-bottom: 20px;'>Download processed images in PNG format</p>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1,4,1])
    with col2:
        is_success, buffer = cv2.imencode(".png", result)
        if is_success:
            st.download_button(
                label="💫 Download Segmented Image with Gaussian Blur",
                data=buffer.tobytes(),
                file_name="segmented_image_withGB.png",
                mime="image/png",
                use_container_width=True,
            )
            st.markdown("<div style='margin: 10px'></div>", unsafe_allow_html=True)
            
        is_success, buffer = cv2.imencode(".png", result2)
        if is_success:
            st.download_button(
                label="✨ Download Segmented Image without Gaussian Blur",
                data=buffer.tobytes(),
                file_name="segmented_image_withoutGB.png",
                mime="image/png",
                use_container_width=True,
            )
            st.markdown("<div style='margin: 10px'></div>", unsafe_allow_html=True)
            
        is_success, buffer = cv2.imencode(".png", ximgproc_result)
        if is_success:
            st.download_button(
                label="🎯 Download XImgProc Segmented Image",
                data=buffer.tobytes(),
                file_name="ximgproc_segmented.png",
                mime="image/png",
                use_container_width=True,
            )
    
    # Cleanup temp file
    os.unlink(temp_path)
else:
    st.write("Please upload an image to begin processing.")
