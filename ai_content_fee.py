import time

# Simulate a web page with content and a cost to access
class WebPage:
    def __init__(self, url, content, access_cost_per_token=0.001):
        self.url = url
        self.content = content
        self.access_cost_per_token = access_cost_per_token

    def get_content(self):
        # Simulate the time it takes to 'read' the content
        time.sleep(0.1) 
        return self.content

    def calculate_access_cost(self, num_tokens):
        # Cost is based on the number of 'tokens' (words/segments) processed
        return num_tokens * self.access_cost_per_token

# Simulate an AI agent that needs to access web content
class AIAgent:
    def __init__(self, name):
        self.name = name
        self.balance = 100.0  # Starting balance for the AI

    def access_page(self, page):
        print(f"[{self.name}] Attempting to access: {page.url}")
        
        # Simulate AI processing: estimate token count (simple word count)
        estimated_tokens = len(page.get_content().split())
        cost = page.calculate_access_cost(estimated_tokens)

        if self.balance >= cost:
            self.balance -= cost
            print(f"[{self.name}] Successfully accessed. Cost: ${cost:.4f}. Remaining balance: ${self.balance:.2f}")
            # In a real scenario, AI would process the content here
            return True
        else:
            print(f"[{self.name}] Insufficient balance to access. Required: ${cost:.4f}, Available: ${self.balance:.2f}")
            return False

# --- Main Simulation ---
if __name__ == "__main__":
    # Create some simulated web pages with different access costs
    page1 = WebPage("https://example.com/article1", "This is the first article. It contains valuable information about AI.", access_cost_per_token=0.0005)
    page2 = WebPage("https://example.com/research/paper", "A detailed research paper on the future of AI models and their economic impact.", access_cost_per_token=0.0015)
    page3 = WebPage("https://example.com/blog/short", "A short blog post about AI trends.", access_cost_per_token=0.0003)

    # Create an AI agent
    ai_bot = AIAgent("ContentBot")

    print("--- Simulating AI content access with fees ---")

    # AI attempts to access pages
    ai_bot.access_page(page1)
    ai_bot.access_page(page2)
    ai_bot.access_page(page3)

    # Simulate another AI with less balance
    ai_bot_lite = AIAgent("LiteAI")
    ai_bot_lite.balance = 0.1
    print("\n--- Simulating LiteAI with limited balance ---")
    ai_bot_lite.access_page(page1)
    ai_bot_lite.access_page(page2)
