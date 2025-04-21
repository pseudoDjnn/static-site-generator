import os, sys
import shutil

from copystatic import copy_files_recursive
from gencontent import generate_pages_recursive

dir_path_static = "./static"
# Switched from "./public" to "./docs" to place onto github pages
dir_path_public = "./docs"
dir_path_content = "./content"
template_path = "./template.html"
default_basepath = "/"


def main():
    basepath = default_basepath
    if len(sys.argv) > 1:
        basepath = sys.argv[1]
        
    print("Deleting public directory...")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)
        
    print("Copying static files to public directory...")
    copy_files_recursive(dir_path_static, dir_path_public)

    print("Generating content...")
    generate_pages_recursive(dir_path_content, template_path, dir_path_public, basepath)
    
if __name__=="__main__":
    main()
