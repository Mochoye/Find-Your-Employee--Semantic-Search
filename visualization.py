"""
PCA visualization module for embeddings.
"""
import numpy as np
from sklearn.decomposition import PCA
import plotly.graph_objects as go
import plotly.express as px

def create_pca_visualization(embeddings, resumes, query_embedding=None, query_text=None, top_indices=None):
    """
    Create a 2D PCA visualization of resume embeddings.
    
    Args:
        embeddings: Array of resume embeddings
        resumes: List of resume dictionaries
        query_embedding: Optional query embedding to plot
        query_text: Text of the query
        top_indices: Indices of top matching resumes to highlight
        
    Returns:
        Plotly figure object
    """
    # Perform PCA to reduce to 2 dimensions
    pca = PCA(n_components=2)
    
    # Include query embedding if provided
    if query_embedding is not None:
        all_embeddings = np.vstack([embeddings, query_embedding.reshape(1, -1)])
        embeddings_2d = pca.fit_transform(all_embeddings)
        query_point = embeddings_2d[-1]
        embeddings_2d = embeddings_2d[:-1]
    else:
        embeddings_2d = pca.fit_transform(embeddings)
        query_point = None
    
    # Prepare data for plotting
    x_coords = embeddings_2d[:, 0]
    y_coords = embeddings_2d[:, 1]
    
    # Create hover text
    hover_texts = []
    for resume in resumes:
        hover_text = (
            f"<b>{resume['name']}</b><br>"
            f"Title: {resume['job_title']}<br>"
            f"Experience: {resume['years_experience']} years<br>"
            f"Top Skills: {', '.join(resume['skills'][:3])}"
        )
        hover_texts.append(hover_text)
    
    # Determine colors and sizes
    colors = ['lightblue'] * len(resumes)
    sizes = [8] * len(resumes)
    
    if top_indices is not None:
        for idx in top_indices:
            colors[idx] = 'orange'
            sizes[idx] = 12
    
    # Create scatter plot
    fig = go.Figure()
    
    # Add resume points
    fig.add_trace(go.Scatter(
        x=x_coords,
        y=y_coords,
        mode='markers',
        marker=dict(
            size=sizes,
            color=colors,
            line=dict(width=1, color='DarkSlateGray'),
            opacity=0.7
        ),
        text=hover_texts,
        hovertemplate='%{text}<extra></extra>',
        name='Resumes'
    ))
    
    # Add query point if provided
    if query_point is not None:
        fig.add_trace(go.Scatter(
            x=[query_point[0]],
            y=[query_point[1]],
            mode='markers',
            marker=dict(
                size=15,
                color='red',
                symbol='star',
                line=dict(width=2, color='darkred')
            ),
            text=[f"Query: {query_text}"],
            hovertemplate='%{text}<extra></extra>',
            name='Query'
        ))
    
    # Update layout
    fig.update_layout(
        title={
            'text': 'Resume Embeddings - PCA Visualization',
            'x': 0.5,
            'xanchor': 'center'
        },
        xaxis_title=f'Principal Component 1 ({pca.explained_variance_ratio_[0]:.1%} variance)',
        yaxis_title=f'Principal Component 2 ({pca.explained_variance_ratio_[1]:.1%} variance)',
        hovermode='closest',
        plot_bgcolor='white',
        height=600,
        showlegend=True
    )
    
    # Add grid
    fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='lightgray')
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='lightgray')
    
    return fig

def create_similarity_distribution(similarities):
    """
    Create a histogram of similarity scores.
    
    Args:
        similarities: Array of similarity scores
        
    Returns:
        Plotly figure object
    """
    fig = go.Figure()
    
    fig.add_trace(go.Histogram(
        x=similarities,
        nbinsx=30,
        marker_color='lightblue',
        marker_line_color='darkblue',
        marker_line_width=1
    ))
    
    fig.update_layout(
        title='Distribution of Similarity Scores',
        xaxis_title='Similarity Score',
        yaxis_title='Count',
        plot_bgcolor='white',
        height=400
    )
    
    fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='lightgray')
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='lightgray')
    
    return fig
