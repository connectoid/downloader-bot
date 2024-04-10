from instaloader import Instaloader, Profile 
L = Instaloader()
PROFILE = "connectoid" #instagram username for profile you want to download data
profile = Profile.from_username(L.context, PROFILE)
posts_sorted_by_likes = sorted(profile.get_posts(), key=lambda post: post.likes,reverse=True)
selected_range = posts_sorted_by_likes[0:2] #to download from only 2 posts
for post in selected_range:
    L.download_post(post, PROFILE)