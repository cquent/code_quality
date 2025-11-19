from app import format_item


def test_format_item():
    assert format_item("apple") == "Apple"

    assert format_item("  banana  ") == "Banana"

    assert format_item("Orange") == "Orange"

    assert format_item("") == ""

    assert format_item("   ") == ""
