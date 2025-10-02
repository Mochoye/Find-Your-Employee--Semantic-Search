# Find Your Employee - Semantic Search 🔍

A Streamlit app that matches job queries to the most relevant resumes using embeddings and PCA visualization (demo trained on synthetic data).

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28.0-red.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

## 🌟 Features

- **Semantic Search**: Uses sentence transformers to understand the meaning of job queries and match them to relevant resumes
- **AI-Powered Matching**: Employs cosine similarity on embeddings for accurate candidate matching
- **PCA Visualization**: Interactive 2D visualization of resume embeddings using Principal Component Analysis
- **Synthetic Data**: Comes with 100 pre-generated synthetic resumes for demonstration
- **Interactive UI**: Clean and intuitive Streamlit interface with real-time search
- **Similarity Metrics**: Visual distribution of similarity scores across all candidates

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- pip

### Installation

1. Clone the repository:
```bash
git clone https://github.com/Mochoye/Find-Your-Employee--Semantic-Search.git
cd Find-Your-Employee--Semantic-Search
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Generate synthetic data and embeddings:
```bash
python semantic_search.py
```

4. Run the Streamlit app:
```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`

## 📖 How It Works

### 1. Data Generation
The app generates 100 synthetic resumes with realistic:
- Job titles (Software Engineer, Data Scientist, etc.)
- Skills (Python, AWS, React, etc.)
- Experience descriptions
- Education backgrounds
- Years of experience

### 2. Embedding Generation
- Uses the `all-MiniLM-L6-v2` sentence transformer model
- Converts resume text into 384-dimensional embeddings
- Embeddings capture semantic meaning of resumes

### 3. Semantic Search
- User enters a job query (e.g., "Python developer with ML experience")
- Query is converted to an embedding using the same model
- Cosine similarity is calculated between query and all resume embeddings
- Top-k most similar resumes are returned

### 4. Visualization
- **PCA Visualization**: Projects high-dimensional embeddings to 2D space
- Query shown as red star, top matches highlighted in orange
- Interactive plot with hover information
- Shows distribution of candidates in semantic space

## 💡 Usage Examples

Try these example queries:

1. **"Python developer with machine learning experience"**
   - Finds candidates with Python and ML skills

2. **"Full stack developer with React and Node.js"**
   - Matches frontend and backend developers

3. **"DevOps engineer with AWS and Kubernetes"**
   - Finds cloud infrastructure specialists

4. **"Data scientist with deep learning and PyTorch"**
   - Matches AI/ML researchers

## 🛠️ Project Structure

```
Find-Your-Employee--Semantic-Search/
├── app.py                  # Main Streamlit application
├── generate_data.py        # Synthetic resume generation
├── semantic_search.py      # Search engine implementation
├── visualization.py        # PCA and plotting functions
├── requirements.txt        # Python dependencies
├── .gitignore             # Git ignore file
└── README.md              # This file
```

## 🔧 Configuration

You can customize the search engine by modifying:

- **Model**: Change the sentence transformer model in `semantic_search.py`
- **Data Size**: Adjust `num_resumes` in `generate_data.py`
- **Search Results**: Use the sidebar slider in the app to change number of results
- **Visualization**: Toggle PCA and distribution plots in the sidebar

## 📊 Technical Details

### Models Used
- **Sentence Transformer**: `all-MiniLM-L6-v2`
  - 384-dimensional embeddings
  - Fast and efficient
  - Good balance of speed and accuracy

### Algorithms
- **Similarity**: Cosine similarity
- **Dimensionality Reduction**: PCA (Principal Component Analysis)
- **Visualization**: Plotly for interactive charts

### Performance
- Embedding generation: ~5 seconds for 100 resumes
- Search query: <1 second
- Visualization: ~1 second

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📝 License

This project is licensed under the MIT License.

## 🙏 Acknowledgments

- [Sentence Transformers](https://www.sbert.net/) for the embedding models
- [Streamlit](https://streamlit.io/) for the awesome web framework
- [Plotly](https://plotly.com/) for interactive visualizations

## 📧 Contact

For questions or feedback, please open an issue on GitHub.

---

**Note**: This is a demonstration project using synthetic data. For production use, you would need to:
- Use real resume data
- Implement proper data privacy measures
- Add authentication and authorization
- Scale the backend for larger datasets
- Fine-tune the model on domain-specific data
