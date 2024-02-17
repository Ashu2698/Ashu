class MovieRecommendationSystem:
    def __init__(self):
        self.users = {}
        self.movies = {}

    def add_user_rating(self, user_id, movie_id, rating):
        if user_id not in self.users:
            self.users[user_id] = {}
        self.users[user_id][movie_id] = rating

        if movie_id not in self.movies:
            self.movies[movie_id] = {}
        self.movies[movie_id][user_id] = rating

    def get_similar_users(self, user_id):
        similar_users = []
        if user_id in self.users:
            user_ratings = self.users[user_id]
            for movie_id, rating in user_ratings.items():
                for other_user_id in self.movies[movie_id]:
                    if other_user_id != user_id and other_user_id not in similar_users:
                        similar_users.append(other_user_id)
        return similar_users

    def recommend_movies(self, user_id):
        recommendations = {}
        similar_users = self.get_similar_users(user_id)
        for other_user_id in similar_users:
            other_user_ratings = self.users[other_user_id]
            for movie_id, rating in other_user_ratings.items():
                if movie_id not in self.users[user_id] and movie_id not in recommendations:
                    recommendations[movie_id] = rating
                elif movie_id in recommendations:
                    recommendations[movie_id] = (recommendations[movie_id] + rating) / 2
        sorted_recommendations = sorted(recommendations.items(), key=lambda x: x[1], reverse=True)
        return sorted_recommendations

def main():
    recommendation_system = MovieRecommendationSystem()

    # Add sample user ratings
    recommendation_system.add_user_rating("user1", "movie1", 5)
    recommendation_system.add_user_rating("user1", "movie2", 4)
    recommendation_system.add_user_rating("user2", "movie1", 4)
    recommendation_system.add_user_rating("user2", "movie3", 5)

    # Get recommendations for a specific user
    user_id = "user1"
    recommendations = recommendation_system.recommend_movies(user_id)

    # Display recommendations
    print(f"Recommendations for {user_id}:")
    for movie_id, rating in recommendations:
        print(f"Movie ID: {movie_id}, Rating: {rating}")

if __name__ == "__main__":
    main()
