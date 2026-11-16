import json  # noqa: F401


def test_h09_ls4psxunum_x1_gbp_redmond_0001(api):
    params = {
        "itemList": json.dumps([{"productId": "LS4PSXUNUM", "quantity": 1}]),
        "currencyCode": "GBP",
        "address": json.dumps({"streetAddress": "One Microsoft Way", "zipCode": "98052", "city": "Redmond", "state": "WA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "GBP"


def test_h09_9siqt8tojo_x2_hkd_cupertino_0002(api):
    params = {
        "itemList": json.dumps([{"productId": "9SIQT8TOJO", "quantity": 2}]),
        "currencyCode": "HKD",
        "address": json.dumps({"streetAddress": "1 Infinite Loop", "zipCode": "95014", "city": "Cupertino", "state": "CA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "HKD"


def test_h09_6e92zmyyfz_x3_hrk_seattle_0003(api):
    params = {
        "itemList": json.dumps([{"productId": "6E92ZMYYFZ", "quantity": 3}]),
        "currencyCode": "HRK",
        "address": json.dumps({"streetAddress": "410 Terry Ave N", "zipCode": "98109", "city": "Seattle", "state": "WA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "HRK"


def test_h09_hqtgwgpnh4_x4_huf_toronto_0004(api):
    params = {
        "itemList": json.dumps([{"productId": "HQTGWGPNH4", "quantity": 4}]),
        "currencyCode": "HUF",
        "address": json.dumps({"streetAddress": "100 Queen St W", "zipCode": "M5H 2N2", "city": "Toronto", "state": "ON", "country": "Canada"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "HUF"


def test_h09_oljcespc7z_x5_idr_mountain_view_0005(api):
    params = {
        "itemList": json.dumps([{"productId": "OLJCESPC7Z", "quantity": 5}]),
        "currencyCode": "IDR",
        "address": json.dumps({"streetAddress": "1600 Amphitheatre Parkway", "zipCode": "94043", "city": "Mountain View", "state": "CA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "IDR"


def test_h09_66vchsjnup_x10_ils_redmond_0006(api):
    params = {
        "itemList": json.dumps([{"productId": "66VCHSJNUP", "quantity": 10}]),
        "currencyCode": "ILS",
        "address": json.dumps({"streetAddress": "One Microsoft Way", "zipCode": "98052", "city": "Redmond", "state": "WA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "ILS"


def test_h09_1ymwwn1n4o_x1_inr_cupertino_0007(api):
    params = {
        "itemList": json.dumps([{"productId": "1YMWWN1N4O", "quantity": 1}]),
        "currencyCode": "INR",
        "address": json.dumps({"streetAddress": "1 Infinite Loop", "zipCode": "95014", "city": "Cupertino", "state": "CA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "INR"


def test_h09_l9ecav7kim_x2_isk_seattle_0008(api):
    params = {
        "itemList": json.dumps([{"productId": "L9ECAV7KIM", "quantity": 2}]),
        "currencyCode": "ISK",
        "address": json.dumps({"streetAddress": "410 Terry Ave N", "zipCode": "98109", "city": "Seattle", "state": "WA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "ISK"


def test_h09_2zyfj3gm2n_x3_jpy_toronto_0009(api):
    params = {
        "itemList": json.dumps([{"productId": "2ZYFJ3GM2N", "quantity": 3}]),
        "currencyCode": "JPY",
        "address": json.dumps({"streetAddress": "100 Queen St W", "zipCode": "M5H 2N2", "city": "Toronto", "state": "ON", "country": "Canada"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "JPY"


def test_h09_0puk6v6ev0_x4_krw_mountain_view_0010(api):
    params = {
        "itemList": json.dumps([{"productId": "0PUK6V6EV0", "quantity": 4}]),
        "currencyCode": "KRW",
        "address": json.dumps({"streetAddress": "1600 Amphitheatre Parkway", "zipCode": "94043", "city": "Mountain View", "state": "CA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "KRW"


def test_h09_ls4psxunum_x5_mxn_redmond_0011(api):
    params = {
        "itemList": json.dumps([{"productId": "LS4PSXUNUM", "quantity": 5}]),
        "currencyCode": "MXN",
        "address": json.dumps({"streetAddress": "One Microsoft Way", "zipCode": "98052", "city": "Redmond", "state": "WA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "MXN"


def test_h09_9siqt8tojo_x10_myr_cupertino_0012(api):
    params = {
        "itemList": json.dumps([{"productId": "9SIQT8TOJO", "quantity": 10}]),
        "currencyCode": "MYR",
        "address": json.dumps({"streetAddress": "1 Infinite Loop", "zipCode": "95014", "city": "Cupertino", "state": "CA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "MYR"


def test_h09_6e92zmyyfz_x1_nok_seattle_0013(api):
    params = {
        "itemList": json.dumps([{"productId": "6E92ZMYYFZ", "quantity": 1}]),
        "currencyCode": "NOK",
        "address": json.dumps({"streetAddress": "410 Terry Ave N", "zipCode": "98109", "city": "Seattle", "state": "WA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "NOK"


def test_h09_hqtgwgpnh4_x2_nzd_toronto_0014(api):
    params = {
        "itemList": json.dumps([{"productId": "HQTGWGPNH4", "quantity": 2}]),
        "currencyCode": "NZD",
        "address": json.dumps({"streetAddress": "100 Queen St W", "zipCode": "M5H 2N2", "city": "Toronto", "state": "ON", "country": "Canada"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "NZD"


def test_h09_oljcespc7z_x3_php_mountain_view_0015(api):
    params = {
        "itemList": json.dumps([{"productId": "OLJCESPC7Z", "quantity": 3}]),
        "currencyCode": "PHP",
        "address": json.dumps({"streetAddress": "1600 Amphitheatre Parkway", "zipCode": "94043", "city": "Mountain View", "state": "CA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "PHP"


def test_h09_66vchsjnup_x4_pln_redmond_0016(api):
    params = {
        "itemList": json.dumps([{"productId": "66VCHSJNUP", "quantity": 4}]),
        "currencyCode": "PLN",
        "address": json.dumps({"streetAddress": "One Microsoft Way", "zipCode": "98052", "city": "Redmond", "state": "WA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "PLN"


def test_h09_1ymwwn1n4o_x5_ron_cupertino_0017(api):
    params = {
        "itemList": json.dumps([{"productId": "1YMWWN1N4O", "quantity": 5}]),
        "currencyCode": "RON",
        "address": json.dumps({"streetAddress": "1 Infinite Loop", "zipCode": "95014", "city": "Cupertino", "state": "CA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "RON"


def test_h09_l9ecav7kim_x10_rub_seattle_0018(api):
    params = {
        "itemList": json.dumps([{"productId": "L9ECAV7KIM", "quantity": 10}]),
        "currencyCode": "RUB",
        "address": json.dumps({"streetAddress": "410 Terry Ave N", "zipCode": "98109", "city": "Seattle", "state": "WA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "RUB"


def test_h09_2zyfj3gm2n_x1_sek_toronto_0019(api):
    params = {
        "itemList": json.dumps([{"productId": "2ZYFJ3GM2N", "quantity": 1}]),
        "currencyCode": "SEK",
        "address": json.dumps({"streetAddress": "100 Queen St W", "zipCode": "M5H 2N2", "city": "Toronto", "state": "ON", "country": "Canada"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "SEK"


def test_h09_0puk6v6ev0_x2_sgd_mountain_view_0020(api):
    params = {
        "itemList": json.dumps([{"productId": "0PUK6V6EV0", "quantity": 2}]),
        "currencyCode": "SGD",
        "address": json.dumps({"streetAddress": "1600 Amphitheatre Parkway", "zipCode": "94043", "city": "Mountain View", "state": "CA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "SGD"


def test_h09_ls4psxunum_x3_thb_redmond_0021(api):
    params = {
        "itemList": json.dumps([{"productId": "LS4PSXUNUM", "quantity": 3}]),
        "currencyCode": "THB",
        "address": json.dumps({"streetAddress": "One Microsoft Way", "zipCode": "98052", "city": "Redmond", "state": "WA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "THB"


def test_h09_9siqt8tojo_x4_try_cupertino_0022(api):
    params = {
        "itemList": json.dumps([{"productId": "9SIQT8TOJO", "quantity": 4}]),
        "currencyCode": "TRY",
        "address": json.dumps({"streetAddress": "1 Infinite Loop", "zipCode": "95014", "city": "Cupertino", "state": "CA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "TRY"


def test_h09_6e92zmyyfz_x5_usd_seattle_0023(api):
    params = {
        "itemList": json.dumps([{"productId": "6E92ZMYYFZ", "quantity": 5}]),
        "currencyCode": "USD",
        "address": json.dumps({"streetAddress": "410 Terry Ave N", "zipCode": "98109", "city": "Seattle", "state": "WA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "USD"
    total_nanos = int(cost["units"]) * 1_000_000_000 + int(cost["nanos"])
    assert abs(total_nanos - 44950000000) <= 1


def test_h09_hqtgwgpnh4_x10_zar_toronto_0024(api):
    params = {
        "itemList": json.dumps([{"productId": "HQTGWGPNH4", "quantity": 10}]),
        "currencyCode": "ZAR",
        "address": json.dumps({"streetAddress": "100 Queen St W", "zipCode": "M5H 2N2", "city": "Toronto", "state": "ON", "country": "Canada"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "ZAR"


def test_h09_oljcespc7z_x1_aud_mountain_view_0025(api):
    params = {
        "itemList": json.dumps([{"productId": "OLJCESPC7Z", "quantity": 1}]),
        "currencyCode": "AUD",
        "address": json.dumps({"streetAddress": "1600 Amphitheatre Parkway", "zipCode": "94043", "city": "Mountain View", "state": "CA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "AUD"


def test_h09_66vchsjnup_x2_bgn_redmond_0026(api):
    params = {
        "itemList": json.dumps([{"productId": "66VCHSJNUP", "quantity": 2}]),
        "currencyCode": "BGN",
        "address": json.dumps({"streetAddress": "One Microsoft Way", "zipCode": "98052", "city": "Redmond", "state": "WA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "BGN"


def test_h09_1ymwwn1n4o_x3_brl_cupertino_0027(api):
    params = {
        "itemList": json.dumps([{"productId": "1YMWWN1N4O", "quantity": 3}]),
        "currencyCode": "BRL",
        "address": json.dumps({"streetAddress": "1 Infinite Loop", "zipCode": "95014", "city": "Cupertino", "state": "CA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "BRL"


def test_h09_l9ecav7kim_x4_cad_seattle_0028(api):
    params = {
        "itemList": json.dumps([{"productId": "L9ECAV7KIM", "quantity": 4}]),
        "currencyCode": "CAD",
        "address": json.dumps({"streetAddress": "410 Terry Ave N", "zipCode": "98109", "city": "Seattle", "state": "WA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "CAD"


def test_h09_2zyfj3gm2n_x5_chf_toronto_0029(api):
    params = {
        "itemList": json.dumps([{"productId": "2ZYFJ3GM2N", "quantity": 5}]),
        "currencyCode": "CHF",
        "address": json.dumps({"streetAddress": "100 Queen St W", "zipCode": "M5H 2N2", "city": "Toronto", "state": "ON", "country": "Canada"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "CHF"


def test_h09_0puk6v6ev0_x10_cny_mountain_view_0030(api):
    params = {
        "itemList": json.dumps([{"productId": "0PUK6V6EV0", "quantity": 10}]),
        "currencyCode": "CNY",
        "address": json.dumps({"streetAddress": "1600 Amphitheatre Parkway", "zipCode": "94043", "city": "Mountain View", "state": "CA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "CNY"


def test_h09_ls4psxunum_x1_czk_redmond_0031(api):
    params = {
        "itemList": json.dumps([{"productId": "LS4PSXUNUM", "quantity": 1}]),
        "currencyCode": "CZK",
        "address": json.dumps({"streetAddress": "One Microsoft Way", "zipCode": "98052", "city": "Redmond", "state": "WA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "CZK"


def test_h09_9siqt8tojo_x2_dkk_cupertino_0032(api):
    params = {
        "itemList": json.dumps([{"productId": "9SIQT8TOJO", "quantity": 2}]),
        "currencyCode": "DKK",
        "address": json.dumps({"streetAddress": "1 Infinite Loop", "zipCode": "95014", "city": "Cupertino", "state": "CA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "DKK"


def test_h09_6e92zmyyfz_x3_eur_seattle_0033(api):
    params = {
        "itemList": json.dumps([{"productId": "6E92ZMYYFZ", "quantity": 3}]),
        "currencyCode": "EUR",
        "address": json.dumps({"streetAddress": "410 Terry Ave N", "zipCode": "98109", "city": "Seattle", "state": "WA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "EUR"


def test_h09_hqtgwgpnh4_x4_gbp_toronto_0034(api):
    params = {
        "itemList": json.dumps([{"productId": "HQTGWGPNH4", "quantity": 4}]),
        "currencyCode": "GBP",
        "address": json.dumps({"streetAddress": "100 Queen St W", "zipCode": "M5H 2N2", "city": "Toronto", "state": "ON", "country": "Canada"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "GBP"


def test_h09_oljcespc7z_x5_hkd_mountain_view_0035(api):
    params = {
        "itemList": json.dumps([{"productId": "OLJCESPC7Z", "quantity": 5}]),
        "currencyCode": "HKD",
        "address": json.dumps({"streetAddress": "1600 Amphitheatre Parkway", "zipCode": "94043", "city": "Mountain View", "state": "CA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "HKD"


def test_h09_66vchsjnup_x10_hrk_redmond_0036(api):
    params = {
        "itemList": json.dumps([{"productId": "66VCHSJNUP", "quantity": 10}]),
        "currencyCode": "HRK",
        "address": json.dumps({"streetAddress": "One Microsoft Way", "zipCode": "98052", "city": "Redmond", "state": "WA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "HRK"


def test_h09_1ymwwn1n4o_x1_huf_cupertino_0037(api):
    params = {
        "itemList": json.dumps([{"productId": "1YMWWN1N4O", "quantity": 1}]),
        "currencyCode": "HUF",
        "address": json.dumps({"streetAddress": "1 Infinite Loop", "zipCode": "95014", "city": "Cupertino", "state": "CA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "HUF"


def test_h09_l9ecav7kim_x2_idr_seattle_0038(api):
    params = {
        "itemList": json.dumps([{"productId": "L9ECAV7KIM", "quantity": 2}]),
        "currencyCode": "IDR",
        "address": json.dumps({"streetAddress": "410 Terry Ave N", "zipCode": "98109", "city": "Seattle", "state": "WA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "IDR"


def test_h09_2zyfj3gm2n_x3_ils_toronto_0039(api):
    params = {
        "itemList": json.dumps([{"productId": "2ZYFJ3GM2N", "quantity": 3}]),
        "currencyCode": "ILS",
        "address": json.dumps({"streetAddress": "100 Queen St W", "zipCode": "M5H 2N2", "city": "Toronto", "state": "ON", "country": "Canada"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "ILS"


def test_h09_0puk6v6ev0_x4_inr_mountain_view_0040(api):
    params = {
        "itemList": json.dumps([{"productId": "0PUK6V6EV0", "quantity": 4}]),
        "currencyCode": "INR",
        "address": json.dumps({"streetAddress": "1600 Amphitheatre Parkway", "zipCode": "94043", "city": "Mountain View", "state": "CA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "INR"


def test_h09_ls4psxunum_x5_isk_redmond_0041(api):
    params = {
        "itemList": json.dumps([{"productId": "LS4PSXUNUM", "quantity": 5}]),
        "currencyCode": "ISK",
        "address": json.dumps({"streetAddress": "One Microsoft Way", "zipCode": "98052", "city": "Redmond", "state": "WA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "ISK"


def test_h09_9siqt8tojo_x10_jpy_cupertino_0042(api):
    params = {
        "itemList": json.dumps([{"productId": "9SIQT8TOJO", "quantity": 10}]),
        "currencyCode": "JPY",
        "address": json.dumps({"streetAddress": "1 Infinite Loop", "zipCode": "95014", "city": "Cupertino", "state": "CA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "JPY"


def test_h09_6e92zmyyfz_x1_krw_seattle_0043(api):
    params = {
        "itemList": json.dumps([{"productId": "6E92ZMYYFZ", "quantity": 1}]),
        "currencyCode": "KRW",
        "address": json.dumps({"streetAddress": "410 Terry Ave N", "zipCode": "98109", "city": "Seattle", "state": "WA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "KRW"


def test_h09_hqtgwgpnh4_x2_mxn_toronto_0044(api):
    params = {
        "itemList": json.dumps([{"productId": "HQTGWGPNH4", "quantity": 2}]),
        "currencyCode": "MXN",
        "address": json.dumps({"streetAddress": "100 Queen St W", "zipCode": "M5H 2N2", "city": "Toronto", "state": "ON", "country": "Canada"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "MXN"


def test_h09_oljcespc7z_x3_myr_mountain_view_0045(api):
    params = {
        "itemList": json.dumps([{"productId": "OLJCESPC7Z", "quantity": 3}]),
        "currencyCode": "MYR",
        "address": json.dumps({"streetAddress": "1600 Amphitheatre Parkway", "zipCode": "94043", "city": "Mountain View", "state": "CA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "MYR"


def test_h09_66vchsjnup_x4_nok_redmond_0046(api):
    params = {
        "itemList": json.dumps([{"productId": "66VCHSJNUP", "quantity": 4}]),
        "currencyCode": "NOK",
        "address": json.dumps({"streetAddress": "One Microsoft Way", "zipCode": "98052", "city": "Redmond", "state": "WA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "NOK"


def test_h09_1ymwwn1n4o_x5_nzd_cupertino_0047(api):
    params = {
        "itemList": json.dumps([{"productId": "1YMWWN1N4O", "quantity": 5}]),
        "currencyCode": "NZD",
        "address": json.dumps({"streetAddress": "1 Infinite Loop", "zipCode": "95014", "city": "Cupertino", "state": "CA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "NZD"


def test_h09_l9ecav7kim_x10_php_seattle_0048(api):
    params = {
        "itemList": json.dumps([{"productId": "L9ECAV7KIM", "quantity": 10}]),
        "currencyCode": "PHP",
        "address": json.dumps({"streetAddress": "410 Terry Ave N", "zipCode": "98109", "city": "Seattle", "state": "WA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "PHP"


def test_h09_2zyfj3gm2n_x1_pln_toronto_0049(api):
    params = {
        "itemList": json.dumps([{"productId": "2ZYFJ3GM2N", "quantity": 1}]),
        "currencyCode": "PLN",
        "address": json.dumps({"streetAddress": "100 Queen St W", "zipCode": "M5H 2N2", "city": "Toronto", "state": "ON", "country": "Canada"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "PLN"


def test_h09_0puk6v6ev0_x2_ron_mountain_view_0050(api):
    params = {
        "itemList": json.dumps([{"productId": "0PUK6V6EV0", "quantity": 2}]),
        "currencyCode": "RON",
        "address": json.dumps({"streetAddress": "1600 Amphitheatre Parkway", "zipCode": "94043", "city": "Mountain View", "state": "CA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "RON"


def test_h09_ls4psxunum_x3_rub_redmond_0051(api):
    params = {
        "itemList": json.dumps([{"productId": "LS4PSXUNUM", "quantity": 3}]),
        "currencyCode": "RUB",
        "address": json.dumps({"streetAddress": "One Microsoft Way", "zipCode": "98052", "city": "Redmond", "state": "WA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "RUB"


def test_h09_9siqt8tojo_x4_sek_cupertino_0052(api):
    params = {
        "itemList": json.dumps([{"productId": "9SIQT8TOJO", "quantity": 4}]),
        "currencyCode": "SEK",
        "address": json.dumps({"streetAddress": "1 Infinite Loop", "zipCode": "95014", "city": "Cupertino", "state": "CA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "SEK"


def test_h09_6e92zmyyfz_x5_sgd_seattle_0053(api):
    params = {
        "itemList": json.dumps([{"productId": "6E92ZMYYFZ", "quantity": 5}]),
        "currencyCode": "SGD",
        "address": json.dumps({"streetAddress": "410 Terry Ave N", "zipCode": "98109", "city": "Seattle", "state": "WA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "SGD"


def test_h09_hqtgwgpnh4_x10_thb_toronto_0054(api):
    params = {
        "itemList": json.dumps([{"productId": "HQTGWGPNH4", "quantity": 10}]),
        "currencyCode": "THB",
        "address": json.dumps({"streetAddress": "100 Queen St W", "zipCode": "M5H 2N2", "city": "Toronto", "state": "ON", "country": "Canada"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "THB"


def test_h09_oljcespc7z_x1_try_mountain_view_0055(api):
    params = {
        "itemList": json.dumps([{"productId": "OLJCESPC7Z", "quantity": 1}]),
        "currencyCode": "TRY",
        "address": json.dumps({"streetAddress": "1600 Amphitheatre Parkway", "zipCode": "94043", "city": "Mountain View", "state": "CA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "TRY"


def test_h09_66vchsjnup_x2_usd_redmond_0056(api):
    params = {
        "itemList": json.dumps([{"productId": "66VCHSJNUP", "quantity": 2}]),
        "currencyCode": "USD",
        "address": json.dumps({"streetAddress": "One Microsoft Way", "zipCode": "98052", "city": "Redmond", "state": "WA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "USD"
    total_nanos = int(cost["units"]) * 1_000_000_000 + int(cost["nanos"])
    assert abs(total_nanos - 17980000000) <= 1


def test_h09_1ymwwn1n4o_x3_zar_cupertino_0057(api):
    params = {
        "itemList": json.dumps([{"productId": "1YMWWN1N4O", "quantity": 3}]),
        "currencyCode": "ZAR",
        "address": json.dumps({"streetAddress": "1 Infinite Loop", "zipCode": "95014", "city": "Cupertino", "state": "CA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "ZAR"


def test_h09_l9ecav7kim_x4_aud_seattle_0058(api):
    params = {
        "itemList": json.dumps([{"productId": "L9ECAV7KIM", "quantity": 4}]),
        "currencyCode": "AUD",
        "address": json.dumps({"streetAddress": "410 Terry Ave N", "zipCode": "98109", "city": "Seattle", "state": "WA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "AUD"


def test_h09_2zyfj3gm2n_x5_bgn_toronto_0059(api):
    params = {
        "itemList": json.dumps([{"productId": "2ZYFJ3GM2N", "quantity": 5}]),
        "currencyCode": "BGN",
        "address": json.dumps({"streetAddress": "100 Queen St W", "zipCode": "M5H 2N2", "city": "Toronto", "state": "ON", "country": "Canada"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "BGN"


def test_h09_0puk6v6ev0_x10_brl_mountain_view_0060(api):
    params = {
        "itemList": json.dumps([{"productId": "0PUK6V6EV0", "quantity": 10}]),
        "currencyCode": "BRL",
        "address": json.dumps({"streetAddress": "1600 Amphitheatre Parkway", "zipCode": "94043", "city": "Mountain View", "state": "CA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "BRL"


def test_h09_ls4psxunum_x1_cad_redmond_0061(api):
    params = {
        "itemList": json.dumps([{"productId": "LS4PSXUNUM", "quantity": 1}]),
        "currencyCode": "CAD",
        "address": json.dumps({"streetAddress": "One Microsoft Way", "zipCode": "98052", "city": "Redmond", "state": "WA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "CAD"


def test_h09_9siqt8tojo_x2_chf_cupertino_0062(api):
    params = {
        "itemList": json.dumps([{"productId": "9SIQT8TOJO", "quantity": 2}]),
        "currencyCode": "CHF",
        "address": json.dumps({"streetAddress": "1 Infinite Loop", "zipCode": "95014", "city": "Cupertino", "state": "CA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "CHF"


def test_h09_6e92zmyyfz_x3_cny_seattle_0063(api):
    params = {
        "itemList": json.dumps([{"productId": "6E92ZMYYFZ", "quantity": 3}]),
        "currencyCode": "CNY",
        "address": json.dumps({"streetAddress": "410 Terry Ave N", "zipCode": "98109", "city": "Seattle", "state": "WA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "CNY"


def test_h09_hqtgwgpnh4_x4_czk_toronto_0064(api):
    params = {
        "itemList": json.dumps([{"productId": "HQTGWGPNH4", "quantity": 4}]),
        "currencyCode": "CZK",
        "address": json.dumps({"streetAddress": "100 Queen St W", "zipCode": "M5H 2N2", "city": "Toronto", "state": "ON", "country": "Canada"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "CZK"


def test_h09_oljcespc7z_x5_dkk_mountain_view_0065(api):
    params = {
        "itemList": json.dumps([{"productId": "OLJCESPC7Z", "quantity": 5}]),
        "currencyCode": "DKK",
        "address": json.dumps({"streetAddress": "1600 Amphitheatre Parkway", "zipCode": "94043", "city": "Mountain View", "state": "CA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "DKK"


def test_h09_66vchsjnup_x10_eur_redmond_0066(api):
    params = {
        "itemList": json.dumps([{"productId": "66VCHSJNUP", "quantity": 10}]),
        "currencyCode": "EUR",
        "address": json.dumps({"streetAddress": "One Microsoft Way", "zipCode": "98052", "city": "Redmond", "state": "WA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "EUR"


def test_h09_1ymwwn1n4o_x1_gbp_cupertino_0067(api):
    params = {
        "itemList": json.dumps([{"productId": "1YMWWN1N4O", "quantity": 1}]),
        "currencyCode": "GBP",
        "address": json.dumps({"streetAddress": "1 Infinite Loop", "zipCode": "95014", "city": "Cupertino", "state": "CA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "GBP"


def test_h09_l9ecav7kim_x2_hkd_seattle_0068(api):
    params = {
        "itemList": json.dumps([{"productId": "L9ECAV7KIM", "quantity": 2}]),
        "currencyCode": "HKD",
        "address": json.dumps({"streetAddress": "410 Terry Ave N", "zipCode": "98109", "city": "Seattle", "state": "WA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "HKD"


def test_h09_2zyfj3gm2n_x3_hrk_toronto_0069(api):
    params = {
        "itemList": json.dumps([{"productId": "2ZYFJ3GM2N", "quantity": 3}]),
        "currencyCode": "HRK",
        "address": json.dumps({"streetAddress": "100 Queen St W", "zipCode": "M5H 2N2", "city": "Toronto", "state": "ON", "country": "Canada"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "HRK"


def test_h09_0puk6v6ev0_x4_huf_mountain_view_0070(api):
    params = {
        "itemList": json.dumps([{"productId": "0PUK6V6EV0", "quantity": 4}]),
        "currencyCode": "HUF",
        "address": json.dumps({"streetAddress": "1600 Amphitheatre Parkway", "zipCode": "94043", "city": "Mountain View", "state": "CA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "HUF"


def test_h09_ls4psxunum_x5_idr_redmond_0071(api):
    params = {
        "itemList": json.dumps([{"productId": "LS4PSXUNUM", "quantity": 5}]),
        "currencyCode": "IDR",
        "address": json.dumps({"streetAddress": "One Microsoft Way", "zipCode": "98052", "city": "Redmond", "state": "WA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "IDR"


def test_h09_9siqt8tojo_x10_ils_cupertino_0072(api):
    params = {
        "itemList": json.dumps([{"productId": "9SIQT8TOJO", "quantity": 10}]),
        "currencyCode": "ILS",
        "address": json.dumps({"streetAddress": "1 Infinite Loop", "zipCode": "95014", "city": "Cupertino", "state": "CA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "ILS"


def test_h09_6e92zmyyfz_x1_inr_seattle_0073(api):
    params = {
        "itemList": json.dumps([{"productId": "6E92ZMYYFZ", "quantity": 1}]),
        "currencyCode": "INR",
        "address": json.dumps({"streetAddress": "410 Terry Ave N", "zipCode": "98109", "city": "Seattle", "state": "WA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "INR"


def test_h09_hqtgwgpnh4_x2_isk_toronto_0074(api):
    params = {
        "itemList": json.dumps([{"productId": "HQTGWGPNH4", "quantity": 2}]),
        "currencyCode": "ISK",
        "address": json.dumps({"streetAddress": "100 Queen St W", "zipCode": "M5H 2N2", "city": "Toronto", "state": "ON", "country": "Canada"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "ISK"


def test_h09_oljcespc7z_x3_jpy_mountain_view_0075(api):
    params = {
        "itemList": json.dumps([{"productId": "OLJCESPC7Z", "quantity": 3}]),
        "currencyCode": "JPY",
        "address": json.dumps({"streetAddress": "1600 Amphitheatre Parkway", "zipCode": "94043", "city": "Mountain View", "state": "CA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "JPY"


def test_h09_66vchsjnup_x4_krw_redmond_0076(api):
    params = {
        "itemList": json.dumps([{"productId": "66VCHSJNUP", "quantity": 4}]),
        "currencyCode": "KRW",
        "address": json.dumps({"streetAddress": "One Microsoft Way", "zipCode": "98052", "city": "Redmond", "state": "WA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "KRW"


def test_h09_1ymwwn1n4o_x5_mxn_cupertino_0077(api):
    params = {
        "itemList": json.dumps([{"productId": "1YMWWN1N4O", "quantity": 5}]),
        "currencyCode": "MXN",
        "address": json.dumps({"streetAddress": "1 Infinite Loop", "zipCode": "95014", "city": "Cupertino", "state": "CA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "MXN"


def test_h09_l9ecav7kim_x10_myr_seattle_0078(api):
    params = {
        "itemList": json.dumps([{"productId": "L9ECAV7KIM", "quantity": 10}]),
        "currencyCode": "MYR",
        "address": json.dumps({"streetAddress": "410 Terry Ave N", "zipCode": "98109", "city": "Seattle", "state": "WA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "MYR"


def test_h09_2zyfj3gm2n_x1_nok_toronto_0079(api):
    params = {
        "itemList": json.dumps([{"productId": "2ZYFJ3GM2N", "quantity": 1}]),
        "currencyCode": "NOK",
        "address": json.dumps({"streetAddress": "100 Queen St W", "zipCode": "M5H 2N2", "city": "Toronto", "state": "ON", "country": "Canada"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "NOK"


def test_h09_0puk6v6ev0_x2_nzd_mountain_view_0080(api):
    params = {
        "itemList": json.dumps([{"productId": "0PUK6V6EV0", "quantity": 2}]),
        "currencyCode": "NZD",
        "address": json.dumps({"streetAddress": "1600 Amphitheatre Parkway", "zipCode": "94043", "city": "Mountain View", "state": "CA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "NZD"


def test_h09_ls4psxunum_x3_php_redmond_0081(api):
    params = {
        "itemList": json.dumps([{"productId": "LS4PSXUNUM", "quantity": 3}]),
        "currencyCode": "PHP",
        "address": json.dumps({"streetAddress": "One Microsoft Way", "zipCode": "98052", "city": "Redmond", "state": "WA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "PHP"


def test_h09_9siqt8tojo_x4_pln_cupertino_0082(api):
    params = {
        "itemList": json.dumps([{"productId": "9SIQT8TOJO", "quantity": 4}]),
        "currencyCode": "PLN",
        "address": json.dumps({"streetAddress": "1 Infinite Loop", "zipCode": "95014", "city": "Cupertino", "state": "CA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "PLN"


def test_h09_6e92zmyyfz_x5_ron_seattle_0083(api):
    params = {
        "itemList": json.dumps([{"productId": "6E92ZMYYFZ", "quantity": 5}]),
        "currencyCode": "RON",
        "address": json.dumps({"streetAddress": "410 Terry Ave N", "zipCode": "98109", "city": "Seattle", "state": "WA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "RON"


def test_h09_hqtgwgpnh4_x10_rub_toronto_0084(api):
    params = {
        "itemList": json.dumps([{"productId": "HQTGWGPNH4", "quantity": 10}]),
        "currencyCode": "RUB",
        "address": json.dumps({"streetAddress": "100 Queen St W", "zipCode": "M5H 2N2", "city": "Toronto", "state": "ON", "country": "Canada"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "RUB"


def test_h09_oljcespc7z_x1_sek_mountain_view_0085(api):
    params = {
        "itemList": json.dumps([{"productId": "OLJCESPC7Z", "quantity": 1}]),
        "currencyCode": "SEK",
        "address": json.dumps({"streetAddress": "1600 Amphitheatre Parkway", "zipCode": "94043", "city": "Mountain View", "state": "CA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "SEK"


def test_h09_66vchsjnup_x2_sgd_redmond_0086(api):
    params = {
        "itemList": json.dumps([{"productId": "66VCHSJNUP", "quantity": 2}]),
        "currencyCode": "SGD",
        "address": json.dumps({"streetAddress": "One Microsoft Way", "zipCode": "98052", "city": "Redmond", "state": "WA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "SGD"


def test_h09_1ymwwn1n4o_x3_thb_cupertino_0087(api):
    params = {
        "itemList": json.dumps([{"productId": "1YMWWN1N4O", "quantity": 3}]),
        "currencyCode": "THB",
        "address": json.dumps({"streetAddress": "1 Infinite Loop", "zipCode": "95014", "city": "Cupertino", "state": "CA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "THB"


def test_h09_l9ecav7kim_x4_try_seattle_0088(api):
    params = {
        "itemList": json.dumps([{"productId": "L9ECAV7KIM", "quantity": 4}]),
        "currencyCode": "TRY",
        "address": json.dumps({"streetAddress": "410 Terry Ave N", "zipCode": "98109", "city": "Seattle", "state": "WA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "TRY"


def test_h09_2zyfj3gm2n_x5_usd_toronto_0089(api):
    params = {
        "itemList": json.dumps([{"productId": "2ZYFJ3GM2N", "quantity": 5}]),
        "currencyCode": "USD",
        "address": json.dumps({"streetAddress": "100 Queen St W", "zipCode": "M5H 2N2", "city": "Toronto", "state": "ON", "country": "Canada"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "USD"
    total_nanos = int(cost["units"]) * 1_000_000_000 + int(cost["nanos"])
    assert abs(total_nanos - 44950000000) <= 1


def test_h09_0puk6v6ev0_x10_zar_mountain_view_0090(api):
    params = {
        "itemList": json.dumps([{"productId": "0PUK6V6EV0", "quantity": 10}]),
        "currencyCode": "ZAR",
        "address": json.dumps({"streetAddress": "1600 Amphitheatre Parkway", "zipCode": "94043", "city": "Mountain View", "state": "CA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "ZAR"


def test_h09_ls4psxunum_x1_aud_redmond_0091(api):
    params = {
        "itemList": json.dumps([{"productId": "LS4PSXUNUM", "quantity": 1}]),
        "currencyCode": "AUD",
        "address": json.dumps({"streetAddress": "One Microsoft Way", "zipCode": "98052", "city": "Redmond", "state": "WA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "AUD"


def test_h09_9siqt8tojo_x2_bgn_cupertino_0092(api):
    params = {
        "itemList": json.dumps([{"productId": "9SIQT8TOJO", "quantity": 2}]),
        "currencyCode": "BGN",
        "address": json.dumps({"streetAddress": "1 Infinite Loop", "zipCode": "95014", "city": "Cupertino", "state": "CA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "BGN"


def test_h09_6e92zmyyfz_x3_brl_seattle_0093(api):
    params = {
        "itemList": json.dumps([{"productId": "6E92ZMYYFZ", "quantity": 3}]),
        "currencyCode": "BRL",
        "address": json.dumps({"streetAddress": "410 Terry Ave N", "zipCode": "98109", "city": "Seattle", "state": "WA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "BRL"


def test_h09_hqtgwgpnh4_x4_cad_toronto_0094(api):
    params = {
        "itemList": json.dumps([{"productId": "HQTGWGPNH4", "quantity": 4}]),
        "currencyCode": "CAD",
        "address": json.dumps({"streetAddress": "100 Queen St W", "zipCode": "M5H 2N2", "city": "Toronto", "state": "ON", "country": "Canada"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "CAD"


def test_h09_oljcespc7z_x5_chf_mountain_view_0095(api):
    params = {
        "itemList": json.dumps([{"productId": "OLJCESPC7Z", "quantity": 5}]),
        "currencyCode": "CHF",
        "address": json.dumps({"streetAddress": "1600 Amphitheatre Parkway", "zipCode": "94043", "city": "Mountain View", "state": "CA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "CHF"


def test_h09_66vchsjnup_x10_cny_redmond_0096(api):
    params = {
        "itemList": json.dumps([{"productId": "66VCHSJNUP", "quantity": 10}]),
        "currencyCode": "CNY",
        "address": json.dumps({"streetAddress": "One Microsoft Way", "zipCode": "98052", "city": "Redmond", "state": "WA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "CNY"


def test_h09_1ymwwn1n4o_x1_czk_cupertino_0097(api):
    params = {
        "itemList": json.dumps([{"productId": "1YMWWN1N4O", "quantity": 1}]),
        "currencyCode": "CZK",
        "address": json.dumps({"streetAddress": "1 Infinite Loop", "zipCode": "95014", "city": "Cupertino", "state": "CA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "CZK"


def test_h09_l9ecav7kim_x2_dkk_seattle_0098(api):
    params = {
        "itemList": json.dumps([{"productId": "L9ECAV7KIM", "quantity": 2}]),
        "currencyCode": "DKK",
        "address": json.dumps({"streetAddress": "410 Terry Ave N", "zipCode": "98109", "city": "Seattle", "state": "WA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "DKK"


def test_h09_2zyfj3gm2n_x3_eur_toronto_0099(api):
    params = {
        "itemList": json.dumps([{"productId": "2ZYFJ3GM2N", "quantity": 3}]),
        "currencyCode": "EUR",
        "address": json.dumps({"streetAddress": "100 Queen St W", "zipCode": "M5H 2N2", "city": "Toronto", "state": "ON", "country": "Canada"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "EUR"


def test_h09_0puk6v6ev0_x4_gbp_mountain_view_0100(api):
    params = {
        "itemList": json.dumps([{"productId": "0PUK6V6EV0", "quantity": 4}]),
        "currencyCode": "GBP",
        "address": json.dumps({"streetAddress": "1600 Amphitheatre Parkway", "zipCode": "94043", "city": "Mountain View", "state": "CA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "GBP"


def test_h09_ls4psxunum_x5_hkd_redmond_0101(api):
    params = {
        "itemList": json.dumps([{"productId": "LS4PSXUNUM", "quantity": 5}]),
        "currencyCode": "HKD",
        "address": json.dumps({"streetAddress": "One Microsoft Way", "zipCode": "98052", "city": "Redmond", "state": "WA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "HKD"


def test_h09_9siqt8tojo_x10_hrk_cupertino_0102(api):
    params = {
        "itemList": json.dumps([{"productId": "9SIQT8TOJO", "quantity": 10}]),
        "currencyCode": "HRK",
        "address": json.dumps({"streetAddress": "1 Infinite Loop", "zipCode": "95014", "city": "Cupertino", "state": "CA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "HRK"


def test_h09_6e92zmyyfz_x1_huf_seattle_0103(api):
    params = {
        "itemList": json.dumps([{"productId": "6E92ZMYYFZ", "quantity": 1}]),
        "currencyCode": "HUF",
        "address": json.dumps({"streetAddress": "410 Terry Ave N", "zipCode": "98109", "city": "Seattle", "state": "WA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "HUF"


def test_h09_hqtgwgpnh4_x2_idr_toronto_0104(api):
    params = {
        "itemList": json.dumps([{"productId": "HQTGWGPNH4", "quantity": 2}]),
        "currencyCode": "IDR",
        "address": json.dumps({"streetAddress": "100 Queen St W", "zipCode": "M5H 2N2", "city": "Toronto", "state": "ON", "country": "Canada"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "IDR"


def test_h09_oljcespc7z_x3_ils_mountain_view_0105(api):
    params = {
        "itemList": json.dumps([{"productId": "OLJCESPC7Z", "quantity": 3}]),
        "currencyCode": "ILS",
        "address": json.dumps({"streetAddress": "1600 Amphitheatre Parkway", "zipCode": "94043", "city": "Mountain View", "state": "CA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "ILS"


def test_h09_66vchsjnup_x4_inr_redmond_0106(api):
    params = {
        "itemList": json.dumps([{"productId": "66VCHSJNUP", "quantity": 4}]),
        "currencyCode": "INR",
        "address": json.dumps({"streetAddress": "One Microsoft Way", "zipCode": "98052", "city": "Redmond", "state": "WA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "INR"


def test_h09_1ymwwn1n4o_x5_isk_cupertino_0107(api):
    params = {
        "itemList": json.dumps([{"productId": "1YMWWN1N4O", "quantity": 5}]),
        "currencyCode": "ISK",
        "address": json.dumps({"streetAddress": "1 Infinite Loop", "zipCode": "95014", "city": "Cupertino", "state": "CA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "ISK"


def test_h09_l9ecav7kim_x10_jpy_seattle_0108(api):
    params = {
        "itemList": json.dumps([{"productId": "L9ECAV7KIM", "quantity": 10}]),
        "currencyCode": "JPY",
        "address": json.dumps({"streetAddress": "410 Terry Ave N", "zipCode": "98109", "city": "Seattle", "state": "WA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "JPY"


def test_h09_2zyfj3gm2n_x1_krw_toronto_0109(api):
    params = {
        "itemList": json.dumps([{"productId": "2ZYFJ3GM2N", "quantity": 1}]),
        "currencyCode": "KRW",
        "address": json.dumps({"streetAddress": "100 Queen St W", "zipCode": "M5H 2N2", "city": "Toronto", "state": "ON", "country": "Canada"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "KRW"


def test_h09_0puk6v6ev0_x2_mxn_mountain_view_0110(api):
    params = {
        "itemList": json.dumps([{"productId": "0PUK6V6EV0", "quantity": 2}]),
        "currencyCode": "MXN",
        "address": json.dumps({"streetAddress": "1600 Amphitheatre Parkway", "zipCode": "94043", "city": "Mountain View", "state": "CA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "MXN"


def test_h09_ls4psxunum_x3_myr_redmond_0111(api):
    params = {
        "itemList": json.dumps([{"productId": "LS4PSXUNUM", "quantity": 3}]),
        "currencyCode": "MYR",
        "address": json.dumps({"streetAddress": "One Microsoft Way", "zipCode": "98052", "city": "Redmond", "state": "WA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "MYR"


def test_h09_9siqt8tojo_x4_nok_cupertino_0112(api):
    params = {
        "itemList": json.dumps([{"productId": "9SIQT8TOJO", "quantity": 4}]),
        "currencyCode": "NOK",
        "address": json.dumps({"streetAddress": "1 Infinite Loop", "zipCode": "95014", "city": "Cupertino", "state": "CA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "NOK"


def test_h09_6e92zmyyfz_x5_nzd_seattle_0113(api):
    params = {
        "itemList": json.dumps([{"productId": "6E92ZMYYFZ", "quantity": 5}]),
        "currencyCode": "NZD",
        "address": json.dumps({"streetAddress": "410 Terry Ave N", "zipCode": "98109", "city": "Seattle", "state": "WA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "NZD"


def test_h09_hqtgwgpnh4_x10_php_toronto_0114(api):
    params = {
        "itemList": json.dumps([{"productId": "HQTGWGPNH4", "quantity": 10}]),
        "currencyCode": "PHP",
        "address": json.dumps({"streetAddress": "100 Queen St W", "zipCode": "M5H 2N2", "city": "Toronto", "state": "ON", "country": "Canada"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "PHP"


def test_h09_oljcespc7z_x1_pln_mountain_view_0115(api):
    params = {
        "itemList": json.dumps([{"productId": "OLJCESPC7Z", "quantity": 1}]),
        "currencyCode": "PLN",
        "address": json.dumps({"streetAddress": "1600 Amphitheatre Parkway", "zipCode": "94043", "city": "Mountain View", "state": "CA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "PLN"


def test_h09_66vchsjnup_x2_ron_redmond_0116(api):
    params = {
        "itemList": json.dumps([{"productId": "66VCHSJNUP", "quantity": 2}]),
        "currencyCode": "RON",
        "address": json.dumps({"streetAddress": "One Microsoft Way", "zipCode": "98052", "city": "Redmond", "state": "WA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "RON"


def test_h09_1ymwwn1n4o_x3_rub_cupertino_0117(api):
    params = {
        "itemList": json.dumps([{"productId": "1YMWWN1N4O", "quantity": 3}]),
        "currencyCode": "RUB",
        "address": json.dumps({"streetAddress": "1 Infinite Loop", "zipCode": "95014", "city": "Cupertino", "state": "CA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "RUB"


def test_h09_l9ecav7kim_x4_sek_seattle_0118(api):
    params = {
        "itemList": json.dumps([{"productId": "L9ECAV7KIM", "quantity": 4}]),
        "currencyCode": "SEK",
        "address": json.dumps({"streetAddress": "410 Terry Ave N", "zipCode": "98109", "city": "Seattle", "state": "WA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "SEK"


def test_h09_2zyfj3gm2n_x5_sgd_toronto_0119(api):
    params = {
        "itemList": json.dumps([{"productId": "2ZYFJ3GM2N", "quantity": 5}]),
        "currencyCode": "SGD",
        "address": json.dumps({"streetAddress": "100 Queen St W", "zipCode": "M5H 2N2", "city": "Toronto", "state": "ON", "country": "Canada"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "SGD"


def test_h09_0puk6v6ev0_x10_thb_mountain_view_0120(api):
    params = {
        "itemList": json.dumps([{"productId": "0PUK6V6EV0", "quantity": 10}]),
        "currencyCode": "THB",
        "address": json.dumps({"streetAddress": "1600 Amphitheatre Parkway", "zipCode": "94043", "city": "Mountain View", "state": "CA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "THB"


def test_h09_ls4psxunum_x1_try_redmond_0121(api):
    params = {
        "itemList": json.dumps([{"productId": "LS4PSXUNUM", "quantity": 1}]),
        "currencyCode": "TRY",
        "address": json.dumps({"streetAddress": "One Microsoft Way", "zipCode": "98052", "city": "Redmond", "state": "WA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "TRY"


def test_h09_9siqt8tojo_x2_usd_cupertino_0122(api):
    params = {
        "itemList": json.dumps([{"productId": "9SIQT8TOJO", "quantity": 2}]),
        "currencyCode": "USD",
        "address": json.dumps({"streetAddress": "1 Infinite Loop", "zipCode": "95014", "city": "Cupertino", "state": "CA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "USD"
    total_nanos = int(cost["units"]) * 1_000_000_000 + int(cost["nanos"])
    assert abs(total_nanos - 17980000000) <= 1


def test_h09_6e92zmyyfz_x3_zar_seattle_0123(api):
    params = {
        "itemList": json.dumps([{"productId": "6E92ZMYYFZ", "quantity": 3}]),
        "currencyCode": "ZAR",
        "address": json.dumps({"streetAddress": "410 Terry Ave N", "zipCode": "98109", "city": "Seattle", "state": "WA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "ZAR"


def test_h09_hqtgwgpnh4_x4_aud_toronto_0124(api):
    params = {
        "itemList": json.dumps([{"productId": "HQTGWGPNH4", "quantity": 4}]),
        "currencyCode": "AUD",
        "address": json.dumps({"streetAddress": "100 Queen St W", "zipCode": "M5H 2N2", "city": "Toronto", "state": "ON", "country": "Canada"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "AUD"


def test_h09_oljcespc7z_x5_bgn_mountain_view_0125(api):
    params = {
        "itemList": json.dumps([{"productId": "OLJCESPC7Z", "quantity": 5}]),
        "currencyCode": "BGN",
        "address": json.dumps({"streetAddress": "1600 Amphitheatre Parkway", "zipCode": "94043", "city": "Mountain View", "state": "CA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "BGN"


def test_h09_66vchsjnup_x10_brl_redmond_0126(api):
    params = {
        "itemList": json.dumps([{"productId": "66VCHSJNUP", "quantity": 10}]),
        "currencyCode": "BRL",
        "address": json.dumps({"streetAddress": "One Microsoft Way", "zipCode": "98052", "city": "Redmond", "state": "WA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "BRL"


def test_h09_1ymwwn1n4o_x1_cad_cupertino_0127(api):
    params = {
        "itemList": json.dumps([{"productId": "1YMWWN1N4O", "quantity": 1}]),
        "currencyCode": "CAD",
        "address": json.dumps({"streetAddress": "1 Infinite Loop", "zipCode": "95014", "city": "Cupertino", "state": "CA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "CAD"


def test_h09_l9ecav7kim_x2_chf_seattle_0128(api):
    params = {
        "itemList": json.dumps([{"productId": "L9ECAV7KIM", "quantity": 2}]),
        "currencyCode": "CHF",
        "address": json.dumps({"streetAddress": "410 Terry Ave N", "zipCode": "98109", "city": "Seattle", "state": "WA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "CHF"


def test_h09_2zyfj3gm2n_x3_cny_toronto_0129(api):
    params = {
        "itemList": json.dumps([{"productId": "2ZYFJ3GM2N", "quantity": 3}]),
        "currencyCode": "CNY",
        "address": json.dumps({"streetAddress": "100 Queen St W", "zipCode": "M5H 2N2", "city": "Toronto", "state": "ON", "country": "Canada"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "CNY"


def test_h09_0puk6v6ev0_x4_czk_mountain_view_0130(api):
    params = {
        "itemList": json.dumps([{"productId": "0PUK6V6EV0", "quantity": 4}]),
        "currencyCode": "CZK",
        "address": json.dumps({"streetAddress": "1600 Amphitheatre Parkway", "zipCode": "94043", "city": "Mountain View", "state": "CA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "CZK"


def test_h09_ls4psxunum_x5_dkk_redmond_0131(api):
    params = {
        "itemList": json.dumps([{"productId": "LS4PSXUNUM", "quantity": 5}]),
        "currencyCode": "DKK",
        "address": json.dumps({"streetAddress": "One Microsoft Way", "zipCode": "98052", "city": "Redmond", "state": "WA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "DKK"


def test_h09_9siqt8tojo_x10_eur_cupertino_0132(api):
    params = {
        "itemList": json.dumps([{"productId": "9SIQT8TOJO", "quantity": 10}]),
        "currencyCode": "EUR",
        "address": json.dumps({"streetAddress": "1 Infinite Loop", "zipCode": "95014", "city": "Cupertino", "state": "CA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "EUR"


def test_h09_6e92zmyyfz_x1_gbp_seattle_0133(api):
    params = {
        "itemList": json.dumps([{"productId": "6E92ZMYYFZ", "quantity": 1}]),
        "currencyCode": "GBP",
        "address": json.dumps({"streetAddress": "410 Terry Ave N", "zipCode": "98109", "city": "Seattle", "state": "WA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "GBP"


def test_h09_hqtgwgpnh4_x2_hkd_toronto_0134(api):
    params = {
        "itemList": json.dumps([{"productId": "HQTGWGPNH4", "quantity": 2}]),
        "currencyCode": "HKD",
        "address": json.dumps({"streetAddress": "100 Queen St W", "zipCode": "M5H 2N2", "city": "Toronto", "state": "ON", "country": "Canada"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "HKD"


def test_h09_oljcespc7z_x3_hrk_mountain_view_0135(api):
    params = {
        "itemList": json.dumps([{"productId": "OLJCESPC7Z", "quantity": 3}]),
        "currencyCode": "HRK",
        "address": json.dumps({"streetAddress": "1600 Amphitheatre Parkway", "zipCode": "94043", "city": "Mountain View", "state": "CA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "HRK"


def test_h09_66vchsjnup_x4_huf_redmond_0136(api):
    params = {
        "itemList": json.dumps([{"productId": "66VCHSJNUP", "quantity": 4}]),
        "currencyCode": "HUF",
        "address": json.dumps({"streetAddress": "One Microsoft Way", "zipCode": "98052", "city": "Redmond", "state": "WA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "HUF"


def test_h09_1ymwwn1n4o_x5_idr_cupertino_0137(api):
    params = {
        "itemList": json.dumps([{"productId": "1YMWWN1N4O", "quantity": 5}]),
        "currencyCode": "IDR",
        "address": json.dumps({"streetAddress": "1 Infinite Loop", "zipCode": "95014", "city": "Cupertino", "state": "CA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "IDR"


def test_h09_l9ecav7kim_x10_ils_seattle_0138(api):
    params = {
        "itemList": json.dumps([{"productId": "L9ECAV7KIM", "quantity": 10}]),
        "currencyCode": "ILS",
        "address": json.dumps({"streetAddress": "410 Terry Ave N", "zipCode": "98109", "city": "Seattle", "state": "WA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "ILS"


def test_h09_2zyfj3gm2n_x1_inr_toronto_0139(api):
    params = {
        "itemList": json.dumps([{"productId": "2ZYFJ3GM2N", "quantity": 1}]),
        "currencyCode": "INR",
        "address": json.dumps({"streetAddress": "100 Queen St W", "zipCode": "M5H 2N2", "city": "Toronto", "state": "ON", "country": "Canada"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "INR"


def test_h09_0puk6v6ev0_x2_isk_mountain_view_0140(api):
    params = {
        "itemList": json.dumps([{"productId": "0PUK6V6EV0", "quantity": 2}]),
        "currencyCode": "ISK",
        "address": json.dumps({"streetAddress": "1600 Amphitheatre Parkway", "zipCode": "94043", "city": "Mountain View", "state": "CA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "ISK"


def test_h09_ls4psxunum_x3_jpy_redmond_0141(api):
    params = {
        "itemList": json.dumps([{"productId": "LS4PSXUNUM", "quantity": 3}]),
        "currencyCode": "JPY",
        "address": json.dumps({"streetAddress": "One Microsoft Way", "zipCode": "98052", "city": "Redmond", "state": "WA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "JPY"


def test_h09_9siqt8tojo_x4_krw_cupertino_0142(api):
    params = {
        "itemList": json.dumps([{"productId": "9SIQT8TOJO", "quantity": 4}]),
        "currencyCode": "KRW",
        "address": json.dumps({"streetAddress": "1 Infinite Loop", "zipCode": "95014", "city": "Cupertino", "state": "CA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "KRW"


def test_h09_6e92zmyyfz_x5_mxn_seattle_0143(api):
    params = {
        "itemList": json.dumps([{"productId": "6E92ZMYYFZ", "quantity": 5}]),
        "currencyCode": "MXN",
        "address": json.dumps({"streetAddress": "410 Terry Ave N", "zipCode": "98109", "city": "Seattle", "state": "WA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "MXN"


def test_h09_hqtgwgpnh4_x10_myr_toronto_0144(api):
    params = {
        "itemList": json.dumps([{"productId": "HQTGWGPNH4", "quantity": 10}]),
        "currencyCode": "MYR",
        "address": json.dumps({"streetAddress": "100 Queen St W", "zipCode": "M5H 2N2", "city": "Toronto", "state": "ON", "country": "Canada"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "MYR"


def test_h09_oljcespc7z_x1_nok_mountain_view_0145(api):
    params = {
        "itemList": json.dumps([{"productId": "OLJCESPC7Z", "quantity": 1}]),
        "currencyCode": "NOK",
        "address": json.dumps({"streetAddress": "1600 Amphitheatre Parkway", "zipCode": "94043", "city": "Mountain View", "state": "CA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "NOK"


def test_h09_66vchsjnup_x2_nzd_redmond_0146(api):
    params = {
        "itemList": json.dumps([{"productId": "66VCHSJNUP", "quantity": 2}]),
        "currencyCode": "NZD",
        "address": json.dumps({"streetAddress": "One Microsoft Way", "zipCode": "98052", "city": "Redmond", "state": "WA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "NZD"


def test_h09_1ymwwn1n4o_x3_php_cupertino_0147(api):
    params = {
        "itemList": json.dumps([{"productId": "1YMWWN1N4O", "quantity": 3}]),
        "currencyCode": "PHP",
        "address": json.dumps({"streetAddress": "1 Infinite Loop", "zipCode": "95014", "city": "Cupertino", "state": "CA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "PHP"


def test_h09_l9ecav7kim_x4_pln_seattle_0148(api):
    params = {
        "itemList": json.dumps([{"productId": "L9ECAV7KIM", "quantity": 4}]),
        "currencyCode": "PLN",
        "address": json.dumps({"streetAddress": "410 Terry Ave N", "zipCode": "98109", "city": "Seattle", "state": "WA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "PLN"


def test_h09_2zyfj3gm2n_x5_ron_toronto_0149(api):
    params = {
        "itemList": json.dumps([{"productId": "2ZYFJ3GM2N", "quantity": 5}]),
        "currencyCode": "RON",
        "address": json.dumps({"streetAddress": "100 Queen St W", "zipCode": "M5H 2N2", "city": "Toronto", "state": "ON", "country": "Canada"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "RON"


def test_h09_0puk6v6ev0_x10_rub_mountain_view_0150(api):
    params = {
        "itemList": json.dumps([{"productId": "0PUK6V6EV0", "quantity": 10}]),
        "currencyCode": "RUB",
        "address": json.dumps({"streetAddress": "1600 Amphitheatre Parkway", "zipCode": "94043", "city": "Mountain View", "state": "CA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "RUB"


def test_h09_ls4psxunum_x1_sek_redmond_0151(api):
    params = {
        "itemList": json.dumps([{"productId": "LS4PSXUNUM", "quantity": 1}]),
        "currencyCode": "SEK",
        "address": json.dumps({"streetAddress": "One Microsoft Way", "zipCode": "98052", "city": "Redmond", "state": "WA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "SEK"


def test_h09_9siqt8tojo_x2_sgd_cupertino_0152(api):
    params = {
        "itemList": json.dumps([{"productId": "9SIQT8TOJO", "quantity": 2}]),
        "currencyCode": "SGD",
        "address": json.dumps({"streetAddress": "1 Infinite Loop", "zipCode": "95014", "city": "Cupertino", "state": "CA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "SGD"


def test_h09_6e92zmyyfz_x3_thb_seattle_0153(api):
    params = {
        "itemList": json.dumps([{"productId": "6E92ZMYYFZ", "quantity": 3}]),
        "currencyCode": "THB",
        "address": json.dumps({"streetAddress": "410 Terry Ave N", "zipCode": "98109", "city": "Seattle", "state": "WA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "THB"


def test_h09_hqtgwgpnh4_x4_try_toronto_0154(api):
    params = {
        "itemList": json.dumps([{"productId": "HQTGWGPNH4", "quantity": 4}]),
        "currencyCode": "TRY",
        "address": json.dumps({"streetAddress": "100 Queen St W", "zipCode": "M5H 2N2", "city": "Toronto", "state": "ON", "country": "Canada"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "TRY"


def test_h09_oljcespc7z_x5_usd_mountain_view_0155(api):
    params = {
        "itemList": json.dumps([{"productId": "OLJCESPC7Z", "quantity": 5}]),
        "currencyCode": "USD",
        "address": json.dumps({"streetAddress": "1600 Amphitheatre Parkway", "zipCode": "94043", "city": "Mountain View", "state": "CA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "USD"
    total_nanos = int(cost["units"]) * 1_000_000_000 + int(cost["nanos"])
    assert abs(total_nanos - 44950000000) <= 1


def test_h09_66vchsjnup_x10_zar_redmond_0156(api):
    params = {
        "itemList": json.dumps([{"productId": "66VCHSJNUP", "quantity": 10}]),
        "currencyCode": "ZAR",
        "address": json.dumps({"streetAddress": "One Microsoft Way", "zipCode": "98052", "city": "Redmond", "state": "WA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "ZAR"


def test_h09_1ymwwn1n4o_x1_aud_cupertino_0157(api):
    params = {
        "itemList": json.dumps([{"productId": "1YMWWN1N4O", "quantity": 1}]),
        "currencyCode": "AUD",
        "address": json.dumps({"streetAddress": "1 Infinite Loop", "zipCode": "95014", "city": "Cupertino", "state": "CA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "AUD"


def test_h09_l9ecav7kim_x2_bgn_seattle_0158(api):
    params = {
        "itemList": json.dumps([{"productId": "L9ECAV7KIM", "quantity": 2}]),
        "currencyCode": "BGN",
        "address": json.dumps({"streetAddress": "410 Terry Ave N", "zipCode": "98109", "city": "Seattle", "state": "WA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "BGN"


def test_h09_2zyfj3gm2n_x3_brl_toronto_0159(api):
    params = {
        "itemList": json.dumps([{"productId": "2ZYFJ3GM2N", "quantity": 3}]),
        "currencyCode": "BRL",
        "address": json.dumps({"streetAddress": "100 Queen St W", "zipCode": "M5H 2N2", "city": "Toronto", "state": "ON", "country": "Canada"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "BRL"


def test_h09_0puk6v6ev0_x4_cad_mountain_view_0160(api):
    params = {
        "itemList": json.dumps([{"productId": "0PUK6V6EV0", "quantity": 4}]),
        "currencyCode": "CAD",
        "address": json.dumps({"streetAddress": "1600 Amphitheatre Parkway", "zipCode": "94043", "city": "Mountain View", "state": "CA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "CAD"


def test_h09_ls4psxunum_x5_chf_redmond_0161(api):
    params = {
        "itemList": json.dumps([{"productId": "LS4PSXUNUM", "quantity": 5}]),
        "currencyCode": "CHF",
        "address": json.dumps({"streetAddress": "One Microsoft Way", "zipCode": "98052", "city": "Redmond", "state": "WA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "CHF"


def test_h09_9siqt8tojo_x10_cny_cupertino_0162(api):
    params = {
        "itemList": json.dumps([{"productId": "9SIQT8TOJO", "quantity": 10}]),
        "currencyCode": "CNY",
        "address": json.dumps({"streetAddress": "1 Infinite Loop", "zipCode": "95014", "city": "Cupertino", "state": "CA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "CNY"


def test_h09_6e92zmyyfz_x1_czk_seattle_0163(api):
    params = {
        "itemList": json.dumps([{"productId": "6E92ZMYYFZ", "quantity": 1}]),
        "currencyCode": "CZK",
        "address": json.dumps({"streetAddress": "410 Terry Ave N", "zipCode": "98109", "city": "Seattle", "state": "WA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "CZK"


def test_h09_hqtgwgpnh4_x2_dkk_toronto_0164(api):
    params = {
        "itemList": json.dumps([{"productId": "HQTGWGPNH4", "quantity": 2}]),
        "currencyCode": "DKK",
        "address": json.dumps({"streetAddress": "100 Queen St W", "zipCode": "M5H 2N2", "city": "Toronto", "state": "ON", "country": "Canada"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "DKK"


def test_h09_oljcespc7z_x3_eur_mountain_view_0165(api):
    params = {
        "itemList": json.dumps([{"productId": "OLJCESPC7Z", "quantity": 3}]),
        "currencyCode": "EUR",
        "address": json.dumps({"streetAddress": "1600 Amphitheatre Parkway", "zipCode": "94043", "city": "Mountain View", "state": "CA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "EUR"


def test_h09_66vchsjnup_x4_gbp_redmond_0166(api):
    params = {
        "itemList": json.dumps([{"productId": "66VCHSJNUP", "quantity": 4}]),
        "currencyCode": "GBP",
        "address": json.dumps({"streetAddress": "One Microsoft Way", "zipCode": "98052", "city": "Redmond", "state": "WA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "GBP"


def test_h09_1ymwwn1n4o_x5_hkd_cupertino_0167(api):
    params = {
        "itemList": json.dumps([{"productId": "1YMWWN1N4O", "quantity": 5}]),
        "currencyCode": "HKD",
        "address": json.dumps({"streetAddress": "1 Infinite Loop", "zipCode": "95014", "city": "Cupertino", "state": "CA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "HKD"


def test_h09_l9ecav7kim_x10_hrk_seattle_0168(api):
    params = {
        "itemList": json.dumps([{"productId": "L9ECAV7KIM", "quantity": 10}]),
        "currencyCode": "HRK",
        "address": json.dumps({"streetAddress": "410 Terry Ave N", "zipCode": "98109", "city": "Seattle", "state": "WA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "HRK"


def test_h09_2zyfj3gm2n_x1_huf_toronto_0169(api):
    params = {
        "itemList": json.dumps([{"productId": "2ZYFJ3GM2N", "quantity": 1}]),
        "currencyCode": "HUF",
        "address": json.dumps({"streetAddress": "100 Queen St W", "zipCode": "M5H 2N2", "city": "Toronto", "state": "ON", "country": "Canada"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "HUF"


def test_h09_0puk6v6ev0_x2_idr_mountain_view_0170(api):
    params = {
        "itemList": json.dumps([{"productId": "0PUK6V6EV0", "quantity": 2}]),
        "currencyCode": "IDR",
        "address": json.dumps({"streetAddress": "1600 Amphitheatre Parkway", "zipCode": "94043", "city": "Mountain View", "state": "CA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "IDR"


def test_h09_ls4psxunum_x3_ils_redmond_0171(api):
    params = {
        "itemList": json.dumps([{"productId": "LS4PSXUNUM", "quantity": 3}]),
        "currencyCode": "ILS",
        "address": json.dumps({"streetAddress": "One Microsoft Way", "zipCode": "98052", "city": "Redmond", "state": "WA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "ILS"


def test_h09_9siqt8tojo_x4_inr_cupertino_0172(api):
    params = {
        "itemList": json.dumps([{"productId": "9SIQT8TOJO", "quantity": 4}]),
        "currencyCode": "INR",
        "address": json.dumps({"streetAddress": "1 Infinite Loop", "zipCode": "95014", "city": "Cupertino", "state": "CA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "INR"


def test_h09_6e92zmyyfz_x5_isk_seattle_0173(api):
    params = {
        "itemList": json.dumps([{"productId": "6E92ZMYYFZ", "quantity": 5}]),
        "currencyCode": "ISK",
        "address": json.dumps({"streetAddress": "410 Terry Ave N", "zipCode": "98109", "city": "Seattle", "state": "WA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "ISK"


def test_h09_hqtgwgpnh4_x10_jpy_toronto_0174(api):
    params = {
        "itemList": json.dumps([{"productId": "HQTGWGPNH4", "quantity": 10}]),
        "currencyCode": "JPY",
        "address": json.dumps({"streetAddress": "100 Queen St W", "zipCode": "M5H 2N2", "city": "Toronto", "state": "ON", "country": "Canada"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "JPY"


def test_h09_oljcespc7z_x1_krw_mountain_view_0175(api):
    params = {
        "itemList": json.dumps([{"productId": "OLJCESPC7Z", "quantity": 1}]),
        "currencyCode": "KRW",
        "address": json.dumps({"streetAddress": "1600 Amphitheatre Parkway", "zipCode": "94043", "city": "Mountain View", "state": "CA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "KRW"


def test_h09_66vchsjnup_x2_mxn_redmond_0176(api):
    params = {
        "itemList": json.dumps([{"productId": "66VCHSJNUP", "quantity": 2}]),
        "currencyCode": "MXN",
        "address": json.dumps({"streetAddress": "One Microsoft Way", "zipCode": "98052", "city": "Redmond", "state": "WA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "MXN"


def test_h09_1ymwwn1n4o_x3_myr_cupertino_0177(api):
    params = {
        "itemList": json.dumps([{"productId": "1YMWWN1N4O", "quantity": 3}]),
        "currencyCode": "MYR",
        "address": json.dumps({"streetAddress": "1 Infinite Loop", "zipCode": "95014", "city": "Cupertino", "state": "CA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "MYR"


def test_h09_l9ecav7kim_x4_nok_seattle_0178(api):
    params = {
        "itemList": json.dumps([{"productId": "L9ECAV7KIM", "quantity": 4}]),
        "currencyCode": "NOK",
        "address": json.dumps({"streetAddress": "410 Terry Ave N", "zipCode": "98109", "city": "Seattle", "state": "WA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "NOK"


def test_h09_2zyfj3gm2n_x5_nzd_toronto_0179(api):
    params = {
        "itemList": json.dumps([{"productId": "2ZYFJ3GM2N", "quantity": 5}]),
        "currencyCode": "NZD",
        "address": json.dumps({"streetAddress": "100 Queen St W", "zipCode": "M5H 2N2", "city": "Toronto", "state": "ON", "country": "Canada"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "NZD"


def test_h09_0puk6v6ev0_x10_php_mountain_view_0180(api):
    params = {
        "itemList": json.dumps([{"productId": "0PUK6V6EV0", "quantity": 10}]),
        "currencyCode": "PHP",
        "address": json.dumps({"streetAddress": "1600 Amphitheatre Parkway", "zipCode": "94043", "city": "Mountain View", "state": "CA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "PHP"


def test_h09_ls4psxunum_x1_pln_redmond_0181(api):
    params = {
        "itemList": json.dumps([{"productId": "LS4PSXUNUM", "quantity": 1}]),
        "currencyCode": "PLN",
        "address": json.dumps({"streetAddress": "One Microsoft Way", "zipCode": "98052", "city": "Redmond", "state": "WA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "PLN"


def test_h09_9siqt8tojo_x2_ron_cupertino_0182(api):
    params = {
        "itemList": json.dumps([{"productId": "9SIQT8TOJO", "quantity": 2}]),
        "currencyCode": "RON",
        "address": json.dumps({"streetAddress": "1 Infinite Loop", "zipCode": "95014", "city": "Cupertino", "state": "CA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "RON"


def test_h09_6e92zmyyfz_x3_rub_seattle_0183(api):
    params = {
        "itemList": json.dumps([{"productId": "6E92ZMYYFZ", "quantity": 3}]),
        "currencyCode": "RUB",
        "address": json.dumps({"streetAddress": "410 Terry Ave N", "zipCode": "98109", "city": "Seattle", "state": "WA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "RUB"


def test_h09_hqtgwgpnh4_x4_sek_toronto_0184(api):
    params = {
        "itemList": json.dumps([{"productId": "HQTGWGPNH4", "quantity": 4}]),
        "currencyCode": "SEK",
        "address": json.dumps({"streetAddress": "100 Queen St W", "zipCode": "M5H 2N2", "city": "Toronto", "state": "ON", "country": "Canada"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "SEK"


def test_h09_oljcespc7z_x5_sgd_mountain_view_0185(api):
    params = {
        "itemList": json.dumps([{"productId": "OLJCESPC7Z", "quantity": 5}]),
        "currencyCode": "SGD",
        "address": json.dumps({"streetAddress": "1600 Amphitheatre Parkway", "zipCode": "94043", "city": "Mountain View", "state": "CA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "SGD"


def test_h09_66vchsjnup_x10_thb_redmond_0186(api):
    params = {
        "itemList": json.dumps([{"productId": "66VCHSJNUP", "quantity": 10}]),
        "currencyCode": "THB",
        "address": json.dumps({"streetAddress": "One Microsoft Way", "zipCode": "98052", "city": "Redmond", "state": "WA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "THB"


def test_h09_1ymwwn1n4o_x1_try_cupertino_0187(api):
    params = {
        "itemList": json.dumps([{"productId": "1YMWWN1N4O", "quantity": 1}]),
        "currencyCode": "TRY",
        "address": json.dumps({"streetAddress": "1 Infinite Loop", "zipCode": "95014", "city": "Cupertino", "state": "CA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "TRY"


def test_h09_l9ecav7kim_x2_usd_seattle_0188(api):
    params = {
        "itemList": json.dumps([{"productId": "L9ECAV7KIM", "quantity": 2}]),
        "currencyCode": "USD",
        "address": json.dumps({"streetAddress": "410 Terry Ave N", "zipCode": "98109", "city": "Seattle", "state": "WA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "USD"
    total_nanos = int(cost["units"]) * 1_000_000_000 + int(cost["nanos"])
    assert abs(total_nanos - 17980000000) <= 1


def test_h09_2zyfj3gm2n_x3_zar_toronto_0189(api):
    params = {
        "itemList": json.dumps([{"productId": "2ZYFJ3GM2N", "quantity": 3}]),
        "currencyCode": "ZAR",
        "address": json.dumps({"streetAddress": "100 Queen St W", "zipCode": "M5H 2N2", "city": "Toronto", "state": "ON", "country": "Canada"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "ZAR"


def test_h09_0puk6v6ev0_x4_aud_mountain_view_0190(api):
    params = {
        "itemList": json.dumps([{"productId": "0PUK6V6EV0", "quantity": 4}]),
        "currencyCode": "AUD",
        "address": json.dumps({"streetAddress": "1600 Amphitheatre Parkway", "zipCode": "94043", "city": "Mountain View", "state": "CA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "AUD"


def test_h09_ls4psxunum_x5_bgn_redmond_0191(api):
    params = {
        "itemList": json.dumps([{"productId": "LS4PSXUNUM", "quantity": 5}]),
        "currencyCode": "BGN",
        "address": json.dumps({"streetAddress": "One Microsoft Way", "zipCode": "98052", "city": "Redmond", "state": "WA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "BGN"


def test_h09_9siqt8tojo_x10_brl_cupertino_0192(api):
    params = {
        "itemList": json.dumps([{"productId": "9SIQT8TOJO", "quantity": 10}]),
        "currencyCode": "BRL",
        "address": json.dumps({"streetAddress": "1 Infinite Loop", "zipCode": "95014", "city": "Cupertino", "state": "CA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "BRL"


def test_h09_6e92zmyyfz_x1_cad_seattle_0193(api):
    params = {
        "itemList": json.dumps([{"productId": "6E92ZMYYFZ", "quantity": 1}]),
        "currencyCode": "CAD",
        "address": json.dumps({"streetAddress": "410 Terry Ave N", "zipCode": "98109", "city": "Seattle", "state": "WA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "CAD"


def test_h09_hqtgwgpnh4_x2_chf_toronto_0194(api):
    params = {
        "itemList": json.dumps([{"productId": "HQTGWGPNH4", "quantity": 2}]),
        "currencyCode": "CHF",
        "address": json.dumps({"streetAddress": "100 Queen St W", "zipCode": "M5H 2N2", "city": "Toronto", "state": "ON", "country": "Canada"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "CHF"


def test_h09_oljcespc7z_x3_cny_mountain_view_0195(api):
    params = {
        "itemList": json.dumps([{"productId": "OLJCESPC7Z", "quantity": 3}]),
        "currencyCode": "CNY",
        "address": json.dumps({"streetAddress": "1600 Amphitheatre Parkway", "zipCode": "94043", "city": "Mountain View", "state": "CA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "CNY"


def test_h09_66vchsjnup_x4_czk_redmond_0196(api):
    params = {
        "itemList": json.dumps([{"productId": "66VCHSJNUP", "quantity": 4}]),
        "currencyCode": "CZK",
        "address": json.dumps({"streetAddress": "One Microsoft Way", "zipCode": "98052", "city": "Redmond", "state": "WA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "CZK"


def test_h09_1ymwwn1n4o_x5_dkk_cupertino_0197(api):
    params = {
        "itemList": json.dumps([{"productId": "1YMWWN1N4O", "quantity": 5}]),
        "currencyCode": "DKK",
        "address": json.dumps({"streetAddress": "1 Infinite Loop", "zipCode": "95014", "city": "Cupertino", "state": "CA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "DKK"


def test_h09_l9ecav7kim_x10_eur_seattle_0198(api):
    params = {
        "itemList": json.dumps([{"productId": "L9ECAV7KIM", "quantity": 10}]),
        "currencyCode": "EUR",
        "address": json.dumps({"streetAddress": "410 Terry Ave N", "zipCode": "98109", "city": "Seattle", "state": "WA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "EUR"


def test_h09_2zyfj3gm2n_x1_gbp_toronto_0199(api):
    params = {
        "itemList": json.dumps([{"productId": "2ZYFJ3GM2N", "quantity": 1}]),
        "currencyCode": "GBP",
        "address": json.dumps({"streetAddress": "100 Queen St W", "zipCode": "M5H 2N2", "city": "Toronto", "state": "ON", "country": "Canada"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "GBP"


def test_h09_0puk6v6ev0_x2_hkd_mountain_view_0200(api):
    params = {
        "itemList": json.dumps([{"productId": "0PUK6V6EV0", "quantity": 2}]),
        "currencyCode": "HKD",
        "address": json.dumps({"streetAddress": "1600 Amphitheatre Parkway", "zipCode": "94043", "city": "Mountain View", "state": "CA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "HKD"


def test_h09_ls4psxunum_x3_hrk_redmond_0201(api):
    params = {
        "itemList": json.dumps([{"productId": "LS4PSXUNUM", "quantity": 3}]),
        "currencyCode": "HRK",
        "address": json.dumps({"streetAddress": "One Microsoft Way", "zipCode": "98052", "city": "Redmond", "state": "WA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "HRK"


def test_h09_9siqt8tojo_x4_huf_cupertino_0202(api):
    params = {
        "itemList": json.dumps([{"productId": "9SIQT8TOJO", "quantity": 4}]),
        "currencyCode": "HUF",
        "address": json.dumps({"streetAddress": "1 Infinite Loop", "zipCode": "95014", "city": "Cupertino", "state": "CA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "HUF"


def test_h09_6e92zmyyfz_x5_idr_seattle_0203(api):
    params = {
        "itemList": json.dumps([{"productId": "6E92ZMYYFZ", "quantity": 5}]),
        "currencyCode": "IDR",
        "address": json.dumps({"streetAddress": "410 Terry Ave N", "zipCode": "98109", "city": "Seattle", "state": "WA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "IDR"


def test_h09_hqtgwgpnh4_x10_ils_toronto_0204(api):
    params = {
        "itemList": json.dumps([{"productId": "HQTGWGPNH4", "quantity": 10}]),
        "currencyCode": "ILS",
        "address": json.dumps({"streetAddress": "100 Queen St W", "zipCode": "M5H 2N2", "city": "Toronto", "state": "ON", "country": "Canada"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "ILS"


def test_h09_oljcespc7z_x1_inr_mountain_view_0205(api):
    params = {
        "itemList": json.dumps([{"productId": "OLJCESPC7Z", "quantity": 1}]),
        "currencyCode": "INR",
        "address": json.dumps({"streetAddress": "1600 Amphitheatre Parkway", "zipCode": "94043", "city": "Mountain View", "state": "CA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "INR"


def test_h09_66vchsjnup_x2_isk_redmond_0206(api):
    params = {
        "itemList": json.dumps([{"productId": "66VCHSJNUP", "quantity": 2}]),
        "currencyCode": "ISK",
        "address": json.dumps({"streetAddress": "One Microsoft Way", "zipCode": "98052", "city": "Redmond", "state": "WA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "ISK"


def test_h09_1ymwwn1n4o_x3_jpy_cupertino_0207(api):
    params = {
        "itemList": json.dumps([{"productId": "1YMWWN1N4O", "quantity": 3}]),
        "currencyCode": "JPY",
        "address": json.dumps({"streetAddress": "1 Infinite Loop", "zipCode": "95014", "city": "Cupertino", "state": "CA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "JPY"


def test_h09_l9ecav7kim_x4_krw_seattle_0208(api):
    params = {
        "itemList": json.dumps([{"productId": "L9ECAV7KIM", "quantity": 4}]),
        "currencyCode": "KRW",
        "address": json.dumps({"streetAddress": "410 Terry Ave N", "zipCode": "98109", "city": "Seattle", "state": "WA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "KRW"


def test_h09_2zyfj3gm2n_x5_mxn_toronto_0209(api):
    params = {
        "itemList": json.dumps([{"productId": "2ZYFJ3GM2N", "quantity": 5}]),
        "currencyCode": "MXN",
        "address": json.dumps({"streetAddress": "100 Queen St W", "zipCode": "M5H 2N2", "city": "Toronto", "state": "ON", "country": "Canada"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "MXN"


def test_h09_0puk6v6ev0_x10_myr_mountain_view_0210(api):
    params = {
        "itemList": json.dumps([{"productId": "0PUK6V6EV0", "quantity": 10}]),
        "currencyCode": "MYR",
        "address": json.dumps({"streetAddress": "1600 Amphitheatre Parkway", "zipCode": "94043", "city": "Mountain View", "state": "CA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "MYR"


def test_h09_ls4psxunum_x1_nok_redmond_0211(api):
    params = {
        "itemList": json.dumps([{"productId": "LS4PSXUNUM", "quantity": 1}]),
        "currencyCode": "NOK",
        "address": json.dumps({"streetAddress": "One Microsoft Way", "zipCode": "98052", "city": "Redmond", "state": "WA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "NOK"


def test_h09_9siqt8tojo_x2_nzd_cupertino_0212(api):
    params = {
        "itemList": json.dumps([{"productId": "9SIQT8TOJO", "quantity": 2}]),
        "currencyCode": "NZD",
        "address": json.dumps({"streetAddress": "1 Infinite Loop", "zipCode": "95014", "city": "Cupertino", "state": "CA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "NZD"


def test_h09_6e92zmyyfz_x3_php_seattle_0213(api):
    params = {
        "itemList": json.dumps([{"productId": "6E92ZMYYFZ", "quantity": 3}]),
        "currencyCode": "PHP",
        "address": json.dumps({"streetAddress": "410 Terry Ave N", "zipCode": "98109", "city": "Seattle", "state": "WA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "PHP"


def test_h09_hqtgwgpnh4_x4_pln_toronto_0214(api):
    params = {
        "itemList": json.dumps([{"productId": "HQTGWGPNH4", "quantity": 4}]),
        "currencyCode": "PLN",
        "address": json.dumps({"streetAddress": "100 Queen St W", "zipCode": "M5H 2N2", "city": "Toronto", "state": "ON", "country": "Canada"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "PLN"


def test_h09_oljcespc7z_x5_ron_mountain_view_0215(api):
    params = {
        "itemList": json.dumps([{"productId": "OLJCESPC7Z", "quantity": 5}]),
        "currencyCode": "RON",
        "address": json.dumps({"streetAddress": "1600 Amphitheatre Parkway", "zipCode": "94043", "city": "Mountain View", "state": "CA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "RON"


def test_h09_66vchsjnup_x10_rub_redmond_0216(api):
    params = {
        "itemList": json.dumps([{"productId": "66VCHSJNUP", "quantity": 10}]),
        "currencyCode": "RUB",
        "address": json.dumps({"streetAddress": "One Microsoft Way", "zipCode": "98052", "city": "Redmond", "state": "WA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "RUB"


def test_h09_1ymwwn1n4o_x1_sek_cupertino_0217(api):
    params = {
        "itemList": json.dumps([{"productId": "1YMWWN1N4O", "quantity": 1}]),
        "currencyCode": "SEK",
        "address": json.dumps({"streetAddress": "1 Infinite Loop", "zipCode": "95014", "city": "Cupertino", "state": "CA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "SEK"


def test_h09_l9ecav7kim_x2_sgd_seattle_0218(api):
    params = {
        "itemList": json.dumps([{"productId": "L9ECAV7KIM", "quantity": 2}]),
        "currencyCode": "SGD",
        "address": json.dumps({"streetAddress": "410 Terry Ave N", "zipCode": "98109", "city": "Seattle", "state": "WA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "SGD"


def test_h09_2zyfj3gm2n_x3_thb_toronto_0219(api):
    params = {
        "itemList": json.dumps([{"productId": "2ZYFJ3GM2N", "quantity": 3}]),
        "currencyCode": "THB",
        "address": json.dumps({"streetAddress": "100 Queen St W", "zipCode": "M5H 2N2", "city": "Toronto", "state": "ON", "country": "Canada"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "THB"


def test_h09_0puk6v6ev0_x4_try_mountain_view_0220(api):
    params = {
        "itemList": json.dumps([{"productId": "0PUK6V6EV0", "quantity": 4}]),
        "currencyCode": "TRY",
        "address": json.dumps({"streetAddress": "1600 Amphitheatre Parkway", "zipCode": "94043", "city": "Mountain View", "state": "CA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "TRY"


def test_h09_ls4psxunum_x5_usd_redmond_0221(api):
    params = {
        "itemList": json.dumps([{"productId": "LS4PSXUNUM", "quantity": 5}]),
        "currencyCode": "USD",
        "address": json.dumps({"streetAddress": "One Microsoft Way", "zipCode": "98052", "city": "Redmond", "state": "WA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "USD"
    total_nanos = int(cost["units"]) * 1_000_000_000 + int(cost["nanos"])
    assert abs(total_nanos - 44950000000) <= 1


def test_h09_9siqt8tojo_x10_zar_cupertino_0222(api):
    params = {
        "itemList": json.dumps([{"productId": "9SIQT8TOJO", "quantity": 10}]),
        "currencyCode": "ZAR",
        "address": json.dumps({"streetAddress": "1 Infinite Loop", "zipCode": "95014", "city": "Cupertino", "state": "CA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "ZAR"


def test_h09_6e92zmyyfz_x1_aud_seattle_0223(api):
    params = {
        "itemList": json.dumps([{"productId": "6E92ZMYYFZ", "quantity": 1}]),
        "currencyCode": "AUD",
        "address": json.dumps({"streetAddress": "410 Terry Ave N", "zipCode": "98109", "city": "Seattle", "state": "WA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "AUD"


def test_h09_hqtgwgpnh4_x2_bgn_toronto_0224(api):
    params = {
        "itemList": json.dumps([{"productId": "HQTGWGPNH4", "quantity": 2}]),
        "currencyCode": "BGN",
        "address": json.dumps({"streetAddress": "100 Queen St W", "zipCode": "M5H 2N2", "city": "Toronto", "state": "ON", "country": "Canada"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "BGN"


def test_h09_oljcespc7z_x3_brl_mountain_view_0225(api):
    params = {
        "itemList": json.dumps([{"productId": "OLJCESPC7Z", "quantity": 3}]),
        "currencyCode": "BRL",
        "address": json.dumps({"streetAddress": "1600 Amphitheatre Parkway", "zipCode": "94043", "city": "Mountain View", "state": "CA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "BRL"


def test_h09_66vchsjnup_x4_cad_redmond_0226(api):
    params = {
        "itemList": json.dumps([{"productId": "66VCHSJNUP", "quantity": 4}]),
        "currencyCode": "CAD",
        "address": json.dumps({"streetAddress": "One Microsoft Way", "zipCode": "98052", "city": "Redmond", "state": "WA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "CAD"


def test_h09_1ymwwn1n4o_x5_chf_cupertino_0227(api):
    params = {
        "itemList": json.dumps([{"productId": "1YMWWN1N4O", "quantity": 5}]),
        "currencyCode": "CHF",
        "address": json.dumps({"streetAddress": "1 Infinite Loop", "zipCode": "95014", "city": "Cupertino", "state": "CA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "CHF"


def test_h09_l9ecav7kim_x10_cny_seattle_0228(api):
    params = {
        "itemList": json.dumps([{"productId": "L9ECAV7KIM", "quantity": 10}]),
        "currencyCode": "CNY",
        "address": json.dumps({"streetAddress": "410 Terry Ave N", "zipCode": "98109", "city": "Seattle", "state": "WA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "CNY"


def test_h09_2zyfj3gm2n_x1_czk_toronto_0229(api):
    params = {
        "itemList": json.dumps([{"productId": "2ZYFJ3GM2N", "quantity": 1}]),
        "currencyCode": "CZK",
        "address": json.dumps({"streetAddress": "100 Queen St W", "zipCode": "M5H 2N2", "city": "Toronto", "state": "ON", "country": "Canada"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "CZK"


def test_h09_0puk6v6ev0_x2_dkk_mountain_view_0230(api):
    params = {
        "itemList": json.dumps([{"productId": "0PUK6V6EV0", "quantity": 2}]),
        "currencyCode": "DKK",
        "address": json.dumps({"streetAddress": "1600 Amphitheatre Parkway", "zipCode": "94043", "city": "Mountain View", "state": "CA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "DKK"


def test_h09_ls4psxunum_x3_eur_redmond_0231(api):
    params = {
        "itemList": json.dumps([{"productId": "LS4PSXUNUM", "quantity": 3}]),
        "currencyCode": "EUR",
        "address": json.dumps({"streetAddress": "One Microsoft Way", "zipCode": "98052", "city": "Redmond", "state": "WA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "EUR"


def test_h09_9siqt8tojo_x4_gbp_cupertino_0232(api):
    params = {
        "itemList": json.dumps([{"productId": "9SIQT8TOJO", "quantity": 4}]),
        "currencyCode": "GBP",
        "address": json.dumps({"streetAddress": "1 Infinite Loop", "zipCode": "95014", "city": "Cupertino", "state": "CA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "GBP"


def test_h09_6e92zmyyfz_x5_hkd_seattle_0233(api):
    params = {
        "itemList": json.dumps([{"productId": "6E92ZMYYFZ", "quantity": 5}]),
        "currencyCode": "HKD",
        "address": json.dumps({"streetAddress": "410 Terry Ave N", "zipCode": "98109", "city": "Seattle", "state": "WA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "HKD"


def test_h09_hqtgwgpnh4_x10_hrk_toronto_0234(api):
    params = {
        "itemList": json.dumps([{"productId": "HQTGWGPNH4", "quantity": 10}]),
        "currencyCode": "HRK",
        "address": json.dumps({"streetAddress": "100 Queen St W", "zipCode": "M5H 2N2", "city": "Toronto", "state": "ON", "country": "Canada"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "HRK"


def test_h09_oljcespc7z_x1_huf_mountain_view_0235(api):
    params = {
        "itemList": json.dumps([{"productId": "OLJCESPC7Z", "quantity": 1}]),
        "currencyCode": "HUF",
        "address": json.dumps({"streetAddress": "1600 Amphitheatre Parkway", "zipCode": "94043", "city": "Mountain View", "state": "CA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "HUF"


def test_h09_66vchsjnup_x2_idr_redmond_0236(api):
    params = {
        "itemList": json.dumps([{"productId": "66VCHSJNUP", "quantity": 2}]),
        "currencyCode": "IDR",
        "address": json.dumps({"streetAddress": "One Microsoft Way", "zipCode": "98052", "city": "Redmond", "state": "WA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "IDR"


def test_h09_1ymwwn1n4o_x3_ils_cupertino_0237(api):
    params = {
        "itemList": json.dumps([{"productId": "1YMWWN1N4O", "quantity": 3}]),
        "currencyCode": "ILS",
        "address": json.dumps({"streetAddress": "1 Infinite Loop", "zipCode": "95014", "city": "Cupertino", "state": "CA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "ILS"


def test_h09_l9ecav7kim_x4_inr_seattle_0238(api):
    params = {
        "itemList": json.dumps([{"productId": "L9ECAV7KIM", "quantity": 4}]),
        "currencyCode": "INR",
        "address": json.dumps({"streetAddress": "410 Terry Ave N", "zipCode": "98109", "city": "Seattle", "state": "WA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "INR"


def test_h09_2zyfj3gm2n_x5_isk_toronto_0239(api):
    params = {
        "itemList": json.dumps([{"productId": "2ZYFJ3GM2N", "quantity": 5}]),
        "currencyCode": "ISK",
        "address": json.dumps({"streetAddress": "100 Queen St W", "zipCode": "M5H 2N2", "city": "Toronto", "state": "ON", "country": "Canada"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "ISK"


def test_h09_0puk6v6ev0_x10_jpy_mountain_view_0240(api):
    params = {
        "itemList": json.dumps([{"productId": "0PUK6V6EV0", "quantity": 10}]),
        "currencyCode": "JPY",
        "address": json.dumps({"streetAddress": "1600 Amphitheatre Parkway", "zipCode": "94043", "city": "Mountain View", "state": "CA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "JPY"


def test_h09_ls4psxunum_x1_krw_redmond_0241(api):
    params = {
        "itemList": json.dumps([{"productId": "LS4PSXUNUM", "quantity": 1}]),
        "currencyCode": "KRW",
        "address": json.dumps({"streetAddress": "One Microsoft Way", "zipCode": "98052", "city": "Redmond", "state": "WA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "KRW"


def test_h09_9siqt8tojo_x2_mxn_cupertino_0242(api):
    params = {
        "itemList": json.dumps([{"productId": "9SIQT8TOJO", "quantity": 2}]),
        "currencyCode": "MXN",
        "address": json.dumps({"streetAddress": "1 Infinite Loop", "zipCode": "95014", "city": "Cupertino", "state": "CA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "MXN"


def test_h09_6e92zmyyfz_x3_myr_seattle_0243(api):
    params = {
        "itemList": json.dumps([{"productId": "6E92ZMYYFZ", "quantity": 3}]),
        "currencyCode": "MYR",
        "address": json.dumps({"streetAddress": "410 Terry Ave N", "zipCode": "98109", "city": "Seattle", "state": "WA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "MYR"


def test_h09_hqtgwgpnh4_x4_nok_toronto_0244(api):
    params = {
        "itemList": json.dumps([{"productId": "HQTGWGPNH4", "quantity": 4}]),
        "currencyCode": "NOK",
        "address": json.dumps({"streetAddress": "100 Queen St W", "zipCode": "M5H 2N2", "city": "Toronto", "state": "ON", "country": "Canada"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "NOK"


def test_h09_oljcespc7z_x5_nzd_mountain_view_0245(api):
    params = {
        "itemList": json.dumps([{"productId": "OLJCESPC7Z", "quantity": 5}]),
        "currencyCode": "NZD",
        "address": json.dumps({"streetAddress": "1600 Amphitheatre Parkway", "zipCode": "94043", "city": "Mountain View", "state": "CA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "NZD"


def test_h09_66vchsjnup_x10_php_redmond_0246(api):
    params = {
        "itemList": json.dumps([{"productId": "66VCHSJNUP", "quantity": 10}]),
        "currencyCode": "PHP",
        "address": json.dumps({"streetAddress": "One Microsoft Way", "zipCode": "98052", "city": "Redmond", "state": "WA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "PHP"


def test_h09_1ymwwn1n4o_x1_pln_cupertino_0247(api):
    params = {
        "itemList": json.dumps([{"productId": "1YMWWN1N4O", "quantity": 1}]),
        "currencyCode": "PLN",
        "address": json.dumps({"streetAddress": "1 Infinite Loop", "zipCode": "95014", "city": "Cupertino", "state": "CA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "PLN"


def test_h09_l9ecav7kim_x2_ron_seattle_0248(api):
    params = {
        "itemList": json.dumps([{"productId": "L9ECAV7KIM", "quantity": 2}]),
        "currencyCode": "RON",
        "address": json.dumps({"streetAddress": "410 Terry Ave N", "zipCode": "98109", "city": "Seattle", "state": "WA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "RON"


def test_h09_2zyfj3gm2n_x3_rub_toronto_0249(api):
    params = {
        "itemList": json.dumps([{"productId": "2ZYFJ3GM2N", "quantity": 3}]),
        "currencyCode": "RUB",
        "address": json.dumps({"streetAddress": "100 Queen St W", "zipCode": "M5H 2N2", "city": "Toronto", "state": "ON", "country": "Canada"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "RUB"


def test_h09_0puk6v6ev0_x4_sek_mountain_view_0250(api):
    params = {
        "itemList": json.dumps([{"productId": "0PUK6V6EV0", "quantity": 4}]),
        "currencyCode": "SEK",
        "address": json.dumps({"streetAddress": "1600 Amphitheatre Parkway", "zipCode": "94043", "city": "Mountain View", "state": "CA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "SEK"


def test_h09_ls4psxunum_x5_sgd_redmond_0251(api):
    params = {
        "itemList": json.dumps([{"productId": "LS4PSXUNUM", "quantity": 5}]),
        "currencyCode": "SGD",
        "address": json.dumps({"streetAddress": "One Microsoft Way", "zipCode": "98052", "city": "Redmond", "state": "WA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "SGD"


def test_h09_9siqt8tojo_x10_thb_cupertino_0252(api):
    params = {
        "itemList": json.dumps([{"productId": "9SIQT8TOJO", "quantity": 10}]),
        "currencyCode": "THB",
        "address": json.dumps({"streetAddress": "1 Infinite Loop", "zipCode": "95014", "city": "Cupertino", "state": "CA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "THB"


def test_h09_6e92zmyyfz_x1_try_seattle_0253(api):
    params = {
        "itemList": json.dumps([{"productId": "6E92ZMYYFZ", "quantity": 1}]),
        "currencyCode": "TRY",
        "address": json.dumps({"streetAddress": "410 Terry Ave N", "zipCode": "98109", "city": "Seattle", "state": "WA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "TRY"


def test_h09_hqtgwgpnh4_x2_usd_toronto_0254(api):
    params = {
        "itemList": json.dumps([{"productId": "HQTGWGPNH4", "quantity": 2}]),
        "currencyCode": "USD",
        "address": json.dumps({"streetAddress": "100 Queen St W", "zipCode": "M5H 2N2", "city": "Toronto", "state": "ON", "country": "Canada"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "USD"
    total_nanos = int(cost["units"]) * 1_000_000_000 + int(cost["nanos"])
    assert abs(total_nanos - 17980000000) <= 1


def test_h09_oljcespc7z_x3_zar_mountain_view_0255(api):
    params = {
        "itemList": json.dumps([{"productId": "OLJCESPC7Z", "quantity": 3}]),
        "currencyCode": "ZAR",
        "address": json.dumps({"streetAddress": "1600 Amphitheatre Parkway", "zipCode": "94043", "city": "Mountain View", "state": "CA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "ZAR"


def test_h09_66vchsjnup_x4_aud_redmond_0256(api):
    params = {
        "itemList": json.dumps([{"productId": "66VCHSJNUP", "quantity": 4}]),
        "currencyCode": "AUD",
        "address": json.dumps({"streetAddress": "One Microsoft Way", "zipCode": "98052", "city": "Redmond", "state": "WA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "AUD"


def test_h09_1ymwwn1n4o_x5_bgn_cupertino_0257(api):
    params = {
        "itemList": json.dumps([{"productId": "1YMWWN1N4O", "quantity": 5}]),
        "currencyCode": "BGN",
        "address": json.dumps({"streetAddress": "1 Infinite Loop", "zipCode": "95014", "city": "Cupertino", "state": "CA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "BGN"


def test_h09_l9ecav7kim_x10_brl_seattle_0258(api):
    params = {
        "itemList": json.dumps([{"productId": "L9ECAV7KIM", "quantity": 10}]),
        "currencyCode": "BRL",
        "address": json.dumps({"streetAddress": "410 Terry Ave N", "zipCode": "98109", "city": "Seattle", "state": "WA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "BRL"


def test_h09_2zyfj3gm2n_x1_cad_toronto_0259(api):
    params = {
        "itemList": json.dumps([{"productId": "2ZYFJ3GM2N", "quantity": 1}]),
        "currencyCode": "CAD",
        "address": json.dumps({"streetAddress": "100 Queen St W", "zipCode": "M5H 2N2", "city": "Toronto", "state": "ON", "country": "Canada"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "CAD"


def test_h09_0puk6v6ev0_x2_chf_mountain_view_0260(api):
    params = {
        "itemList": json.dumps([{"productId": "0PUK6V6EV0", "quantity": 2}]),
        "currencyCode": "CHF",
        "address": json.dumps({"streetAddress": "1600 Amphitheatre Parkway", "zipCode": "94043", "city": "Mountain View", "state": "CA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "CHF"


def test_h09_ls4psxunum_x3_cny_redmond_0261(api):
    params = {
        "itemList": json.dumps([{"productId": "LS4PSXUNUM", "quantity": 3}]),
        "currencyCode": "CNY",
        "address": json.dumps({"streetAddress": "One Microsoft Way", "zipCode": "98052", "city": "Redmond", "state": "WA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "CNY"


def test_h09_9siqt8tojo_x4_czk_cupertino_0262(api):
    params = {
        "itemList": json.dumps([{"productId": "9SIQT8TOJO", "quantity": 4}]),
        "currencyCode": "CZK",
        "address": json.dumps({"streetAddress": "1 Infinite Loop", "zipCode": "95014", "city": "Cupertino", "state": "CA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "CZK"


def test_h09_6e92zmyyfz_x5_dkk_seattle_0263(api):
    params = {
        "itemList": json.dumps([{"productId": "6E92ZMYYFZ", "quantity": 5}]),
        "currencyCode": "DKK",
        "address": json.dumps({"streetAddress": "410 Terry Ave N", "zipCode": "98109", "city": "Seattle", "state": "WA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "DKK"


def test_h09_hqtgwgpnh4_x10_eur_toronto_0264(api):
    params = {
        "itemList": json.dumps([{"productId": "HQTGWGPNH4", "quantity": 10}]),
        "currencyCode": "EUR",
        "address": json.dumps({"streetAddress": "100 Queen St W", "zipCode": "M5H 2N2", "city": "Toronto", "state": "ON", "country": "Canada"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "EUR"


def test_h09_oljcespc7z_x1_gbp_mountain_view_0265(api):
    params = {
        "itemList": json.dumps([{"productId": "OLJCESPC7Z", "quantity": 1}]),
        "currencyCode": "GBP",
        "address": json.dumps({"streetAddress": "1600 Amphitheatre Parkway", "zipCode": "94043", "city": "Mountain View", "state": "CA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "GBP"


def test_h09_66vchsjnup_x2_hkd_redmond_0266(api):
    params = {
        "itemList": json.dumps([{"productId": "66VCHSJNUP", "quantity": 2}]),
        "currencyCode": "HKD",
        "address": json.dumps({"streetAddress": "One Microsoft Way", "zipCode": "98052", "city": "Redmond", "state": "WA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "HKD"


def test_h09_1ymwwn1n4o_x3_hrk_cupertino_0267(api):
    params = {
        "itemList": json.dumps([{"productId": "1YMWWN1N4O", "quantity": 3}]),
        "currencyCode": "HRK",
        "address": json.dumps({"streetAddress": "1 Infinite Loop", "zipCode": "95014", "city": "Cupertino", "state": "CA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "HRK"


def test_h09_l9ecav7kim_x4_huf_seattle_0268(api):
    params = {
        "itemList": json.dumps([{"productId": "L9ECAV7KIM", "quantity": 4}]),
        "currencyCode": "HUF",
        "address": json.dumps({"streetAddress": "410 Terry Ave N", "zipCode": "98109", "city": "Seattle", "state": "WA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "HUF"


def test_h09_2zyfj3gm2n_x5_idr_toronto_0269(api):
    params = {
        "itemList": json.dumps([{"productId": "2ZYFJ3GM2N", "quantity": 5}]),
        "currencyCode": "IDR",
        "address": json.dumps({"streetAddress": "100 Queen St W", "zipCode": "M5H 2N2", "city": "Toronto", "state": "ON", "country": "Canada"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "IDR"


def test_h09_0puk6v6ev0_x10_ils_mountain_view_0270(api):
    params = {
        "itemList": json.dumps([{"productId": "0PUK6V6EV0", "quantity": 10}]),
        "currencyCode": "ILS",
        "address": json.dumps({"streetAddress": "1600 Amphitheatre Parkway", "zipCode": "94043", "city": "Mountain View", "state": "CA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "ILS"


def test_h09_ls4psxunum_x1_inr_redmond_0271(api):
    params = {
        "itemList": json.dumps([{"productId": "LS4PSXUNUM", "quantity": 1}]),
        "currencyCode": "INR",
        "address": json.dumps({"streetAddress": "One Microsoft Way", "zipCode": "98052", "city": "Redmond", "state": "WA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "INR"


def test_h09_9siqt8tojo_x2_isk_cupertino_0272(api):
    params = {
        "itemList": json.dumps([{"productId": "9SIQT8TOJO", "quantity": 2}]),
        "currencyCode": "ISK",
        "address": json.dumps({"streetAddress": "1 Infinite Loop", "zipCode": "95014", "city": "Cupertino", "state": "CA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "ISK"


def test_h09_6e92zmyyfz_x3_jpy_seattle_0273(api):
    params = {
        "itemList": json.dumps([{"productId": "6E92ZMYYFZ", "quantity": 3}]),
        "currencyCode": "JPY",
        "address": json.dumps({"streetAddress": "410 Terry Ave N", "zipCode": "98109", "city": "Seattle", "state": "WA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "JPY"


def test_h09_hqtgwgpnh4_x4_krw_toronto_0274(api):
    params = {
        "itemList": json.dumps([{"productId": "HQTGWGPNH4", "quantity": 4}]),
        "currencyCode": "KRW",
        "address": json.dumps({"streetAddress": "100 Queen St W", "zipCode": "M5H 2N2", "city": "Toronto", "state": "ON", "country": "Canada"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "KRW"


def test_h09_oljcespc7z_x5_mxn_mountain_view_0275(api):
    params = {
        "itemList": json.dumps([{"productId": "OLJCESPC7Z", "quantity": 5}]),
        "currencyCode": "MXN",
        "address": json.dumps({"streetAddress": "1600 Amphitheatre Parkway", "zipCode": "94043", "city": "Mountain View", "state": "CA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "MXN"


def test_h09_66vchsjnup_x10_myr_redmond_0276(api):
    params = {
        "itemList": json.dumps([{"productId": "66VCHSJNUP", "quantity": 10}]),
        "currencyCode": "MYR",
        "address": json.dumps({"streetAddress": "One Microsoft Way", "zipCode": "98052", "city": "Redmond", "state": "WA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "MYR"


def test_h09_1ymwwn1n4o_x1_nok_cupertino_0277(api):
    params = {
        "itemList": json.dumps([{"productId": "1YMWWN1N4O", "quantity": 1}]),
        "currencyCode": "NOK",
        "address": json.dumps({"streetAddress": "1 Infinite Loop", "zipCode": "95014", "city": "Cupertino", "state": "CA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "NOK"


def test_h09_l9ecav7kim_x2_nzd_seattle_0278(api):
    params = {
        "itemList": json.dumps([{"productId": "L9ECAV7KIM", "quantity": 2}]),
        "currencyCode": "NZD",
        "address": json.dumps({"streetAddress": "410 Terry Ave N", "zipCode": "98109", "city": "Seattle", "state": "WA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "NZD"


def test_h09_2zyfj3gm2n_x3_php_toronto_0279(api):
    params = {
        "itemList": json.dumps([{"productId": "2ZYFJ3GM2N", "quantity": 3}]),
        "currencyCode": "PHP",
        "address": json.dumps({"streetAddress": "100 Queen St W", "zipCode": "M5H 2N2", "city": "Toronto", "state": "ON", "country": "Canada"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "PHP"


def test_h09_0puk6v6ev0_x4_pln_mountain_view_0280(api):
    params = {
        "itemList": json.dumps([{"productId": "0PUK6V6EV0", "quantity": 4}]),
        "currencyCode": "PLN",
        "address": json.dumps({"streetAddress": "1600 Amphitheatre Parkway", "zipCode": "94043", "city": "Mountain View", "state": "CA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "PLN"


def test_h09_ls4psxunum_x5_ron_redmond_0281(api):
    params = {
        "itemList": json.dumps([{"productId": "LS4PSXUNUM", "quantity": 5}]),
        "currencyCode": "RON",
        "address": json.dumps({"streetAddress": "One Microsoft Way", "zipCode": "98052", "city": "Redmond", "state": "WA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "RON"


def test_h09_9siqt8tojo_x10_rub_cupertino_0282(api):
    params = {
        "itemList": json.dumps([{"productId": "9SIQT8TOJO", "quantity": 10}]),
        "currencyCode": "RUB",
        "address": json.dumps({"streetAddress": "1 Infinite Loop", "zipCode": "95014", "city": "Cupertino", "state": "CA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "RUB"


def test_h09_6e92zmyyfz_x1_sek_seattle_0283(api):
    params = {
        "itemList": json.dumps([{"productId": "6E92ZMYYFZ", "quantity": 1}]),
        "currencyCode": "SEK",
        "address": json.dumps({"streetAddress": "410 Terry Ave N", "zipCode": "98109", "city": "Seattle", "state": "WA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "SEK"


def test_h09_hqtgwgpnh4_x2_sgd_toronto_0284(api):
    params = {
        "itemList": json.dumps([{"productId": "HQTGWGPNH4", "quantity": 2}]),
        "currencyCode": "SGD",
        "address": json.dumps({"streetAddress": "100 Queen St W", "zipCode": "M5H 2N2", "city": "Toronto", "state": "ON", "country": "Canada"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "SGD"


def test_h09_oljcespc7z_x3_thb_mountain_view_0285(api):
    params = {
        "itemList": json.dumps([{"productId": "OLJCESPC7Z", "quantity": 3}]),
        "currencyCode": "THB",
        "address": json.dumps({"streetAddress": "1600 Amphitheatre Parkway", "zipCode": "94043", "city": "Mountain View", "state": "CA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "THB"


def test_h09_66vchsjnup_x4_try_redmond_0286(api):
    params = {
        "itemList": json.dumps([{"productId": "66VCHSJNUP", "quantity": 4}]),
        "currencyCode": "TRY",
        "address": json.dumps({"streetAddress": "One Microsoft Way", "zipCode": "98052", "city": "Redmond", "state": "WA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "TRY"


def test_h09_1ymwwn1n4o_x5_usd_cupertino_0287(api):
    params = {
        "itemList": json.dumps([{"productId": "1YMWWN1N4O", "quantity": 5}]),
        "currencyCode": "USD",
        "address": json.dumps({"streetAddress": "1 Infinite Loop", "zipCode": "95014", "city": "Cupertino", "state": "CA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "USD"
    total_nanos = int(cost["units"]) * 1_000_000_000 + int(cost["nanos"])
    assert abs(total_nanos - 44950000000) <= 1


def test_h09_l9ecav7kim_x10_zar_seattle_0288(api):
    params = {
        "itemList": json.dumps([{"productId": "L9ECAV7KIM", "quantity": 10}]),
        "currencyCode": "ZAR",
        "address": json.dumps({"streetAddress": "410 Terry Ave N", "zipCode": "98109", "city": "Seattle", "state": "WA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "ZAR"


def test_h09_2zyfj3gm2n_x1_aud_toronto_0289(api):
    params = {
        "itemList": json.dumps([{"productId": "2ZYFJ3GM2N", "quantity": 1}]),
        "currencyCode": "AUD",
        "address": json.dumps({"streetAddress": "100 Queen St W", "zipCode": "M5H 2N2", "city": "Toronto", "state": "ON", "country": "Canada"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "AUD"


def test_h09_0puk6v6ev0_x2_bgn_mountain_view_0290(api):
    params = {
        "itemList": json.dumps([{"productId": "0PUK6V6EV0", "quantity": 2}]),
        "currencyCode": "BGN",
        "address": json.dumps({"streetAddress": "1600 Amphitheatre Parkway", "zipCode": "94043", "city": "Mountain View", "state": "CA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "BGN"


def test_h09_ls4psxunum_x3_brl_redmond_0291(api):
    params = {
        "itemList": json.dumps([{"productId": "LS4PSXUNUM", "quantity": 3}]),
        "currencyCode": "BRL",
        "address": json.dumps({"streetAddress": "One Microsoft Way", "zipCode": "98052", "city": "Redmond", "state": "WA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "BRL"


def test_h09_9siqt8tojo_x4_cad_cupertino_0292(api):
    params = {
        "itemList": json.dumps([{"productId": "9SIQT8TOJO", "quantity": 4}]),
        "currencyCode": "CAD",
        "address": json.dumps({"streetAddress": "1 Infinite Loop", "zipCode": "95014", "city": "Cupertino", "state": "CA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "CAD"


def test_h09_6e92zmyyfz_x5_chf_seattle_0293(api):
    params = {
        "itemList": json.dumps([{"productId": "6E92ZMYYFZ", "quantity": 5}]),
        "currencyCode": "CHF",
        "address": json.dumps({"streetAddress": "410 Terry Ave N", "zipCode": "98109", "city": "Seattle", "state": "WA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "CHF"


def test_h09_hqtgwgpnh4_x10_cny_toronto_0294(api):
    params = {
        "itemList": json.dumps([{"productId": "HQTGWGPNH4", "quantity": 10}]),
        "currencyCode": "CNY",
        "address": json.dumps({"streetAddress": "100 Queen St W", "zipCode": "M5H 2N2", "city": "Toronto", "state": "ON", "country": "Canada"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "CNY"


def test_h09_oljcespc7z_x1_czk_mountain_view_0295(api):
    params = {
        "itemList": json.dumps([{"productId": "OLJCESPC7Z", "quantity": 1}]),
        "currencyCode": "CZK",
        "address": json.dumps({"streetAddress": "1600 Amphitheatre Parkway", "zipCode": "94043", "city": "Mountain View", "state": "CA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "CZK"


def test_h09_66vchsjnup_x2_dkk_redmond_0296(api):
    params = {
        "itemList": json.dumps([{"productId": "66VCHSJNUP", "quantity": 2}]),
        "currencyCode": "DKK",
        "address": json.dumps({"streetAddress": "One Microsoft Way", "zipCode": "98052", "city": "Redmond", "state": "WA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "DKK"


def test_h09_1ymwwn1n4o_x3_eur_cupertino_0297(api):
    params = {
        "itemList": json.dumps([{"productId": "1YMWWN1N4O", "quantity": 3}]),
        "currencyCode": "EUR",
        "address": json.dumps({"streetAddress": "1 Infinite Loop", "zipCode": "95014", "city": "Cupertino", "state": "CA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "EUR"


def test_h09_l9ecav7kim_x4_gbp_seattle_0298(api):
    params = {
        "itemList": json.dumps([{"productId": "L9ECAV7KIM", "quantity": 4}]),
        "currencyCode": "GBP",
        "address": json.dumps({"streetAddress": "410 Terry Ave N", "zipCode": "98109", "city": "Seattle", "state": "WA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "GBP"


def test_h09_2zyfj3gm2n_x5_hkd_toronto_0299(api):
    params = {
        "itemList": json.dumps([{"productId": "2ZYFJ3GM2N", "quantity": 5}]),
        "currencyCode": "HKD",
        "address": json.dumps({"streetAddress": "100 Queen St W", "zipCode": "M5H 2N2", "city": "Toronto", "state": "ON", "country": "Canada"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "HKD"


def test_h09_0puk6v6ev0_x10_hrk_mountain_view_0300(api):
    params = {
        "itemList": json.dumps([{"productId": "0PUK6V6EV0", "quantity": 10}]),
        "currencyCode": "HRK",
        "address": json.dumps({"streetAddress": "1600 Amphitheatre Parkway", "zipCode": "94043", "city": "Mountain View", "state": "CA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "HRK"


def test_h09_ls4psxunum_x1_huf_redmond_0301(api):
    params = {
        "itemList": json.dumps([{"productId": "LS4PSXUNUM", "quantity": 1}]),
        "currencyCode": "HUF",
        "address": json.dumps({"streetAddress": "One Microsoft Way", "zipCode": "98052", "city": "Redmond", "state": "WA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "HUF"


def test_h09_9siqt8tojo_x2_idr_cupertino_0302(api):
    params = {
        "itemList": json.dumps([{"productId": "9SIQT8TOJO", "quantity": 2}]),
        "currencyCode": "IDR",
        "address": json.dumps({"streetAddress": "1 Infinite Loop", "zipCode": "95014", "city": "Cupertino", "state": "CA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "IDR"


def test_h09_6e92zmyyfz_x3_ils_seattle_0303(api):
    params = {
        "itemList": json.dumps([{"productId": "6E92ZMYYFZ", "quantity": 3}]),
        "currencyCode": "ILS",
        "address": json.dumps({"streetAddress": "410 Terry Ave N", "zipCode": "98109", "city": "Seattle", "state": "WA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "ILS"


def test_h09_hqtgwgpnh4_x4_inr_toronto_0304(api):
    params = {
        "itemList": json.dumps([{"productId": "HQTGWGPNH4", "quantity": 4}]),
        "currencyCode": "INR",
        "address": json.dumps({"streetAddress": "100 Queen St W", "zipCode": "M5H 2N2", "city": "Toronto", "state": "ON", "country": "Canada"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "INR"


def test_h09_oljcespc7z_x5_isk_mountain_view_0305(api):
    params = {
        "itemList": json.dumps([{"productId": "OLJCESPC7Z", "quantity": 5}]),
        "currencyCode": "ISK",
        "address": json.dumps({"streetAddress": "1600 Amphitheatre Parkway", "zipCode": "94043", "city": "Mountain View", "state": "CA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "ISK"


def test_h09_66vchsjnup_x10_jpy_redmond_0306(api):
    params = {
        "itemList": json.dumps([{"productId": "66VCHSJNUP", "quantity": 10}]),
        "currencyCode": "JPY",
        "address": json.dumps({"streetAddress": "One Microsoft Way", "zipCode": "98052", "city": "Redmond", "state": "WA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "JPY"


def test_h09_1ymwwn1n4o_x1_krw_cupertino_0307(api):
    params = {
        "itemList": json.dumps([{"productId": "1YMWWN1N4O", "quantity": 1}]),
        "currencyCode": "KRW",
        "address": json.dumps({"streetAddress": "1 Infinite Loop", "zipCode": "95014", "city": "Cupertino", "state": "CA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "KRW"


def test_h09_l9ecav7kim_x2_mxn_seattle_0308(api):
    params = {
        "itemList": json.dumps([{"productId": "L9ECAV7KIM", "quantity": 2}]),
        "currencyCode": "MXN",
        "address": json.dumps({"streetAddress": "410 Terry Ave N", "zipCode": "98109", "city": "Seattle", "state": "WA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "MXN"


def test_h09_2zyfj3gm2n_x3_myr_toronto_0309(api):
    params = {
        "itemList": json.dumps([{"productId": "2ZYFJ3GM2N", "quantity": 3}]),
        "currencyCode": "MYR",
        "address": json.dumps({"streetAddress": "100 Queen St W", "zipCode": "M5H 2N2", "city": "Toronto", "state": "ON", "country": "Canada"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "MYR"


def test_h09_0puk6v6ev0_x4_nok_mountain_view_0310(api):
    params = {
        "itemList": json.dumps([{"productId": "0PUK6V6EV0", "quantity": 4}]),
        "currencyCode": "NOK",
        "address": json.dumps({"streetAddress": "1600 Amphitheatre Parkway", "zipCode": "94043", "city": "Mountain View", "state": "CA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "NOK"


def test_h09_ls4psxunum_x5_nzd_redmond_0311(api):
    params = {
        "itemList": json.dumps([{"productId": "LS4PSXUNUM", "quantity": 5}]),
        "currencyCode": "NZD",
        "address": json.dumps({"streetAddress": "One Microsoft Way", "zipCode": "98052", "city": "Redmond", "state": "WA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "NZD"


def test_h09_9siqt8tojo_x10_php_cupertino_0312(api):
    params = {
        "itemList": json.dumps([{"productId": "9SIQT8TOJO", "quantity": 10}]),
        "currencyCode": "PHP",
        "address": json.dumps({"streetAddress": "1 Infinite Loop", "zipCode": "95014", "city": "Cupertino", "state": "CA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "PHP"


def test_h09_6e92zmyyfz_x1_pln_seattle_0313(api):
    params = {
        "itemList": json.dumps([{"productId": "6E92ZMYYFZ", "quantity": 1}]),
        "currencyCode": "PLN",
        "address": json.dumps({"streetAddress": "410 Terry Ave N", "zipCode": "98109", "city": "Seattle", "state": "WA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "PLN"


def test_h09_hqtgwgpnh4_x2_ron_toronto_0314(api):
    params = {
        "itemList": json.dumps([{"productId": "HQTGWGPNH4", "quantity": 2}]),
        "currencyCode": "RON",
        "address": json.dumps({"streetAddress": "100 Queen St W", "zipCode": "M5H 2N2", "city": "Toronto", "state": "ON", "country": "Canada"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "RON"


def test_h09_oljcespc7z_x3_rub_mountain_view_0315(api):
    params = {
        "itemList": json.dumps([{"productId": "OLJCESPC7Z", "quantity": 3}]),
        "currencyCode": "RUB",
        "address": json.dumps({"streetAddress": "1600 Amphitheatre Parkway", "zipCode": "94043", "city": "Mountain View", "state": "CA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "RUB"


def test_h09_66vchsjnup_x4_sek_redmond_0316(api):
    params = {
        "itemList": json.dumps([{"productId": "66VCHSJNUP", "quantity": 4}]),
        "currencyCode": "SEK",
        "address": json.dumps({"streetAddress": "One Microsoft Way", "zipCode": "98052", "city": "Redmond", "state": "WA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "SEK"


def test_h09_1ymwwn1n4o_x5_sgd_cupertino_0317(api):
    params = {
        "itemList": json.dumps([{"productId": "1YMWWN1N4O", "quantity": 5}]),
        "currencyCode": "SGD",
        "address": json.dumps({"streetAddress": "1 Infinite Loop", "zipCode": "95014", "city": "Cupertino", "state": "CA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "SGD"


def test_h09_l9ecav7kim_x10_thb_seattle_0318(api):
    params = {
        "itemList": json.dumps([{"productId": "L9ECAV7KIM", "quantity": 10}]),
        "currencyCode": "THB",
        "address": json.dumps({"streetAddress": "410 Terry Ave N", "zipCode": "98109", "city": "Seattle", "state": "WA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "THB"


def test_h09_2zyfj3gm2n_x1_try_toronto_0319(api):
    params = {
        "itemList": json.dumps([{"productId": "2ZYFJ3GM2N", "quantity": 1}]),
        "currencyCode": "TRY",
        "address": json.dumps({"streetAddress": "100 Queen St W", "zipCode": "M5H 2N2", "city": "Toronto", "state": "ON", "country": "Canada"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "TRY"


def test_h09_0puk6v6ev0_x2_usd_mountain_view_0320(api):
    params = {
        "itemList": json.dumps([{"productId": "0PUK6V6EV0", "quantity": 2}]),
        "currencyCode": "USD",
        "address": json.dumps({"streetAddress": "1600 Amphitheatre Parkway", "zipCode": "94043", "city": "Mountain View", "state": "CA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "USD"
    total_nanos = int(cost["units"]) * 1_000_000_000 + int(cost["nanos"])
    assert abs(total_nanos - 17980000000) <= 1


def test_h09_ls4psxunum_x3_zar_redmond_0321(api):
    params = {
        "itemList": json.dumps([{"productId": "LS4PSXUNUM", "quantity": 3}]),
        "currencyCode": "ZAR",
        "address": json.dumps({"streetAddress": "One Microsoft Way", "zipCode": "98052", "city": "Redmond", "state": "WA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "ZAR"


def test_h09_9siqt8tojo_x4_aud_cupertino_0322(api):
    params = {
        "itemList": json.dumps([{"productId": "9SIQT8TOJO", "quantity": 4}]),
        "currencyCode": "AUD",
        "address": json.dumps({"streetAddress": "1 Infinite Loop", "zipCode": "95014", "city": "Cupertino", "state": "CA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "AUD"


def test_h09_6e92zmyyfz_x5_bgn_seattle_0323(api):
    params = {
        "itemList": json.dumps([{"productId": "6E92ZMYYFZ", "quantity": 5}]),
        "currencyCode": "BGN",
        "address": json.dumps({"streetAddress": "410 Terry Ave N", "zipCode": "98109", "city": "Seattle", "state": "WA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "BGN"


def test_h09_hqtgwgpnh4_x10_brl_toronto_0324(api):
    params = {
        "itemList": json.dumps([{"productId": "HQTGWGPNH4", "quantity": 10}]),
        "currencyCode": "BRL",
        "address": json.dumps({"streetAddress": "100 Queen St W", "zipCode": "M5H 2N2", "city": "Toronto", "state": "ON", "country": "Canada"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "BRL"


def test_h09_oljcespc7z_x1_cad_mountain_view_0325(api):
    params = {
        "itemList": json.dumps([{"productId": "OLJCESPC7Z", "quantity": 1}]),
        "currencyCode": "CAD",
        "address": json.dumps({"streetAddress": "1600 Amphitheatre Parkway", "zipCode": "94043", "city": "Mountain View", "state": "CA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "CAD"


def test_h09_66vchsjnup_x2_chf_redmond_0326(api):
    params = {
        "itemList": json.dumps([{"productId": "66VCHSJNUP", "quantity": 2}]),
        "currencyCode": "CHF",
        "address": json.dumps({"streetAddress": "One Microsoft Way", "zipCode": "98052", "city": "Redmond", "state": "WA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "CHF"


def test_h09_1ymwwn1n4o_x3_cny_cupertino_0327(api):
    params = {
        "itemList": json.dumps([{"productId": "1YMWWN1N4O", "quantity": 3}]),
        "currencyCode": "CNY",
        "address": json.dumps({"streetAddress": "1 Infinite Loop", "zipCode": "95014", "city": "Cupertino", "state": "CA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "CNY"


def test_h09_l9ecav7kim_x4_czk_seattle_0328(api):
    params = {
        "itemList": json.dumps([{"productId": "L9ECAV7KIM", "quantity": 4}]),
        "currencyCode": "CZK",
        "address": json.dumps({"streetAddress": "410 Terry Ave N", "zipCode": "98109", "city": "Seattle", "state": "WA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "CZK"


def test_h09_2zyfj3gm2n_x5_dkk_toronto_0329(api):
    params = {
        "itemList": json.dumps([{"productId": "2ZYFJ3GM2N", "quantity": 5}]),
        "currencyCode": "DKK",
        "address": json.dumps({"streetAddress": "100 Queen St W", "zipCode": "M5H 2N2", "city": "Toronto", "state": "ON", "country": "Canada"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "DKK"


def test_h09_0puk6v6ev0_x10_eur_mountain_view_0330(api):
    params = {
        "itemList": json.dumps([{"productId": "0PUK6V6EV0", "quantity": 10}]),
        "currencyCode": "EUR",
        "address": json.dumps({"streetAddress": "1600 Amphitheatre Parkway", "zipCode": "94043", "city": "Mountain View", "state": "CA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "EUR"


def test_h09_ls4psxunum_x1_gbp_redmond_0331(api):
    params = {
        "itemList": json.dumps([{"productId": "LS4PSXUNUM", "quantity": 1}]),
        "currencyCode": "GBP",
        "address": json.dumps({"streetAddress": "One Microsoft Way", "zipCode": "98052", "city": "Redmond", "state": "WA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "GBP"


def test_h09_9siqt8tojo_x2_hkd_cupertino_0332(api):
    params = {
        "itemList": json.dumps([{"productId": "9SIQT8TOJO", "quantity": 2}]),
        "currencyCode": "HKD",
        "address": json.dumps({"streetAddress": "1 Infinite Loop", "zipCode": "95014", "city": "Cupertino", "state": "CA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "HKD"


def test_h09_6e92zmyyfz_x3_hrk_seattle_0333(api):
    params = {
        "itemList": json.dumps([{"productId": "6E92ZMYYFZ", "quantity": 3}]),
        "currencyCode": "HRK",
        "address": json.dumps({"streetAddress": "410 Terry Ave N", "zipCode": "98109", "city": "Seattle", "state": "WA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "HRK"


def test_h09_hqtgwgpnh4_x4_huf_toronto_0334(api):
    params = {
        "itemList": json.dumps([{"productId": "HQTGWGPNH4", "quantity": 4}]),
        "currencyCode": "HUF",
        "address": json.dumps({"streetAddress": "100 Queen St W", "zipCode": "M5H 2N2", "city": "Toronto", "state": "ON", "country": "Canada"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "HUF"


def test_h09_oljcespc7z_x5_idr_mountain_view_0335(api):
    params = {
        "itemList": json.dumps([{"productId": "OLJCESPC7Z", "quantity": 5}]),
        "currencyCode": "IDR",
        "address": json.dumps({"streetAddress": "1600 Amphitheatre Parkway", "zipCode": "94043", "city": "Mountain View", "state": "CA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "IDR"


def test_h09_66vchsjnup_x10_ils_redmond_0336(api):
    params = {
        "itemList": json.dumps([{"productId": "66VCHSJNUP", "quantity": 10}]),
        "currencyCode": "ILS",
        "address": json.dumps({"streetAddress": "One Microsoft Way", "zipCode": "98052", "city": "Redmond", "state": "WA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "ILS"


def test_h09_1ymwwn1n4o_x1_inr_cupertino_0337(api):
    params = {
        "itemList": json.dumps([{"productId": "1YMWWN1N4O", "quantity": 1}]),
        "currencyCode": "INR",
        "address": json.dumps({"streetAddress": "1 Infinite Loop", "zipCode": "95014", "city": "Cupertino", "state": "CA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "INR"


def test_h09_l9ecav7kim_x2_isk_seattle_0338(api):
    params = {
        "itemList": json.dumps([{"productId": "L9ECAV7KIM", "quantity": 2}]),
        "currencyCode": "ISK",
        "address": json.dumps({"streetAddress": "410 Terry Ave N", "zipCode": "98109", "city": "Seattle", "state": "WA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "ISK"


def test_h09_2zyfj3gm2n_x3_jpy_toronto_0339(api):
    params = {
        "itemList": json.dumps([{"productId": "2ZYFJ3GM2N", "quantity": 3}]),
        "currencyCode": "JPY",
        "address": json.dumps({"streetAddress": "100 Queen St W", "zipCode": "M5H 2N2", "city": "Toronto", "state": "ON", "country": "Canada"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "JPY"


def test_h09_0puk6v6ev0_x4_krw_mountain_view_0340(api):
    params = {
        "itemList": json.dumps([{"productId": "0PUK6V6EV0", "quantity": 4}]),
        "currencyCode": "KRW",
        "address": json.dumps({"streetAddress": "1600 Amphitheatre Parkway", "zipCode": "94043", "city": "Mountain View", "state": "CA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "KRW"


def test_h09_ls4psxunum_x5_mxn_redmond_0341(api):
    params = {
        "itemList": json.dumps([{"productId": "LS4PSXUNUM", "quantity": 5}]),
        "currencyCode": "MXN",
        "address": json.dumps({"streetAddress": "One Microsoft Way", "zipCode": "98052", "city": "Redmond", "state": "WA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "MXN"


def test_h09_9siqt8tojo_x10_myr_cupertino_0342(api):
    params = {
        "itemList": json.dumps([{"productId": "9SIQT8TOJO", "quantity": 10}]),
        "currencyCode": "MYR",
        "address": json.dumps({"streetAddress": "1 Infinite Loop", "zipCode": "95014", "city": "Cupertino", "state": "CA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "MYR"


def test_h09_6e92zmyyfz_x1_nok_seattle_0343(api):
    params = {
        "itemList": json.dumps([{"productId": "6E92ZMYYFZ", "quantity": 1}]),
        "currencyCode": "NOK",
        "address": json.dumps({"streetAddress": "410 Terry Ave N", "zipCode": "98109", "city": "Seattle", "state": "WA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "NOK"


def test_h09_hqtgwgpnh4_x2_nzd_toronto_0344(api):
    params = {
        "itemList": json.dumps([{"productId": "HQTGWGPNH4", "quantity": 2}]),
        "currencyCode": "NZD",
        "address": json.dumps({"streetAddress": "100 Queen St W", "zipCode": "M5H 2N2", "city": "Toronto", "state": "ON", "country": "Canada"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "NZD"


def test_h09_oljcespc7z_x3_php_mountain_view_0345(api):
    params = {
        "itemList": json.dumps([{"productId": "OLJCESPC7Z", "quantity": 3}]),
        "currencyCode": "PHP",
        "address": json.dumps({"streetAddress": "1600 Amphitheatre Parkway", "zipCode": "94043", "city": "Mountain View", "state": "CA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "PHP"


def test_h09_66vchsjnup_x4_pln_redmond_0346(api):
    params = {
        "itemList": json.dumps([{"productId": "66VCHSJNUP", "quantity": 4}]),
        "currencyCode": "PLN",
        "address": json.dumps({"streetAddress": "One Microsoft Way", "zipCode": "98052", "city": "Redmond", "state": "WA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "PLN"


def test_h09_1ymwwn1n4o_x5_ron_cupertino_0347(api):
    params = {
        "itemList": json.dumps([{"productId": "1YMWWN1N4O", "quantity": 5}]),
        "currencyCode": "RON",
        "address": json.dumps({"streetAddress": "1 Infinite Loop", "zipCode": "95014", "city": "Cupertino", "state": "CA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "RON"


def test_h09_l9ecav7kim_x10_rub_seattle_0348(api):
    params = {
        "itemList": json.dumps([{"productId": "L9ECAV7KIM", "quantity": 10}]),
        "currencyCode": "RUB",
        "address": json.dumps({"streetAddress": "410 Terry Ave N", "zipCode": "98109", "city": "Seattle", "state": "WA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "RUB"


def test_h09_2zyfj3gm2n_x1_sek_toronto_0349(api):
    params = {
        "itemList": json.dumps([{"productId": "2ZYFJ3GM2N", "quantity": 1}]),
        "currencyCode": "SEK",
        "address": json.dumps({"streetAddress": "100 Queen St W", "zipCode": "M5H 2N2", "city": "Toronto", "state": "ON", "country": "Canada"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "SEK"


def test_h09_0puk6v6ev0_x2_sgd_mountain_view_0350(api):
    params = {
        "itemList": json.dumps([{"productId": "0PUK6V6EV0", "quantity": 2}]),
        "currencyCode": "SGD",
        "address": json.dumps({"streetAddress": "1600 Amphitheatre Parkway", "zipCode": "94043", "city": "Mountain View", "state": "CA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "SGD"


def test_h09_ls4psxunum_x3_thb_redmond_0351(api):
    params = {
        "itemList": json.dumps([{"productId": "LS4PSXUNUM", "quantity": 3}]),
        "currencyCode": "THB",
        "address": json.dumps({"streetAddress": "One Microsoft Way", "zipCode": "98052", "city": "Redmond", "state": "WA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "THB"


def test_h09_9siqt8tojo_x4_try_cupertino_0352(api):
    params = {
        "itemList": json.dumps([{"productId": "9SIQT8TOJO", "quantity": 4}]),
        "currencyCode": "TRY",
        "address": json.dumps({"streetAddress": "1 Infinite Loop", "zipCode": "95014", "city": "Cupertino", "state": "CA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "TRY"


def test_h09_6e92zmyyfz_x5_usd_seattle_0353(api):
    params = {
        "itemList": json.dumps([{"productId": "6E92ZMYYFZ", "quantity": 5}]),
        "currencyCode": "USD",
        "address": json.dumps({"streetAddress": "410 Terry Ave N", "zipCode": "98109", "city": "Seattle", "state": "WA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "USD"
    total_nanos = int(cost["units"]) * 1_000_000_000 + int(cost["nanos"])
    assert abs(total_nanos - 44950000000) <= 1


def test_h09_hqtgwgpnh4_x10_zar_toronto_0354(api):
    params = {
        "itemList": json.dumps([{"productId": "HQTGWGPNH4", "quantity": 10}]),
        "currencyCode": "ZAR",
        "address": json.dumps({"streetAddress": "100 Queen St W", "zipCode": "M5H 2N2", "city": "Toronto", "state": "ON", "country": "Canada"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "ZAR"


def test_h09_oljcespc7z_x1_aud_mountain_view_0355(api):
    params = {
        "itemList": json.dumps([{"productId": "OLJCESPC7Z", "quantity": 1}]),
        "currencyCode": "AUD",
        "address": json.dumps({"streetAddress": "1600 Amphitheatre Parkway", "zipCode": "94043", "city": "Mountain View", "state": "CA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "AUD"


def test_h09_66vchsjnup_x2_bgn_redmond_0356(api):
    params = {
        "itemList": json.dumps([{"productId": "66VCHSJNUP", "quantity": 2}]),
        "currencyCode": "BGN",
        "address": json.dumps({"streetAddress": "One Microsoft Way", "zipCode": "98052", "city": "Redmond", "state": "WA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "BGN"


def test_h09_1ymwwn1n4o_x3_brl_cupertino_0357(api):
    params = {
        "itemList": json.dumps([{"productId": "1YMWWN1N4O", "quantity": 3}]),
        "currencyCode": "BRL",
        "address": json.dumps({"streetAddress": "1 Infinite Loop", "zipCode": "95014", "city": "Cupertino", "state": "CA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "BRL"


def test_h09_l9ecav7kim_x4_cad_seattle_0358(api):
    params = {
        "itemList": json.dumps([{"productId": "L9ECAV7KIM", "quantity": 4}]),
        "currencyCode": "CAD",
        "address": json.dumps({"streetAddress": "410 Terry Ave N", "zipCode": "98109", "city": "Seattle", "state": "WA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "CAD"


def test_h09_2zyfj3gm2n_x5_chf_toronto_0359(api):
    params = {
        "itemList": json.dumps([{"productId": "2ZYFJ3GM2N", "quantity": 5}]),
        "currencyCode": "CHF",
        "address": json.dumps({"streetAddress": "100 Queen St W", "zipCode": "M5H 2N2", "city": "Toronto", "state": "ON", "country": "Canada"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "CHF"


def test_h09_0puk6v6ev0_x10_cny_mountain_view_0360(api):
    params = {
        "itemList": json.dumps([{"productId": "0PUK6V6EV0", "quantity": 10}]),
        "currencyCode": "CNY",
        "address": json.dumps({"streetAddress": "1600 Amphitheatre Parkway", "zipCode": "94043", "city": "Mountain View", "state": "CA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "CNY"
