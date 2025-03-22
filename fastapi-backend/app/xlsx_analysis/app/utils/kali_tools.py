import subprocess

def run_kali_tool(tool_name, args):
    try:
        result = subprocess.run([tool_name] + args, capture_output=True, text=True)
        return result.stdout
    except Exception as e:
        return f"Error running {tool_name}: {str(e)}"
