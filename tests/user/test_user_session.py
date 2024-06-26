import allure

from petstore_api_test_framework.utils.user_api.create import create
from petstore_api_test_framework.utils.user_api.login import login
from petstore_api_test_framework.utils.user_api.logout import logout


@allure.epic('User API')
@allure.story('Session')
class TestUserSession:
    @allure.title('User login')
    @allure.feature('Authentication API')
    @allure.label('microservice', 'API')
    @allure.label('owner', 'allure8')
    @allure.tag('smoke', 'regress', 'API', 'critical')
    @allure.severity('critical')
    def test_user_login(self, base_url, headers):
        # WHEN
        user_data = create(base_url, headers)

        # THEN
        login(base_url, headers, username=user_data['username'], password=user_data['password'])

    @allure.title('User logout')
    @allure.feature('User logout API')
    @allure.label('microservice', 'API')
    @allure.label('owner', 'allure8')
    @allure.tag('smoke', 'regress', 'API', 'critical')
    @allure.severity('critical')
    def test_user_logout(self, base_url, headers):
        # THEN
        logout(base_url, headers)
