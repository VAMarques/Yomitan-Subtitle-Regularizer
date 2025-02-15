import os
import sys
# Define input and output folders
INPUT_FOLDER = sys.argv[1] # "input"
OUTPUT_FOLDER = sys.argv[2] # "output"

# Ensure output folder exists
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# Process each .srt file in the input folder
for filename in os.listdir(INPUT_FOLDER):
    if filename.endswith(".srt"):
        input_path = os.path.join(INPUT_FOLDER, filename)
        output_path = os.path.join(OUTPUT_FOLDER, filename)
        
        with open(input_path, "r", encoding="utf-8") as f:
            lines = f.readlines()
        
        modified_lines = []
        k = 1 # Current subtitle number
        line_1 = ""
        line_2 = ""
        line_3 = ""
        add_line = ""
        while lines:
            line_1 = line_2
            line_2 = line_3
            # Sometimes there's a zero-width space at the beginning of the line
            # It is removed as to not cause problems.
            line_3 = lines.pop(0).strip().strip("﻿")

            if line_2 == "" and line_3 == str(k):
                if len(lines) >= 2:
                    line_1 = lines.pop(0).strip() # Subtitle time indicator, gets ignored next iteration
                    line_2 = lines.pop(0).strip() # Almost certainly, the subtitle itself

                    if k != 1: # Not the first line.
                        modified_lines.append(add_line + "›\n") # Add previous line
                        modified_lines.append("\n") # Add empty line
                    modified_lines.append(str(k) + "\n") # Add subtitle number
                    modified_lines.append(line_1 + "\n") # Add time indicator

                    add_line = "‹" + line_2
                    if len(lines) >= 1:
                        line_3 = lines.pop(0).strip() # Unknown, possibly more subtitle
                    if len(lines) == 0: # No more lines.
                        if line_3 != "":
                            add_line = add_line + "\n" + line_3
                        modified_lines.append(add_line + "›\n")
                    k += 1
                    continue
                else:
                    print(f"Error: Unexpected end of file at {filename}")
                    break
            else:
                if line_2 != "":
                    add_line = add_line + "\n" + line_2
                if len(lines) == 0:
                    if line_3 != "":
                        add_line = add_line + "\n" + line_3
                    modified_lines.append(add_line + "›\n")
                continue
        modified_lines.append("\n") # Add extra empty line
        with open(output_path, "w", encoding="utf-8") as f:
            f.writelines(modified_lines)

print(f"Processed all .srt files from '{INPUT_FOLDER}' to '{OUTPUT_FOLDER}'.")
