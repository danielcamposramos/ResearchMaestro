
# ResearchMaestro Deployment Script
import os
import shutil

def compress_system(output_file="ResearchMaestroChatGPT.zip"):
    system_path = "/mnt/data/ResearchMaestroTest"
    if not os.path.exists(system_path):
        return "System directory not found."
    
    output_path = f"/mnt/data/{output_file}"
    shutil.make_archive(output_path.replace('.zip', ''), 'zip', system_path)
    return output_path

if __name__ == "__main__":
    print(compress_system())
