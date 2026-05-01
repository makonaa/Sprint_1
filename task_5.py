class TestCase:
    #initializing steps and result attributes for TestCase
    def __init__(self):
        self.steps = {}
        self.result = None
    #set_step method adds a new step to TestCase.steps
    def set_step(self, step_number, step_text):
        self.steps[step_number] = step_text
    #delete_step removes a step from TestCase.steps by its key
    def delete_step(self, step_number):
        del self.steps[step_number]
    #set_result method sets ER in TestCase.result
    def set_result(self, result):
        self.result = result
    #get_test_case method displays TestCase information - its steps and ER
    def get_test_case (self):
        case_info = {}
        case_info['Шаги'] = self.steps
        case_info['Ожидаемый результат'] = self.result
        print(case_info)

test_case_1 = TestCase()
test_case_1.set_step(1, 'Перейти на сайт')
test_case_1.set_step(3, 'Перейти в раздел Товары')
test_case_1.delete_step(3)
test_case_1.set_step(2, 'Перейти в раздел Товары')
test_case_1.set_step(3, 'Нажать кнопку «В корзину» у первого товара')
test_case_1.set_result('Товар окажется в корзине')
test_case_1.get_test_case()

test_case_2 = TestCase()
test_case_2.set_step(1, 'Перейти на сайт')
test_case_2.set_step(2, 'Перейти в раздел Корзина')
test_case_2.set_step(3, 'Нажать кнопку "Удалить"')
test_case_2.set_result('Товар удален из корзины')
test_case_2.get_test_case()