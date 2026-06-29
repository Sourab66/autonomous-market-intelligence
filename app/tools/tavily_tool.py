from tavily import TavilyClient
from app.config import TAVILY_API_KEY

from datetime import datetime
import time

client = TavilyClient(api_key=TAVILY_API_KEY)

# In-memory cache
_cache = {}


def search_market(query: str):

    # Return cached result if available
    if query in _cache:
        print(f"Using cached Tavily result for: {query}")
        return _cache[query]

    max_retries = 3

    for attempt in range(max_retries):

        try:

            result = client.search(
                query=query,
                search_depth="advanced",
                max_results=5
            )

            response = {

                "answer": result.get("answer", ""),

                "sources": result.get("results", []),

                "timestamp": datetime.now().strftime(
                    "%d-%m-%Y %H:%M:%S"
                )

            }

            # Save in cache
            _cache[query] = response

            return response

        except Exception as e:

            print(f"Tavily attempt {attempt+1} failed: {e}")

            if attempt < max_retries - 1:
                time.sleep(2)

            else:

                return {

                    "answer": "Unable to retrieve market research.",

                    "sources": [],

                    "timestamp": datetime.now().strftime(
                        "%d-%m-%Y %H:%M:%S"
                    )

                }