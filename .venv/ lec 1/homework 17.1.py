import re

def delete_html_tags(html_file=r"C:\Users\User\Downloads\draft.html",result_file=r"C:\Users\User\Downloads\cleaned.txt"):
    with open(html_file, 'r', encoding= 'utf-8') as f:
        html=f.read()

        cleaned_text=re.sub(r'<.*?>', '', html,flags=re.DOTALL)
        lines = [line.strip() for line in cleaned_text.splitlines() if line.strip()]
        cleaned_text_final= '\n'.join(lines)
        with open(result_file, 'w', encoding = 'utf-8') as f:
            f.write(cleaned_text_final)

delete_html_tags()

