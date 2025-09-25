#!/usr/bin/env python3
"""
Streamlit Web App for Text Summarizer
A modern web interface for text summarization using transformer models
"""

import streamlit as st
import torch
from transformers import pipeline
import re

# Configure page
st.set_page_config(
    page_title="Text Summarizer",
    page_icon="📝",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Title and description
st.title("🤖 AI Text Summarizer")
st.markdown("""
Powered by state-of-the-art transformer models for intelligent text summarization.
Enter your text below and get a concise, meaningful summary instantly!
""")

@st.cache_resource
def load_summarizer():
    """Load the summarization model with caching"""
    try:
        # Use BART model for summarization
        summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
        return summarizer
    except Exception as e:
        st.error(f"Error loading model: {str(e)}")
        return None

def clean_text(text):
    """Clean and preprocess text"""
    # Remove extra whitespace
    text = re.sub(r'\s+', ' ', text)
    text = text.strip()
    return text

def main():
    # Sidebar configuration
    with st.sidebar:
        st.header("⚙️ Configuration")
        max_length = st.slider(
            "Max Summary Length", 
            min_value=50, 
            max_value=300, 
            value=130, 
            help="Maximum length of the generated summary"
        )
        min_length = st.slider(
            "Min Summary Length", 
            min_value=10, 
            max_value=100, 
            value=30, 
            help="Minimum length of the generated summary"
        )
        
        st.markdown("---")
        st.markdown("""
        ### About
        This app uses Facebook's BART model to generate 
        extractive and abstractive summaries of your text.
        
        **Features:**
        - 🚀 Fast processing
        - 🎯 Accurate summaries
        - 🔧 Customizable length
        - 📱 Mobile friendly
        """)
    
    # Main content area
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.subheader("📄 Input Text")
        input_text = st.text_area(
            "Enter your text here:",
            height=300,
            placeholder="Paste your text here to summarize..."
        )
        
        # Example texts
        st.markdown("**Try these examples:**")
        example_texts = {
            "AI Research": "Artificial intelligence (AI) is intelligence demonstrated by machines, in contrast to the natural intelligence displayed by humans and animals. Leading AI textbooks define the field as the study of intelligent agents: any device that perceives its environment and takes actions that maximize its chance of successfully achieving its goals. Colloquially, the term artificial intelligence is often used to describe machines that mimic cognitive functions that humans associate with the human mind, such as learning and problem solving.",
            "Technology News": "The latest breakthrough in quantum computing has been achieved by researchers at MIT, who have successfully demonstrated a 100-qubit quantum processor that maintains coherence for over 10 seconds. This advancement represents a significant step toward practical quantum computing applications, potentially revolutionizing fields such as cryptography, drug discovery, and financial modeling.",
            "Climate Science": "Climate change refers to long-term shifts in global or regional climate patterns. Since the mid-20th century, the pace of climate change has dramatically accelerated due to human activities, particularly the burning of fossil fuels, which increases heat-trapping greenhouse gas levels in Earth's atmosphere. The effects include rising global temperatures, melting ice caps, rising sea levels, and more frequent extreme weather events."
        }
        
        selected_example = st.selectbox("Choose an example:", list(example_texts.keys()))
        if st.button("Load Example"):
            st.session_state.example_text = example_texts[selected_example]
            st.rerun()
    
    with col2:
        st.subheader("📋 Summary")
        
        # Use example text if loaded
        text_to_process = st.session_state.get('example_text', input_text)
        if hasattr(st.session_state, 'example_text'):
            input_text = st.session_state.example_text
            del st.session_state.example_text
        
        if st.button("🔄 Generate Summary", type="primary") or text_to_process:
            if text_to_process and len(text_to_process.strip()) > 50:
                with st.spinner("Generating summary..."):
                    try:
                        # Load model
                        summarizer = load_summarizer()
                        
                        if summarizer:
                            # Clean and process text
                            cleaned_text = clean_text(text_to_process)
                            
                            # Generate summary
                            summary = summarizer(
                                cleaned_text,
                                max_length=max_length,
                                min_length=min_length,
                                do_sample=False
                            )[0]['summary_text']
                            
                            # Display summary
                            st.success("Summary generated successfully!")
                            st.text_area(
                                "Generated Summary:",
                                value=summary,
                                height=200,
                                disabled=True
                            )
                            
                            # Statistics
                            st.markdown("### 📊 Statistics")
                            col_a, col_b, col_c = st.columns(3)
                            
                            with col_a:
                                st.metric(
                                    "Original Words",
                                    len(cleaned_text.split())
                                )
                            
                            with col_b:
                                st.metric(
                                    "Summary Words",
                                    len(summary.split())
                                )
                            
                            with col_c:
                                compression_ratio = len(summary.split()) / len(cleaned_text.split())
                                st.metric(
                                    "Compression",
                                    f"{compression_ratio:.1%}"
                                )
                        
                    except Exception as e:
                        st.error(f"Error generating summary: {str(e)}")
                        st.info("Please try with a shorter text or adjust the parameters.")
            else:
                st.warning("Please enter at least 50 characters of text to summarize.")
    
    # Footer
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; color: #666;">
    <p>Built with ❤️ using Streamlit and Transformers | 
    <a href="https://github.com/chandrikachandra30/text-summarizer" target="_blank">View Source Code</a></p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
