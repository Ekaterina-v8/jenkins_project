import time


# def test_tc_10_034_02(page):
#     """launch the URL"""
#     page.goto("/")
#
#     expected_url = "http://localhost:8080/manage/"
#     expected_status = 302
#
#     """Our variables"""
#     username = "jen_admin"
#     password = "Ev08081981!!"
#
#
#     """Locators for login page"""
#     username_field_loc = "input[id='j_username']"
#     password_field_loc = "input[id='j_password']"
#     submit_btn_loc = "button[name='Submit']"
#
#     user_settings_btn_loc = "a[id='root-action-ManageJenkinsAction']"
#
#     """Login page"""
#     page.locator(username_field_loc).fill(username)
#     page.locator(password_field_loc).fill(password)
#     page.locator(submit_btn_loc).click()
#
#     with page.expect_response(lambda response: response.status) as response_info:
#         page.locator(user_settings_btn_loc).click()
#     print(response_info.value)
#
#     response = response_info.value
#     status_code = response.status
#
#     actual_url = page.url
#
#     assert actual_url == expected_url and status_code == expected_status

# def test(page):
#     page.goto("/")
#     time.sleep(4)


def test_tc_10_034_02(page):
    """launch the URL"""
    page.goto("/")

    expected_url = "http://localhost:8080/manage/"
    expected_status = 302

    user_settings_btn_loc = "a[id='root-action-ManageJenkinsAction']"

    with page.expect_response(lambda response: response.status) as response_info:
        page.locator(user_settings_btn_loc).click()
    print(response_info.value)

    response = response_info.value
    status_code = response.status

    actual_url = page.url

    assert actual_url == expected_url and status_code == expected_status