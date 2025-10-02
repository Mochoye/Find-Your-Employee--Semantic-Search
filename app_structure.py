"""
Create a visual representation of the app structure for documentation.
"""

APP_STRUCTURE = """
╔══════════════════════════════════════════════════════════════════════════════╗
║                                                                              ║
║                     🔍 Find Your Employee                                    ║
║                                                                              ║
║          Semantic Resume Search with AI-powered matching                    ║
║                                                                              ║
╠══════════════════════════════════════════════════════════════════════════════╣
║                                                                              ║
║  ✅ Loaded 100 resumes                                                       ║
║                                                                              ║
║  ┌────────────────────────────────────────────────────────────────────────┐ ║
║  │                      🔎 Search for Candidates                          │ ║
║  ├────────────────────────────────────────────────────────────────────────┤ ║
║  │                                                                        │ ║
║  │  [🐍 Python Developer] [🤖 Machine Learning] [☁️ Cloud Engineer]      │ ║
║  │                                                                        │ ║
║  │  Enter your job requirements:                                         │ ║
║  │  ┌──────────────────────────────────────────────────────────────────┐ │ ║
║  │  │ Python developer with machine learning experience              │ │ ║
║  │  └──────────────────────────────────────────────────────────────────┘ │ ║
║  │                                                                        │ ║
║  │                         [🚀 Search]                                    │ ║
║  └────────────────────────────────────────────────────────────────────────┘ ║
║                                                                              ║
║  ┌────────────────────────────────────────────────────────────────────────┐ ║
║  │                      📊 Search Results                                 │ ║
║  ├────────────────────────────────────────────────────────────────────────┤ ║
║  │                                                                        │ ║
║  │  Average Similarity Score: 0.73                                       │ ║
║  │                                                                        │ ║
║  │  ┌──────────────────────────────────────────────────────────────────┐ │ ║
║  │  │ #1 - Candidate 42                                                │ │ ║
║  │  │ Job Title: Machine Learning Engineer                             │ │ ║
║  │  │ Years of Experience: 5                                           │ │ ║
║  │  │ [Similarity: 85%]                                                │ │ ║
║  │  │ ▼ View Details                                                   │ │ ║
║  │  └──────────────────────────────────────────────────────────────────┘ │ ║
║  │                                                                        │ ║
║  │  ┌──────────────────────────────────────────────────────────────────┐ │ ║
║  │  │ #2 - Candidate 17                                                │ │ ║
║  │  │ Job Title: Data Scientist                                        │ │ ║
║  │  │ Years of Experience: 7                                           │ │ ║
║  │  │ [Similarity: 78%]                                                │ │ ║
║  │  │ ▼ View Details                                                   │ │ ║
║  │  └──────────────────────────────────────────────────────────────────┘ │ ║
║  │                                                                        │ ║
║  │  ... (more results)                                                   │ ║
║  │                                                                        │ ║
║  │  ┌────────────────────────────────────────────────────────────────┐   │ ║
║  │  │       PCA Visualization Tab (Interactive Plot)                 │   │ ║
║  │  │                                                                │   │ ║
║  │  │        ⭐ Query                                                 │   │ ║
║  │  │        🟠 Top Matches                                          │   │ ║
║  │  │        🔵 Other Resumes                                        │   │ ║
║  │  │                                                                │   │ ║
║  │  │           [Interactive 2D Scatter Plot Here]                   │   │ ║
║  │  │                                                                │   │ ║
║  │  └────────────────────────────────────────────────────────────────┘   │ ║
║  └────────────────────────────────────────────────────────────────────────┘ ║
║                                                                              ║
╠═══════════════════════════════════════════════════════════════╦══════════════╣
║                        SIDEBAR                                 ║              ║
║  ⚙️ Search Settings                                           ║              ║
║  ─────────────────────                                        ║              ║
║  Number of results: [━━━●━━━━━━] 5                           ║              ║
║  ☑ Show PCA Visualization                                    ║              ║
║  ☐ Show Similarity Distribution                              ║              ║
║  ───────────────────────────────────────────                 ║              ║
║  ℹ️ About                                                     ║              ║
║  This app uses semantic search to find                       ║              ║
║  the most relevant resumes based on                          ║              ║
║  your job query. It employs:                                 ║              ║
║  • Sentence Transformers for embeddings                      ║              ║
║  • Cosine Similarity for matching                            ║              ║
║  • PCA for visualization                                     ║              ║
║                                                               ║              ║
║  Note: This demo uses synthetic data.                        ║              ║
╚═══════════════════════════════════════════════════════════════╩══════════════╝

Key Features:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. SEARCH INTERFACE
   • Quick example buttons for common queries
   • Free-text search input
   • Real-time semantic matching

2. RESULTS DISPLAY
   • Ranked by similarity score
   • Expandable details for each candidate
   • Clean, card-based layout

3. VISUALIZATIONS
   • Interactive PCA plot showing embedding space
   • Query shown as red star
   • Top matches highlighted in orange
   • Hover for detailed information

4. SIDEBAR CONTROLS
   • Adjust number of results (1-20)
   • Toggle visualization options
   • App information and tips

5. METRICS
   • Average similarity score
   • Distribution of scores
   • Explained variance for PCA
"""

if __name__ == "__main__":
    print(APP_STRUCTURE)
