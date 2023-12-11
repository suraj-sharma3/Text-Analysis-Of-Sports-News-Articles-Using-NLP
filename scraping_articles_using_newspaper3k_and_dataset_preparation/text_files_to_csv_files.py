import re
import pandas as pd

# Read the text file containing articles
with open('..\\scraped_articles_files\\scraped_articles_text_files\\ESPN_Cricket_articles_1.txt', 'r', encoding='utf-8') as file:
    articles_text = file.read()

# Split the text into individual articles based on the "===================" separator
articles = re.split(r'={10,}', articles_text)

# Initialize lists to store extracted data
titles = []
contents = []
published_dates = []
websites = []
source_urls = []
categories = []

# Extract data for each article
for article in articles:
    lines = article.strip().split('\n')
    if len(lines) >= 2:
        title = lines[0].strip()
        content = '\n'.join(lines[1:]).strip()

        # Extract the published date (if available)
        date_match = re.search(r'\b(?:\d{4}-\d{2}-\d{2}|[\d]{1,2} [A-Za-z]+ \d{4})\b', content)
        published_date = date_match.group(0) if date_match else None

        # Append the extracted data to the lists
        titles.append(title)
        contents.append(content)
        published_dates.append(published_date)
        ######################################
        websites.append("ESPN")  # ESPN is the website for all articles
        source_urls.append("https://www.espn.in/cricket/")  # You can add the source URL if available
        categories.append("Cricket")  # Cricket is the category for all articles

# Create a DataFrame
data = {
    'Serial Number': range(1, len(titles) + 1),  # Generate serial numbers
    'Title': titles,
    'Content': contents,
    'Published_Date': published_dates,
    'Website': websites,
    'Source_URL': source_urls,
    'Category': categories
}

df = pd.DataFrame(data)

# Save the DataFrame to a CSV file
df.to_csv('..\\scraped_articles_files\\scraped_articles_csv_files\\ESPN_Cricket_articles_1.csv', index=False)

print("CSV file created successfully.")
