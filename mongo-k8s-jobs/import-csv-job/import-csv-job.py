import subprocess

def import_csv_to_mongo():
    try:
        command = [
            "mongoimport",
            "--host=blog-mongodb",
            "--port=27017",
            "--db=sample_training",
            "--collection=posts",
            "--type=csv",
            "--file=/app/posts.csv",
            "--headerline"
        ]
        subprocess.run(command, check=True)
        print("Import completed successfully.")
    except Exception as e:
        print(f"Error during import: {e}")

if __name__ == "__main__":
    import_csv_to_mongo()