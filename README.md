# 🤖 AI Text Summarizer

> **Live Demo**: [Coming Soon - Deploy to Streamlit Cloud]
> **Status**: 🌟 Ready for Deployment

An advanced NLP project for summarizing text using state-of-the-art transformer models with a beautiful web interface.

## 🎆 Features

- 🚀 **Fast Processing**: Powered by Facebook's BART model
- 🎯 **Accurate Summaries**: Both extractive and abstractive summarization
- 🔧 **Customizable Length**: Adjustable min/max summary length
- 📱 **Mobile Friendly**: Responsive Streamlit interface
- 📊 **Analytics**: Word count and compression ratio metrics
- ✨ **Example Texts**: Pre-loaded samples for quick testing

## 🚀 Quick Start

### Local Development

```bash
# Clone the repository
git clone https://github.com/chandrikachandra30/text-summarizer.git
cd text-summarizer

# Install dependencies
pip install -r requirements.txt

# Run the Streamlit app
streamlit run app.py
```

### 🌍 Live Deployment Options

#### 1. Streamlit Community Cloud (Recommended)

1. Fork this repository
2. Go to [share.streamlit.io](https://share.streamlit.io/)
3. Connect your GitHub account
4. Select this repository and `app.py` as the main file
5. Deploy! 🎆

**Deployment URL**: `https://share.streamlit.io/[your-username]/text-summarizer/main/app.py`

#### 2. Hugging Face Spaces

1. Create a new Space on [huggingface.co/spaces](https://huggingface.co/spaces)
2. Choose "Streamlit" as the SDK
3. Upload the repository files
4. Your app will be live at: `https://huggingface.co/spaces/[username]/text-summarizer`

#### 3. Render.com

1. Connect your GitHub repository to [render.com](https://render.com)
2. Create a new Web Service
3. Use the following settings:
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `streamlit run app.py --server.port $PORT --server.address 0.0.0.0`

#### 4. Railway

1. Connect to [railway.app](https://railway.app)
2. Deploy from GitHub repository
3. Add environment variables if needed
4. Your app will be automatically deployed

## 📝 API Usage

The main summarization logic can also be used programmatically:

```python
from main import main

# Run the basic summarization demo
main()
```

## 📦 Dependencies

- `torch>=1.9.0` - PyTorch for deep learning
- `transformers>=4.20.0` - Hugging Face transformers
- `streamlit>=1.25.0` - Web interface framework
- `numpy>=1.21.0` - Numerical computing
- `nltk>=3.7` - Natural language toolkit
- `scikit-learn>=1.0.0` - Machine learning utilities

See `requirements.txt` for the complete list.

## 🔧 Configuration

Customize the app behavior by modifying these parameters in `app.py`:

- **Model**: Currently using `facebook/bart-large-cnn`
- **Max Length**: Default 130 words (adjustable via UI)
- **Min Length**: Default 30 words (adjustable via UI)

## 📊 Performance

- **Model Size**: ~1.6B parameters (BART-large)
- **Processing Time**: ~2-5 seconds per summary
- **Max Input Length**: ~1024 tokens
- **Compression Ratio**: Typically 10-30% of original text

## 👥 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🚀 Related Projects

- [AI Chatbot](https://github.com/chandrikachandra30/ai-chatbot) - Conversational AI using transformer models
- [Image Classifier](https://github.com/chandrikachandra30/image-classifier) - Deep learning image classification

## 📞 Contact

- GitHub: [@chandrikachandra30](https://github.com/chandrikachandra30)
- Repository: [text-summarizer](https://github.com/chandrikachandra30/text-summarizer)

---

**Built with ❤️ using Streamlit and Transformers**
