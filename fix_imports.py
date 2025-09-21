import os
import re

BASE_DIR = "/Users/homesachin/Desktop/zoneone/practice/YT_video_share_library"

# Patterns to replace
patterns = {
    r"from\s+videos(\..*)": r"from YT_video_share_library.videos\1",
    r"from\s+users(\..*)": r"from YT_video_share_library.users\1",
    r"from\s+reactions(\..*)": r"from YT_video_share_library.reactions\1",
    r"import\s+videos(\..*)": r"import YT_video_share_library.videos\1",
    r"import\s+users(\..*)": r"import YT_video_share_library.users\1",
    r"import\s+reactions(\..*)": r"import YT_video_share_library.reactions\1",
}

def fix_imports_in_file(file_path):
    with open(file_path, "r") as f:
        content = f.read()

    new_content = content
    for pattern, replacement in patterns.items():
        new_content = re.sub(pattern, replacement, new_content)

    if new_content != content:
        print(f"🔧 Fixed imports in: {file_path}")
        with open(file_path, "w") as f:
            f.write(new_content)

def scan_and_fix():
    for root, _, files in os.walk(BASE_DIR):
        for file in files:
            if file.endswith(".py"):
                fix_imports_in_file(os.path.join(root, file))

if __name__ == "__main__":
    scan_and_fix()
    print("✅ Import fix completed!")
