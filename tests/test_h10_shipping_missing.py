import json  # noqa: F401


def test_h10_no_address_0001(api):
    resp = api.get("/api/shipping", params={'itemList': '[{"productId": "LS4PSXUNUM", "quantity": 1}]', 'currencyCode': 'USD'})
    assert resp.status_code >= 400


def test_h10_no_itemlist_0002(api):
    resp = api.get("/api/shipping", params={'currencyCode': 'USD', 'address': '{"streetAddress": "1600 Amphitheatre Parkway", "zipCode": "94043", "city": "Mountain View", "state": "CA", "country": "United States"}'})
    assert resp.status_code >= 400


def test_h10_no_address_0003(api):
    resp = api.get("/api/shipping", params={'itemList': '[{"productId": "6E92ZMYYFZ", "quantity": 1}]', 'currencyCode': 'USD'})
    assert resp.status_code >= 400


def test_h10_no_itemlist_0004(api):
    resp = api.get("/api/shipping", params={'currencyCode': 'USD', 'address': '{"streetAddress": "1600 Amphitheatre Parkway", "zipCode": "94043", "city": "Mountain View", "state": "CA", "country": "United States"}'})
    assert resp.status_code >= 400


def test_h10_no_address_0005(api):
    resp = api.get("/api/shipping", params={'itemList': '[{"productId": "OLJCESPC7Z", "quantity": 1}]', 'currencyCode': 'USD'})
    assert resp.status_code >= 400


def test_h10_no_itemlist_0006(api):
    resp = api.get("/api/shipping", params={'currencyCode': 'USD', 'address': '{"streetAddress": "1600 Amphitheatre Parkway", "zipCode": "94043", "city": "Mountain View", "state": "CA", "country": "United States"}'})
    assert resp.status_code >= 400


def test_h10_no_address_0007(api):
    resp = api.get("/api/shipping", params={'itemList': '[{"productId": "1YMWWN1N4O", "quantity": 1}]', 'currencyCode': 'USD'})
    assert resp.status_code >= 400


def test_h10_no_itemlist_0008(api):
    resp = api.get("/api/shipping", params={'currencyCode': 'USD', 'address': '{"streetAddress": "1600 Amphitheatre Parkway", "zipCode": "94043", "city": "Mountain View", "state": "CA", "country": "United States"}'})
    assert resp.status_code >= 400


def test_h10_no_address_0009(api):
    resp = api.get("/api/shipping", params={'itemList': '[{"productId": "2ZYFJ3GM2N", "quantity": 1}]', 'currencyCode': 'USD'})
    assert resp.status_code >= 400


def test_h10_no_itemlist_0010(api):
    resp = api.get("/api/shipping", params={'currencyCode': 'USD', 'address': '{"streetAddress": "1600 Amphitheatre Parkway", "zipCode": "94043", "city": "Mountain View", "state": "CA", "country": "United States"}'})
    assert resp.status_code >= 400


def test_h10_no_address_0011(api):
    resp = api.get("/api/shipping", params={'itemList': '[{"productId": "LS4PSXUNUM", "quantity": 1}]', 'currencyCode': 'USD'})
    assert resp.status_code >= 400


def test_h10_no_itemlist_0012(api):
    resp = api.get("/api/shipping", params={'currencyCode': 'USD', 'address': '{"streetAddress": "1600 Amphitheatre Parkway", "zipCode": "94043", "city": "Mountain View", "state": "CA", "country": "United States"}'})
    assert resp.status_code >= 400


def test_h10_no_address_0013(api):
    resp = api.get("/api/shipping", params={'itemList': '[{"productId": "6E92ZMYYFZ", "quantity": 1}]', 'currencyCode': 'USD'})
    assert resp.status_code >= 400


def test_h10_no_itemlist_0014(api):
    resp = api.get("/api/shipping", params={'currencyCode': 'USD', 'address': '{"streetAddress": "1600 Amphitheatre Parkway", "zipCode": "94043", "city": "Mountain View", "state": "CA", "country": "United States"}'})
    assert resp.status_code >= 400


def test_h10_no_address_0015(api):
    resp = api.get("/api/shipping", params={'itemList': '[{"productId": "OLJCESPC7Z", "quantity": 1}]', 'currencyCode': 'USD'})
    assert resp.status_code >= 400


def test_h10_no_itemlist_0016(api):
    resp = api.get("/api/shipping", params={'currencyCode': 'USD', 'address': '{"streetAddress": "1600 Amphitheatre Parkway", "zipCode": "94043", "city": "Mountain View", "state": "CA", "country": "United States"}'})
    assert resp.status_code >= 400


def test_h10_no_address_0017(api):
    resp = api.get("/api/shipping", params={'itemList': '[{"productId": "1YMWWN1N4O", "quantity": 1}]', 'currencyCode': 'USD'})
    assert resp.status_code >= 400


def test_h10_no_itemlist_0018(api):
    resp = api.get("/api/shipping", params={'currencyCode': 'USD', 'address': '{"streetAddress": "1600 Amphitheatre Parkway", "zipCode": "94043", "city": "Mountain View", "state": "CA", "country": "United States"}'})
    assert resp.status_code >= 400


def test_h10_no_address_0019(api):
    resp = api.get("/api/shipping", params={'itemList': '[{"productId": "2ZYFJ3GM2N", "quantity": 1}]', 'currencyCode': 'USD'})
    assert resp.status_code >= 400


def test_h10_no_itemlist_0020(api):
    resp = api.get("/api/shipping", params={'currencyCode': 'USD', 'address': '{"streetAddress": "1600 Amphitheatre Parkway", "zipCode": "94043", "city": "Mountain View", "state": "CA", "country": "United States"}'})
    assert resp.status_code >= 400


