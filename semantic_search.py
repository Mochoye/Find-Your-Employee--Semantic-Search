"""
Semantic search functionality using sentence transformers.
"""
import numpy as np
from sentence_transformers import SentenceTransformer
import json
import pickle
import os

class SemanticSearchEngine:
    def __init__(self, model_name='all-MiniLM-L6-v2'):
        """
        Initialize the semantic search engine.
        
        Args:
            model_name: Name of the sentence transformer model to use
        """
        self.model = SentenceTransformer(model_name)
        self.resumes = None
        self.embeddings = None
        
    def load_resumes(self, filename="resumes.json"):
        """Load resumes from JSON file."""
        with open(filename, 'r') as f:
            self.resumes = json.load(f)
        return self.resumes
    
    def generate_embeddings(self, texts=None):
        """
        Generate embeddings for resume texts.
        
        Args:
            texts: List of texts to embed. If None, uses loaded resumes.
        """
        if texts is None:
            if self.resumes is None:
                raise ValueError("No resumes loaded. Call load_resumes() first.")
            texts = [resume['resume_text'] for resume in self.resumes]
        
        print(f"Generating embeddings for {len(texts)} resumes...")
        self.embeddings = self.model.encode(texts, show_progress_bar=True)
        return self.embeddings
    
    def save_embeddings(self, filename="embeddings.pkl"):
        """Save embeddings to file."""
        if self.embeddings is None:
            raise ValueError("No embeddings to save. Call generate_embeddings() first.")
        
        with open(filename, 'wb') as f:
            pickle.dump({
                'embeddings': self.embeddings,
                'resumes': self.resumes
            }, f)
        print(f"Saved embeddings to {filename}")
    
    def load_embeddings(self, filename="embeddings.pkl"):
        """Load embeddings from file."""
        with open(filename, 'rb') as f:
            data = pickle.load(f)
            self.embeddings = data['embeddings']
            self.resumes = data['resumes']
        print(f"Loaded embeddings for {len(self.resumes)} resumes")
        return self.embeddings, self.resumes
    
    def search(self, query, top_k=5):
        """
        Search for resumes matching the query.
        
        Args:
            query: Search query string
            top_k: Number of top results to return
            
        Returns:
            List of (resume, similarity_score) tuples
        """
        if self.embeddings is None or self.resumes is None:
            raise ValueError("No embeddings loaded. Call load_embeddings() or generate_embeddings() first.")
        
        # Generate query embedding
        query_embedding = self.model.encode([query])[0]
        
        # Calculate cosine similarity
        similarities = np.dot(self.embeddings, query_embedding) / (
            np.linalg.norm(self.embeddings, axis=1) * np.linalg.norm(query_embedding)
        )
        
        # Get top k indices
        top_indices = np.argsort(similarities)[::-1][:top_k]
        
        # Return results
        results = []
        for idx in top_indices:
            results.append({
                'resume': self.resumes[idx],
                'similarity': float(similarities[idx])
            })
        
        return results

def prepare_embeddings():
    """Prepare embeddings for the dataset."""
    engine = SemanticSearchEngine()
    
    # Check if embeddings already exist
    if os.path.exists('embeddings.pkl'):
        print("Embeddings already exist. Loading...")
        engine.load_embeddings()
    else:
        print("Generating new embeddings...")
        engine.load_resumes()
        engine.generate_embeddings()
        engine.save_embeddings()
    
    return engine

if __name__ == "__main__":
    # Generate data if it doesn't exist
    if not os.path.exists('resumes.json'):
        print("Generating synthetic resume data...")
        from generate_data import generate_dataset, save_dataset
        resumes = generate_dataset(100)
        save_dataset(resumes)
    
    # Prepare embeddings
    engine = prepare_embeddings()
    
    # Test search
    print("\nTesting search functionality...")
    query = "Python developer with machine learning experience"
    results = engine.search(query, top_k=3)
    
    print(f"\nTop 3 results for query: '{query}'")
    for i, result in enumerate(results, 1):
        print(f"\n{i}. {result['resume']['name']} - {result['resume']['job_title']}")
        print(f"   Similarity: {result['similarity']:.4f}")
        print(f"   Skills: {', '.join(result['resume']['skills'][:5])}...")
