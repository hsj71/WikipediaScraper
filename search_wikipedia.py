def search_wikipedia():
    name = name_entry.get().strip()
    level = scrape_level.get().lower()
    summary_sentences = custom_summary.get()

    if not name:
        messagebox.showwarning("Input Error", "Please enter a person's name.")
        return

    try:
        summary_sentences = int(summary_sentences)
        if summary_sentences <= 0:
            raise ValueError
    except ValueError:
        summary_sentences = None

    output_text.config(state=tk.NORMAL)
    output_text.delete("1.0", tk.END)
    summary_text.config(state=tk.NORMAL)
    summary_text.delete("1.0", tk.END)
    summary_text.config(state=tk.DISABLED)
    status_label.config(text="🔍 Searching Wikipedia...", foreground="blue")
    root.update()

    def run():
        global latest_content, latest_filename
        try:
            if level == "low":
                content = wikipedia.summary(name, sentences=15)
                preview = content
            elif level == "medium":
                content = wikipedia.summary(name, sentences=55)
                preview = content
            else:
                page = wikipedia.page(name)
                content = page.content
                preview = content

            latest_content = content
            latest_filename = f"{name.replace(' ', '_')}_{level}.txt"

            output_text.config(state=tk.NORMAL)
            output_text.delete("1.0", tk.END)
            output_text.insert(tk.END, preview)
            output_text.config(state=tk.DISABLED)

            if summary_sentences:
                summary = wikipedia.summary(name, sentences=summary_sentences)
                summary_text.config(state=tk.NORMAL)
                summary_text.delete("1.0", tk.END)
                summary_text.insert(tk.END, summary)
                summary_text.config(state=tk.DISABLED)

            status_label.config(text=f"✅ Content ready to save", foreground="green")

        except wikipedia.exceptions.DisambiguationError as e:
            msg = f"⚠️ Multiple matches found for '{name}'. Try to be more specific.\n\nSuggestions:\n" + "\n".join(e.options[:5])
            output_text.config(state=tk.NORMAL)
            output_text.delete("1.0", tk.END)
            output_text.insert(tk.END, msg)
            output_text.config(state=tk.DISABLED)
            summary_text.config(state=tk.NORMAL)
            summary_text.delete("1.0", tk.END)
            summary_text.config(state=tk.DISABLED)
            latest_content = ""
            status_label.config(text="⚠️ Disambiguation Error", foreground="orange")
        except wikipedia.exceptions.PageError:
            output_text.config(state=tk.NORMAL)
            output_text.delete("1.0", tk.END)
            output_text.insert(tk.END, "❌ No page found. Please check the name.")
            output_text.config(state=tk.DISABLED)
            summary_text.config(state=tk.NORMAL)
            summary_text.delete("1.0", tk.END)
            summary_text.config(state=tk.DISABLED)
            latest_content = ""
            status_label.config(text="❌ Page Not Found", foreground="red")
        except Exception as e:
            output_text.config(state=tk.NORMAL)
            output_text.delete("1.0", tk.END)
            output_text.insert(tk.END, f"❌ Unexpected error: {e}")
            output_text.config(state=tk.DISABLED)
            summary_text.config(state=tk.NORMAL)
            summary_text.delete("1.0", tk.END)
            summary_text.config(state=tk.DISABLED)
            latest_content = ""
            status_label.config(text="❌ Error", foreground="red")

    threading.Thread(target=run).start()

