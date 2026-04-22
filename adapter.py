import csv


#SCRIPT USED TO ADAPT ANOTHER CSV FOUND ONLINE TO OUR FORMAT
input_file = "./bbc_articles_vava.csv"
output_file = "output2.csv"

with open(input_file, newline='', encoding='utf-8') as infile, \
     open(output_file, 'w', newline='', encoding='utf-8') as outfile:

    reader = csv.DictReader(infile)  
    
    fieldnames = ['title', 'text', 'category', 'url']
    writer = csv.DictWriter(outfile, fieldnames=fieldnames, delimiter=';')
    writer.writeheader()

    for row in reader:
        content = row.get('content', '').strip()

        if not content:
            continue

        new_row = {
            'title': row.get('title', '').strip(),
            'text': content,
            'category': row.get('category', '').strip(),
            'url': ''
        }
        writer.writerow(new_row)