import tkinter as tk
from tkinter import scrolledtext
import threading
import time

BG_COLOR = "#000000"
FG_COLOR = "#00FF00"
TITLE = "🦉 Cybersecurity by Khaled.S.Haddad"

topics = {
    "Advanced OSINT Techniques": {
        "tools": {
            "Maltego": "Visualize connections between domains, IPs, and people in a safe lab.",
            "Recon-ng": "Automate OSINT data collection conceptually.",
            "SpiderFoot": "Collect public intelligence data in a controlled environment.",
            "Shodan": "Search for exposed devices safely.",
            "Censys": "Analyze internet-wide scan data for learning purposes.",
            "Google Dorks": "Use advanced search queries conceptually.",
            "Whois": "Lookup domain ownership for analysis.",
            "NSLookup": "Resolve DNS records in lab.",
            "Amass": "Map subdomains safely in virtual lab.",
            "Social Media OSINT": "Gather open-source info from social media accounts for learning."
        },
        "guidance": "Master advanced techniques to gather public intelligence without interacting with target systems."
    },
    "Passive Reconnaissance Without Detection": {
        "tools": {
            "Passive DNS": "Analyze DNS history without active probing.",
            "WHOIS History": "Study domain registration changes safely.",
            "Archive.org": "Check historical website versions.",
            "Censys Passive Data": "Learn to query public scan data.",
            "Shodan Passive Queries": "Use Shodan info passively.",
            "Public SSL Certificates": "Analyze certificates without connecting to hosts.",
            "Metadata Analysis": "Inspect publicly shared documents.",
            "Netcraft": "Gather server information passively.",
            "Google Cache": "Use cached pages for analysis.",
            "Online Footprint Mapping": "Compile target's public digital footprint."
        },
        "guidance": "Collect intelligence in a completely passive manner, leaving no trace."
    },
    "Subdomain Enumeration & DNS Intelligence": {
        "tools": {
            "Amass": "Enumerate subdomains safely in lab.",
            "Sublist3r": "Discover subdomains using passive techniques.",
            "crt.sh": "Query certificate transparency logs.",
            "DNSdumpster": "Map DNS info without active scans.",
            "SecurityTrails": "Collect historical DNS data safely.",
            "Fierce": "Simulate DNS enumeration in lab.",
            "Knockpy": "Discover subdomains passively.",
            "Dig": "Query DNS records for learning purposes.",
            "Host": "Resolve hostnames in lab environment.",
            "Online Recon Tools": "Use online tools for safe subdomain collection."
        },
        "guidance": "Learn how to map domains, subdomains, and DNS infrastructure without detection."
    },
    "Email Harvesting and Phishing Target Profiling": {
        "tools": {
            "theHarvester": "Collect emails and related data from public sources.",
            "Hunter.io": "Discover email addresses for learning purposes.",
            "Email Permutator": "Generate possible target emails conceptually.",
            "LinkedIn OSINT": "Analyze profiles safely for research.",
            "Clearbit Connect": "Gather company email formats.",
            "Google Dorking": "Find public emails using search queries.",
            "VoilaNorbert": "Simulate email discovery safely.",
            "HaveIBeenPwned": "Check exposed emails in a learning environment.",
            "PhishTool Simulation": "Understand phishing techniques safely.",
            "Social Engineering Labs": "Learn profiling targets in lab environment."
        },
        "guidance": "Gather target emails and understand profiling without sending any phishing emails."
    }
}

class CyberMasterclassApp:
    def __init__(self, root):
        self.root = root
        self.root.title(TITLE)
        self.root.configure(bg=BG_COLOR)
        self.root.geometry("1200x850")

        self.text_area = scrolledtext.ScrolledText(root, bg=BG_COLOR, fg=FG_COLOR, font=("Consolas", 14))
        self.text_area.pack(fill="both", expand=True, padx=10, pady=10)
        self.text_area.insert(tk.END, "🦉 Welcome to the Cybersecurity Masterclass!\nSelect a topic and choose a tool (10 per topic) to see guidance.\n\n")
        self.text_area.configure(state='disabled')

        self.topic_frame = tk.Frame(root, bg=BG_COLOR)
        self.topic_frame.pack(fill="x", pady=5)

        rows = 3
        cols = (len(topics) + rows - 1) // rows
        topic_names = list(topics.keys())

        for i in range(rows):
            for j in range(cols):
                idx = i * cols + j
                if idx < len(topic_names):
                    topic_name = topic_names[idx]
                    btn = tk.Button(
                        self.topic_frame,
                        text=topic_name,
                        bg=BG_COLOR,
                        fg=FG_COLOR,
                        font=("Consolas", 10, "bold"),
                        width=35,
                        command=lambda t=topic_name: self.show_tool_options(t)
                    )
                    btn.grid(row=i, column=j, padx=5, pady=5, sticky="nsew")

        for j in range(cols):
            self.topic_frame.grid_columnconfigure(j, weight=1)

    def show_tool_options(self, topic_name):
        tools = topics[topic_name]["tools"]
        options_window = tk.Toplevel(self.root)
        options_window.title(f"Tools for {topic_name}")
        options_window.configure(bg=BG_COLOR)
        options_window.geometry("700x500")

        tk.Label(options_window, text=f"Choose a tool for {topic_name}", bg=BG_COLOR, fg=FG_COLOR, font=("Consolas", 12, "bold")).pack(pady=10)

        for tool_name, tool_desc in tools.items():
            btn = tk.Button(
                options_window,
                text=tool_name,
                bg=BG_COLOR,
                fg=FG_COLOR,
                font=("Consolas", 11),
                width=50,
                command=lambda d=tool_desc, g=topic_name: self.display_tool_description(g, d)
            )
            btn.pack(pady=3)

    def display_tool_description(self, topic_name, description):
        self.text_area.configure(state='normal')
        content = f"\n🦉 {topic_name} Tool Guidance:\n{description}\n\n"
        for char in content:
            self.text_area.insert(tk.END, char)
            self.text_area.see(tk.END)
            self.text_area.update()
            time.sleep(0.002)
        self.text_area.configure(state='disabled')

if __name__ == "__main__":
    root = tk.Tk()
    app = CyberMasterclassApp(root)
    root.mainloop()

