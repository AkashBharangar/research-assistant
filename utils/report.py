from datetime import datetime
import os

def save_report(topic: str, report: str):

    os.makedirs("output", exist_ok=True)

    filename = topic.lower().replace(" ", "_") + ".md"

    path = os.path.join("output", filename)

    with open(path, "w", encoding="utf-8") as f:
        f.write(f"# Research Topic: \n\n")
        f.write(f"**Topic:** {topic} \n\n")
        f.write(f"**Generated on:** {datetime.now()} \n\n")
        f.write(f"--- \n\n")
        f.write(f"{report} \n\n")