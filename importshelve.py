import shelve
import pyperclip

def save_to_clipboard(keyword, text):
    """Save a keyword-text pair into the clipboard database."""
    with shelve.open('mcb') as mcbShelf:
        mcbShelf[keyword] = text
        print(f"Saved content under keyword: '{keyword}'")

def list_keywords():
    """List all saved keywords and copy them to the clipboard."""
    with shelve.open('mcb') as mcbShelf:
        keywords = list(mcbShelf.keys())
        if keywords:
            pyperclip.copy(', '.join(keywords))
            print("Keywords:", ', '.join(keywords))
        else:
            print("No keywords found.")

def load_from_clipboard(keyword):
    """Load a snippet by its keyword and copy it to the clipboard."""
    with shelve.open('mcb') as mcbShelf:
        if keyword in mcbShelf:
            pyperclip.copy(mcbShelf[keyword])
            print(f"Content for '{keyword}' copied to the clipboard.")
        else:
            print(f"Keyword '{keyword}' not found.")

def main():
    """Main function to handle user interaction."""
    while True:
        print("\nMultiClipboard Options:")
        print("1. Save a New Snippet")
        print("2. List all Keywords")
        print("3. Load a Snippet")
        print("4. Exit")

        choice = input("Enter your choice (1/2/3/4): ").strip()

        if choice == '1':
            keyword = input("Enter a keyword: ").strip()
            text = input("Enter the text to save: ").strip()
            save_to_clipboard(keyword, text)
        elif choice == '2':
            list_keywords()
        elif choice == '3':
            keyword = input("Enter the keyword to retrieve: ").strip()
            load_from_clipboard(keyword)
        elif choice == '4':
            print("Exiting MultiClipboard. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option (1/2/3/4).")

# Run the MultiClipboard program
if __name__ == "__main__":
    main()
