
# ResearchFileMaster Module with Deployment Automation
import zlib
import os
import subprocess

class ResearchFileMaster:
    def __init__(self):
        self.file_cache = {}

    def add_to_cache(self, filename, content):
        compressed_content = zlib.compress(content.encode())
        self.file_cache[filename] = compressed_content

    def retrieve_from_cache(self, filename):
        if filename in self.file_cache:
            return zlib.decompress(self.file_cache[filename]).decode()
        return "File not found in cache."

    def trigger_deployment(self):
        """Trigger the deployment process to package the system."""
        deployment_script = "/mnt/data/ResearchMaestroTest/deployment_script.py"
        if os.path.exists(deployment_script):
            subprocess.run(["python3", deployment_script], check=True)
            print("Deployment process completed successfully.")
        else:
            print("Deployment script not found.")
