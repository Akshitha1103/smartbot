import requests
from bs4 import BeautifulSoup
import pandas as pd

def fetch_data_from_usaspending(keyword):
  """
  Fetches relevant spending data from USAspending.gov based on a keyword.

  Args:
    keyword: The keyword to search for (e.g., "Department of Defense", "AI").

  Returns:
    A pandas DataFrame containing the relevant spending data, or None if no data is found.
  """
  try:
    # Construct the URL for the search query
    url = f"https://www.usaspending.gov/search/?q={keyword}" 

    # Fetch the webpage content
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception for bad status codes

    # Parse the HTML content
    soup = BeautifulSoup(response.content, "html.parser")

    # Extract data from the search results (this will depend on the structure of the USAspending.gov website)
    # ... (Your code to extract relevant data from the parsed HTML)
    # Example: Extracting data from a table
    table = soup.find("table", {"class": "search-results-table"})  # Replace with the actual table class
    if table:
      df = pd.read_html(str(table))[0]  # Read the table into a pandas DataFrame
      return df
    else:
      return None 

  except requests.exceptions.RequestException as e:
    print(f"Error fetching data from USAspending.gov: {e}")
    return None


def format_data_for_gemini(df):
  """
  Formats the spending data into a string suitable for input to the Gemini model.

  Args:
    df: A pandas DataFrame containing the spending data.

  Returns:
    A formatted string representation of the data.
  """
  if df is None:
    return "No data available."

  # Format the DataFrame into a string (you can customize this based on your needs)
  # Example: Convert to a Markdown table
  formatted_data = df.to_markdown(index=False, numalign="left", stralign="left")  
  return formatted_data
