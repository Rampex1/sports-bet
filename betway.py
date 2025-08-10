from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.add_argument("--headless")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument(
    "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")

driver = webdriver.Chrome(options=options)

try:
    driver.get("https://betway.com/en/sports/grp/soccer/usa/mls")

    # Wait for dynamic content to load
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".eventHolder"))
    )

    # Scroll to load more content if needed
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)

    # Extract match data
    matches = driver.find_elements(By.CSS_SELECTOR, ".eventHolder")
    for match in matches:
        try:
            # Get all team name elements
            team_elements = match.find_elements(By.CSS_SELECTOR, ".teamName")

            # Extract team names
            home_team = team_elements[0].text if len(team_elements) > 0 else "N/A"
            away_team = team_elements[1].text if len(team_elements) > 1 else "N/A"
            odds = [odd.text for odd in match.find_elements(By.CSS_SELECTOR, ".odds")]
            print(f"Match: {home_team} vs {away_team} | Odds: {odds}")
        except Exception as e:
            print(f"Error extracting match: {e}")

finally:
    driver.quit()