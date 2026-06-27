from tools import web_search
from utils.scraper import read_webpage
from agent import summarize

query = input("Enter Research Topic: ")

print("\n Getting results...")
results = web_search(query)

combined_text = ""

for result in results:
    print(f"\n Reading {result['title']}")
    text = read_webpage(result['link'])

    combined_text += "\n \n" + text[:2000]

report = summarize(combined_text)
print("\n ---------------------------------------- \n")
print(report.content)