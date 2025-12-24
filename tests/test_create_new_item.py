
import random
import time


def get_name_loc(name):
    return f"td > a[href='job/{name}/']"


# def test_tc_01_001_01(page):
#     """launch the URL"""
#     page.goto("/")
#
#     """Our variables"""
#     username = "jen_admin"
#     password = "Ev08081981!!"
#     new_item_name = f"jen_admin-{random.randint(0, 9999999)}"
#
#     """Locators for login page"""
#     username_field_loc = "input[id='j_username']"
#     password_field_loc = "input[id='j_password']"
#     submit_btn_loc = "button[name='Submit']"
#
#     """Locator for button + new item"""
#     new_item_btn_loc = "a[href='/view/all/newJob']"
#
#     """Page locators for creating a new item"""
#     item_name_field_loc = "input[class='jenkins-input']"
#     item_type_text = "Pipeline"
#     ok_btn_loc = "button[id='ok-button']"
#
#     """Locator for logo"""
#     logo_loc = "a[class='app-jenkins-logo']"
#
#     """Locator for the created item"""
#     created_item_loc = lambda name: f"td > a[href='job/{name}/']"
#
#     """Login page"""
#     page.locator(username_field_loc).fill(username)
#     page.locator(password_field_loc).fill(password)
#     page.locator(submit_btn_loc).click()
#
#     """Click on the button + new item"""
#     page.locator(new_item_btn_loc).click()
#
#     """New item creation page"""
#     page.locator(item_name_field_loc).fill(new_item_name)
#     page.get_by_text(item_type_text, exact=True).click()
#     page.locator(ok_btn_loc).click()
#
#     """Click on the logo"""
#     page.locator(logo_loc).click()
#
#     """Getting the text of the created item"""
#     text = page.locator(created_item_loc(new_item_name)).text_content()
#     # text = page.locator(get_name_loc(new_item_name)).text_content()
#     time.sleep(10)
#
#     assert text == new_item_name

# def test(get_all_jobs):
#     a = get_all_jobs


# def test(delete_jobs):
#     assert 1 == 1


def test_tc_01_001_01(page):
    """launch the URL"""
    page.goto("/")

    """Our variables"""
    new_item_name = f"jen_admin-{random.randint(0, 9999999)}"

    """Locator for button + new item"""
    new_item_btn_loc = "a[href='/view/all/newJob']"

    """Page locators for creating a new item"""
    item_name_field_loc = "input[class='jenkins-input']"
    item_type_text = "Pipeline"
    ok_btn_loc = "button[id='ok-button']"

    """Locator for logo"""
    logo_loc = "a[class='app-jenkins-logo']"

    """Locator for the created item"""
    created_item_loc = lambda name: f"td > a[href='job/{name}/']"

    """Click on the button + new item"""
    page.locator(new_item_btn_loc).click()

    """New item creation page"""
    page.locator(item_name_field_loc).fill(new_item_name)
    page.get_by_text(item_type_text, exact=True).click()
    page.locator(ok_btn_loc).click()

    """Click on the logo"""
    page.locator(logo_loc).click()

    """Getting the text of the created item"""
    text = page.locator(created_item_loc(new_item_name)).text_content()
    # text = page.locator(get_name_loc(new_item_name)).text_content()
    time.sleep(10)

    assert text == new_item_name


