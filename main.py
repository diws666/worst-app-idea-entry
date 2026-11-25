import os

ENTRY_SENTENCE = (
    "Meet LinePal: an app that saves your spot in queues you never joined, "
    "by paying strangers to stand in them on your behalf, for $9.99 a month."
)


def write_entry(output_dir):
    entry_path = os.path.join(output_dir, "entry.txt")
    with open(entry_path, "w", encoding="utf-8") as f:
        f.write(ENTRY_SENTENCE)


def main():
    write_entry(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))


if __name__ == "__main__":
    main()
