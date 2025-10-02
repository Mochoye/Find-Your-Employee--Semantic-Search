"""
Streamlit app for semantic resume search with PCA visualization.
"""
import streamlit as st
import numpy as np
import os
from semantic_search import SemanticSearchEngine
from visualization import create_pca_visualization, create_similarity_distribution

# Page configuration
st.set_page_config(
    page_title="Find Your Employee - Semantic Search",
    page_icon="🔍",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        text-align: center;
        color: #1f77b4;
        margin-bottom: 1rem;
    }
    .sub-header {
        font-size: 1.2rem;
        text-align: center;
        color: #666;
        margin-bottom: 2rem;
    }
    .result-card {
        background-color: #f8f9fa;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 5px solid #1f77b4;
        margin-bottom: 1rem;
    }
    .similarity-badge {
        background-color: #28a745;
        color: white;
        padding: 0.3rem 0.8rem;
        border-radius: 15px;
        font-weight: bold;
        display: inline-block;
        margin-top: 0.5rem;
    }
</style>
""", unsafe_allow_html=True)

@st.cache_resource
def load_search_engine():
    """Load the search engine (cached)."""
    engine = SemanticSearchEngine()
    
    # Check if data exists
    if not os.path.exists('embeddings.pkl'):
        st.warning("Embeddings not found. Generating synthetic data and embeddings...")
        
        # Generate data if needed
        if not os.path.exists('resumes.json'):
            from generate_data import generate_dataset, save_dataset
            resumes = generate_dataset(100)
            save_dataset(resumes)
            st.success("Generated 100 synthetic resumes!")
        
        # Generate embeddings
        engine.load_resumes()
        engine.generate_embeddings()
        engine.save_embeddings()
        st.success("Embeddings generated and saved!")
    else:
        engine.load_embeddings()
    
    return engine

def display_resume(resume, rank, similarity):
    """Display a single resume result."""
    with st.container():
        st.markdown(f"""
        <div class="result-card">
            <h3>#{rank} - {resume['name']}</h3>
            <p><strong>Job Title:</strong> {resume['job_title']}</p>
            <p><strong>Years of Experience:</strong> {resume['years_experience']}</p>
            <span class="similarity-badge">Similarity: {similarity:.2%}</span>
        </div>
        """, unsafe_allow_html=True)
        
        with st.expander("View Details"):
            col1, col2 = st.columns(2)
            
            with col1:
                st.write("**Skills:**")
                for skill in resume['skills']:
                    st.write(f"- {skill}")
            
            with col2:
                st.write("**Experience:**")
                for exp in resume['experience']:
                    st.write(f"- {exp}")
            
            st.write("**Education:**")
            st.write(resume['education'])

def main():
    # Header
    st.markdown('<div class="main-header">🔍 Find Your Employee</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-header">Semantic Resume Search with AI-powered matching</div>', unsafe_allow_html=True)
    
    # Load search engine
    with st.spinner("Loading search engine..."):
        engine = load_search_engine()
    
    st.success(f"✅ Loaded {len(engine.resumes)} resumes")
    
    # Sidebar for configuration
    with st.sidebar:
        st.header("⚙️ Search Settings")
        
        num_results = st.slider(
            "Number of results",
            min_value=1,
            max_value=20,
            value=5,
            help="Number of top matching resumes to display"
        )
        
        show_visualization = st.checkbox(
            "Show PCA Visualization",
            value=True,
            help="Display 2D visualization of embeddings using PCA"
        )
        
        show_distribution = st.checkbox(
            "Show Similarity Distribution",
            value=False,
            help="Display histogram of similarity scores"
        )
        
        st.divider()
        
        st.header("ℹ️ About")
        st.info(
            """
            This app uses semantic search to find the most relevant resumes 
            based on your job query. It employs:
            
            - **Sentence Transformers** for embeddings
            - **Cosine Similarity** for matching
            - **PCA** for visualization
            
            *Note: This demo uses synthetic data for demonstration purposes.*
            """
        )
    
    # Search interface
    st.header("🔎 Search for Candidates")
    
    # Example queries
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("🐍 Python Developer"):
            st.session_state.query = "Python developer with backend experience"
    with col2:
        if st.button("🤖 Machine Learning"):
            st.session_state.query = "Machine learning engineer with deep learning experience"
    with col3:
        if st.button("☁️ Cloud Engineer"):
            st.session_state.query = "DevOps engineer with AWS and Kubernetes experience"
    
    # Query input
    query = st.text_input(
        "Enter your job requirements:",
        value=st.session_state.get('query', ''),
        placeholder="e.g., 'Full stack developer with React and Python experience'",
        help="Describe the ideal candidate or job requirements"
    )
    
    if query:
        st.session_state.query = query
        
        # Search button
        if st.button("🚀 Search", type="primary"):
            with st.spinner("Searching for matching candidates..."):
                # Perform search
                results = engine.search(query, top_k=num_results)
                
                # Store results in session state
                st.session_state.results = results
                st.session_state.current_query = query
        
        # Display results if available
        if 'results' in st.session_state and st.session_state.current_query == query:
            results = st.session_state.results
            
            st.divider()
            st.header("📊 Search Results")
            
            # Display search summary
            avg_similarity = np.mean([r['similarity'] for r in results])
            st.metric(
                "Average Similarity Score",
                f"{avg_similarity:.2%}",
                help="Average cosine similarity of top results"
            )
            
            # Create tabs for results and visualization
            if show_visualization or show_distribution:
                tab_names = ["Results"]
                if show_visualization:
                    tab_names.append("PCA Visualization")
                if show_distribution:
                    tab_names.append("Similarity Distribution")
                
                tabs = st.tabs(tab_names)
                
                # Results tab
                with tabs[0]:
                    for i, result in enumerate(results, 1):
                        display_resume(result['resume'], i, result['similarity'])
                
                # Visualization tab
                current_tab = 1
                if show_visualization:
                    with tabs[current_tab]:
                        st.subheader("2D PCA Visualization of Resume Embeddings")
                        st.write(
                            "This visualization shows how resumes are distributed in a 2D space. "
                            "The query is shown as a red star, and top matches are highlighted in orange."
                        )
                        
                        # Generate query embedding
                        query_embedding = engine.model.encode([query])[0]
                        
                        # Get top indices
                        top_indices = [engine.resumes.index(r['resume']) for r in results]
                        
                        # Create visualization
                        fig = create_pca_visualization(
                            engine.embeddings,
                            engine.resumes,
                            query_embedding=query_embedding,
                            query_text=query,
                            top_indices=top_indices
                        )
                        
                        st.plotly_chart(fig, use_container_width=True)
                    current_tab += 1
                
                # Distribution tab
                if show_distribution:
                    with tabs[current_tab]:
                        st.subheader("Similarity Score Distribution")
                        st.write("Distribution of cosine similarity scores across all resumes.")
                        
                        # Calculate all similarities
                        query_embedding = engine.model.encode([query])[0]
                        similarities = np.dot(engine.embeddings, query_embedding) / (
                            np.linalg.norm(engine.embeddings, axis=1) * np.linalg.norm(query_embedding)
                        )
                        
                        fig = create_similarity_distribution(similarities)
                        st.plotly_chart(fig, use_container_width=True)
            else:
                # Just display results
                for i, result in enumerate(results, 1):
                    display_resume(result['resume'], i, result['similarity'])
    else:
        # Show welcome message
        st.info(
            """
            👋 Welcome! Start by entering a job query above or click one of the example buttons.
            
            **Tips for better results:**
            - Be specific about required skills and technologies
            - Mention years of experience if relevant
            - Include both technical and soft skills
            - Describe the role or responsibilities
            """
        )

if __name__ == "__main__":
    main()
