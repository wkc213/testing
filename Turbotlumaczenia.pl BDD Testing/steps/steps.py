from selenium.webdriver.common.by import By
from behave import Given, When, Then
from languages import spis as lang_dict
import text_generator


@Given ("Użytkownik jest na stronie {site}")
def enter_site_1(context, site):
    context.browser.get(site)


@Given ("Użytkownik przeszedł na stronę wyceny zamówienia")
def enter_site_2(context):
    context.browser.find_element(By.XPATH, '//a[text()="Wyceń i zamów tłumaczenie"]').click()
    # zamknięcie okna cookies
    context.browser.find_element(By.CLASS_NAME, "btn.btn-danger").click()


@When('Użytkownik wybrał tłumaczenie z język "{lang_from}" na język "{lang_to}"')
def translate_from_to(context, lang_from, lang_to):
    if (lang_from.lower() not in lang_dict) or (lang_to.lower() not in lang_dict):
        raise ValueError    # brak języka/ów na liście
    else:
        lang_from_cc = lang_dict[lang_from.lower()]
        lang_to_cc = lang_dict[lang_to.lower()]

        # otwarcie listy języków z których tłumaczymy
        context.browser.find_element(By.ID, "dropdown-col-from1").click()
        # znalezienie języka wejściowego po skrócie
        context.browser.find_element(By.XPATH, '//li[@data-cc="%s"]' % lang_from_cc).click()

        # otwarcie listy języków na które tłumaczymy
        context.browser.find_element(By.ID, "dropdown-col-to1").click()
        # odznaczenie domyślnego języka
        context.browser.find_element(By.ID, "Row_1en").click()
        # znalezienie języka wyjściowego po skrócie
        context.browser.find_element(By.XPATH, '//input[@data-cc="%s"]' % lang_to_cc).click()


@When('Użytkownik wybrał opcję dodatkową "{extra_option}"')
def extra_option_choice(context, extra_option):
    if extra_option == "dodatkowa korekta native speakera":
        context.browser.find_element(By.ID, "proofreading").click()
    elif extra_option == "dodatkowa weryfikacja drugiego tłumacza":
        context.browser.find_element(By.ID, "verification").click()
    elif extra_option == "" or extra_option == "brak":
        pass
    else:
        raise ValueError    # niedozwolona opcja dodatkowa


@When("Użytkownik wprowadził tekst do tłumaczenia o długości od {min_words} do {max_words} słów")
def enter_text(context, min_words, max_words):
    # lorem ipsum w zakresie <min_words, max_words> słów
    context.browser.find_element(By.ID, "content").send_keys(text_generator.of_range(int(min_words), int(max_words)))


@When("Pole adresu email jest puste")
def empty_mail_field(context):
    mail = context.browser.find_element(By.ID, "email").get_attribute("value")
    assert mail == "", "Pole adresu email zawiera treść!"


@Then("Wycena jest obecna")
def expected_price(context):
    context.browser.find_element(By.XPATH, '//span[@data-bind-expected-price]')


@Then("Szacowany czas wykonania jest obecny")
def expected_realisation_time(context):
    context.browser.find_element(By.XPATH, '//span[@data-bind-expected-realisation-time]')

