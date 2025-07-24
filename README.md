💱 Currency Converter
Currency Converter is a Python-based project developed as part of a school subject. The purpose of the application is to convert amounts between different currencies using up-to-date exchange rates.

🧠 Description
The application uses a web crawler to automatically fetch real-time exchange rate data from a dedicated currency exchange webpage. These values are then processed and used within the app to perform accurate currency conversions (e.g., EUR → RON, USD → RON, etc.).

The crawler is responsible for:

Accessing a public webpage with current exchange rates

Extracting relevant exchange rate values

Updating the application's internal data accordingly

🛠️ Technologies Used
Python 3

requests for HTTP requests

BeautifulSoup for HTML parsing

datetime for working with dates

Other standard Python libraries

🚀 How to Run
Clone the repository:

bash
Copy
Edit
git clone https://github.com/username/Currency-Converter.git
cd Currency-Converter
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Run the application:

bash
Copy
Edit
python main.py
📚 Usage
Enter the amount you want to convert.

Select the source and target currencies.

The app will display the converted amount using the latest available exchange rate.

📌 Note
This project was created for educational purposes and demonstrates:

Fetching and parsing external data

Using web scraping techniques

String and number manipulation

Control structures and function organization in Python

