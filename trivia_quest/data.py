import requests
def fetch_questions(amount, category, difficulty, question_type):
    url = f"https://opentdb.com/api.php?amount={amount}&category={category}&difficulty={difficulty}&type={question_type}"
    response = requests.get(url)
    data = response.json()
    return data['results']

def fetch_categories():
    url = "https://opentdb.com/api_category.php"
    response = requests.get(url)
    data = response.json()
    return data["trivia_categories"]