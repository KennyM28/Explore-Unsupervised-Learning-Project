import streamlit as st
import pandas as pd
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go


# Set page configuration
st.set_page_config(
    page_title="Anime Recommender System",
    layout="wide"
)

# CSS for styling
st.markdown("""
<style>
    .header-container {
        background-color: #27a3e6;
        padding: 1rem;
        margin-bottom: 2rem;
        border-radius: 5px;
        color: white;
        text-align: center;
    }
    .stRadio > div {
        margin-top: 10px;
    }
    .anime-input-label {
        font-weight: bold;
        margin-top: 20px;
    }
    .centered-title {
        text-align: center;
    }
    .team-members-title {  
        text-align: center; 
        font-size: 1.2em;
        font-weight: bold;
        margin-bottom: 10px;
    }
    .team-members-description {
        text-align: center; 
        margin-bottom: 10px;
        font-size: 1.1em;
    }
    .team-member {
        text-align: center; 
        margin-bottom: 10px;
        font-size: 1.1em;
    }
    .role {
        text-align: center; 
        font-style: italic;
        color: #777;
        margin-left: 20px;
    }
    .project-overview-container {
        padding: 20px;
        border: 1px solid #eee;
        border-radius: 10px;
        background-color: #f9f9f9;
    }
    .key-features-description {
        margin-bottom: 5px;
        list-style-type: none; 
        margin-left: 20px; 
        text-align: center;
    }
    .key-features-title {  
        text-align: center; 
        font-size: 1.2em;
        font-weight: bold;
        margin-bottom: 10px;
    }
    .key-feature {
        margin-bottom: 5px;
        list-style-type: none; 
        margin-left: 20px; 
        text-align: center;
    }
</style>
""", unsafe_allow_html=True)

# Load the anime data from CSV - MOVED TO TOP LEVEL
@st.cache_data
def load_anime_data():
    try:
        df = pd.read_csv('anime.csv')
        
        # Convert numeric columns to appropriate data types
        # Convert episodes to numeric, errors='coerce' will set invalid values to NaN
        if 'episodes' in df.columns:
            df['episodes'] = pd.to_numeric(df['episodes'], errors='coerce')
            
        # Convert rating to numeric
        if 'rating' in df.columns:
            df['rating'] = pd.to_numeric(df['rating'], errors='coerce')
            
        # Convert members to numeric
        if 'members' in df.columns:
            df['members'] = pd.to_numeric(df['members'], errors='coerce')
            
        return df
    except FileNotFoundError:
        st.error("Anime CSV file not found. Using sample data instead.")
        # Sample data as fallback
        data = {
            "anime_id": list(range(1, 12)),
            "name": [
                "Attack on Titan", 
                "Death Note", 
                "Fullmetal Alchemist: Brotherhood", 
                "One Punch Man", 
                "My Hero Academia", 
                "Demon Slayer", 
                "Naruto", 
                "Hunter x Hunter", 
                "One Piece", 
                "Sword Art Online", 
                "Dragon Ball Z"
            ],
            "genre": [
                "Action, Drama, Fantasy", 
                "Mystery, Psychological, Thriller", 
                "Action, Adventure, Fantasy", 
                "Action, Comedy", 
                "Action, Comedy, School", 
                "Action, Demons, Historical", 
                "Action, Adventure, Martial Arts", 
                "Action, Adventure, Fantasy", 
                "Action, Adventure, Fantasy", 
                "Action, Adventure, Fantasy", 
                "Action, Adventure, Fantasy"
            ],
            "type": ["TV", "TV", "TV", "TV", "TV", "TV", "TV", "TV", "TV", "TV", "TV"],
            "episodes": [75, 37, 64, 24, 113, 26, 220, 148, 1000, 96, 291],
            "rating": [8.53, 8.62, 9.11, 8.71, 8.12, 8.92, 7.98, 9.05, 8.54, 7.29, 8.15],
            "members": [200000, 300000, 400000, 250000, 180000, 190000, 350000, 280000, 450000, 320000, 290000]
        }
        return pd.DataFrame(data)

# Load the data
anime_df = load_anime_data()

# Get list of anime names for the dropdown
anime_list = anime_df['name'].tolist()

# Header
st.markdown('<div class="header-container"><h1>Anime Recommender System</h1></div>', unsafe_allow_html=True)

# Tabs
tab1, tab2, tab3, tab4 = st.tabs(["Team Info", "Project Overview", "Visualizations", "Anime Recommender"])

# Tab 1: Team Info
with tab1:
    st.markdown("<h1 class='centered-title'>Team Information</h1>", unsafe_allow_html=True)
    
    st.markdown("<div class='team-members-description'>We are a team of data science enthusiasts passionate about leveraging machine learning for anime recommendations.</div>", unsafe_allow_html=True) 

    st.markdown("<div class='team-members-title'>Team Members and Roles:</div>", unsafe_allow_html=True) 

    team_members = [
        {"name": "Kennety Mashishi", "role": "Role"},
        {"name": "Gaba Keefelakae", "role": "Role"},
        {"name": "Wanga Maswime", "role": "Role"},
        {"name": "Nokulinda Mthimunye", "role": "Role"},
    ]

    for member in team_members:
        st.markdown(f"<div class='team-member'>{member['name']} <span class='role'>({member['role']})</span></div>", unsafe_allow_html=True)

