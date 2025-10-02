"""
Demo script to test the semantic search functionality without Streamlit.
"""
import json
import os

def demo_without_embeddings():
    """Demo using just the data generation."""
    print("=" * 60)
    print("SEMANTIC SEARCH DEMO - DATA GENERATION")
    print("=" * 60)
    
    # Check if data exists
    if not os.path.exists('resumes.json'):
        print("\n1. Generating synthetic resumes...")
        from generate_data import generate_dataset, save_dataset
        resumes = generate_dataset(100)
        save_dataset(resumes)
    else:
        print("\n1. Loading existing resumes...")
        with open('resumes.json', 'r') as f:
            resumes = json.load(f)
    
    print(f"   ✓ Loaded {len(resumes)} resumes")
    
    # Show sample resumes
    print("\n2. Sample Resumes:")
    print("-" * 60)
    for i in range(3):
        resume = resumes[i]
        print(f"\n   Resume #{i+1}:")
        print(f"   Name: {resume['name']}")
        print(f"   Job Title: {resume['job_title']}")
        print(f"   Years of Experience: {resume['years_experience']}")
        print(f"   Top Skills: {', '.join(resume['skills'][:5])}")
    
    # Simple keyword matching demo
    print("\n3. Simple Keyword Matching Demo:")
    print("-" * 60)
    
    query = "Python developer"
    print(f"\n   Query: '{query}'")
    print("\n   Matching resumes (by keyword):")
    
    matches = []
    for resume in resumes:
        # Simple keyword matching
        resume_text = resume['resume_text'].lower()
        if 'python' in resume_text:
            matches.append(resume)
    
    for i, resume in enumerate(matches[:5], 1):
        print(f"   {i}. {resume['name']} - {resume['job_title']}")
    
    print(f"\n   Found {len(matches)} resumes mentioning 'Python'")
    
    print("\n" + "=" * 60)
    print("To run the full semantic search with embeddings:")
    print("1. Install dependencies: pip install -r requirements.txt")
    print("2. Generate embeddings: python semantic_search.py")
    print("3. Run the app: streamlit run app.py")
    print("=" * 60)

if __name__ == "__main__":
    demo_without_embeddings()
