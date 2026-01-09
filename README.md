# 📊 System analizy klientów i prognozowania sprzedaży

## 🧩 Opis projektu

System analizy klientów i prognozowania sprzedaży to **pełnostackowa aplikacja webowa**, która symuluje wewnętrzne narzędzie analityczne wykorzystywane w firmach **e‑commerce / SaaS**. Projekt łączy **backend we Flasku**, **modele Machine Learning (scikit‑learn)**, **bazę danych SQL** oraz **responsywny frontend oparty o Bootstrap**.

Celem aplikacji jest wsparcie decyzji biznesowych poprzez:

* analizę zachowań klientów,
* prognozowanie przyszłej sprzedaży,
* przewidywanie prawdopodobieństwa zakupu.

Projekt został zaprojektowany w sposób zbliżony do realnych systemów komercyjnych.

---

## 🎯 Cel biznesowy

System umożliwia firmie:

* **planowanie przychodów** na podstawie prognoz sprzedaży,
* **segmentację klientów** według przewidywanej wartości,
* **targetowanie kampanii marketingowych**,
* **optymalizację kosztów reklam** poprzez analizę prawdopodobieństwa zakupu.

Dane i predykcje są dostępne w przejrzystym panelu webowym dla analityków i administratorów.

---

## 🛠️ Technologie

### Backend

* **Python 3**
* **Flask** – REST API
* **SQLAlchemy** – ORM
* **PostgreSQL / SQLite** (na start)

### Machine Learning

* **scikit‑learn**

  * Linear Regression
  * Logistic Regression
* Normalizacja danych
* Walidacja modeli
* Zapisywanie i ładowanie modeli z plików

### Frontend

* HTML / CSS
* (Opcjonalnie) **Chart.js** – wizualizacja danych

---

## 🧠 Moduł Machine Learning

### 1️⃣ Regresja liniowa – prognozowanie sprzedaży

**Cel:**
Prognozowanie wartości sprzedaży klienta w kolejnym miesiącu.

**Dane wejściowe (features):**

* Liczba zakupów w ostatnich 30 dniach
* Średnia wartość koszyka
* Liczba wizyt na stronie
* Liczba dni od ostatniego zakupu
* Staż klienta (w miesiącach)

**Dane wyjściowe (target):**

* Prognozowana wartość sprzedaży (PLN)

**Funkcjonalności:**

* trenowanie modelu na danych historycznych,
* normalizacja danych,
* metryki: **R², MSE**,
* zapis modelu do pliku,
* możliwość ponownego trenowania z panelu admina.

---

### 2️⃣ Regresja logistyczna – przewidywanie zakupu

**Cel:**
Określenie, czy klient dokona zakupu w ciągu najbliższych 14 dni.

**Dane wejściowe:**

* Liczba wizyt w ostatnich 7 dniach
* Otworzone newslettery (0/1)
* Kliknięcia w reklamy
* Historia zakupów (0/1)
* Czas spędzony na stronie

**Dane wyjściowe:**

* 0 – brak zakupu
* 1 – zakup

**Funkcjonalności:**

* klasyfikacja binarna,
* predykcja prawdopodobieństwa zakupu,
* **Confusion Matrix**,
* metryki: Accuracy, Precision, Recall,
* próg decyzyjny (np. >70%).

---

## 🗄️ Baza danych – struktura

### users

* id
* email
* hasło (hash)
* rola (admin / analityk)

### clients

* id
* imię
* nazwisko
* email
* data rejestracji
* staż klienta

### client_activity

* client_id
* liczba wizyt
* liczba zakupów
* średnia wartość koszyka
* dni od ostatniego zakupu

### sales_predictions

* client_id
* prognozowana sprzedaż
* data predykcji

### purchase_predictions

* client_id
* prawdopodobieństwo zakupu
* decyzja (0/1)

---

## 🌐 Backend – funkcjonalności

* Autoryzacja i logowanie użytkowników
* Role użytkowników (admin / analityk)
* REST API (JSON)
* Endpointy do:

  * dodawania i edycji klientów,
  * uruchamiania predykcji ML,
  * trenowania modeli ML,
* walidacja danych wejściowych,
* obsługa błędów i logowanie.

---

## 🎨 Frontend – widoki aplikacji

### 🔐 Strona logowania

* formularz email + hasło,
* walidacja danych,
* komunikaty błędów.

### 📋 Dashboard główny

* liczba klientów,
* średnia prognozowana sprzedaż,
* % klientów z wysokim prawdopodobieństwem zakupu,
* wykres trendu sprzedaży.

### 👤 Lista klientów

* tabela klientów,
* prognoza sprzedaży,
* prawdopodobieństwo zakupu,
* filtrowanie i sortowanie.

### 📈 Szczegóły klienta

* dane klienta,
* historia aktywności,
* wyniki predykcji ML,
* wizualizacja (progress bar).

### 🤖 Panel ML (admin)

* trenowanie modeli ML,
* wyświetlanie metryk,
* informacja o ostatnim trenowaniu.

---

## 🧪 Testowanie i jakość

* testy jednostkowe backendu,
* walidacja danych wejściowych,
* logowanie błędów,
* czytelna struktura projektu.

---

## 💼 Jak opisać projekt na rozmowie kwalifikacyjnej

> „Zbudowałem system analityczny we Flasku, który wykorzystuje regresję liniową do prognozowania sprzedaży oraz regresję logistyczną do przewidywania zachowań klientów. Projekt obejmuje pełny stack: bazę danych, REST API, warstwę Machine Learning oraz responsywny frontend oparty o Bootstrap.”

---

## 🚀 Możliwe rozszerzenia

* Docker + Docker Compose
* CI/CD
* Harmonogram trenowania modeli
* Więcej modeli ML
* Integracja z realnymi danymi

---

## 👨‍💻 Autor

Projekt edukacyjny / portfolio – przygotowany z myślą o **stanowisku Junior Python / ML / Backend Developer**.