# Tab 2: Project Overview
with tab2:
    st.markdown("<h1 class='centered-title'>Project Overview</h1>", unsafe_allow_html=True)
    
    st.markdown("<div class='key-features-description'>This project aims to develop an anime recommendation system using multiple machine learning approaches. The goal is to accurately suggest anime based on user preferences, providing a valuable tool for anime discovery.</div>", unsafe_allow_html=True) 

    st.markdown("<br><div class='key-features-title'>Key Features:</div>", unsafe_allow_html=True) 

    st.markdown("""
    <ul class="key-feature">
        <li class="key-feature">Multiple recommendation algorithms: Content-Based Filtering and Collaborative Filtering.</li>
        <li class="key-feature">User-friendly Streamlit interface.</li>
        <li class="key-feature">Anime recommendations based on user favorites.</li>
        <li class="key-feature">Techniques used: NLP, similarity metrics, and collaborative filtering methods.</li>
    </ul>
    """, unsafe_allow_html=True)

     # Data description
    st.markdown("<br><div class='key-features-title'>Dataset Information:</div>", unsafe_allow_html=True)
    
    st.markdown("""
    <div class="key-features-description">
    Our anime recommendation system is built using a dataset that contains the following information:
    </div>
    """, unsafe_allow_html=True)
    
    data_fields = {
        "Field": ["anime_id", "name", "genre", "type", "episodes", "rating", "members"],
        "Description": [
            "Unique identifier for each anime",
            "Title of the anime",
            "Comma-separated list of genres",
            "TV, Movie, etc.",
            "Number of episodes (1 for movies)",
            "Average user rating (1-10)",
            "Number of community members that are in this anime's group"
        ]
    }
    
    df_fields = pd.DataFrame(data_fields)
    st.table(df_fields)
    
    # Project workflow
    st.markdown("<br><div class='key-features-title'>Project Workflow:</div>", unsafe_allow_html=True)
    
    st.markdown("""
    <ul class="key-feature">
        <li class="key-feature">Data Collection: Gathering anime data.</li>
        <li class="key-feature">Data Preprocessing: Cleaning and transforming raw data for modeling.</li>
        <li class="key-feature">Model Development: Implementing collaborative and content-based filtering algorithms.</li>
        <li class="key-feature">Model Evaluation: Assessing recommendation accuracy with metrics like RMSE and MAE.</li>
        <li class="key-feature">System Integration: Creating a user-friendly interface with Streamlit.</li>
    </ul>
    """, unsafe_allow_html=True)

