import streamlit as st
import pandas as pd

# Set page configuration
st.set_page_config(
    page_title="Anime  Recommender System",
    layout="centered"
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
    }
    .stRadio > div {
        margin-top: 10px;
    }
    .anime-input-label {
        font-weight: bold;
        margin-top: 20px;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown('<div class="header-container"><h1>Anime  Recommender System</h1></div>', unsafe_allow_html=True)

st.write("Select an algorithm")
recommendation_algorithm = st.radio(
    label="",
    options=["Content Based Filtering", "Collaborative Based Filtering"],
    index=0,
    label_visibility="collapsed"
)

# Anime input section
st.markdown("<h3>Enter Your Three Favorite Animes</h3>", unsafe_allow_html=True)

# Anime Options ===
Anime_Options = [

]

# Anime selection dropdowns
st.markdown('<p class="anime-input-label">First Option</p>', unsafe_allow_html=True)
anime1 = st.selectbox(
    label="Example Anime",
    options=Anime_Options,
    index=Anime_Options.index("Death Note") if "Death Note" in Anime_Options else 0,
    label_visibility="collapsed"
)


# Recommendation button
if st.button("Recommend"):
    st.write("### Recommended Anime")
    
    # Content Based Filtering
    if recommendation_algorithm == "Content Based Filtering":
        st.write("Based on content similarity, we recommend:")
        recommendations = [

        ]
    else:  # Collaborative Filtering
        st.write("Based on what similar users liked, we recommend:")
        recommendations = [

        ]
    
    # Display recommendations
    for i, anime in enumerate(recommendations, 1):
        st.write(f"{i}. {anime}")