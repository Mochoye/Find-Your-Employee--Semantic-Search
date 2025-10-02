# Quick Start Guide

## Option 1: Run with Full Features (Recommended)

If you have the dependencies installed or can install them:

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Generate embeddings (takes ~1-2 minutes)
python semantic_search.py

# 3. Run the Streamlit app
streamlit run app.py
```

The app will open in your browser at http://localhost:8501

## Option 2: Quick Demo (No Dependencies)

To see a simple demo without installing dependencies:

```bash
python demo.py
```

This will:
- Generate 100 synthetic resumes
- Show sample resumes
- Demonstrate basic keyword matching

## What to Expect

### Main Features:
1. **Search Interface**: Enter any job requirement or query
2. **Smart Matching**: AI-powered semantic search finds relevant candidates
3. **Visual Results**: See similarity scores and detailed candidate information
4. **PCA Visualization**: Interactive 2D plot showing how resumes cluster
5. **Similarity Distribution**: Histogram of all similarity scores

### Example Queries:
- "Python developer with machine learning experience"
- "Full stack developer with React and Node.js"
- "DevOps engineer with AWS and Kubernetes"
- "Data scientist with deep learning and PyTorch"

### Tips:
- Use the sidebar to adjust number of results (1-20)
- Toggle visualizations on/off
- Click "View Details" on any result to see full information
- Try the example query buttons for quick searches

## Troubleshooting

### Issue: Dependencies taking too long to install
Try installing just the core dependencies:
```bash
pip install streamlit sentence-transformers scikit-learn numpy pandas plotly
```

### Issue: Out of memory during embedding generation
Reduce the number of resumes in `generate_data.py` (change `num_resumes=100` to a smaller number like 50)

### Issue: Streamlit won't start
Make sure you're in the correct directory and Streamlit is installed:
```bash
cd Find-Your-Employee--Semantic-Search
streamlit --version
streamlit run app.py
```

## Understanding the Technology

### What are Embeddings?
Embeddings are numerical representations of text that capture semantic meaning. Similar text has similar embeddings, allowing us to find matches even when exact words don't match.

### What is PCA?
Principal Component Analysis reduces high-dimensional embeddings (384 dimensions) to 2D for visualization while preserving the most important information.

### What is Cosine Similarity?
A measure of similarity between two vectors (embeddings). Higher scores (closer to 1.0) mean more similar.

## Next Steps

Once you have the app running:
1. Try different queries to see how semantic search works
2. Explore the PCA visualization to understand candidate clustering
3. Check the similarity distribution to see overall match quality
4. Experiment with the number of results displayed

For production use, you would replace the synthetic data with real resumes and potentially fine-tune the model on your specific domain.
