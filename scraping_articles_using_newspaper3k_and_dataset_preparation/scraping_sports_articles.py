from newspaper import build, ArticleException
import os

# Define website URLs and their corresponding names and categories
websites = [
    {
        "url": "https://www.espn.in/cricket/",
        "name": "ESPN",
        "category": "Cricket",
    }, 
    {
        "url": "https://www.espn.in/football/",
        "name": "ESPN",
        "category": "Football",
    },
    {
        "url": "https://www.espn.in/olympics/",
        "name": "ESPN",
        "category": "Olympics",
    } 
    # Add more websites as needed
]

# Create a directory to store the scraped articles
output_directory = "..\\scraped_articles_files"
os.makedirs(output_directory, exist_ok=True)

# Iterate through the websites
for idx, website_info in enumerate(websites, start=1):
    website_url = website_info["url"]
    website_name = website_info["name"]
    sports_category = website_info["category"]

    # Build a source object for the website
    website_source = build(website_url, memoize_articles=False)

    # List to store article data
    articles_data = []

    # Iterate through the articles on the website
    for article in website_source.articles:
        try:
            article.download()
            article.parse()

            # Extract title, content, and publication date
            title = article.title
            content = article.text
            published_date = article.publish_date

            # Store article data in a dictionary
            article_info = {
                "Title": title,
                "Publication Date": published_date,
                "Content": content,
            }

            articles_data.append(article_info)
        except ArticleException as e:
            print(f"Error processing article: {str(e)}")

    # Create a new file for each website and save the articles
    file_name = f"{website_name}_{sports_category}_articles_{idx}.txt"
    file_path = os.path.join(output_directory, file_name)
    
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(f"Website Name: {website_name}\n")
        file.write(f"Sports Category: {sports_category}\n\n")
        articles_count = 0
        for article_info in articles_data:
            file.write(f"Title: {article_info['Title']}\n")
            if article_info['Publication Date']:
                file.write(f"Publication Date: {article_info['Publication Date']}\n")
            file.write("\n")
            file.write(article_info['Content'] + "\n")
            file.write("=" * 50 + "\n\n")
            articles_count += 1
        
        finished = "All articles from the " + website_url + "have been added to the " + file_name
        number_of_articles = "The total number of articles from " + website_url + " in this file is " + str(articles_count)
        file.write(finished + "\n\n")
        file.write(number_of_articles)

    print(f"Articles from {website_name} ({sports_category}) saved to {file_path}\n\n")
    print(number_of_articles)


