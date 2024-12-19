import json
from playwright.sync_api import Playwright


class ApiUtils:
    baseurl = "https://reqres.in"

    def login_with_user(self, playwright: Playwright):
        api_request_context = playwright.request.new_context(base_url=self.baseurl)
        with open('C:/Users/visha/PycharmProjects/Playwright_API_Automation/testdata/login_user.json', 'r') as f:
            data = json.load(f)
        user_data = data
        response = api_request_context.post(url="/api/login",
                                            data=user_data)
        assert response.ok
        return response

    def create_new_user(self, playwright: Playwright):
        api_request_context = playwright.request.new_context(base_url=self.baseurl)
        response = api_request_context.post(url="/api/users",
                                            data={"name": "morpheus", "job": "leader"}
                                            )
        data = response.json()
        print(data)
        return data

    def get_single_user_details(self, userid, playwright: Playwright):
        api_request_context = playwright.request.new_context(base_url=self.baseurl)
        single_user_url = "/api/users/" + userid
        response = api_request_context.get(url=single_user_url)
        data = response.json()
        print(data)
        assert response.status == 404
        return data

    def register_user(self, playwright: Playwright):
        api_request_context = playwright.request.new_context(base_url=self.baseurl)
        with open('C:/Users/visha/PycharmProjects/Playwright_API_Automation/testdata/user_detail.json', 'r') as f:
            data = json.load(f)
        user_data = data
        response = api_request_context.post(url="/api/register",
                                            data=user_data)
        return response

    def get_invalid_single_user(self, playwright: Playwright):
        api_request_context = playwright.request.new_context(base_url=self.baseurl)
        response = api_request_context.get(url="/api/users/23")
        response_data = response.json()
        return response_data

    def update_single_user(self, playwright: Playwright):
        api_request_context = playwright.request.new_context(base_url=self.baseurl)
        with open('C:/Users/visha/PycharmProjects/Playwright_API_Automation/testdata/update_user.json', 'r') as file:
            user = json.load(file)
        response = api_request_context.put(url="/api/users/12",
                                           data=user)
        assert response.ok
        response_data = response.json()
        return response_data

    def delete_single_user(self, playwright: Playwright):
        api_request_context = playwright.request.new_context(base_url=self.baseurl)
        with open('C:/Users/visha/PycharmProjects/Playwright_API_Automation/testdata/delete_user.json', 'r') as file:
            user = json.load(file)
        response = api_request_context.delete(url="/api/users/12",
                                              data=user)
        assert response.status == 204
        return response.status_text

    def verify_users_in_list(self, playwright: Playwright):
        api_request_context = playwright.request.new_context(base_url=self.baseurl)
        response = api_request_context.get(url="/api/unknown")
        return response
