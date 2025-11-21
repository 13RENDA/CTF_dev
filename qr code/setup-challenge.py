import sys
import os
import subprocess
import re
import json

# Import QR challenge generator
# Try Docker path first, then local path
if os.path.exists('/challenge'):
    sys.path.insert(0, '/challenge')
    challenge_dir = '/challenge'
else:
    # Local testing - use current directory
    challenge_dir = os.path.dirname(os.path.abspath(__file__)) or '.'
    sys.path.insert(0, challenge_dir)

from qr_challenge import generate_qr_challenge

def main():

    try:
        # Get flag from environment ============================================
        flag = os.environ.get("FLAG")

        if not flag or flag == "":
            print("Flag was not read from environment. Aborting.")
            sys.exit(-1)
        else:
            # Get hash part - handle both with and without curly braces
            flag_rand = re.search("{.*}$", flag)
            if flag_rand == None:
                # No curly braces - treat entire value as the random part
                flag_rand = flag
            else:
                # Extract content from curly braces
                flag_rand = flag_rand.group()
                flag_rand = flag_rand[1:-1]

        flag = "picoCTF{enjoy_winter_break_" + flag_rand + "}"
        
        # Write flag file
        flag_file = os.path.join(challenge_dir, "flag")
        with open(flag_file, "w") as f:
            f.write(flag)
        print(f"Flag written to {flag_file}")
        # =====================================================================

        # Generate QR code challenge files ====================================
        print("Generating QR code challenge files...")
        artifacts_dir = os.path.join(challenge_dir, "cmgr", "artifacts")
        os.makedirs(artifacts_dir, exist_ok=True)
        
        result = generate_qr_challenge(flag, output_dir=artifacts_dir)
        print(f"[+] QR challenge files generated in {artifacts_dir}")
        # =====================================================================

        # Create and update metadata.json =====================================
        metadata = {}
        metadata['flag'] = str(flag)
        json_metadata = json.dumps(metadata)
        
        metadata_file = os.path.join(challenge_dir, "metadata.json")
        with open(metadata_file, "w") as f:
            f.write(json_metadata)
        print(f"Metadata written to {metadata_file}")
        # =====================================================================

    except subprocess.CalledProcessError:
        print("A subprocess has returned an error code")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    main()