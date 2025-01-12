# AI Blog Generator

A streamlined web application that helps you generate high-quality blog content using AI. Built with Streamlit and powered by LangChain and Hugging Face's language models, this tool makes blog creation efficient and engaging.

## Features ✨

- **Title Generation**: Get 10 creative, SEO-friendly title suggestions for your blog topic 
- **Content Generation**: Create complete blog posts with structured sections
- **Keyword Management**: Add and track keywords to be incorporated into your content
- **Flexible Word Count**: Choose your desired content length (100-2000 words)
- **Adaptive Content Style**: Automatically adjusts tone and style based on topic type
- **Smart Formatting**: Well-structured content with proper sections and formatting

## Prerequisites 📋

Before running the application, ensure you have:

- Python 3.8 or higher
- A Hugging Face API key
- Required Python packages

## Installation 🚀

1. Clone the repository:
   ```bash
   git clone [your-repository-url]
   cd ai-blog-generator
   ```

2. Install the required dependencies:
   ```bash
   pip install langchain
   pip install langchain-huggingface
   pip install streamlit
   ```

3. Create a `secret_api_keys.py` file in the root directory:
   ```python
   huggingface_api_key = "your-api-key-here"
   ```

## Usage 💡

1. Start the Streamlit application:
   ```bash
   streamlit run app.py
   ```

2. Generate content in three simple steps:
   - Enter your topic to get title suggestions
   - Select your preferred title and add relevant keywords
   - Generate your blog content with desired word count

## Features in Detail 🔍

### Title Generation
- Input your blog topic
- Get 10 unique, SEO-friendly titles
- Titles adapt to topic type (technical, business, lifestyle)
- Character-optimized for maximum impact

### Content Generation
- Structured content with introduction, main body, and conclusion
- Smart adaptation to technical vs non-technical topics
- Professional formatting with headers and sections
- Natural keyword integration
- Adjustable word count (100-2000 words)

### Keyword Management
- Add multiple keywords
- Visual keyword display
- Automatic keyword integration in content
- Easy keyword management interface

## Configuration ⚙️

The following constants can be modified in the code:
```python
HUGGINGFACE_MODEL_ID = "meta-llama/Meta-Llama-3-8B-Instruct"
TEMPERATURE = 0.6
MIN_WORD_COUNT = 100
MAX_WORD_COUNT = 2000
WORD_COUNT_STEP = 50
```

## Project Structure 📁

```
ai-blog-generator/
├── app.py                 # Main application file
├── secret_api_keys.py     # API key configuration
├── requirements.txt       # Project dependencies
└── README.md             # Documentation
```

## Contributing 🤝

Contributions are welcome! Please feel free to submit a Pull Request. For major changes:

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Open a Pull Request

## Troubleshooting 🔧

Common issues and solutions:

1. **API Key Issues**:
   - Ensure your Hugging Face API key is correctly set in `secret_api_keys.py`
   - Check if your API key has the necessary permissions

2. **Installation Issues**:
   - Make sure all dependencies are installed correctly
   - Use a virtual environment to avoid package conflicts

## Acknowledgments 🙏

- Built with [LangChain](https://github.com/hwchase17/langchain)
- Powered by [Hugging Face](https://huggingface.co/)
- Interface created with [Streamlit](https://streamlit.io/)

##  Local URL: http://localhost:8501
##  Network URL: http://192.168.68.91:8501



![image](https://github.com/user-attachments/assets/52b6779f-977a-4b07-8f09-66867f83af48)


![image](https://github.com/user-attachments/assets/fd703fb1-0b45-46cc-b104-7ff558936a61)


![image](https://github.com/user-attachments/assets/d30e4252-c133-49f8-bc52-5cbbacd21f75)



![image](https://github.com/user-attachments/assets/096d590f-5a20-4b49-89b5-8a90077bada5)



