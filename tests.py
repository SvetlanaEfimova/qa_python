from main import BooksCollector


# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    def test_add_new_book_set_the_default_rating(self):
        collector = BooksCollector()
        collector.add_new_book('Война и мир в комиксах')
        assert collector.get_books_rating()['Война и мир в комиксах'] == 1

    def test_set_book_rating_setting_the_rating(self):
        collector = BooksCollector()
        collector.add_new_book('Как незаметно выспаться на совещании')
        collector.set_book_rating('Как незаметно выспаться на совещании', 5)
        assert collector.get_books_rating()['Как незаметно выспаться на совещании'] == 5

    def test_get_book_rating_no_book_no_rating(self):
        collector = BooksCollector()
        assert collector.get_book_rating('Сентябрь горит') is None

    def test_get_books_with_specific_rating_output_a_book_by_rating(self):
        collector = BooksCollector()
        collector.add_new_book('400 слов из трех букв')
        collector.add_new_book('Гадание на клавиатуре')
        collector.add_new_book('Парные носки: миф или реальность')
        collector.set_book_rating('400 слов из трех букв', 8)
        collector.set_book_rating('Гадание на клавиатуре', 8)
        collector.set_book_rating('Парные носки: миф или реальность', 9)
        assert collector.get_books_with_specific_rating(8) == ['400 слов из трех букв', 'Гадание на клавиатуре']

    def test_get_books_rating_output_the_current_dictionary(self):
        collector = BooksCollector()
        collector.add_new_book('400 слов из трех букв')
        collector.add_new_book('Гадание на клавиатуре')
        collector.add_new_book('Парные носки: миф или реальность')
        collector.set_book_rating('400 слов из трех букв', 8)
        collector.set_book_rating('Гадание на клавиатуре', 8)
        collector.set_book_rating('Парные носки: миф или реальность', 9)
        assert collector.get_books_rating() == {'400 слов из трех букв': 8, 'Гадание на клавиатуре': 8, 'Парные носки: миф или реальность': 9}

    def test_add_book_in_favorites_add_to_favorites_a_book_not_from_the_list(self):
        collector = BooksCollector()
        collector.add_new_book('501 блюдо из чипсов')
        collector.add_new_book('Час пик в метро: руководство по выживанию')
        collector.add_new_book('18 стилей плача на каждый день')
        collector.set_book_rating('501 блюдо из чипсов', 7)
        collector.set_book_rating('Час пик в метро: руководство по выживанию', 10)
        collector.set_book_rating('18 стилей плача на каждый день', 9)
        collector.add_book_in_favorites('Подготовка к концу света')
        assert collector.get_list_of_favorites_books() == []

    def test_delete_book_from_favorites_delete_from_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('501 блюдо из чипсов')
        collector.set_book_rating('501 блюдо из чипсов', 7)
        collector.add_book_in_favorites('501 блюдо из чипсов')
        collector.delete_book_from_favorites('501 блюдо из чипсов')
        assert collector.get_list_of_favorites_books() == []

    def test_get_list_of_favorites_books_list_of_selected_books(self):
        collector = BooksCollector()
        collector.add_new_book('501 блюдо из чипсов')
        collector.set_book_rating('501 блюдо из чипсов', 7)
        collector.add_book_in_favorites('501 блюдо из чипсов')
        assert collector.get_list_of_favorites_books() == ['501 блюдо из чипсов']

