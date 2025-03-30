import streamlit as st
import pandas as pd

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

# Header
st.markdown('<div class="header-container"><h1>Anime Recommender System</h1></div>', unsafe_allow_html=True)

# Tabs
tab1, tab2, tab3 = st.tabs(["Team Info", "Project Overview", "Anime Recommender"])

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


# Tab 3: Anime Recommender
with tab3:
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

    # Anime List
    anime_list = [
        "Attack on Titan (2013)",
        "Death Note (2006)",
        "Fullmetal Alchemist: Brotherhood (2009)",
        "One Punch Man (2015)",
        "My Hero Academia (2016)",
        "Demon Slayer (2019)",
        "Naruto (2002)",
        "Hunter x Hunter (2011)",
        "One Piece (1999)",
        "Sword Art Online (2012)",
        "Dragon Ball Z (1989)"
    ]

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
        index=1,
        label_visibility="collapsed"
    )

    st.markdown('<p class="anime-input-label">Third Option</p>', unsafe_allow_html=True)
    anime3 = st.selectbox(
        label="Third anime",
        options=anime_list,
        index=2,
        label_visibility="collapsed"
    )

    # Recommendation button
    if st.button("Recommend"):
        st.write("### Recommended Anime")
        
        # Content Based Filtering
        if recommendation_algorithm == "Content Based Filtering":
            st.write("Based on content similarity, we recommend:")
            recommendations = [
                "Jujutsu Kaisen (2020)",
                "Vinland Saga (2019)",
                "Chainsaw Man (2022)"
            ]
        else:  # Collaborative filtering
            st.write("Based on what similar users liked, we recommend:")
            recommendations = [
                "Steins;Gate (2011)",
                "Code Geass (2006)",
                "Cowboy Bebop (1998)"
            ]
        
        # Display recommendations
        for i, anime in enumerate(recommendations, 1):
            st.write(f"{i}. {anime}")