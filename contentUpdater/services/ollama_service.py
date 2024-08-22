from ollama import Client
import os


class OllamaService:
    def __init__(self):
        self.model_name = os.getenv('OLLAMA_MODEL_NAME')
        self.client_port = os.getenv('OLLAMA_CLIENT_PORT')
        print(f"Initializing Model: {self.model_name}")
        self.client = Client(host=f'http://localhost:{self.client_port}')
        print("Model is Running Successfully.")

    def rewrite_title(self, ttile):
        response = self.client.generate(
            model=self.model_name, prompt=f'Title:{ttile}. Rewrite this title. Only give one rewrited title nothing else.',)
        return response['response'].strip()

    def rewrite_description(self, old_description):
        response = self.client.generate(
            model=self.model_name, prompt=f'Description:{old_description}. Rewrite and expand this descrption. Only give the rewrited description nothing else.',)
        return response['response'].strip()

    def summarize(self, text):
        response = self.client.generate(
            model=self.model_name, prompt=f'Description:{text}. \n Summarize this text in 2-3 sentences. Only give the summarized text nothing else.',)
        print(response['response'].strip())
        return response['response'].strip()
