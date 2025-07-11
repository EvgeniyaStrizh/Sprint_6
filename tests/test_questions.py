import pytest
from pages.main_page import MainPage
from data import expected_answers

class TestMainPage:
    @pytest.mark.parametrize("index, expected_text", expected_answers)
    def test_question_expands(self, driver, index, expected_text):
        page = MainPage(driver)
        page.open()
        page.click_question(index)
        assert expected_text in page.get_answer_text(index)
