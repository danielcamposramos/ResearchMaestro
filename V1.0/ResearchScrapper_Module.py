
# Refined ResearchScrapper with Multiple Predefined Sources
import requests

class ResearchScrapper:
    def __init__(self):
        self.repositories = [
            {"name": "arXiv", "url": "https://export.arxiv.org/api/query?search_query={query}&start=0&max_results=10"},
            {"name": "PubMed Central", "url": "https://www.ncbi.nlm.nih.gov/pmc/?term={query}"},
            {"name": "CORE", "url": "https://core.ac.uk/search?q={query}"},
            {"name": "DOAJ", "url": "https://doaj.org/search?source={query}"},
            {"name": "Semantic Scholar", "url": "https://api.semanticscholar.org/graph/v1/paper/search?query={query}"}
        ]

    def search_repository(self, repository, query):
        try:
            response = requests.get(repository["url"].format(query=query))
            if response.status_code == 200:
                return f"Results from {repository['name']}: {response.text[:500]}"
            else:
                return f"Error accessing {repository['name']}: {response.status_code}"
        except Exception as e:
            return f"Failed to access {repository['name']}: {str(e)}"

    def search_all(self, query):
        results = []
        for repo in self.repositories:
            results.append(self.search_repository(repo, query))
        return results

# Example Usage
if __name__ == "__main__":
    scrapper = ResearchScrapper()
    print(scrapper.search_all("machine learning"))
