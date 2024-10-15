import requests
import csv
import time

# Params
api_url = "http://blog-server:5050/posts"
csv_file_path = "/app/post.csv"
new_post_data = {
    "author": "Python Script",
    "title": "New Post from Python",
    "body": "This post was created using a Kubernetes Job!",
    "tags": ["automation", "kubernetes", "python"]
}


# Functions 
def create_post(api_url, post_data):
    """
    Creates a new post using the API
    """
    try:
        headers = {"Content-Type": "application/json"}
        response = requests.post(api_url, json=post_data, headers=headers)

        if response.status_code == 200:
            print("Post created successfully!")
        else:
            print(f"Failed to create post. Status code: {response.status_code}")
            print(response.json())

    except Exception as e:
        print(f"An error occurred: {e}")

def get_all_posts(api_url):
    """
    Get all posts from the API
    """
    try:
        response = requests.get(api_url)
        
        if response.status_code == 200:
            posts = response.json()
            return posts
        else:
            print(f"Failed to get posts. Status code: {response.status_code}")
            return None

    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def export_to_csv(posts, csv_file_path):
    """
    Exports the posts to a CSV file.
    """
    if posts:
        try:
            with open(csv_file_path, mode='w', newline='', encoding='utf-8') as csv_file:
                writer = csv.writer(csv_file)
                writer.writerow(['ID', 'Author', 'Title', 'Body', 'Tags', 'Date'])  # Header row

                for post in posts:
                    writer.writerow([
                        post.get('_id'),
                        post.get('author'),
                        post.get('title'),
                        post.get('body'),
                        post.get('tags'),
                        post.get('date')
                    ])

            print("Posts exported to CSV successfully!")
        except Exception as e:
            print(f"An error occurred while exporting to CSV: {e}")
    else:
        print("No posts available to export.")


if __name__ == "__main__":

    create_post(api_url, new_post_data)
    posts = get_all_posts(api_url)
    export_to_csv(posts, csv_file_path)

    time.sleep(300) 