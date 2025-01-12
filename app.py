# Import necessary libraries
from langchain_huggingface import HuggingFaceEndpoint  # Updated import for current LangChain version
from secret_api_keys import huggingface_api_key
from langchain.prompts import PromptTemplate
import os
import streamlit as st

# Configuration constants
HUGGINGFACE_MODEL_ID = "meta-llama/Meta-Llama-3-8B-Instruct"
TEMPERATURE = 0.6
MIN_WORD_COUNT = 100
MAX_WORD_COUNT = 2000
WORD_COUNT_STEP = 50

# Set up environment variables
os.environ['HUGGINGFACEHUB_API_TOKEN'] = huggingface_api_key

# Initialize LLM
def initialize_llm():
    """Initialize the Hugging Face language model w`ith specified parameters."""
    return HuggingFaceEndpoint(
        repo_id=HUGGINGFACE_MODEL_ID,
        temperature=TEMPERATURE,
        token=huggingface_api_key,
    )

# Define generalized prompt templates
TITLE_SUGGESTION_TEMPLATE = '''You are an expert content writer specializing in creating engaging titles. Create compelling titles for a blog post on the topic: {topic}.

Requirements for the titles:
- Generate exactly 10 unique titles
- Each title should be 50-70 characters long
- Suggest creative and attention-grabbing titles for this blog post. 

Consider these elements in your titles:
- Include relevant field-specific terms when appropriate
- Make them SEO-friendly and searchable
- Ensure they're clear and specific to the topic
- Target the appropriate audience level
- Create genuine interest or urgency when relevant
- Adapt style based on topic (professional for business, casual for lifestyle, etc.)

If the topic is technical:
- Include relevant technical terms
- Mention specific technologies or methodologies
- Consider adding skill level indicators (e.g., "Beginner's Guide", "Advanced Techniques")

Format each title on a new line, numbered from 1-10.
Only provide the titles - no explanations or additional text.
'''

BLOG_CONTENT_TEMPLATE = '''You are an expert content writer creating an engaging blog post on: "{title}"

Content Requirements:
- Target word count: {blog_length} words
- Required keywords to incorporate naturally: {keywords}
- Reading level: Adapt to topic complexity while remaining accessible

Structure the blog post with these sections:
1. Introduction:
   - Start with an engaging hook relevant to the topic
   - Establish relevance and context
   - Preview the key points readers will learn
   - Set appropriate expectations for the content

2. Main Content:
   - Break down concepts into clear, digestible sections
   - Use examples and analogies appropriate to the field
   - Include practical applications or actionable insights
   - Address common questions or misconceptions
   - If technical topic:
     * Include relevant code snippets or technical examples
     * Explain technical concepts progressively
     * Provide practical implementation details
   - If non-technical topic:
     * Include relevant real-world examples
     * Provide practical applications
     * Use appropriate field-specific case studies

3. Supporting Content:
   - Each section should focus on one main concept
   - Use smooth transitions between ideas
   - Include relevant details and evidence
   - Provide step-by-step guidance where applicable
   - Add visual descriptions or data points when relevant

4. Conclusion:
   - Summarize key insights
   - Provide next steps or applications
   - Include relevant resources for further learning
   - End with an engaging call to action

Writing Style Guidelines:
- Adapt tone to match topic and audience:
  * Professional and precise for business/technical topics
  * Warm and approachable for lifestyle/personal topics
  * Academic and thorough for educational content
- Define specialized terms when first introduced
- Use clear, concise paragraphs
- Include formatting for better readability:
  * Bulleted lists for multiple points
  * Numbered lists for sequential steps
  * Headers for content organization
  * Block quotes for important statements
- If technical topic:
  * Format code snippets properly
  * Include comments in code examples
  * Explain technical concepts with analogies

Ensure the content is valuable, engaging, and appropriate for the target audience while maintaining accuracy and authority in the subject matter.
'''

def setup_langchain_components(llm):
    """Set up LangChain prompt templates and chains."""
    # Title suggestion components
    title_prompt = PromptTemplate(
        input_variables=['topic'],
        template=TITLE_SUGGESTION_TEMPLATE
    )
    title_suggestion_chain = title_prompt | llm

    # Blog content components
    content_prompt = PromptTemplate(
        input_variables=['title', 'keywords', 'blog_length'],
        template=BLOG_CONTENT_TEMPLATE
    )
    content_chain = content_prompt | llm

    return title_suggestion_chain, content_chain

def create_streamlit_ui():
    """Create and configure the Streamlit user interface."""
    st.title("AI Blog Generator")
    st.header("Create High-Quality Blog Content using AI")

def handle_title_generation(title_suggestion_chain):
    """Handle the title generation section of the UI."""
    st.subheader('Title Generation')
    topic_expander = st.expander("Input the topic")
    
    with topic_expander:
        topic_name = st.text_input("", key="topic_name")
        submit_topic = st.button('Submit topic')

    if submit_topic and topic_name:
        titles = title_suggestion_chain.invoke({'topic': topic_name})
        formatted_titles = '\n'.join(line.strip() for line in titles.split('\n') if line.strip())
        st.text(formatted_titles)

def handle_keyword_management():
    """Manage the keyword input and display system."""
    if 'keywords' not in st.session_state:
        st.session_state['keywords'] = []
    
    keyword_input = st.text_input("Enter a keyword:")
    if st.button("Add Keyword") and keyword_input:
        st.session_state['keywords'].append(keyword_input)
        for keyword in st.session_state['keywords']:
            st.write(
                f"<div style='display: inline-block; background-color: lightgray; "
                f"padding: 5px; margin: 5px;'>{keyword}</div>", 
                unsafe_allow_html=True
            )

def handle_blog_generation(content_chain):
    """Handle the blog content generation section of the UI."""
    st.subheader('Blog Generation')
    blog_expander = st.expander("Input the title")
    
    with blog_expander:
        blog_title = st.text_input("", key="title_of_the_blog")
        word_count = st.slider(
            'Number of Words',
            min_value=MIN_WORD_COUNT,
            max_value=MAX_WORD_COUNT,
            step=WORD_COUNT_STEP
        )
        
        handle_keyword_management()
        submit_content = st.button('Generate Blog')

        if submit_content and blog_title:
            formatted_keywords = ', '.join(
                keyword.strip() for keyword in st.session_state.get('keywords', [])
                if keyword.strip()
            )
            
            st.subheader(blog_title)
            blog_content = content_chain.invoke({
                'title': blog_title,
                'keywords': formatted_keywords,
                'blog_length': word_count
            })
            st.write(blog_content)

def main():
    """Main application entry point."""
    llm = initialize_llm()
    title_chain, content_chain = setup_langchain_components(llm)
    
    create_streamlit_ui()
    handle_title_generation(title_chain)
    handle_blog_generation(content_chain)

if __name__ == "__main__":
    main()