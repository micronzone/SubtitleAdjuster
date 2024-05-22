import os
import re
import sys
import chardet
import codecs
import argparse

def detect_encoding(file_path):
    with open(file_path, 'rb') as f:
        rawdata = f.read()
    result = chardet.detect(rawdata)
    return result['encoding']

def convert_encoding(file_path, target_encoding, debug=False):
    source_encoding = detect_encoding(file_path)
    if debug:
        print(f"[DEBUG] Converting {file_path} from {source_encoding} to {target_encoding}")
    if source_encoding.lower() == target_encoding.lower():
        if debug:
            print(f"[DEBUG] Source and target encodings are the same. Skipping conversion for {file_path}")
        return source_encoding
    try:
        with codecs.open(file_path, 'r', source_encoding) as f:
            content = f.read()
        with codecs.open(file_path, 'w', target_encoding) as f:
            f.write(content)
        if debug:
            print(f"[DEBUG] Conversion successful for {file_path}")
        return target_encoding
    except Exception as e:
        print(f"[ERROR] Failed to convert {file_path}: {e}")
        return None

def adjust_sync(file_path, offset, encoding, debug=False):
    if file_path.lower().endswith('.srt'):
        adjust_sync_srt(file_path, offset, encoding, debug)
    elif file_path.lower().endswith('.smi'):
        adjust_sync_smi(file_path, offset, encoding, debug)
    else:
        print(f"[ERROR] Unsupported file format: {file_path}")

def adjust_sync_srt(file_path, offset, encoding, debug=False):
    if debug:
        print(f"[DEBUG] Adjusting sync for {file_path} by {offset} milliseconds")
    try:
        with codecs.open(file_path, 'r', encoding) as f:
            lines = f.readlines()

        new_lines = []
        for line in lines:
            new_lines.append(adjust_line_sync_srt(line, offset, debug))

        with codecs.open(file_path, 'w', encoding) as f:
            f.writelines(new_lines)
        if debug:
            print(f"[DEBUG] Sync adjustment successful for {file_path}")
    except Exception as e:
        print(f"[ERROR] Failed to adjust sync for {file_path}: {e}")

def adjust_line_sync_srt(line, offset, debug=False):
    def change_timecode(tc, offset):
        h, m, s, ms = map(int, re.split('[:,]', tc))
        total_ms = ((h * 3600 + m * 60 + s) * 1000) + ms + offset
        if total_ms < 0:
            total_ms = 0
        new_h = total_ms // 3600000
        total_ms %= 3600000
        new_m = total_ms // 60000
        total_ms %= 60000
        new_s = total_ms // 1000
        new_ms = total_ms % 1000
        return f"{new_h:02}:{new_m:02}:{new_s:02},{new_ms:03}"

    pattern = re.compile(r"(\d{2}:\d{2}:\d{2},\d{3})")
    matches = pattern.findall(line)
    if matches:
        for match in matches:
            new_tc = change_timecode(match, offset)
            if debug:
                print(f"[DEBUG] Changing timecode {match} to {new_tc}")
            line = line.replace(match, new_tc)
    return line

def adjust_sync_smi(file_path, offset, encoding, debug=False):
    if debug:
        print(f"[DEBUG] Adjusting sync for {file_path} by {offset} milliseconds")
    try:
        with codecs.open(file_path, 'r', encoding) as f:
            lines = f.readlines()

        new_lines = []
        for line in lines:
            new_lines.append(adjust_line_sync_smi(line, offset, debug))

        with codecs.open(file_path, 'w', encoding) as f:
            f.writelines(new_lines)
        if debug:
            print(f"[DEBUG] Sync adjustment successful for {file_path}")
    except Exception as e:
        print(f"[ERROR] Failed to adjust sync for {file_path}: {e}")

def adjust_line_sync_smi(line, offset, debug=False):
    def change_timecode(tc, offset):
        total_ms = int(tc) + offset
        if total_ms < 0:
            total_ms = 0
        return str(total_ms)

    pattern = re.compile(r"(<SYNC Start=)(\d+)(>)")
    matches = pattern.findall(line)
    if matches:
        for match in matches:
            new_tc = change_timecode(match[1], offset)
            if debug:
                print(f"[DEBUG] Changing timecode {match[1]} to {new_tc}")
            line = line.replace(f"{match[0]}{match[1]}{match[2]}", f"{match[0]}{new_tc}{match[2]}")
    return line

def process_files(files, encoding=None, sync_offset=None, debug=False):
    for file_path in files:
        if not file_path.lower().endswith(('.srt', '.smi')):
            print(f"[ERROR] Unsupported file format: {file_path}")
            continue

        if encoding:
            source_encoding = convert_encoding(file_path, encoding, debug)
            if not source_encoding:
                continue
        else:
            source_encoding = detect_encoding(file_path)

        if sync_offset is not None:
            adjust_sync(file_path, sync_offset, source_encoding, debug)

def get_files_from_path(path):
    if os.path.isfile(path):
        return [path]
    elif os.path.isdir(path):
        return [os.path.join(path, f) for f in os.listdir(path) if f.lower().endswith(('.srt', '.smi'))]
    else:
        print(f"[ERROR] Invalid path: {path}")
        return []

def interactive_mode(path, debug=False):
    files = get_files_from_path(path)
    if not files:
        print(f"[ERROR] No subtitle files found in {path}")
        return

    print("Select encoding conversion:")
    print("1. EUC-KR")
    print("2. UTF-8")
    encoding_choice = input("Enter choice (1/2): ").strip()
    encoding = 'euc-kr' if encoding_choice == '1' else 'utf-8' if encoding_choice == '2' else None

    sync_choice = input("Enter sync adjustment (e.g., +1000, -1000): ").strip()
    try:
        sync_offset = int(sync_choice)
    except ValueError:
        sync_offset = None

    process_files(files, encoding, sync_offset, debug)

def main():
    parser = argparse.ArgumentParser(description="Subtitle file encoding converter and sync adjuster")
    parser.add_argument('path', help="Path to subtitle file or directory")
    parser.add_argument('-a', action='store_true', help="Run in interactive mode")
    parser.add_argument('-e', type=str, choices=['euc-kr', 'utf-8'], help="Encoding to convert to")
    parser.add_argument('-d', type=int, help="Decrease sync time by milliseconds")
    parser.add_argument('-i', type=int, help="Increase sync time by milliseconds")
    parser.add_argument('--debug', action='store_true', help="Enable debug logs")

    args = parser.parse_args()

    if args.a:
        interactive_mode(args.path, args.debug)
    else:
        sync_offset = None
        if args.d:
            sync_offset = -args.d
        elif args.i:
            sync_offset = args.i

        files = get_files_from_path(args.path)
        if not files:
            print(f"[ERROR] No subtitle files found in {args.path}")
            return

        process_files(files, args.e, sync_offset, args.debug)

if __name__ == "__main__":
    main()

