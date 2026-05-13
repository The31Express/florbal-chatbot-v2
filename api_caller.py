import requests

class ollama_api:
    def __init__(self, url: str, key: str):
        self.url = url
        self.key = key
    
    def query(self, question: str) -> str:
        try:
            response = requests.post(
                self.url,
                headers={
                    "Authorization": f"Bearer {self.key}",
                    "Content-Type": "application/json"
                },
                json={
                    "model": "gemma3:27b",
                    "messages": [
                        {"role": "user", "content": question}
                    ]
                }
            )

            data = response.json()
            #print("DEBUG:", data)

            return data["choices"][0]["message"]["content"]

        except Exception as e:
            return f"Chyba: {e}"