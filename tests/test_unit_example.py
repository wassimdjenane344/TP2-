def is_valid_item(item):
    return item is not None and item.strip() != ""


def test_valid_item():
    assert is_valid_item("pomme")


def test_empty_item_rejected():
    assert not is_valid_item("")

