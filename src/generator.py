from openai import OpenAI


class ArticleToHtmlGenerator:
    def __init__(self, api_key):
        self.client = OpenAI(api_key=api_key)

    def read_article(self, file_path):
        """Wczytuje zawartość pliku tekstowego z artykułem."""
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                return file.read()
        except FileNotFoundError:
            raise Exception(f"Nie znaleziono pliku: {file_path}")

    def preprocess_with_ai(self, content):
        """Przetwarza artykuł z wykorzystaniem API OpenAI."""
        
        prompt = """
        Przekształć poniższy artykuł w kod HTML, stosując następujące zasady:
        1. Użyj odpowiednich tagów HTML do strukturyzacji treści (nagłówki, paragrafy, listy itp.)
        2. W odpowiednich miejscach wstaw znaczniki img z src="image_placeholder.jpg"
        3. Każdy znacznik img powinien mieć atrybut alt z dokładnym promptem do wygenerowania grafiki przez AI, nawiązującym do treści artykułu
        4. Pod każdą grafiką umieść podpis używając tagu figcaption wewnątrz figure
        5. Nie dodawaj tagów html, head, body, ani żadnego CSS czy JavaScript. Kod HTML powinien dać się wkleić między znaczniki body bez ingerencji.

        Artykuł do przetworzenia:

        {content}
        """

        try:
            response = self.client.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {
                        "role": "system",
                        "content":  """
                                    Jesteś ekspertem w tworzeniu semantycznego kodu HTML, który jest zgodny z zasadami dostępności i SEO.
                                    Twoim zadaniem jest przekształcenie artykułu w kod HTML, który będzie czytelny i przyjazny dla ludzi i wyszukiwarek.
                                    """
                    },
                    {
                        "role": "user",
                        "content": prompt.format(content=content)
                    }
                ],
                temperature=0.6
            )
            return response.choices[0].message.content
        
        except Exception as e:
            raise Exception(f"Błąd podczas przetwarzania przez API OpenAI: {str(e)}")
        
    def _strip_if_needed(self, html_content):
        """Usuwa nadmiarowe znaki z wygenerowanego kodu HTML."""
        if html_content.startswith("```html\n") and html_content.endswith("\n```"):
            html_content = html_content.strip("```html\n").strip("\n```")
        return html_content

    def save_to_html(self, html_content, output_path):
        """Zapisuje wygenerowany kod HTML do pliku."""
        
        html_content = self._strip_if_needed(html_content) # Usuwa znaki formatowania kodu, dodawane przez gpt
                                                           # żeby dało się wkleić kod bezpośrednio do body
        
        try:
            with open(output_path, 'w', encoding='utf-8') as file:
                file.write(html_content)
        except Exception as e:
            raise Exception(f"Błąd podczas zapisywania pliku: {str(e)}")