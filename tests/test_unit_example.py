def is_valid_item(item):
    return item is not None and item.strip() != ""


def test_valid_item():
    assert is_valid_item("pomme") == True


def test_empty_item_rejected():
    assert is_valid_item("") == False
