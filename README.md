# God's Eye 👁️

> **An Intelligent, Human-in-the-Loop OSINT Automation Framework.**

![God's Eye](assets/Banner.png)

**God's Eye** is a modular reconnaissance tool designed to automate the digital footprinting process while maintaining high accuracy. Unlike rigid scrapers that fail when a specific source is missing, God's Eye uses a **configurable priority engine** to pivot across multiple platforms (LinkedIn, Twitter, Behance, etc.) based on user-defined strategies.

## 🚀 How It Works

1.  **Configurable Strategy:** You define the "search mode" (e.g., *Professional* prioritizes LinkedIn $\rightarrow$ GitHub; *Social* prioritizes Twitter $\rightarrow$ Instagram; *Informational* prioritizes $\rightarrow$ Public Data Sources).
2.  **Smart Fallback:** If the primary source yields no results, the engine automatically pivots to the next available source, ensuring the search never hits a dead end.
3.  **Human-in-the-Loop (HITL):** Between pivots, the tool presents potential profile matches. You verify the correct "Persona," and that verified data is used to seed the next search.
4.  **Dossier Generation:** All verified intelligence is aggregated into a structured report (PDF/HTML/MD).

## ✨ Key Features

* **Dynamic Source Fallback:** Handles missing profiles gracefully by switching to alternate data sources.
* **Case Management:** Built-in database to save, view, and delete investigations (`run_id`).
* **Human-in-the-Loop Verification:** Prevents false data propagation by allowing manual target confirmation.
* **Multi-Format Export:** Generate clean HTML/PDF/MD dossiers for your investigations.

## 🛠️ Installation

God's Eye is packaged for easy installation via pip.

```bash
# Clone the repository
git clone [https://github.com/Shajal-Kumar/Gods-Eye.git](https://github.com/Shajal-Kumar/Gods-Eye.git)

# Navigate to the directory
cd Gods-Eye

# Install as a command-line tool
pip install .

Here is the text converted into clean Markdown, ready to be pasted into your `README.md`.

```

## 💻 Usage

Once installed, use `godseye` followed by a subcommand.

### 1. Start a Search
Initiate a new investigation using known details.

```bash
godseye search -n "John Doe" -l "New York" -e "Google"

```

**Flags:**

* `-n, --name` (Required): Target's full name.
* `-u, --username`: Known username or handle.
* `-l, --location`: Target's city or region.
* `-e, --employer`: Target's workplace.
* `-m, --email`: Target's email address.
* `-nc, --no-cache`: Force a fresh search (ignore cached results).

### 2. View Past Investigations

Check the status or details of previous runs using the Run ID.

```bash
godseye view -r 12345

```

### 3. Export Dossier

Generate a final report for a completed run.

```bash
godseye export -r 12345 -f pdf

```

**Flags:**

* `-f, --format`: Output format (`html` or `pdf` or `md`). Default is `html`.

### 4. Manage Data

Delete old investigations to clean up the database.

```bash
godseye delete -r 12345

```

## 🗺️ Roadmap & Future Integration

* [ ] **Public Database Integration:**
* **Indian Context:** Zauba Corp (Corporate Directors), eCourts services.
* **Global:** Breach data (HIBP) and username enumeration.


* [ ] **Visual Graphing:** Generating a relationship map of the target's digital presence.

## ⚠️ Disclaimer

This tool is designed for **educational purposes, authorized security testing (Red Teaming), and open-source intelligence research only**. The author is not responsible for any misuse of this tool. Always ensure you have permission or are conducting research on public data.

---

*Created by* [Shajal Kumar](https://github.com/Shajal-Kumar)