def test_h10_no_address_0021(api):
    resp = api.get("/api/shipping", params={'itemList': '[{"productId": "LS4PSXUNUM", "quantity": 1}]', 'currencyCode': 'USD'})
    assert resp.status_code >= 400


def test_h10_no_itemlist_0022(api):
    resp = api.get("/api/shipping", params={'currencyCode': 'USD', 'address': '{"streetAddress": "1600 Amphitheatre Parkway", "zipCode": "94043", "city": "Mountain View", "state": "CA", "country": "United States"}'})
    assert resp.status_code >= 400


def test_h10_no_address_0023(api):
    resp = api.get("/api/shipping", params={'itemList': '[{"productId": "6E92ZMYYFZ", "quantity": 1}]', 'currencyCode': 'USD'})
    assert resp.status_code >= 400


def test_h10_no_itemlist_0024(api):
    resp = api.get("/api/shipping", params={'currencyCode': 'USD', 'address': '{"streetAddress": "1600 Amphitheatre Parkway", "zipCode": "94043", "city": "Mountain View", "state": "CA", "country": "United States"}'})
    assert resp.status_code >= 400


def test_h10_no_address_0025(api):
    resp = api.get("/api/shipping", params={'itemList': '[{"productId": "OLJCESPC7Z", "quantity": 1}]', 'currencyCode': 'USD'})
    assert resp.status_code >= 400


def test_h10_no_itemlist_0026(api):
    resp = api.get("/api/shipping", params={'currencyCode': 'USD', 'address': '{"streetAddress": "1600 Amphitheatre Parkway", "zipCode": "94043", "city": "Mountain View", "state": "CA", "country": "United States"}'})
    assert resp.status_code >= 400


def test_h10_no_address_0027(api):
    resp = api.get("/api/shipping", params={'itemList': '[{"productId": "1YMWWN1N4O", "quantity": 1}]', 'currencyCode': 'USD'})
    assert resp.status_code >= 400


def test_h10_no_itemlist_0028(api):
    resp = api.get("/api/shipping", params={'currencyCode': 'USD', 'address': '{"streetAddress": "1600 Amphitheatre Parkway", "zipCode": "94043", "city": "Mountain View", "state": "CA", "country": "United States"}'})
    assert resp.status_code >= 400


def test_h10_no_address_0029(api):
    resp = api.get("/api/shipping", params={'itemList': '[{"productId": "2ZYFJ3GM2N", "quantity": 1}]', 'currencyCode': 'USD'})
    assert resp.status_code >= 400


def test_h10_no_itemlist_0030(api):
    resp = api.get("/api/shipping", params={'currencyCode': 'USD', 'address': '{"streetAddress": "1600 Amphitheatre Parkway", "zipCode": "94043", "city": "Mountain View", "state": "CA", "country": "United States"}'})
    assert resp.status_code >= 400


def test_h10_no_address_0031(api):
    resp = api.get("/api/shipping", params={'itemList': '[{"productId": "LS4PSXUNUM", "quantity": 1}]', 'currencyCode': 'USD'})
    assert resp.status_code >= 400


def test_h10_no_itemlist_0032(api):
    resp = api.get("/api/shipping", params={'currencyCode': 'USD', 'address': '{"streetAddress": "1600 Amphitheatre Parkway", "zipCode": "94043", "city": "Mountain View", "state": "CA", "country": "United States"}'})
    assert resp.status_code >= 400


def test_h10_no_address_0033(api):
    resp = api.get("/api/shipping", params={'itemList': '[{"productId": "6E92ZMYYFZ", "quantity": 1}]', 'currencyCode': 'USD'})
    assert resp.status_code >= 400


def test_h10_no_itemlist_0034(api):
    resp = api.get("/api/shipping", params={'currencyCode': 'USD', 'address': '{"streetAddress": "1600 Amphitheatre Parkway", "zipCode": "94043", "city": "Mountain View", "state": "CA", "country": "United States"}'})
    assert resp.status_code >= 400


def test_h10_no_address_0035(api):
    resp = api.get("/api/shipping", params={'itemList': '[{"productId": "OLJCESPC7Z", "quantity": 1}]', 'currencyCode': 'USD'})
    assert resp.status_code >= 400


def test_h10_no_itemlist_0036(api):
    resp = api.get("/api/shipping", params={'currencyCode': 'USD', 'address': '{"streetAddress": "1600 Amphitheatre Parkway", "zipCode": "94043", "city": "Mountain View", "state": "CA", "country": "United States"}'})
    assert resp.status_code >= 400


def test_h10_no_address_0037(api):
    resp = api.get("/api/shipping", params={'itemList': '[{"productId": "1YMWWN1N4O", "quantity": 1}]', 'currencyCode': 'USD'})
    assert resp.status_code >= 400


def test_h10_no_itemlist_0038(api):
    resp = api.get("/api/shipping", params={'currencyCode': 'USD', 'address': '{"streetAddress": "1600 Amphitheatre Parkway", "zipCode": "94043", "city": "Mountain View", "state": "CA", "country": "United States"}'})
    assert resp.status_code >= 400


def test_h10_no_address_0039(api):
    resp = api.get("/api/shipping", params={'itemList': '[{"productId": "2ZYFJ3GM2N", "quantity": 1}]', 'currencyCode': 'USD'})
    assert resp.status_code >= 400


def test_h10_no_itemlist_0040(api):
    resp = api.get("/api/shipping", params={'currencyCode': 'USD', 'address': '{"streetAddress": "1600 Amphitheatre Parkway", "zipCode": "94043", "city": "Mountain View", "state": "CA", "country": "United States"}'})
    assert resp.status_code >= 400
