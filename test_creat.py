

def test_tc_01_001_01(page):
    """Переходим по ссылке"""
    page.goto("/")
    username = "jen_admin"
    password = "Ev08081981!!"
    new_item_name = f"jen_admin-{random.randint(0, 9999999)}"