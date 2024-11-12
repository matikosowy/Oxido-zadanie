from generator import ArticleToHtmlGenerator


API_KEY = "-----------------------TUTAJ_WSTAW_SWOJ_KLUCZ_API---------------------------"
INPUT_FILE = "./przykladowy_artykul.txt"
OUTPUT_FILE = "./artykul.html"


def main():
    if not API_KEY:
        raise Exception("Nie znaleziono klucza API. Ustaw wartość zmiennej API_KEY.")

    generator = ArticleToHtmlGenerator(api_key=API_KEY)

    try:
        content = generator.read_article(INPUT_FILE)
        html_content = generator.preprocess_with_ai(content)
        generator.save_to_html(html_content, OUTPUT_FILE)

        print(f"Artykuł został pomyślnie przetworzony i zapisany w {OUTPUT_FILE}")

    except Exception as e:
        print(f"Wystąpił błąd: {str(e)}")


if __name__ == "__main__":
    main()