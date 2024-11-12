# Zadanie rekrutacyjne Oxido

Aplikacja napisana w Pythonie do przetwarzania artykułów przy użyciu API OpenAI. Program konwertuje tekst na semantyczny kod HTML z sugestiami miejsc na grafiki i promptami do ich wygenerowania.

## Funkcjonalności

<ul>
  <li>Łączenie z API OpenAI</li>
  <li>Przetwarzanie plików tekstowych na kod HTML</li>
  <li>Automatyczne sugestie miejsc na grafiki z promptami</li>
  <li>Podgląd wygenerowanego artykułu</li>
</ul>

## Wymagania

- Python 3.x
- Biblioteka openai
- Klucz API OpenAI

## Struktura projektu

```
Oxido-zadanie/
├── src/                          # Katalog z kodem źródłowym
│   ├── main.py                   # Główny skrypt do przetwarzania artykułów
│   └── generator.py              # Klasa obsługująca API OpenAI
│    
├── artykul.html                  # Sformatowany artykuł otrzymany od API
├── szablon.html                  # Pusty szablon do podglądu artykułów
├── podglad.html                  # Przykładowy artykuł z pełnym formatowaniem
├── requirements.txt              # Wymagane biblioteki
└── przykladowy_artykul.txt       # Tekst artykułu do przetworzenia
```
