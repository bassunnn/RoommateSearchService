"""Тестирование функций работы с объявлениями."""

from ads import add_ad, filter_ads, sort_ads_by_price


def test_filter_ads_by_price():
    data = [
        {"id": 1, "price": 10000, "district": "центр"},
        {"id": 2, "price": 20000, "district": "центр"},
    ]
    res = filter_ads(data, max_price=15000)
    assert len(res) == 1
    assert res[0]["id"] == 1


def test_sort_ads_by_price():
    data = [{"price": 20000}, {"price": 10000}, {"price": 15000}]
    sorted_res = sort_ads_by_price(data)
    assert sorted_res[0]["price"] == 10000
    assert sorted_res[-1]["price"] == 20000


def test_add_ad():
    ads = []
    new_ad = add_ad(ads, "юг", 13000, "Уютная комната")
    assert len(ads) == 1
    assert new_ad["id"] == 1
    assert new_ad["district"] == "юг"