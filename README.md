📊 Projekt: System analizy klientów i prognozowania sprzedaży

Technologie:

Backend: Python + Flask

ML: scikit-learn (Linear Regression, Logistic Regression)

Frontend: Bootstrap (eBootstrap)

Baza danych: PostgreSQL / SQLite (na start)

ORM: SQLAlchemy

🎯 Cel biznesowy projektu (jak w prawdziwej pracy)

Celem systemu jest:

Analiza danych klientów

Prognozowanie przyszłej sprzedaży (regresja liniowa)

Przewidywanie, czy klient dokona zakupu (regresja logistyczna)

Umożliwienie pracownikom firmy zarządzania danymi klientów i wynikami modeli ML przez panel webowy

Projekt symuluje wewnętrzne narzędzie analityczne używane np. w firmie e-commerce lub SaaS.

🧠 Moduł Machine Learning (KLUCZOWY)
1️⃣ Regresja liniowa – prognozowanie sprzedaży

Opis:
Model regresji liniowej przewiduje wartość sprzedaży w kolejnym miesiącu na podstawie historycznych danych klienta.

Dane wejściowe (features):

Liczba zakupów w ostatnich 30 dniach

Średnia wartość koszyka

Liczba wizyt na stronie

Liczba dni od ostatniego zakupu

Staż klienta (w miesiącach)

Dane wyjściowe (target):

Prognozowana wartość sprzedaży (PLN)

Funkcjonalności ML:

Trenowanie modelu na danych historycznych

Normalizacja danych

Walidacja modelu (R², MSE)

Zapisywanie modelu do pliku

Możliwość ponownego trenowania modelu z poziomu panelu admina

Zastosowanie biznesowe:

Planowanie przychodów

Segmentacja klientów według przewidywanej wartości

2️⃣ Regresja logistyczna – przewidywanie zakupu

Opis:
Model klasyfikuje, czy klient dokona zakupu w ciągu najbliższych 14 dni.

Dane wejściowe:

Liczba wizyt w ostatnich 7 dniach

Otworzone newslettery (tak/nie)

Kliknięcia w reklamy

Historia zakupów (0/1)

Czas spędzony na stronie

Dane wyjściowe:

0 – brak zakupu

1 – zakup

Funkcjonalności ML:

Klasyfikacja binarna

Predykcja prawdopodobieństwa zakupu

Confusion Matrix

Accuracy, Precision, Recall

Threshold do decyzji biznesowej (np. >70%)

Zastosowanie biznesowe:

Kampanie marketingowe

Targetowanie klientów

Optymalizacja kosztów reklam

🗄️ Baza danych – struktura logiczna
Tabele:

users

id

email

hasło (hash)

rola (admin / analityk)

clients

id

imię

nazwisko

email

data rejestracji

staż klienta

client_activity

client_id

liczba wizyt

liczba zakupów

średnia wartość koszyka

dni od ostatniego zakupu

sales_predictions

client_id

prognozowana sprzedaż

data predykcji

purchase_predictions

client_id

prawdopodobieństwo zakupu

decyzja (0/1)

🌐 Backend (Flask) – wymagania
Moduły aplikacji:

Autoryzacja i logowanie

API do:

dodawania klientów

edycji danych klientów

uruchamiania predykcji ML

Obsługa błędów i walidacja danych

Integracja z modelem ML

REST API (JSON)

🎨 Frontend – wygląd i UX (Bootstrap)
Styl:

Kolorystyka: jasny dashboard (biały + niebieski)

Responsywność (desktop + mobile)

Spójne karty (Bootstrap Cards)

Wykresy (np. Chart.js – opcjonalnie)

Widoki aplikacji:
🔐 1. Strona logowania

Formularz email + hasło

Walidacja danych

Komunikaty błędów

📋 2. Dashboard główny

Karty:

Liczba klientów

Średnia prognozowana sprzedaż

% klientów z wysokim prawdopodobieństwem zakupu

Wykres trendu sprzedaży

👤 3. Lista klientów

Tabela:

Imię, email

Prognoza sprzedaży

Prawdopodobieństwo zakupu

Filtrowanie

Sortowanie

📈 4. Szczegóły klienta

Dane klienta

Historia aktywności

Wyniki predykcji ML

Wizualizacja (progress bar dla prawdopodobieństwa zakupu)

🤖 5. Panel ML (admin)

Przycisk „Trenuj model regresji liniowej”

Przycisk „Trenuj model logistyczny”

Wyświetlanie metryk modeli

Informacja o ostatnim trenowaniu

🧪 Testowanie i jakość

Testy jednostkowe backendu

Walidacja danych wejściowych

Logowanie błędów

💼 Jak to sprzedać na rozmowie?

„Zbudowałem system analityczny we Flasku, który wykorzystuje regresję liniową do prognozowania sprzedaży oraz regresję logistyczną do przewidywania zachowań klientów. Projekt obejmuje pełny stack: bazę danych, REST API, warstwę ML oraz responsywny frontend oparty o Bootstrap.”

Jeśli chcesz:

📄 opis do README

🗂️ rozpisanie user stories

🧩 diagram architektury

🎯 wersję „na zaliczenie” albo „pod juniora”

to daj znać 👍
