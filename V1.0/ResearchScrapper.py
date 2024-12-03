
# ResearchScrapper Module with Retry Mechanism
import requests
from time import sleep

class ResearchScrapper:
    def __init__(self):
        self.repositories = [
            {"name": "arXiv", "url": "https://export.arxiv.org/api/query?search_query={query}&start=0&max_results=1"},
            {"name": "PubMed Central", "url": "https://www.ncbi.nlm.nih.gov/pmc/?term={query}"}
        ]

    def search_repository(self, repository, query, retries=3):
        for attempt in range(retries):
            try:
                response = requests.get(repository["url"].format(query=query))
                if response.status_code == 200:
                    return f"Results from {repository['name']}: {response.text[:100]}"
                else:
                    return f"Error accessing {repository['name']}: {response.status_code}"
            except Exception as e:
                if attempt < retries - 1:
                    sleep(1)  # Wait before retrying
                    continue
                return f"Failed to access {repository['name']}: {str(e)}"

    def search_all(self, query):
        results = []
        for repo in self.repositories:
            results.append(self.search_repository(repo, query))
        return results

__all__ = ["ResearchScrapper"]
