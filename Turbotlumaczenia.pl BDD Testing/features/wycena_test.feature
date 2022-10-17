Feature: Funkcjonalność - wycena tłumaczenia
  Scenario: Niezalogowany użytkownik sprawdza wycenę tłumaczenia tekstu
            o długości 250-400 słów z języka polskiego na niemiecki (brak maila, dodatkowa korekta).
    Given Użytkownik jest na stronie https://turbotlumaczenia.pl/
    And Użytkownik przeszedł na stronę wyceny zamówienia
    When Użytkownik wybrał tłumaczenie z język "polski" na język "niemiecki"
    And Użytkownik wybrał opcję dodatkową "dodatkowa korekta native speakera"
    And Użytkownik wprowadził tekst do tłumaczenia o długości od 250 do 400 słów
    And Pole adresu email jest puste
    Then Wycena jest obecna
    And Szacowany czas wykonania jest obecny

