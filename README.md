# WikipediaScraper

A Python-based GUI application that allows users to search Wikipedia articles for any Historical name, fetch full content or a summary, and save it as `.txt` files.

Built using **Tkinter**, **wikipedia API**, and **BeautifulSoup (optional fallback)**, this tool helps you scrape and store Wikipedia content efficiently with different scraping levels.

---

## 🎯 Features

- 🔍 Search Wikipedia articles by person’s name.
- 📊 Choose scraping level:  
  - `Low`: 15-sentence summary  
  - `Medium`: 55-sentence summary  
  - `High`: Full article content
- 📝 Enter custom sentence count for summaries.
- 💾 Save full content or just the summary to text files.
- 🧾 Scrollable content display for both article and summary.
- 🎨 Beautiful, responsive GUI with centered layout.

---

## 📦 Requirements

Install dependencies with:

```
pip install wikipedia
pip install beautifulsoup4 requests
```
---

## 🚀 How to Run
Run it with: wikipedia_scraper.exe

---

## 🧼 Interface 
<h6>exe File</h6>
<p align="center">
  <img src="https://github.com/hsj71/WikipediaScraper/blob/main/Screenshot%20(779).png" alt="View" width="100"/>
</p>

<h6>User Interface</h6>
<p align="center">
  <img src="https://github.com/hsj71/WikipediaScraper/blob/main/Screenshot%20(780).png" alt="View" width="700"/>
</p>

<h6>Working with exe</h6>
  <p align="center">
  <img src="https://github.com/hsj71/WikipediaScraper/blob/main/Screenshot%20(781).png" alt="View" width="700" />
</p>

 <h6>Created File</h6>
 <p align="center">
  <img src="https://github.com/hsj71/WikipediaScraper/blob/main/Screenshot%20(782).png" alt="View" width="100"/>
</p>

<h6>View File</h6>
<p align="center">
  <img src="https://github.com/hsj71/WikipediaScraper/blob/main/Screenshot%20(777).png" alt="View" width="700"/>
</p>

<h6>All Files</h6>
<p align="center">
  <img src="https://github.com/hsj71/WikipediaScraper/blob/main/Screenshot%20(778).png" alt="View" width="700"/>
</p>
---
---

## 🧑‍💻 How It Works
The user enters a person's name.

Selects a scraping level (Low, Medium, or High).

Optionally enters a number of sentences for a custom summary.

Hits the 🔍 Search button:

Article content and custom summary are fetched and shown.

Use 💾 Save to File to store full article text.

Use 📝 Save Summary to save the summary only.

---

## ✍️ Author
Made by Hrishikesh
