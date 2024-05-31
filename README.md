<p align="right">
  [English]
  [<a href="README-ko.md">한국어</a>]
</p>

# SubtitleAdjuster

SubtitleAdjuster is a script that converts the format and encoding of smi and srt subtitle files and adjusts the sync time. This tool allows for the conversion of multiple subtitle files individually or in batches, offers the user the option to preview and choose which subtitle files to convert, and provides detailed debugging features.

> I created this tool because I thought it would be useful to be able to perform encoding conversion and sync time adjustment for entire series subtitle files in one go.

### Key Features

- Convert subtitle file formats (`srt` ↔ `smi`)
- Convert subtitle file encodings (`euc-kr` ↔ `utf-8`)
- Adjust subtitle sync time (increase or decrease in `milliseconds`)
- Convert individual or batch subtitle files
- Interactive mode or Quick execution option
- Output detailed logs via debug mode

### Installation

Clone this repository:

```
git clone https://github.com/micronzone/SubtitleAdjuster.git
cd SubtitleAdjuster
```

Grant execute permission:

```bash
chmod +x subtitle_adjuster
```

(Optional) Create and activate a virtual environment:

```
python3 -m venv .venve
source .venve/bin/activate  # Linux or macOS
.\.venve\Scripts\activate   # Windows
```

Install the `chardet` module.

To install via pip:

```
pip3 install chardet
```

To install via homebrew:

```
brew install python-chardet
```

Add alias (optional):

```bash
nano ~/.zshrc   # macOS ~/.zshrc, Linux `~/.bashrc` or `~/.zshrc`
alias subtitle_adjuster='/path/to/subtitle_adjuster'
```

```bash
source ~/.zshrc
```

### Usage

Convert individual subtitle files:

```
# Using alias (refer to installation) or run ./subtitle_adjuster from the SubtitleAdjuster directory
python3 subtitle_adjuster [options] [subtitle file path]
```

Convert multiple subtitle files in batch:

```
python3 subtitle_adjuster [options] [directory path]
```

### Options

- `-a`: Execute all options sequentially in interactive mode.
- `-e`: Convert encoding. Specify euc-kr or utf-8. Example: `-e euc-kr` or `-e utf-8`
- `-d`: Decrease subtitle sync time in milliseconds. Example: `-d 1000` (decrease by 1000ms)
- `-i`: Increase subtitle sync time in milliseconds. Example: `-i 1000` (increase by 1000ms)
- `-c` {`smi`,`srt`}: Convert subtitle file format. Example: `-c smi` or `-c srt`
- `--cc` {`KRCC`, `ENCC`}: Specify subtitle file format class. Example: `--cc KRCC` or `--cc ENCC`
- `--debug`: Enable debug mode to output detailed logs.

### Examples

Execute all options sequentially in interactive mode:

```
python3 subtitle_adjuster -a /path/to/dir/ or /path/to/file
```

Example with specified options (`srt -> smi`, `ENCC`, `utf-8`, `3.5 seconds slower`, `debug logs`):

```
python3 subtitle_adjuster -c smi --c ENCC -e utf-8 -i 3500 --debug /path/to/dir/ or /path/to/file
```

Convert subtitle file format to smi:

```
python3 subtitle_adjuster -c smi /path/to/dir/ or /path/to/file
```

Convert subtitle file format to srt:

```
python3 subtitle_adjuster -c srt /path/to/dir/ or /path/to/file
```

Specify subtitle file format class as KRCC:

```
python3 subtitle_adjuster --c KRCC /path/to/dir/ or /path/to/file
```

Specify subtitle file format class as ENCC:

```
python3 subtitle_adjuster --c ENCC /path/to/dir/ or /path/to/file
```

Convert subtitle file encoding to euc-kr:

```
python3 subtitle_adjuster -e euc-kr /path/to/dir/ or /path/to/file
```

Convert subtitle file encoding to utf-8:

```
python3 subtitle_adjuster -e utf-8 /path/to/dir/ or /path/to/file
```

Increase subtitle sync time by 1000ms (1 second=1000, adjust to desired value):

```
python3 subtitle_adjuster -i 1000 /path/to/dir/ or /path/to/file
```

Decrease subtitle sync time by 1000ms (1 second=1000, adjust to desired value):

```
python3 subtitle_adjuster -d 1000 /path/to/dir/ or /path/to/file
```

Convert with debug mode enabled:

```
python3 subtitle_adjuster -a --debug /path/to/dir/ or /path/to/file
```

### Updates

It's a good idea to check for updates to the SubtitleAdjuster repository!

```
cd SubtitleAdjuster
git status
```

Fetch changes:

```
git pull origin main
```

### Contributing

Thank you for contributing! To contribute to this project, follow these steps:

1. Fork this repository
2. Create a feature branch (git checkout -b micronzone/SubtitleAdjuster)
3. Commit your changes (git commit -m 'Add some SubtitleAdjuster')
4. Push to the branch (git push origin micronzone/SubtitleAdjuster)
5. Open a pull request

### License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.