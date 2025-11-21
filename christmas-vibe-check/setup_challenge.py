import sys
import os
import re
import json

def main():

    try:

        raw_flag = os.environ.get("FLAG")

        if not raw_flag:
            print("Flag was not read from environment. Using default.")
            raw_flag = "picoCTF{default_random}"
        
        # Extract the content inside the curly braces
        flag_match = re.search(r"\{.*\}$", raw_flag)
        if flag_match is None:
            # Fallback if the input flag format is unexpected
            flag_content = "default_hash_value"
        else:
            # Remove the surrounding {}
            flag_content = flag_match.group()[1:-1]

        # Construct the final flag
        final_flag = "picoCTF{all_the_wishes_come_true_" + flag_content + "}"
        
        # Write the flag to the secure directory
        # The app will read from this file
        with open("/challenge/flag", "w") as f:
            f.write(final_flag)
        # =====================================================================

        # Create and update metadata.json =====================================
        metadata = {}
        metadata['flag'] = str(final_flag)
        json_metadata = json.dumps(metadata)
        
        with open("/challenge/metadata.json", "w") as f:
            f.write(json_metadata)
        # =====================================================================

    except Exception as e:
        print(f"Error in setup-challenge: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()