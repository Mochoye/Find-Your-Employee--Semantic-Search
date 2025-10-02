import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from sklearn.decomposition import PCA
from sklearn.neighbors import DistanceMetric
from sentence_transformers import SentenceTransformer

# Load embedding model once
@st.cache_resource
def load_model():
    return SentenceTransformer("all-MiniLM-L6-v2")

model = load_model()

st.title("🔎 Resume Search & Visualization App")

# File uploader
uploaded_file = st.file_uploader("Upload a CSV file with `resume` and `role` columns", type=["csv"])

if uploaded_file:
    df_resume = pd.read_csv(uploaded_file)

    if "resume" not in df_resume.columns or "role" not in df_resume.columns:
        st.error("❌ CSV must contain columns: `resume` and `role`")
    else:
        # Embed resumes
        with st.spinner("Generating embeddings..."):
            embedding_arr = model.encode(df_resume['resume'])
        
        # Fit PCA
        pca = PCA(n_components=2).fit(embedding_arr)
        
        # Query input
        query = st.text_input("Enter your job query", "I need someone to build out my data infrastructure")
        
        if st.button("Search"):
            query_embedding = model.encode(query)
            dist = DistanceMetric.get_metric('euclidean')
            dist_arr = dist.pairwise(embedding_arr, query_embedding.reshape(1, -1)).flatten()
            idist_arr_sorted = np.argsort(dist_arr)

            st.subheader("📌 Top 10 Matching Roles")
            st.write(df_resume[['role', 'resume']].iloc[idist_arr_sorted[:10]])

            st.subheader("📄 Best Match Resume")
            st.info(df_resume['resume'].iloc[idist_arr_sorted[0]])

            # PCA plot
            query_pca = pca.transform(query_embedding.reshape(1, -1))[0]

            fig, ax = plt.subplots(figsize=(8, 6))
            plt.grid(True)
            c = 0
            cmap = mpl.colormaps['jet']
            for role in df_resume['role'].unique():
                idx = np.where(df_resume['role'] == role)
                ax.scatter(pca.transform(embedding_arr)[idx, 0],
                           pca.transform(embedding_arr)[idx, 1],
                           c=[cmap(c)] * len(idx[0]), label=role)
                c += 1 / len(df_resume['role'].unique())

            ax.scatter(query_pca[0], query_pca[1], c='k', marker='*', s=300, label="query")
            ax.set_xlabel("PC 1")
            ax.set_ylabel("PC 2")
            ax.set_title(f'"{query}"')
            ax.legend(bbox_to_anchor=(1.05, 0.9))
            st.pyplot(fig)
