import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_data(movie_id):
    response = requests.get(f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=b0cd10efad91c13b96eb12ef1458988f')
    data = response.json()
    if not data['poster_path']:
        return 'https://static.streamlit.io/examples/dice.jpg', data['overview'],data['vote_average']

    return 'https://image.tmdb.org/t/p/w500'+data['poster_path'],data['overview'],data['vote_average']



def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:11]
    recom_movies = []
    recom_movies_data = []
    #poster, overview, rating
    for i in movies_list:
        recom_movies.append(movies.iloc[i[0]]['title'])
        data=fetch_data(movies.iloc[i[0]]['movie_id'])
        recom_movies_data.append(data)
    return recom_movies, recom_movies_data


movie_list = pickle.load(open('Movies.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))


movies = pd.DataFrame(movie_list)
selected_movie = st.selectbox("Select Movie", movies['title'].values)

# if st.button('Recommend'):
#     recommended_movies, data = recommend(selected_movie)
#     n = len(recommended_movies)
#     for i in range(n):
#         with st.expander(recommended_movies[i]):
#             st.write(data[i][1])
#             st.image(data[i][0])
#             # st.write(data[i][2])
#             color='Yellow'
#             if data[i][2]> 7:
#                 color='Green'
#             elif data[i][2]< 5:
#                 color='Red'
#             t = f'<p>Rating: <span style="color:{color}">{data[i][2]}</span></p>'
#             st.markdown(t, unsafe_allow_html=True)
st.write("YO")

#streamlit run app.py
