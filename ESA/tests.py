from django.test import TestCase
import csv
from io import StringIO
from concurrent.futures import ThreadPoolExecutor, as_completed
from .langchain_service import get_huggingface_result, get_berttweet_result  # Import your new function
import os
# Convert emojis to text



class SentimentAnalysisTestCase(TestCase):
    def setUp(self):
        # Load CSV data from the filesystem
        csv_path = 'ESA/passed_cases.csv'
        if not os.path.isfile(csv_path):
            raise FileNotFoundError(f"CSV file not found: {csv_path}")
        
        with open(csv_path, 'r') as csv_file:
            # Read CSV data into memory
            self.csv_data = csv_file.read()
        
        # Use StringIO to simulate a file object
        self.csv_file = StringIO(self.csv_data)
        self.reader = csv.DictReader(self.csv_file)
    
    def analyze_text(self, text, expected_label, model_name):
        result = None
        try:
            if model_name == 'hf':
                result = get_huggingface_result(text)
            elif model_name == 'berttweet':
                result = get_berttweet_result(text)
            
            if result:
                print(f"{model_name.capitalize()} Result: {result}")  # Debugging line
                return result['Category'].strip().lower() == expected_label
        except Exception as e:
            print(f"{model_name.capitalize()} Error for text '{text}': {e}")
            return False

    def test_sentiment_analysis(self):
        # Initialize counters
        hf_passed = 0
        hf_failed = 0
        berttweet_passed = 0
        berttweet_failed = 0

        def worker(row):
            text = row.get('text', '').strip()
            expected_label = row.get('expected_label', '').strip().lower()
            
            if not text or not expected_label:
                print(f"Skipping row with text: '{text}' and expected_label: '{expected_label}'")
                return None, None

            hf_result = self.analyze_text(text, expected_label, 'hf')
            berttweet_result = self.analyze_text(text, expected_label, 'berttweet')

            return hf_result, berttweet_result
        
        with ThreadPoolExecutor() as executor:
            futures = [executor.submit(worker, row) for row in self.reader]
            
            for future in as_completed(futures):
                hf_result, berttweet_result = future.result()
                
                if hf_result is not None:
                    if hf_result:
                        hf_passed += 1
                    else:
                        hf_failed += 1
                
                if berttweet_result is not None:
                    if berttweet_result:
                        berttweet_passed += 1
                    else:
                        berttweet_failed += 1

        print(f"Hugging Face Passed Count: {hf_passed}")
        print(f"Hugging Face Failed Count: {hf_failed}")
        print(f"BERTweet Passed Count: {berttweet_passed}")
        print(f"BERTweet Failed Count: {berttweet_failed}")

        # Assert results
        self.assertGreater(hf_passed, 0, "No Hugging Face cases passed.")
        self.assertGreater(berttweet_passed, 0, "No BERTweet cases passed.")
