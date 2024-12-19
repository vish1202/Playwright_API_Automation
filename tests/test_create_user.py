import datetime
import time

import pytest
from playwright.sync_api import Playwright
from api.api_utils import ApiUtils


@pytest.mark.login
def test_user_login(playwright: Playwright):
    api_utils_obj = ApiUtils()
    response = api_utils_obj.login_with_user(playwright)
    print(response)
    response_data = response.json()
    assert response_data['token'] == 'QpwL5tke4Pnpja7X4'


@pytest.mark.useraction
def test_create_user(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://reqres.in")
    api_utils_obj = ApiUtils()
    response = api_utils_obj.create_new_user(playwright)
    user_id = response['id']
    page.goto(api_utils_obj.baseurl + '/api/users/' + user_id)
    print("Created date:" + response['createdAt'])
    current_date = str(datetime.date.today())
    assert current_date in response['createdAt']
    page.close()
    return user_id


@pytest.mark.useraction
def test_get_user_details(playwright: Playwright):
    userid = test_create_user(playwright)
    api_utils_obj = ApiUtils()
    response_data = api_utils_obj.get_single_user_details(userid, playwright)
    print(response_data)


@pytest.mark.useraction
def test_user_registration(playwright: Playwright):
    api_utils_obj = ApiUtils()
    response_data = api_utils_obj.register_user(playwright)
    print(response_data)


@pytest.mark.useraction
def test_invalid_single_user(playwright: Playwright):
    api_utils_obj = ApiUtils()
    response_data = api_utils_obj.get_invalid_single_user(playwright)
    print(response_data)
    assert response_data == {}


@pytest.mark.useraction
def test_update_single_user(playwright: Playwright):
    api_utils_obj = ApiUtils()
    response_data = api_utils_obj.update_single_user(playwright)
    print(response_data)
    current_date = datetime.date.today()
    assert str(current_date) in response_data['updatedAt']


@pytest.mark.useraction
def test_delete_single_user(playwright: Playwright):
    api_utils_obj = ApiUtils()
    response_data = api_utils_obj.delete_single_user(playwright)
    assert response_data == 'No Content'
    print('user deleted successfully')


@pytest.mark.userlist
def test_verify_list_resource(playwright: Playwright):
    api_utils_obj = ApiUtils()
    response = api_utils_obj.verify_users_in_list(playwright)
    response_data = response.json()
    user_list = response_data['data']
    expected_user_list = ['cerulean', 'fuchsia rose', 'true red', 'aqua sky', 'tigerlily', 'blue turquoise']
    i = 0
    for user in user_list:
        if user_list[i]['name'] == expected_user_list[i]:
            i = i + 1
            continue
        else:
            pass