# Tab 3: Visualizations
with tab3:
    st.markdown("<h1 class='centered-title'>Anime Insights</h1>", unsafe_allow_html=True)
    
    # Check if we have the necessary columns for visualizations
    required_columns = ["rating", "members", "type", "episodes", "genre"]
    missing_columns = [col for col in required_columns if col not in anime_df.columns]
    
    if missing_columns:
        st.error(f"Missing columns in dataset: {', '.join(missing_columns)}. Some visualizations may not be available.")
    
    # Top Rated Anime
    if "rating" in anime_df.columns:
        st.subheader("Top Rated Anime")
        top_rated = anime_df.sort_values(by="rating", ascending=False).head(10)
        
        fig = px.bar(
            top_rated, 
            x="name", 
            y="rating",
            title="Top 10 Highest Rated Anime",
            labels={"name": "Anime Title", "rating": "Rating (out of 10)"},
            color="rating",
            color_continuous_scale=px.colors.sequential.Reds
        )
        fig.update_layout(xaxis_tickangle=-45)
        st.plotly_chart(fig, use_container_width=True)
    
    # Most Popular Anime by Members
    if "members" in anime_df.columns:
        st.subheader("Most Popular Anime")
        most_popular = anime_df.sort_values(by="members", ascending=False).head(10)
        
        fig = px.bar(
            most_popular, 
            x="name", 
            y="members",
            title="Top 10 Most Popular Anime by Membership",
            labels={"name": "Anime Title", "members": "Number of Members"},
            color="members",
            color_continuous_scale=px.colors.sequential.Blues
        )
        fig.update_layout(xaxis_tickangle=-45)
        st.plotly_chart(fig, use_container_width=True)
    
    # Distribution visualizations in two columns
    col1, col2 = st.columns(2)
    
    with col1:
        # Rating Distribution
        if "rating" in anime_df.columns:
            st.subheader("Rating Distribution")
            fig = px.histogram(
                anime_df,
                x="rating",
                nbins=20,
                title="Distribution of Anime Ratings",
                labels={"rating": "Rating"},
                color_discrete_sequence=["#ff6b6b"]
            )
            st.plotly_chart(fig, use_container_width=True)
        
        # Type Distribution
        if "type" in anime_df.columns:
            st.subheader("Anime Types")
            type_counts = anime_df["type"].value_counts().reset_index()
            type_counts.columns = ["Type", "Count"]
            
            fig = px.pie(
                type_counts, 
                values="Count", 
                names="Type",
                title="Distribution of Anime Types",
                color_discrete_sequence=px.colors.qualitative.Set3
            )
            st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        # Episodes Distribution
        if "episodes" in anime_df.columns:
            st.subheader("Episodes Distribution")

            episodes_df = anime_df[anime_df["episodes"] <= anime_df["episodes"].quantile(0.99)]
            
            fig = px.histogram(
                episodes_df,
                x="episodes",
                nbins=30,
                title="Distribution of Episode Counts",
                labels={"episodes": "Number of Episodes"},
                color_discrete_sequence=["#5c7cfa"]
            )
            st.plotly_chart(fig, use_container_width=True)
        
        # Members Distribution
        if "members" in anime_df.columns:
            st.subheader("Popularity Distribution")

            fig = px.histogram(
                anime_df,
                x="members",
                nbins=30,
                title="Distribution of Anime Popularity",
                labels={"members": "Number of Members (log scale)"},
                color_discrete_sequence=["#20c997"],
                log_x=True  # Use log scale for x-axis
            )
            st.plotly_chart(fig, use_container_width=True)
    
    # Genre Analysis
    if "genre" in anime_df.columns:
        st.subheader("Top Anime Genres")
        

        all_genres = []
        for genres in anime_df["genre"].dropna().str.split(", "):
            if isinstance(genres, list):
                all_genres.extend(genres)
        
        # Count genre frequencies
        genre_counts = pd.Series(all_genres).value_counts().reset_index().head(15)
        genre_counts.columns = ["Genre", "Count"]
        
        fig = px.bar(
            genre_counts, 
            x="Genre", 
            y="Count",
            title="Top 15 Anime Genres",
            color="Count",
            color_continuous_scale=px.colors.sequential.Viridis
        )
        fig.update_layout(xaxis_tickangle=-45)
        st.plotly_chart(fig, use_container_width=True)
    
    # Scatter plot showing relationship between ratings and popularity
    if all(col in anime_df.columns for col in ["rating", "members"]):
        st.subheader("Rating vs. Popularity")
        
        fig = px.scatter(
            anime_df,
            x="members",
            y="rating",
            title="Relationship Between Popularity and Rating",
            labels={"members": "Number of Members (log scale)", "rating": "Rating"},
            opacity=0.6,
            color="rating",
            color_continuous_scale=px.colors.sequential.Plasma,
            hover_name="name",
            log_x=True  # Use log scale for x-axis
        )
        st.plotly_chart(fig, use_container_width=True)
        
        st.markdown("""
        <div style="text-align: center; padding: 10px; background-color: #f8f9fa; border-radius: 5px;">
            <p>This visualization shows the relationship between an anime's popularity (member count) and its rating. 
            Each point represents an anime title, and the color indicates its rating.</p>
        </div>
        """, unsafe_allow_html=True)


# Tab 4: Anime Recommender
with tab4:
    st.subheader("Find Your Next Favorite Anime")
    
    # Algorithm selection
    st.write("Select an algorithm")
    recommendation_algorithm = st.radio(
        label="",
        options=["Content Based Filtering", "Collaborative Based Filtering"],
        index=0,
        label_visibility="collapsed"
    )

    # Anime input section
    st.markdown("<h3>Enter Your Three Favorite Anime</h3>", unsafe_allow_html=True)

    # Anime selection dropdowns
    st.markdown('<p class="anime-input-label">First Option</p>', unsafe_allow_html=True)
    anime1 = st.selectbox(
        label="First anime",
        options=anime_list,
        index=0,
        label_visibility="collapsed"
    )

    st.markdown('<p class="anime-input-label">Second Option</p>', unsafe_allow_html=True)
    anime2 = st.selectbox(
        label="Second anime",
        options=anime_list,
        index=1 if len(anime_list) > 1 else 0,
        label_visibility="collapsed"
    )

    st.markdown('<p class="anime-input-label">Third Option</p>', unsafe_allow_html=True)
    anime3 = st.selectbox(
        label="Third anime",
        options=anime_list,
        index=2 if len(anime_list) > 2 else 0,
        label_visibility="collapsed"
    )
 

    # Recommendation button
    if st.button("Recommend"):
        st.write("### Recommended Anime")

        # Model Placeholder ########
        st.write(f"Selected anime: {anime1}, {anime2}, {anime3}")
        
        # Content Based Filtering
        if recommendation_algorithm == "Content Based Filtering":
            st.write("Based on content similarity, we recommend:")
            recommendations = [
                "Jujutsu Kaisen",
                "Vinland Saga",
                "Chainsaw Man"
            ]
        else:  # Collaborative filtering
            st.write("Based on what similar users liked, we recommend:")
            recommendations = [
                "Steins;Gate",
                "Code Geass",
                "Cowboy Bebop"
            ]
        
        # Display recommendations
        for i, anime in enumerate(recommendations, 1):
            st.write(f"{i}. {anime}")