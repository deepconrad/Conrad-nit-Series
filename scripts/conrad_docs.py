import json
import os
import argparse
from datetime import datetime

class ConradDocsManager:
    def __init__(self, models_file='docs/models.json', docs_dir='docs/models'):
        self.models_file = models_file
        self.docs_dir = docs_dir
        self.load_models()

    def load_models(self):
        if os.path.exists(self.models_file):
            with open(self.models_file, 'r') as f:
                self.data = json.load(f)
        else:
            self.data = {"models": []}

    def fetch_latest_from_docs(self):
        """
        Placeholder for fetching logic from https://docs.trendwaveconnect.com/docs
        In a real scenario, this would use BeautifulSoup or an API client.
        """
        print("Fetching model updates from trendwaveconnect.com/docs...")
        # For now, we ensure the known 5.1-8B model is in the registry
        return self.data['models']

    def generate_markdown(self):
        print(f"Generating documentation in {self.docs_dir}...")
        if not os.path.exists(self.docs_dir):
            os.makedirs(self.docs_dir)

        for model in self.data['models']:
            file_path = os.path.join(self.docs_dir, f"{model['id']}.md")
            content = f"""# {model['name']}

| Property | Value |
|----------|-------|
| ID | `{model['id']}` |
| Version | {model['version']} |
| Parameters | {model['parameters']} |
| Architecture | {model['architecture']} |
| Last Updated | {datetime.now().strftime('%Y-%m-%d')} |

## Description
{model['description']}

## Resources
- [Hugging Face Repository]({model['huggingface_url']})
- [Trendwave Documentation](https://docs.trendwaveconnect.com/docs)

## Tags
{', '.join([f'`{tag}`' for tag in model['tags']])}
"""
            with open(file_path, 'w') as f:
                f.write(content)
            print(f"Created: {file_path}")

    def talk_about_models(self):
        print("\n--- Conrad NIT Series Registry ---")
        for model in self.data['models']:
            print(f"- {model['name']} ({model['parameters']}): {model['description']}")
        print("----------------------------------\n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Conrad NIT Model Documentation Tool")
    parser.add_argument('--fetch', action='store_true', help='Fetch updates from documentation source')
    parser.add_argument('--generate', action='store_true', help='Generate markdown documentation files')
    parser.add_argument('--summary', action='store_true', help='Print a summary of known models')

    args = parser.parse_args()
    manager = ConradDocsManager()

    if args.fetch:
        manager.fetch_latest_from_docs()
    
    if args.summary:
        manager.talk_about_models()

    if args.generate:
        manager.generate_markdown()
