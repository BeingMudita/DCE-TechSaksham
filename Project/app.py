import streamlit as st
import sqlite3
import os

conn = sqlite3.connect(os.path.join(os.path.dirname(__file__), 'food_recommendations.db'))
cursor = conn.cursor()

# Set page config
st.set_page_config(page_title="SwaadSaga", page_icon="🍛", layout="wide")

# Custom CSS for theme and alignment
st.markdown("""
    <style>
        .title {
            color: #D2691E;
            text-align: center;
        }
        .food-item {
            display: flex;
            align-items: center;
            background-color: #fff5e6;
            border-radius: 10px;
            padding: 10px;
            margin-bottom: 10px;
        }
        .food-item img {
            border-radius: 10px;
            margin-right: 15px;
        }
        .food-item .description {
            color: black;
            text-align: left;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1 class='title'>SwaadSaga – A journey through the tastes of India! 🍲</h1>", unsafe_allow_html=True)

# User inputs
with st.form("preferences_form"):
    cuisine = st.selectbox("Choose a cuisine:", 
    ['Indian', 'South Indian Recipes', 'North Indian Recipes', 'Bengali Recipes', 'Gujarati Recipes\ufeff', 
     'Maharashtrian Recipes', 'Punjabi', 'Kerala Recipes', 'Rajasthani', 'Kashmiri', 'Goan Recipes', 
     'Andhra', 'Tamil Nadu', 'Any'])

    diet = st.selectbox("Choose your diet preference:", 
    ['Vegetarian', 'Non Vegeterian', 'Vegan', 'High Protein Non Vegetarian', 'High Protein Vegetarian', 
     'No Onion No Garlic (Sattvic)', 'Eggetarian', 'Diabetic Friendly', 'Gluten Free', 'Any'])

    course = st.selectbox("Choose the course:", 
    ['Lunch', 'Dinner', 'Appetizer', 'Dessert', 'Snack', 'Side Dish', 'Main Course', 
     'South Indian Breakfast', 'North Indian Breakfast', 'One Pot Dish', 'Any'])

    submit_button = st.form_submit_button(label='Get Recommendations')

# Fetch data based on user input
if submit_button:
    # Build query based on inputs
    query = "SELECT name, image, description FROM food WHERE 1=1"
    params = []

    if cuisine != 'Any':
        query += " AND cuisine = ?"
        params.append(cuisine)
    if diet != 'Any':
        query += " AND diet = ?"
        params.append(diet)
    if course != 'Any':
        query += " AND course = ?"
        params.append(course)

    query += " LIMIT 10"
    cursor.execute(query, params)
    results = cursor.fetchall()

    # Display results
    if results:
        st.subheader("Recommended Dishes:")
        for name, image, description in results:
            st.markdown(f"""
                <div class='food-item'>
                    <img src='{image}' width='150'>
                    <div class='description'>
                        <b>{name}</b><br>{description}
                    </div>
                </div>
            """, unsafe_allow_html=True)
    else:
        st.write("No recommendations available for the selected preferences.")

conn.close()
