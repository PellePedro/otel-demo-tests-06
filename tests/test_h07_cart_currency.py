import json  # noqa: F401


def test_h07_hqtgwgpnh4_bgn_0001(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "HQTGWGPNH4", "quantity": 1}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id, "currencyCode": "BGN"})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert len(items) == 1
    assert items[0]["product"]["priceUsd"]["currencyCode"] == "BGN"


def test_h07_oljcespc7z_brl_0002(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "OLJCESPC7Z", "quantity": 1}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id, "currencyCode": "BRL"})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert len(items) == 1
    assert items[0]["product"]["priceUsd"]["currencyCode"] == "BRL"


def test_h07_66vchsjnup_cad_0003(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "66VCHSJNUP", "quantity": 1}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id, "currencyCode": "CAD"})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert len(items) == 1
    assert items[0]["product"]["priceUsd"]["currencyCode"] == "CAD"


def test_h07_1ymwwn1n4o_chf_0004(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "1YMWWN1N4O", "quantity": 1}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id, "currencyCode": "CHF"})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert len(items) == 1
    assert items[0]["product"]["priceUsd"]["currencyCode"] == "CHF"


def test_h07_l9ecav7kim_cny_0005(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "L9ECAV7KIM", "quantity": 1}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id, "currencyCode": "CNY"})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert len(items) == 1
    assert items[0]["product"]["priceUsd"]["currencyCode"] == "CNY"


def test_h07_2zyfj3gm2n_czk_0006(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "2ZYFJ3GM2N", "quantity": 1}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id, "currencyCode": "CZK"})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert len(items) == 1
    assert items[0]["product"]["priceUsd"]["currencyCode"] == "CZK"


def test_h07_0puk6v6ev0_dkk_0007(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "0PUK6V6EV0", "quantity": 1}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id, "currencyCode": "DKK"})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert len(items) == 1
    assert items[0]["product"]["priceUsd"]["currencyCode"] == "DKK"


def test_h07_ls4psxunum_eur_0008(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "LS4PSXUNUM", "quantity": 1}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id, "currencyCode": "EUR"})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert len(items) == 1
    assert items[0]["product"]["priceUsd"]["currencyCode"] == "EUR"


def test_h07_9siqt8tojo_gbp_0009(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "9SIQT8TOJO", "quantity": 1}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id, "currencyCode": "GBP"})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert len(items) == 1
    assert items[0]["product"]["priceUsd"]["currencyCode"] == "GBP"


def test_h07_6e92zmyyfz_hkd_0010(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "6E92ZMYYFZ", "quantity": 1}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id, "currencyCode": "HKD"})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert len(items) == 1
    assert items[0]["product"]["priceUsd"]["currencyCode"] == "HKD"


def test_h07_hqtgwgpnh4_hrk_0011(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "HQTGWGPNH4", "quantity": 1}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id, "currencyCode": "HRK"})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert len(items) == 1
    assert items[0]["product"]["priceUsd"]["currencyCode"] == "HRK"


def test_h07_oljcespc7z_huf_0012(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "OLJCESPC7Z", "quantity": 1}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id, "currencyCode": "HUF"})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert len(items) == 1
    assert items[0]["product"]["priceUsd"]["currencyCode"] == "HUF"


def test_h07_66vchsjnup_idr_0013(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "66VCHSJNUP", "quantity": 1}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id, "currencyCode": "IDR"})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert len(items) == 1
    assert items[0]["product"]["priceUsd"]["currencyCode"] == "IDR"


def test_h07_1ymwwn1n4o_ils_0014(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "1YMWWN1N4O", "quantity": 1}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id, "currencyCode": "ILS"})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert len(items) == 1
    assert items[0]["product"]["priceUsd"]["currencyCode"] == "ILS"


def test_h07_l9ecav7kim_inr_0015(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "L9ECAV7KIM", "quantity": 1}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id, "currencyCode": "INR"})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert len(items) == 1
    assert items[0]["product"]["priceUsd"]["currencyCode"] == "INR"


def test_h07_2zyfj3gm2n_isk_0016(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "2ZYFJ3GM2N", "quantity": 1}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id, "currencyCode": "ISK"})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert len(items) == 1
    assert items[0]["product"]["priceUsd"]["currencyCode"] == "ISK"


def test_h07_0puk6v6ev0_jpy_0017(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "0PUK6V6EV0", "quantity": 1}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id, "currencyCode": "JPY"})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert len(items) == 1
    assert items[0]["product"]["priceUsd"]["currencyCode"] == "JPY"


def test_h07_ls4psxunum_krw_0018(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "LS4PSXUNUM", "quantity": 1}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id, "currencyCode": "KRW"})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert len(items) == 1
    assert items[0]["product"]["priceUsd"]["currencyCode"] == "KRW"


def test_h07_9siqt8tojo_mxn_0019(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "9SIQT8TOJO", "quantity": 1}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id, "currencyCode": "MXN"})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert len(items) == 1
    assert items[0]["product"]["priceUsd"]["currencyCode"] == "MXN"


def test_h07_6e92zmyyfz_myr_0020(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "6E92ZMYYFZ", "quantity": 1}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id, "currencyCode": "MYR"})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert len(items) == 1
    assert items[0]["product"]["priceUsd"]["currencyCode"] == "MYR"
