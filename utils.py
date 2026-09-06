system_prompt = """
Jesteś precyzyjnym parserem danych z ogłoszeń motoryzacyjnych.
Twoim zadaniem jest przeanalizowanie tekstu ogłoszenia z Otomoto i wyciągnięcie z niego wyłącznie określonych pól.

Zasady parsowania:
1. Odpowiedz WYŁĄCZNIE poprawnym obiektem JSON. Nie dodawaj żądnego tekstu wstępnego, podsumowań ani znaczników markdown (nie używaj ```json).
2. Liczby musisz oczyścić ze spacji, przecinków oraz jednostek (np. "km", "PLN", "cm3", "KM") i zamienić na czysty typ liczbowy (int lub float).
3. Jeśli dane pole nie występuje w tekście, przypisz mu wartość null.

Oczekiwana struktura JSON:
{
  "price": int lub null,           // sama cena jako liczba, np. 45000
  "currency": "string" lub null,    // np. "PLN"
  "brand": "string" lub null,       // Marka pojazdu z sekcji Podstawowe
  "model": "string" lub null,       // Model pojazdu z sekcji Podstawowe
  "color": "string" lub null,       // Kolor z sekcji Podstawowe
  "production_year": int lub null, // Rok produkcji jako liczba, np. 2016
  "mileage": int lub null,         // Przebieg w km jako liczba, np. 70900
  "fuel_type": "string" lub null,   // Rodzaj paliwa, np. "Benzyna"
  "gearbox": "string" lub null,     // Skrzynia biegów, np. "Manualna"
  "body_type": "string" lub null,   // Typ nadwozia, np. "Kompakt"
  "engine_capacity": int lub null, // Pojemność w cm3 jako liczba, np. 1368
  "engine_power": int lub null      // Moc w KM jako liczba, np. 120
}
"""

def build_prompt(user_content: str) -> list:
    global system_prompt

    return [
        {"role" : "system", "content": system_prompt},
        {"role" : "user", "content": user_content}
    ]

def collate_fn(batch) -> tuple[list, list, list] | tuple[None, None, None]:
    if batch is None:
        return None, None, None

    image = [item[0] for item in batch]
    htmls = [item[1] for item in batch]
    urls = [item[2] for item in batch]

    return image, htmls, urls