from bs4 import BeautifulSoup

def html_to_text(html_file_path, output_txt_path):
    with open(html_file_path, 'r', encoding='utf-8') as file:
        html_content = file.read()
    
    soup = BeautifulSoup(html_content, 'html.parser')
    plain_text = soup.get_text(separator='\n', strip=True)
    
    with open(output_txt_path, 'w', encoding='utf-8') as file:
        file.write(plain_text)
    print(f"Metin dosyası oluşturuldu: {output_txt_path}")

html_file = 'sawtooth_network.html' 
txt_file = 'cikti.txt'   
html_to_text(html_file, txt_file)
