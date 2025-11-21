import sys
import os
import re
import json

def main():

    try:
        # Split flag into parts to preserve the random token ==================
        # Standard cmgr/picoCTF flags often come as "picoCTF{...}" or just "flag{...}"
        # We want to inject our own theme prefix while keeping the random hash.
        
        raw_flag = os.environ.get("FLAG")

        if not raw_flag:
            print("Flag was not read from environment. Using default.")
            raw_flag = "picoCTF{default_random_hash_1234}"
        
        # Extract the content inside the curly braces
        flag_match = re.search(r"\{.*\}$", raw_flag)
        if flag_match is None:
            # Fallback if the input flag format is unexpected
            flag_content = "default_hash_value"
        else:
            # Remove the surrounding {}
            flag_content = flag_match.group()[1:-1]

        # Construct the final Vibe Check flag
        # e.g., picoCTF{t1m3_is_k3y_abcd12345}
        final_flag = "picoCTF{t1m3_is_k3y_" + flag_content + "}"
        
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