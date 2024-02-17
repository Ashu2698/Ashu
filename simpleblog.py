import os

class BlogSystem:
    def __init__(self, storage_folder):
        self.storage_folder = storage_folder
        os.makedirs(storage_folder, exist_ok=True)

    def write_post(self, post_id, title, content):
        filename = os.path.join(self.storage_folder, f"{post_id}.txt")
        with open(filename, 'w') as file:
            file.write(f"Title: {title}\n\n")
            file.write(content)

    def read_post(self, post_id):
        filename = os.path.join(self.storage_folder, f"{post_id}.txt")
        try:
            with open(filename, 'r') as file:
                return file.read()
        except FileNotFoundError:
            return "Post not found."

    def edit_post(self, post_id, new_title, new_content):
        filename = os.path.join(self.storage_folder, f"{post_id}.txt")
        try:
            with open(filename, 'w') as file:
                file.write(f"Title: {new_title}\n\n")
                file.write(new_content)
        except FileNotFoundError:
            print("Post not found.")

    def delete_post(self, post_id):
        filename = os.path.join(self.storage_folder, f"{post_id}.txt")
        try:
            os.remove(filename)
            print("Post deleted successfully.")
        except FileNotFoundError:
            print("Post not found.")

def main():
    blog = BlogSystem("posts")

    while True:
        print("\nBlog Menu:")
        print("1. Write Post")
        print("2. Read Post")
        print("3. Edit Post")
        print("4. Delete Post")
        print("5. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            post_id = input("Enter post ID: ")
            title = input("Enter post title: ")
            content = input("Enter post content: ")
            blog.write_post(post_id, title, content)
            print("Post written successfully.")
        elif choice == '2':
            post_id = input("Enter post ID: ")
            print(blog.read_post(post_id))
        elif choice == '3':
            post_id = input("Enter post ID: ")
            new_title = input("Enter new title: ")
            new_content = input("Enter new content: ")
            blog.edit_post(post_id, new_title, new_content)
            print("Post edited successfully.")
        elif choice == '4':
            post_id = input("Enter post ID: ")
            blog.delete_post(post_id)
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")

if __name__ == "__main__":
    main()
