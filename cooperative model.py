import math

def cosine_similarity(v1, v2):
    dot_product = sum([v1[i] * v2[i] for i in range(len(v1))])
    magnitude1 = math.sqrt(sum([x**2 for x in v1]))
    magnitude2 = math.sqrt(sum([x**2 for x in v2]))
    return dot_product / (magnitude1 * magnitude2)

# Example user interests
user1_interests = ["music", "movies", "books", "sports"]
user2_interests = ["music", "movies", "travel", "photography"]

# Create a set of all unique interests
all_interests = set(user1_interests + user2_interests)

# Create interest vectors for each user
user1_vector = [1 if interest in user1_interests else 0 for interest in all_interests]
user2_vector = [1 if interest in user2_interests else 0 for interest in all_interests]

# Calculate cosine similarity between the two users
similarity = cosine_similarity(user1_vector, user2_vector)

print(f"The similarity between the two users is: {similarity}")
