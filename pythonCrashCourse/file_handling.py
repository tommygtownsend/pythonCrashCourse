# =======================================
# FILE HANDLING (Text Files)
# =======================================
# We'll cover:
#  - open() basics and file modes
#  - reading: read(), readline(), readlines(), iterating lines
#  - writing/appending text
#  - why context managers (`with`) are the safest way
#  - relative vs absolute paths + encodings


# =======================================
# Paths & Where is my file?
# =======================================
# If you use a plain filename like "notes.txt", Python looks in the CURRENT WORKING DIRECTORY.
# You can use a relative path like "data/notes.txt" or an absolute path like "/home/me/data/notes.txt".
# Tip: On Windows use raw strings r"C:\path\to\file.txt" or forward slashes "C:/path/to/file.txt".


# =======================================
# Opening a file with open()
# =======================================
# open(path, mode, encoding)
# Common text modes:
#   "r"  = read (default; error if missing)
#   "w"  = write (create or OVERWRITE)
#   "a"  = append (create if missing; add to end)
#   "r+" = read & write (must exist)
# Add "t" for text (default) or "b" for binary (e.g., "rb")
# Always set encoding for text files (e.g., "utf-8")

path = "example.txt"

# BAD pattern (works, but you must remember to close):
f = open(path, mode="w", encoding="utf-8")
f.write("First line\n")
f.write("Second line\n")
f.close()  # If you forget this, you can leak resources!


# =======================================
# Context Manager: with ... as ...
# =======================================
# Using `with` auto-closes the file, even if errors happen. This is the recommended pattern.

# Write (overwrite) a file
with open(path, mode="w", encoding="utf-8") as f:
    f.write("Hello, file handling! 👋\n")
    f.write("This will overwrite any previous content.\n")

# Append to the same file (adds to the end)
with open(path, mode="a", encoding="utf-8") as f:
    f.write("Appended line 1\n")
    f.write("Appended line 2\n")


# =======================================
# Reading Text Files
# =======================================
# 1) read()     -> whole file as one string (careful with huge files)
# 2) readline() -> one line at a time (keeps the trailing '\n')
# 3) readlines()-> list of all lines (each ending with '\n')
# 4) Iterate file object -> memory-friendly way to stream lines

# 1) read()
with open(path, mode="r", encoding="utf-8") as f:
    content = f.read()
print("[read()] Entire file:\n", content)

# 2) readline()
with open(path, mode="r", encoding="utf-8") as f:
    first_line = f.readline()
    second_line = f.readline()
print("[readline()] first:", first_line.strip())
print("[readline()] second:", second_line.strip())

# 3) readlines()
with open(path, mode="r", encoding="utf-8") as f:
    lines = f.readlines()
print("[readlines()] got", len(lines), "lines")

# 4) Iterate line-by-line (best for large files)
print("[iterate] lines without loading everything:")
with open(path, mode="r", encoding="utf-8") as f:
    for i, line in enumerate(f, start=1):
        print(f"Line {i} -> {line.strip()}")


# =======================================
# Writing Tricks (text)
# =======================================
# print(..., file=f) lets you write with the same print() call you use for console
data = ["alpha", "bravo", "charlie"]
with open("words.txt", mode="w", encoding="utf-8") as f:
    for word in data:
        print(word, file=f)  # auto adds newline

# Overwriting vs Appending demo
with open("words.txt", "a", encoding="utf-8") as f:
    f.write("delta\n")  # appended at the end


# =======================================
# Safer Reads: existence check & error handling
# =======================================
import os

maybe_path = "missing.txt"
if os.path.exists(maybe_path):
    with open(maybe_path, "r", encoding="utf-8") as f:
        print("Missing.txt has", len(f.readlines()), "lines")
else:
    print("missing.txt does not exist (safe to skip).")

# Try/except for unexpected errors (e.g., permissions)
try:
    with open("/protected/system.txt", "r", encoding="utf-8") as f:
        secret = f.read()
except FileNotFoundError:
    print("Not found: /protected/system.txt")
except PermissionError:
    print("Permission denied: /protected/system.txt")


# =======================================
# Read & Write (r+) — careful!
# =======================================
# r+ allows reading and writing, but the file must exist.
# The write position is wherever the file pointer currently is.

with open(path, "r+", encoding="utf-8") as f:
    original = f.read()            # read moves pointer to end
    f.seek(0)                      # move pointer to start
    f.write("OVERWROTE START\n")   # overwrite from beginning
    f.seek(0, os.SEEK_END)         # move pointer to end of file
    f.write("...and wrote at the end\n")


# =======================================
# Newlines and Encoding
# =======================================
# - text mode handles '\n' across platforms
# - specify encoding="utf-8" for non-ASCII safely
# - if you see weird characters, the file might use a different encoding

with open("utf8_demo.txt", "w", encoding="utf-8") as f:
    f.write("naïve café — emojis ✅\n")

with open("utf8_demo.txt", "r", encoding="utf-8") as f:
    print("UTF-8 demo:", f.read().strip())


# =======================================
# Context Managers for multiple files
# =======================================
# You can open multiple files at once with a single `with`.
with open("source.txt", "w", encoding="utf-8") as src:
    src.write("line A\nline B\nline C\n")

with open("source.txt", "r", encoding="utf-8") as src, \
     open("copy.txt",   "w", encoding="utf-8") as dst:
    for line in src:
        dst.write(line)

# Verify copy
with open("copy.txt", "r", encoding="utf-8") as f:
    print("Copied:\n" + f.read())


# =======================================
# Practice !!!
# =======================================
# 1) Create a file called "practice.txt" and write 3 lines to it.
# 2) Append two more lines.
# 3) Read it back three different ways: read(), readline(), and iterate.
# 4) Make a function write_lines(path, lines) that writes each string in `lines` to `path`.
# 5) Make a function tail(path, n=10) that prints the last n lines of a big text file efficiently.


# =======================================
# Bonus: Small Utilities
# =======================================
def write_lines(path, lines, mode="w", encoding="utf-8"):
    """Write an iterable of strings to a file, each on its own line."""
    with open(path, mode, encoding=encoding) as f:
        for line in lines:
            # Ensure newline endings
            if not line.endswith("\n"):
                line += "\n"
            f.write(line)

def read_first_n(path, n=5, encoding="utf-8"):
    """Read only the first n lines (useful for huge files)."""
    out = []
    with open(path, "r", encoding=encoding) as f:
        for i, line in enumerate(f):
            out.append(line.rstrip("\n"))
            if i + 1 >= n:
                break
    return out

# Demo of utilities
write_lines("practice.txt", ["one", "two", "three"])
write_lines("practice.txt", ["four", "five"], mode="a")  # append
print("First 3 lines:", read_first_n("practice.txt", 3))


# =======================================
# TL;DR
# =======================================
# - Use `with open(..., encoding='utf-8') as f:` for safety and auto-close.
# - Choose mode: "r" read, "w" overwrite, "a" append, "r+" read+write.
# - read()/readline()/readlines()/iteration — pick based on file size needs.
# - Prefer iterating for big files to save memory.
# - Know your working directory or pass absolute paths to avoid "file not found".
