import subprocess
import os
import json

def run_command(command):
    """Execute a shell command and return the output."""
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        return result.stdout.strip()
    except Exception as e:
        return f"Error executing {command}: {str(e)}"

def analyze_exe(file_path):
    """Run various CLI-based EXE analysis commands and save results."""
    report = {
        "file": file_path,
        "malware_scan": "",
        "file_type": "",
        "architecture": "",
        "suspicious_strings": [],
        "pe_header": "",
        "sha256_hash": "",
        "exif_metadata": "",
        "verdict": "SAFE",
        "reason": "No suspicious activity detected.",
        "suggested_action": "No action required. The file appears to be safe."
    }
    
    # 1. Scan for Malware Signatures (ClamAV)
    clamav_result = run_command(f"clamscan --no-summary {file_path}")
    report["malware_scan"] = clamav_result
    
    # 2. Identify File Type & Architecture
    report["file_type"] = run_command(f"file {file_path}")
    report["architecture"] = run_command(f"objdump -f {file_path} | grep 'architecture'")
    
    # 3. Extract Suspicious Strings
    for keyword in ['http', 'cmd', 'powershell']:
        result = run_command(f"strings {file_path} | grep -i '{keyword}'")
        if result:
            report["suspicious_strings"].append(result)
    
    # 4. Analyze PE Header
    report["pe_header"] = run_command(f"readpe -h {file_path}")
    
    # 5. Generate Hashes
    report["sha256_hash"] = run_command(f"sha256sum {file_path}")
    
    # 6. Extract Metadata using ExifTool
    report["exif_metadata"] = run_command(f"exiftool {file_path}")
    
    # Automatic Analysis and Verdict
    if "FOUND" in clamav_result:
        report["verdict"] = "SUSPICIOUS"
        report["reason"] = "ClamAV detected malware signatures in the file."
        report["suggested_action"] = "Do not execute the file. Delete it immediately and avoid downloading files from untrusted sources. Consider using a sandbox environment for further analysis."
    elif report["suspicious_strings"]:
        report["verdict"] = "SUSPICIOUS"
        report["reason"] = "Suspicious strings (URLs, command execution, or PowerShell scripts) found in the file."
        report["suggested_action"] = "Investigate the extracted strings to determine potential threats. Avoid executing the file, and consider running it in an isolated virtual machine."
    
    return report
