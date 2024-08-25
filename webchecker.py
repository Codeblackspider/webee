import requests
from bs4 import BeautifulSoup
from termcolor import colored
import time

# Define the functions
def print_title():
    title = r"""
 _       __     __            __              __
| |     / /__  / /_     _____/ /_  ___  _____/ /_____  _____
| | /| / / _ \/ __ \   / ___/ __ \/ _ \/ ___/ //_/ _ \/ ___/
| |/ |/ /  __/ /_/ /  / /__/ / / /  __/ /__/ ,< /  __/ /    
|__/|__/\___/_.___/   \___/_/ /_/\___/\___/_/|_|\___/_/     
    """
    print(colored(title, 'cyan'))

def keyword_checker(url):
    # Dummy implementation
    print(colored(f"\nKeywords for {url}:", 'green'))
    print(colored("keyword1, keyword2, keyword3", 'pink'))

def backlink_checker(url):
    # Dummy implementation
    print(colored(f"\nBacklinks found for {url}:", 'green'))
    print(colored("http://example.com", 'green'))
    print(colored("Total backlinks collected: 1", 'yellow'))

def page_load_time_checker(url):
    # Dummy implementation
    print(colored(f"\nPage load time for {url}:", 'green'))
    print(colored("0.84 seconds", 'purple'))

def seo_title_description_checker(url):
    # Dummy implementation
    print(colored(f"\nTitle for {url}:", 'blue'))
    print(colored("Page Title", 'blue'))
    print(colored("Description: Not found", 'blue'))

def broken_link_checker(url):
    # Dummy implementation
    print(colored(f"\nBroken links found for {url}:", 'red'))
    print(colored("http://example.com/broken-link", 'red'))
    print(colored("Total broken links: 1", 'yellow'))

def image_alt_text_checker(url):
    # Dummy implementation
    print(colored(f"\nImages missing alt text for {url}:", 'red'))
    print(colored("http://example.com/image-without-alt", 'red'))
    print(colored("Total images missing alt text: 1", 'yellow'))

def broken_images_checker(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        images = soup.find_all('img')
        broken_images = []
        
        for img in images:
            src = img.get('src')
            if src and src.startswith(('http', 'https')):
                try:
                    img_response = requests.head(src, allow_redirects=True)
                    if img_response.status_code != 200:
                        broken_images.append(src)
                except requests.RequestException:
                    broken_images.append(src)
        
        if broken_images:
            print(colored(f"\nBroken images found for {url}:", 'red'))
            for img_src in broken_images:
                print(colored(img_src, 'red'))
            print(colored(f"Total broken images: {len(broken_images)}", 'yellow'))
        else:
            print(colored("No broken images found.", 'green'))
    except Exception as e:
        print(colored(f"Error fetching the URL: {e}", 'red'))

def meta_tags_checker(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        meta_tags = {
            'charset': soup.find('meta', {'charset': True}),
            'viewport': soup.find('meta', {'name': 'viewport'}),
            'author': soup.find('meta', {'name': 'author'}),
            'robots': soup.find('meta', {'name': 'robots'})
        }
        
        print(colored(f"\nMeta Tags Checker for {url}:", 'cyan'))
        
        for tag, meta in meta_tags.items():
            if meta:
                print(colored(f"{tag.capitalize()}: {meta.get('content', 'N/A')}", 'cyan'))
            else:
                print(colored(f"{tag.capitalize()}: Not found", 'red'))
    except Exception as e:
        print(colored(f"Error fetching the URL: {e}", 'red'))

def main():
    while True:
        print_title()
        print(colored("\nPlease choose an option:", 'magenta'))
        print(colored("1. Keyword Checker", 'magenta'))
        print(colored("2. Backlink Checker", 'magenta'))
        print(colored("3. Page Load Time Checker", 'magenta'))
        print(colored("4. SEO Title and Description Checker", 'magenta'))
        print(colored("5. Broken Link Checker", 'magenta'))
        print(colored("6. Image Alt Text Checker", 'magenta'))
        print(colored("7. Broken Images Checker", 'magenta'))
        print(colored("8. Meta Tags Checker", 'magenta'))
        
        choice = input(colored("\nEnter your choice: ", 'magenta'))
        url = input(colored("Enter a URL to check: ", 'magenta'))
        
        if choice == '1':
            keyword_checker(url)
        elif choice == '2':
            backlink_checker(url)
        elif choice == '3':
            page_load_time_checker(url)
        elif choice == '4':
            seo_title_description_checker(url)
        elif choice == '5':
            broken_link_checker(url)
        elif choice == '6':
            image_alt_text_checker(url)
        elif choice == '7':
            broken_images_checker(url)
        elif choice == '8':
            meta_tags_checker(url)
        else:
            print(colored("Invalid choice. Please select a valid option.", 'red'))

        # Adding a small gap between outputs
        time.sleep(1)
        print("\n" + "-"*50 + "\n")
        time.sleep(1)

if __name__ == "__main__":
    main()
