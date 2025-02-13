# Yomitan-Subtitle-Regularizer

Normalizes your .srt files to have a special quote that can be parsed by Yomitan.

## Usage

### Yomitan

In yomitan go to "Text Parsing" and change "Sentence termination characters" (You need advanced options enabled)
to "Custom, no newlines" then, "configure" and disable all quotes and termination characters.
Add a new one, with Quote type. The character should be `‹` and the termination character should be `›`. Disable both Start and End.

### Script

```cmd
python3 script.py <input-folder> <output-folder>
```

## Example

- **Input**

```txt
1
00:00:00,000 --> 00:00:01,000
Hello world!

2
00:00:01,000 --> 00:00:02,000
「こんにちは、
世界！」


```

- **Output**

```txt
1
00:00:00,000 --> 00:00:01,000
‹Hello, world!›

2
00:00:01,000 --> 00:00:02,000
‹「こんにちは、
世界！」›


```