# GUI Setup
root = tk.Tk()
root.title("🌐 Wikipedia Scraper Tool")
root.configure(bg="#f0f4f7")

style = ttk.Style()
style.configure("TButton", font=("Segoe UI", 10), padding=6)
style.configure("TLabel", font=("Segoe UI", 11))

# Dynamic center + 90% height
root.update_idletasks()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
window_width = 750
window_height = int(screen_height * 0.9)
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2
root.geometry(f"{window_width}x{window_height}+{x}+{y}")

# Heading
heading = tk.Label(root, text="🔎 Wikipedia Scraper", font=("Segoe UI", 16, "bold"), bg="#f0f4f7", fg="#333")
heading.pack(pady=10)

# Input Frame
input_frame = tk.Frame(root, bg="#f0f4f7")
input_frame.pack(pady=5)

name_label = ttk.Label(input_frame, text="Enter Name:")
name_label.grid(row=0, column=0, padx=5, sticky="w")

name_entry = ttk.Entry(input_frame, width=40)
name_entry.grid(row=0, column=1, padx=5)

level_label = ttk.Label(input_frame, text="Scrape Level:")
level_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")

scrape_level = ttk.Combobox(input_frame, values=["Low", "Medium", "High"], state="readonly", width=37)
scrape_level.set("Medium")
scrape_level.grid(row=1, column=1, padx=5, pady=5)

custom_summary_label = ttk.Label(input_frame, text="Summary Sentences:")
custom_summary_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")

custom_summary = ttk.Entry(input_frame, width=40)
custom_summary.grid(row=2, column=1, padx=5, pady=5)
custom_summary.insert(0, "5")

# Buttons
button_frame = tk.Frame(root, bg="#f0f4f7")
button_frame.pack(pady=5)

search_button = ttk.Button(button_frame, text="🔍 Search", command=search_wikipedia)
search_button.grid(row=0, column=0, padx=10)

save_button = ttk.Button(button_frame, text="💾 Save to File", command=save_to_file)
save_button.grid(row=0, column=1, padx=10)

save_summary_button = ttk.Button(button_frame, text="📝 Save Summary", command=save_summary_to_file)
save_summary_button.grid(row=0, column=2, padx=10)

# Main content output
text_frame = tk.Frame(root)
text_frame.pack(padx=20, pady=10, fill=tk.BOTH, expand=True)

scrollbar = tk.Scrollbar(text_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

output_text = tk.Text(text_frame, height=20, wrap=tk.WORD, font=("Segoe UI", 10), yscrollcommand=scrollbar.set)
output_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
scrollbar.config(command=output_text.yview)
output_text.config(state=tk.DISABLED)

# Summary output
summary_frame = tk.Frame(root)
summary_frame.pack(padx=20, pady=5, fill=tk.BOTH, expand=False)

summary_scroll = tk.Scrollbar(summary_frame)
summary_scroll.pack(side=tk.RIGHT, fill=tk.Y)

summary_text = tk.Text(summary_frame, height=8, wrap=tk.WORD, font=("Segoe UI", 10), yscrollcommand=summary_scroll.set, bg="#f0f4f7")
summary_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
summary_scroll.config(command=summary_text.yview)
summary_text.config(state=tk.DISABLED)

# Status
status_label = tk.Label(root, text="", font=("Segoe UI", 10), bg="#f0f4f7")
status_label.pack(pady=5)

# Footer / credits
footer_label = tk.Label(root, text="Created by Hrishikesh Jadhav", font=("Segoe UI", 10), bg="#f0f4f7")
footer_label.pack(side=tk.BOTTOM, pady=5)

# Run
root.mainloop()
