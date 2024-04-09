import os

prefix='<html lang="en">\n<head>\n	<meta charset="UTF-8">\n	<meta name="viewport" content="width=device-width\ninitial-scale=1.0">\n	<title>Document</title>\n	<link rel="stylesheet" href="styles.css">\n</head>\n\n<body class="text-red-500 bg-gray-100">\n'
suffix='\n</body>\n</html>'

def edit_html_files(directory_path):
    # List all files in the directory
    files = os.listdir(directory_path)
	
    allowed_edits=0
	
    # Iterate over each file
    for file_name in files:
        if file_name.endswith('.html'):
        
            if allowed_edits==0:
        	    input(allowed_edits)
        
            file_path = os.path.join(directory_path, file_name)
            with open(file_path, 'r') as file:
                # Read the contents of the file
                html_content = file.read()


            if html_content[:5] != "<html" :
                edited_html_content = prefix + html_content + suffix
            else:
                print(html_content)
                edited_html_content = html_content

            # Write the edited content back to the file
            with open(file_path, 'w') as file:
                file.write(edited_html_content)

            print(f"Edited file: {file_name}")

# Provide the directory path here
directory_path = '.'
edit_html_files(directory_path)

