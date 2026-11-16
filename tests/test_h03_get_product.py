import json  # noqa: F401


def test_h03_hqtgwgpnh4_mxn_0001(api):
    resp = api.get("/api/products/HQTGWGPNH4", params={"currencyCode": "MXN"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "HQTGWGPNH4"
    assert product["name"] == 'The Comet Book'
    assert product["priceUsd"]["currencyCode"] == "MXN"


def test_h03_oljcespc7z_myr_0002(api):
    resp = api.get("/api/products/OLJCESPC7Z", params={"currencyCode": "MYR"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "OLJCESPC7Z"
    assert product["name"] == 'National Park Foundation Explorascope'
    assert product["priceUsd"]["currencyCode"] == "MYR"


def test_h03_66vchsjnup_nok_0003(api):
    resp = api.get("/api/products/66VCHSJNUP", params={"currencyCode": "NOK"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "66VCHSJNUP"
    assert product["name"] == 'Starsense Explorer Refractor Telescope'
    assert product["priceUsd"]["currencyCode"] == "NOK"


def test_h03_1ymwwn1n4o_nzd_0004(api):
    resp = api.get("/api/products/1YMWWN1N4O", params={"currencyCode": "NZD"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "1YMWWN1N4O"
    assert product["name"] == 'Eclipsmart Travel Refractor Telescope'
    assert product["priceUsd"]["currencyCode"] == "NZD"


def test_h03_l9ecav7kim_php_0005(api):
    resp = api.get("/api/products/L9ECAV7KIM", params={"currencyCode": "PHP"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "L9ECAV7KIM"
    assert product["name"] == 'Lens Cleaning Kit'
    assert product["priceUsd"]["currencyCode"] == "PHP"


def test_h03_2zyfj3gm2n_pln_0006(api):
    resp = api.get("/api/products/2ZYFJ3GM2N", params={"currencyCode": "PLN"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "2ZYFJ3GM2N"
    assert product["name"] == 'Roof Binoculars'
    assert product["priceUsd"]["currencyCode"] == "PLN"


def test_h03_0puk6v6ev0_ron_0007(api):
    resp = api.get("/api/products/0PUK6V6EV0", params={"currencyCode": "RON"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "0PUK6V6EV0"
    assert product["name"] == 'Solar System Color Imager'
    assert product["priceUsd"]["currencyCode"] == "RON"


def test_h03_ls4psxunum_rub_0008(api):
    resp = api.get("/api/products/LS4PSXUNUM", params={"currencyCode": "RUB"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "LS4PSXUNUM"
    assert product["name"] == 'Red Flashlight'
    assert product["priceUsd"]["currencyCode"] == "RUB"


def test_h03_9siqt8tojo_sek_0009(api):
    resp = api.get("/api/products/9SIQT8TOJO", params={"currencyCode": "SEK"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "9SIQT8TOJO"
    assert product["name"] == 'Optical Tube Assembly'
    assert product["priceUsd"]["currencyCode"] == "SEK"


def test_h03_6e92zmyyfz_sgd_0010(api):
    resp = api.get("/api/products/6E92ZMYYFZ", params={"currencyCode": "SGD"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "6E92ZMYYFZ"
    assert product["name"] == 'Solar Filter'
    assert product["priceUsd"]["currencyCode"] == "SGD"


def test_h03_hqtgwgpnh4_thb_0011(api):
    resp = api.get("/api/products/HQTGWGPNH4", params={"currencyCode": "THB"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "HQTGWGPNH4"
    assert product["name"] == 'The Comet Book'
    assert product["priceUsd"]["currencyCode"] == "THB"


def test_h03_oljcespc7z_try_0012(api):
    resp = api.get("/api/products/OLJCESPC7Z", params={"currencyCode": "TRY"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "OLJCESPC7Z"
    assert product["name"] == 'National Park Foundation Explorascope'
    assert product["priceUsd"]["currencyCode"] == "TRY"


def test_h03_66vchsjnup_usd_0013(api):
    resp = api.get("/api/products/66VCHSJNUP", params={"currencyCode": "USD"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "66VCHSJNUP"
    assert product["name"] == 'Starsense Explorer Refractor Telescope'
    assert product["priceUsd"]["currencyCode"] == "USD"
    assert product["priceUsd"]["units"] == 349
    assert product["priceUsd"]["nanos"] == 950000000


def test_h03_1ymwwn1n4o_zar_0014(api):
    resp = api.get("/api/products/1YMWWN1N4O", params={"currencyCode": "ZAR"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "1YMWWN1N4O"
    assert product["name"] == 'Eclipsmart Travel Refractor Telescope'
    assert product["priceUsd"]["currencyCode"] == "ZAR"


def test_h03_l9ecav7kim_aud_0015(api):
    resp = api.get("/api/products/L9ECAV7KIM", params={"currencyCode": "AUD"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "L9ECAV7KIM"
    assert product["name"] == 'Lens Cleaning Kit'
    assert product["priceUsd"]["currencyCode"] == "AUD"


def test_h03_2zyfj3gm2n_bgn_0016(api):
    resp = api.get("/api/products/2ZYFJ3GM2N", params={"currencyCode": "BGN"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "2ZYFJ3GM2N"
    assert product["name"] == 'Roof Binoculars'
    assert product["priceUsd"]["currencyCode"] == "BGN"


def test_h03_0puk6v6ev0_brl_0017(api):
    resp = api.get("/api/products/0PUK6V6EV0", params={"currencyCode": "BRL"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "0PUK6V6EV0"
    assert product["name"] == 'Solar System Color Imager'
    assert product["priceUsd"]["currencyCode"] == "BRL"


def test_h03_ls4psxunum_cad_0018(api):
    resp = api.get("/api/products/LS4PSXUNUM", params={"currencyCode": "CAD"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "LS4PSXUNUM"
    assert product["name"] == 'Red Flashlight'
    assert product["priceUsd"]["currencyCode"] == "CAD"


def test_h03_9siqt8tojo_chf_0019(api):
    resp = api.get("/api/products/9SIQT8TOJO", params={"currencyCode": "CHF"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "9SIQT8TOJO"
    assert product["name"] == 'Optical Tube Assembly'
    assert product["priceUsd"]["currencyCode"] == "CHF"


def test_h03_6e92zmyyfz_cny_0020(api):
    resp = api.get("/api/products/6E92ZMYYFZ", params={"currencyCode": "CNY"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "6E92ZMYYFZ"
    assert product["name"] == 'Solar Filter'
    assert product["priceUsd"]["currencyCode"] == "CNY"


def test_h03_hqtgwgpnh4_czk_0021(api):
    resp = api.get("/api/products/HQTGWGPNH4", params={"currencyCode": "CZK"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "HQTGWGPNH4"
    assert product["name"] == 'The Comet Book'
    assert product["priceUsd"]["currencyCode"] == "CZK"


def test_h03_oljcespc7z_dkk_0022(api):
    resp = api.get("/api/products/OLJCESPC7Z", params={"currencyCode": "DKK"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "OLJCESPC7Z"
    assert product["name"] == 'National Park Foundation Explorascope'
    assert product["priceUsd"]["currencyCode"] == "DKK"


def test_h03_66vchsjnup_eur_0023(api):
    resp = api.get("/api/products/66VCHSJNUP", params={"currencyCode": "EUR"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "66VCHSJNUP"
    assert product["name"] == 'Starsense Explorer Refractor Telescope'
    assert product["priceUsd"]["currencyCode"] == "EUR"


def test_h03_1ymwwn1n4o_gbp_0024(api):
    resp = api.get("/api/products/1YMWWN1N4O", params={"currencyCode": "GBP"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "1YMWWN1N4O"
    assert product["name"] == 'Eclipsmart Travel Refractor Telescope'
    assert product["priceUsd"]["currencyCode"] == "GBP"


def test_h03_l9ecav7kim_hkd_0025(api):
    resp = api.get("/api/products/L9ECAV7KIM", params={"currencyCode": "HKD"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "L9ECAV7KIM"
    assert product["name"] == 'Lens Cleaning Kit'
    assert product["priceUsd"]["currencyCode"] == "HKD"


def test_h03_2zyfj3gm2n_hrk_0026(api):
    resp = api.get("/api/products/2ZYFJ3GM2N", params={"currencyCode": "HRK"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "2ZYFJ3GM2N"
    assert product["name"] == 'Roof Binoculars'
    assert product["priceUsd"]["currencyCode"] == "HRK"


def test_h03_0puk6v6ev0_huf_0027(api):
    resp = api.get("/api/products/0PUK6V6EV0", params={"currencyCode": "HUF"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "0PUK6V6EV0"
    assert product["name"] == 'Solar System Color Imager'
    assert product["priceUsd"]["currencyCode"] == "HUF"


def test_h03_ls4psxunum_idr_0028(api):
    resp = api.get("/api/products/LS4PSXUNUM", params={"currencyCode": "IDR"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "LS4PSXUNUM"
    assert product["name"] == 'Red Flashlight'
    assert product["priceUsd"]["currencyCode"] == "IDR"


def test_h03_9siqt8tojo_ils_0029(api):
    resp = api.get("/api/products/9SIQT8TOJO", params={"currencyCode": "ILS"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "9SIQT8TOJO"
    assert product["name"] == 'Optical Tube Assembly'
    assert product["priceUsd"]["currencyCode"] == "ILS"


def test_h03_6e92zmyyfz_inr_0030(api):
    resp = api.get("/api/products/6E92ZMYYFZ", params={"currencyCode": "INR"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "6E92ZMYYFZ"
    assert product["name"] == 'Solar Filter'
    assert product["priceUsd"]["currencyCode"] == "INR"


def test_h03_hqtgwgpnh4_isk_0031(api):
    resp = api.get("/api/products/HQTGWGPNH4", params={"currencyCode": "ISK"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "HQTGWGPNH4"
    assert product["name"] == 'The Comet Book'
    assert product["priceUsd"]["currencyCode"] == "ISK"


def test_h03_oljcespc7z_jpy_0032(api):
    resp = api.get("/api/products/OLJCESPC7Z", params={"currencyCode": "JPY"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "OLJCESPC7Z"
    assert product["name"] == 'National Park Foundation Explorascope'
    assert product["priceUsd"]["currencyCode"] == "JPY"


def test_h03_66vchsjnup_krw_0033(api):
    resp = api.get("/api/products/66VCHSJNUP", params={"currencyCode": "KRW"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "66VCHSJNUP"
    assert product["name"] == 'Starsense Explorer Refractor Telescope'
    assert product["priceUsd"]["currencyCode"] == "KRW"


def test_h03_1ymwwn1n4o_mxn_0034(api):
    resp = api.get("/api/products/1YMWWN1N4O", params={"currencyCode": "MXN"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "1YMWWN1N4O"
    assert product["name"] == 'Eclipsmart Travel Refractor Telescope'
    assert product["priceUsd"]["currencyCode"] == "MXN"


def test_h03_l9ecav7kim_myr_0035(api):
    resp = api.get("/api/products/L9ECAV7KIM", params={"currencyCode": "MYR"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "L9ECAV7KIM"
    assert product["name"] == 'Lens Cleaning Kit'
    assert product["priceUsd"]["currencyCode"] == "MYR"


def test_h03_2zyfj3gm2n_nok_0036(api):
    resp = api.get("/api/products/2ZYFJ3GM2N", params={"currencyCode": "NOK"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "2ZYFJ3GM2N"
    assert product["name"] == 'Roof Binoculars'
    assert product["priceUsd"]["currencyCode"] == "NOK"


def test_h03_0puk6v6ev0_nzd_0037(api):
    resp = api.get("/api/products/0PUK6V6EV0", params={"currencyCode": "NZD"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "0PUK6V6EV0"
    assert product["name"] == 'Solar System Color Imager'
    assert product["priceUsd"]["currencyCode"] == "NZD"


def test_h03_ls4psxunum_php_0038(api):
    resp = api.get("/api/products/LS4PSXUNUM", params={"currencyCode": "PHP"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "LS4PSXUNUM"
    assert product["name"] == 'Red Flashlight'
    assert product["priceUsd"]["currencyCode"] == "PHP"


def test_h03_9siqt8tojo_pln_0039(api):
    resp = api.get("/api/products/9SIQT8TOJO", params={"currencyCode": "PLN"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "9SIQT8TOJO"
    assert product["name"] == 'Optical Tube Assembly'
    assert product["priceUsd"]["currencyCode"] == "PLN"


def test_h03_6e92zmyyfz_ron_0040(api):
    resp = api.get("/api/products/6E92ZMYYFZ", params={"currencyCode": "RON"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "6E92ZMYYFZ"
    assert product["name"] == 'Solar Filter'
    assert product["priceUsd"]["currencyCode"] == "RON"


def test_h03_hqtgwgpnh4_rub_0041(api):
    resp = api.get("/api/products/HQTGWGPNH4", params={"currencyCode": "RUB"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "HQTGWGPNH4"
    assert product["name"] == 'The Comet Book'
    assert product["priceUsd"]["currencyCode"] == "RUB"


def test_h03_oljcespc7z_sek_0042(api):
    resp = api.get("/api/products/OLJCESPC7Z", params={"currencyCode": "SEK"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "OLJCESPC7Z"
    assert product["name"] == 'National Park Foundation Explorascope'
    assert product["priceUsd"]["currencyCode"] == "SEK"


def test_h03_66vchsjnup_sgd_0043(api):
    resp = api.get("/api/products/66VCHSJNUP", params={"currencyCode": "SGD"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "66VCHSJNUP"
    assert product["name"] == 'Starsense Explorer Refractor Telescope'
    assert product["priceUsd"]["currencyCode"] == "SGD"


def test_h03_1ymwwn1n4o_thb_0044(api):
    resp = api.get("/api/products/1YMWWN1N4O", params={"currencyCode": "THB"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "1YMWWN1N4O"
    assert product["name"] == 'Eclipsmart Travel Refractor Telescope'
    assert product["priceUsd"]["currencyCode"] == "THB"


def test_h03_l9ecav7kim_try_0045(api):
    resp = api.get("/api/products/L9ECAV7KIM", params={"currencyCode": "TRY"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "L9ECAV7KIM"
    assert product["name"] == 'Lens Cleaning Kit'
    assert product["priceUsd"]["currencyCode"] == "TRY"


def test_h03_2zyfj3gm2n_usd_0046(api):
    resp = api.get("/api/products/2ZYFJ3GM2N", params={"currencyCode": "USD"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "2ZYFJ3GM2N"
    assert product["name"] == 'Roof Binoculars'
    assert product["priceUsd"]["currencyCode"] == "USD"
    assert product["priceUsd"]["units"] == 209
    assert product["priceUsd"]["nanos"] == 950000000


def test_h03_0puk6v6ev0_zar_0047(api):
    resp = api.get("/api/products/0PUK6V6EV0", params={"currencyCode": "ZAR"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "0PUK6V6EV0"
    assert product["name"] == 'Solar System Color Imager'
    assert product["priceUsd"]["currencyCode"] == "ZAR"


def test_h03_ls4psxunum_aud_0048(api):
    resp = api.get("/api/products/LS4PSXUNUM", params={"currencyCode": "AUD"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "LS4PSXUNUM"
    assert product["name"] == 'Red Flashlight'
    assert product["priceUsd"]["currencyCode"] == "AUD"


def test_h03_9siqt8tojo_bgn_0049(api):
    resp = api.get("/api/products/9SIQT8TOJO", params={"currencyCode": "BGN"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "9SIQT8TOJO"
    assert product["name"] == 'Optical Tube Assembly'
    assert product["priceUsd"]["currencyCode"] == "BGN"


def test_h03_6e92zmyyfz_brl_0050(api):
    resp = api.get("/api/products/6E92ZMYYFZ", params={"currencyCode": "BRL"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "6E92ZMYYFZ"
    assert product["name"] == 'Solar Filter'
    assert product["priceUsd"]["currencyCode"] == "BRL"


def test_h03_hqtgwgpnh4_cad_0051(api):
    resp = api.get("/api/products/HQTGWGPNH4", params={"currencyCode": "CAD"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "HQTGWGPNH4"
    assert product["name"] == 'The Comet Book'
    assert product["priceUsd"]["currencyCode"] == "CAD"


def test_h03_oljcespc7z_chf_0052(api):
    resp = api.get("/api/products/OLJCESPC7Z", params={"currencyCode": "CHF"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "OLJCESPC7Z"
    assert product["name"] == 'National Park Foundation Explorascope'
    assert product["priceUsd"]["currencyCode"] == "CHF"


def test_h03_66vchsjnup_cny_0053(api):
    resp = api.get("/api/products/66VCHSJNUP", params={"currencyCode": "CNY"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "66VCHSJNUP"
    assert product["name"] == 'Starsense Explorer Refractor Telescope'
    assert product["priceUsd"]["currencyCode"] == "CNY"


def test_h03_1ymwwn1n4o_czk_0054(api):
    resp = api.get("/api/products/1YMWWN1N4O", params={"currencyCode": "CZK"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "1YMWWN1N4O"
    assert product["name"] == 'Eclipsmart Travel Refractor Telescope'
    assert product["priceUsd"]["currencyCode"] == "CZK"


def test_h03_l9ecav7kim_dkk_0055(api):
    resp = api.get("/api/products/L9ECAV7KIM", params={"currencyCode": "DKK"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "L9ECAV7KIM"
    assert product["name"] == 'Lens Cleaning Kit'
    assert product["priceUsd"]["currencyCode"] == "DKK"


def test_h03_2zyfj3gm2n_eur_0056(api):
    resp = api.get("/api/products/2ZYFJ3GM2N", params={"currencyCode": "EUR"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "2ZYFJ3GM2N"
    assert product["name"] == 'Roof Binoculars'
    assert product["priceUsd"]["currencyCode"] == "EUR"


def test_h03_0puk6v6ev0_gbp_0057(api):
    resp = api.get("/api/products/0PUK6V6EV0", params={"currencyCode": "GBP"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "0PUK6V6EV0"
    assert product["name"] == 'Solar System Color Imager'
    assert product["priceUsd"]["currencyCode"] == "GBP"


def test_h03_ls4psxunum_hkd_0058(api):
    resp = api.get("/api/products/LS4PSXUNUM", params={"currencyCode": "HKD"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "LS4PSXUNUM"
    assert product["name"] == 'Red Flashlight'
    assert product["priceUsd"]["currencyCode"] == "HKD"


def test_h03_9siqt8tojo_hrk_0059(api):
    resp = api.get("/api/products/9SIQT8TOJO", params={"currencyCode": "HRK"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "9SIQT8TOJO"
    assert product["name"] == 'Optical Tube Assembly'
    assert product["priceUsd"]["currencyCode"] == "HRK"


def test_h03_6e92zmyyfz_huf_0060(api):
    resp = api.get("/api/products/6E92ZMYYFZ", params={"currencyCode": "HUF"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "6E92ZMYYFZ"
    assert product["name"] == 'Solar Filter'
    assert product["priceUsd"]["currencyCode"] == "HUF"


def test_h03_hqtgwgpnh4_idr_0061(api):
    resp = api.get("/api/products/HQTGWGPNH4", params={"currencyCode": "IDR"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "HQTGWGPNH4"
    assert product["name"] == 'The Comet Book'
    assert product["priceUsd"]["currencyCode"] == "IDR"


def test_h03_oljcespc7z_ils_0062(api):
    resp = api.get("/api/products/OLJCESPC7Z", params={"currencyCode": "ILS"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "OLJCESPC7Z"
    assert product["name"] == 'National Park Foundation Explorascope'
    assert product["priceUsd"]["currencyCode"] == "ILS"


def test_h03_66vchsjnup_inr_0063(api):
    resp = api.get("/api/products/66VCHSJNUP", params={"currencyCode": "INR"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "66VCHSJNUP"
    assert product["name"] == 'Starsense Explorer Refractor Telescope'
    assert product["priceUsd"]["currencyCode"] == "INR"


def test_h03_1ymwwn1n4o_isk_0064(api):
    resp = api.get("/api/products/1YMWWN1N4O", params={"currencyCode": "ISK"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "1YMWWN1N4O"
    assert product["name"] == 'Eclipsmart Travel Refractor Telescope'
    assert product["priceUsd"]["currencyCode"] == "ISK"


def test_h03_l9ecav7kim_jpy_0065(api):
    resp = api.get("/api/products/L9ECAV7KIM", params={"currencyCode": "JPY"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "L9ECAV7KIM"
    assert product["name"] == 'Lens Cleaning Kit'
    assert product["priceUsd"]["currencyCode"] == "JPY"


def test_h03_2zyfj3gm2n_krw_0066(api):
    resp = api.get("/api/products/2ZYFJ3GM2N", params={"currencyCode": "KRW"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "2ZYFJ3GM2N"
    assert product["name"] == 'Roof Binoculars'
    assert product["priceUsd"]["currencyCode"] == "KRW"


def test_h03_0puk6v6ev0_mxn_0067(api):
    resp = api.get("/api/products/0PUK6V6EV0", params={"currencyCode": "MXN"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "0PUK6V6EV0"
    assert product["name"] == 'Solar System Color Imager'
    assert product["priceUsd"]["currencyCode"] == "MXN"


def test_h03_ls4psxunum_myr_0068(api):
    resp = api.get("/api/products/LS4PSXUNUM", params={"currencyCode": "MYR"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "LS4PSXUNUM"
    assert product["name"] == 'Red Flashlight'
    assert product["priceUsd"]["currencyCode"] == "MYR"


def test_h03_9siqt8tojo_nok_0069(api):
    resp = api.get("/api/products/9SIQT8TOJO", params={"currencyCode": "NOK"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "9SIQT8TOJO"
    assert product["name"] == 'Optical Tube Assembly'
    assert product["priceUsd"]["currencyCode"] == "NOK"


def test_h03_6e92zmyyfz_nzd_0070(api):
    resp = api.get("/api/products/6E92ZMYYFZ", params={"currencyCode": "NZD"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "6E92ZMYYFZ"
    assert product["name"] == 'Solar Filter'
    assert product["priceUsd"]["currencyCode"] == "NZD"


def test_h03_hqtgwgpnh4_php_0071(api):
    resp = api.get("/api/products/HQTGWGPNH4", params={"currencyCode": "PHP"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "HQTGWGPNH4"
    assert product["name"] == 'The Comet Book'
    assert product["priceUsd"]["currencyCode"] == "PHP"


def test_h03_oljcespc7z_pln_0072(api):
    resp = api.get("/api/products/OLJCESPC7Z", params={"currencyCode": "PLN"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "OLJCESPC7Z"
    assert product["name"] == 'National Park Foundation Explorascope'
    assert product["priceUsd"]["currencyCode"] == "PLN"


def test_h03_66vchsjnup_ron_0073(api):
    resp = api.get("/api/products/66VCHSJNUP", params={"currencyCode": "RON"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "66VCHSJNUP"
    assert product["name"] == 'Starsense Explorer Refractor Telescope'
    assert product["priceUsd"]["currencyCode"] == "RON"


def test_h03_1ymwwn1n4o_rub_0074(api):
    resp = api.get("/api/products/1YMWWN1N4O", params={"currencyCode": "RUB"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "1YMWWN1N4O"
    assert product["name"] == 'Eclipsmart Travel Refractor Telescope'
    assert product["priceUsd"]["currencyCode"] == "RUB"


def test_h03_l9ecav7kim_sek_0075(api):
    resp = api.get("/api/products/L9ECAV7KIM", params={"currencyCode": "SEK"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "L9ECAV7KIM"
    assert product["name"] == 'Lens Cleaning Kit'
    assert product["priceUsd"]["currencyCode"] == "SEK"


def test_h03_2zyfj3gm2n_sgd_0076(api):
    resp = api.get("/api/products/2ZYFJ3GM2N", params={"currencyCode": "SGD"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "2ZYFJ3GM2N"
    assert product["name"] == 'Roof Binoculars'
    assert product["priceUsd"]["currencyCode"] == "SGD"


def test_h03_0puk6v6ev0_thb_0077(api):
    resp = api.get("/api/products/0PUK6V6EV0", params={"currencyCode": "THB"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "0PUK6V6EV0"
    assert product["name"] == 'Solar System Color Imager'
    assert product["priceUsd"]["currencyCode"] == "THB"


def test_h03_ls4psxunum_try_0078(api):
    resp = api.get("/api/products/LS4PSXUNUM", params={"currencyCode": "TRY"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "LS4PSXUNUM"
    assert product["name"] == 'Red Flashlight'
    assert product["priceUsd"]["currencyCode"] == "TRY"


def test_h03_9siqt8tojo_usd_0079(api):
    resp = api.get("/api/products/9SIQT8TOJO", params={"currencyCode": "USD"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "9SIQT8TOJO"
    assert product["name"] == 'Optical Tube Assembly'
    assert product["priceUsd"]["currencyCode"] == "USD"
    assert product["priceUsd"]["units"] == 3599
    assert product["priceUsd"]["nanos"] == 0


def test_h03_6e92zmyyfz_zar_0080(api):
    resp = api.get("/api/products/6E92ZMYYFZ", params={"currencyCode": "ZAR"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "6E92ZMYYFZ"
    assert product["name"] == 'Solar Filter'
    assert product["priceUsd"]["currencyCode"] == "ZAR"


def test_h03_hqtgwgpnh4_aud_0081(api):
    resp = api.get("/api/products/HQTGWGPNH4", params={"currencyCode": "AUD"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "HQTGWGPNH4"
    assert product["name"] == 'The Comet Book'
    assert product["priceUsd"]["currencyCode"] == "AUD"


def test_h03_oljcespc7z_bgn_0082(api):
    resp = api.get("/api/products/OLJCESPC7Z", params={"currencyCode": "BGN"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "OLJCESPC7Z"
    assert product["name"] == 'National Park Foundation Explorascope'
    assert product["priceUsd"]["currencyCode"] == "BGN"


def test_h03_66vchsjnup_brl_0083(api):
    resp = api.get("/api/products/66VCHSJNUP", params={"currencyCode": "BRL"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "66VCHSJNUP"
    assert product["name"] == 'Starsense Explorer Refractor Telescope'
    assert product["priceUsd"]["currencyCode"] == "BRL"


def test_h03_1ymwwn1n4o_cad_0084(api):
    resp = api.get("/api/products/1YMWWN1N4O", params={"currencyCode": "CAD"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "1YMWWN1N4O"
    assert product["name"] == 'Eclipsmart Travel Refractor Telescope'
    assert product["priceUsd"]["currencyCode"] == "CAD"


def test_h03_l9ecav7kim_chf_0085(api):
    resp = api.get("/api/products/L9ECAV7KIM", params={"currencyCode": "CHF"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "L9ECAV7KIM"
    assert product["name"] == 'Lens Cleaning Kit'
    assert product["priceUsd"]["currencyCode"] == "CHF"


def test_h03_2zyfj3gm2n_cny_0086(api):
    resp = api.get("/api/products/2ZYFJ3GM2N", params={"currencyCode": "CNY"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "2ZYFJ3GM2N"
    assert product["name"] == 'Roof Binoculars'
    assert product["priceUsd"]["currencyCode"] == "CNY"


def test_h03_0puk6v6ev0_czk_0087(api):
    resp = api.get("/api/products/0PUK6V6EV0", params={"currencyCode": "CZK"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "0PUK6V6EV0"
    assert product["name"] == 'Solar System Color Imager'
    assert product["priceUsd"]["currencyCode"] == "CZK"


def test_h03_ls4psxunum_dkk_0088(api):
    resp = api.get("/api/products/LS4PSXUNUM", params={"currencyCode": "DKK"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "LS4PSXUNUM"
    assert product["name"] == 'Red Flashlight'
    assert product["priceUsd"]["currencyCode"] == "DKK"


def test_h03_9siqt8tojo_eur_0089(api):
    resp = api.get("/api/products/9SIQT8TOJO", params={"currencyCode": "EUR"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "9SIQT8TOJO"
    assert product["name"] == 'Optical Tube Assembly'
    assert product["priceUsd"]["currencyCode"] == "EUR"


def test_h03_6e92zmyyfz_gbp_0090(api):
    resp = api.get("/api/products/6E92ZMYYFZ", params={"currencyCode": "GBP"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "6E92ZMYYFZ"
    assert product["name"] == 'Solar Filter'
    assert product["priceUsd"]["currencyCode"] == "GBP"


def test_h03_hqtgwgpnh4_hkd_0091(api):
    resp = api.get("/api/products/HQTGWGPNH4", params={"currencyCode": "HKD"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "HQTGWGPNH4"
    assert product["name"] == 'The Comet Book'
    assert product["priceUsd"]["currencyCode"] == "HKD"


def test_h03_oljcespc7z_hrk_0092(api):
    resp = api.get("/api/products/OLJCESPC7Z", params={"currencyCode": "HRK"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "OLJCESPC7Z"
    assert product["name"] == 'National Park Foundation Explorascope'
    assert product["priceUsd"]["currencyCode"] == "HRK"


def test_h03_66vchsjnup_huf_0093(api):
    resp = api.get("/api/products/66VCHSJNUP", params={"currencyCode": "HUF"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "66VCHSJNUP"
    assert product["name"] == 'Starsense Explorer Refractor Telescope'
    assert product["priceUsd"]["currencyCode"] == "HUF"


def test_h03_1ymwwn1n4o_idr_0094(api):
    resp = api.get("/api/products/1YMWWN1N4O", params={"currencyCode": "IDR"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "1YMWWN1N4O"
    assert product["name"] == 'Eclipsmart Travel Refractor Telescope'
    assert product["priceUsd"]["currencyCode"] == "IDR"


def test_h03_l9ecav7kim_ils_0095(api):
    resp = api.get("/api/products/L9ECAV7KIM", params={"currencyCode": "ILS"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "L9ECAV7KIM"
    assert product["name"] == 'Lens Cleaning Kit'
    assert product["priceUsd"]["currencyCode"] == "ILS"


def test_h03_2zyfj3gm2n_inr_0096(api):
    resp = api.get("/api/products/2ZYFJ3GM2N", params={"currencyCode": "INR"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "2ZYFJ3GM2N"
    assert product["name"] == 'Roof Binoculars'
    assert product["priceUsd"]["currencyCode"] == "INR"


def test_h03_0puk6v6ev0_isk_0097(api):
    resp = api.get("/api/products/0PUK6V6EV0", params={"currencyCode": "ISK"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "0PUK6V6EV0"
    assert product["name"] == 'Solar System Color Imager'
    assert product["priceUsd"]["currencyCode"] == "ISK"


def test_h03_ls4psxunum_jpy_0098(api):
    resp = api.get("/api/products/LS4PSXUNUM", params={"currencyCode": "JPY"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "LS4PSXUNUM"
    assert product["name"] == 'Red Flashlight'
    assert product["priceUsd"]["currencyCode"] == "JPY"


def test_h03_9siqt8tojo_krw_0099(api):
    resp = api.get("/api/products/9SIQT8TOJO", params={"currencyCode": "KRW"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "9SIQT8TOJO"
    assert product["name"] == 'Optical Tube Assembly'
    assert product["priceUsd"]["currencyCode"] == "KRW"


def test_h03_6e92zmyyfz_mxn_0100(api):
    resp = api.get("/api/products/6E92ZMYYFZ", params={"currencyCode": "MXN"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "6E92ZMYYFZ"
    assert product["name"] == 'Solar Filter'
    assert product["priceUsd"]["currencyCode"] == "MXN"


def test_h03_hqtgwgpnh4_myr_0101(api):
    resp = api.get("/api/products/HQTGWGPNH4", params={"currencyCode": "MYR"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "HQTGWGPNH4"
    assert product["name"] == 'The Comet Book'
    assert product["priceUsd"]["currencyCode"] == "MYR"


def test_h03_oljcespc7z_nok_0102(api):
    resp = api.get("/api/products/OLJCESPC7Z", params={"currencyCode": "NOK"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "OLJCESPC7Z"
    assert product["name"] == 'National Park Foundation Explorascope'
    assert product["priceUsd"]["currencyCode"] == "NOK"


def test_h03_66vchsjnup_nzd_0103(api):
    resp = api.get("/api/products/66VCHSJNUP", params={"currencyCode": "NZD"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "66VCHSJNUP"
    assert product["name"] == 'Starsense Explorer Refractor Telescope'
    assert product["priceUsd"]["currencyCode"] == "NZD"


def test_h03_1ymwwn1n4o_php_0104(api):
    resp = api.get("/api/products/1YMWWN1N4O", params={"currencyCode": "PHP"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "1YMWWN1N4O"
    assert product["name"] == 'Eclipsmart Travel Refractor Telescope'
    assert product["priceUsd"]["currencyCode"] == "PHP"


def test_h03_l9ecav7kim_pln_0105(api):
    resp = api.get("/api/products/L9ECAV7KIM", params={"currencyCode": "PLN"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "L9ECAV7KIM"
    assert product["name"] == 'Lens Cleaning Kit'
    assert product["priceUsd"]["currencyCode"] == "PLN"


def test_h03_2zyfj3gm2n_ron_0106(api):
    resp = api.get("/api/products/2ZYFJ3GM2N", params={"currencyCode": "RON"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "2ZYFJ3GM2N"
    assert product["name"] == 'Roof Binoculars'
    assert product["priceUsd"]["currencyCode"] == "RON"


def test_h03_0puk6v6ev0_rub_0107(api):
    resp = api.get("/api/products/0PUK6V6EV0", params={"currencyCode": "RUB"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "0PUK6V6EV0"
    assert product["name"] == 'Solar System Color Imager'
    assert product["priceUsd"]["currencyCode"] == "RUB"


def test_h03_ls4psxunum_sek_0108(api):
    resp = api.get("/api/products/LS4PSXUNUM", params={"currencyCode": "SEK"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "LS4PSXUNUM"
    assert product["name"] == 'Red Flashlight'
    assert product["priceUsd"]["currencyCode"] == "SEK"


def test_h03_9siqt8tojo_sgd_0109(api):
    resp = api.get("/api/products/9SIQT8TOJO", params={"currencyCode": "SGD"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "9SIQT8TOJO"
    assert product["name"] == 'Optical Tube Assembly'
    assert product["priceUsd"]["currencyCode"] == "SGD"


def test_h03_6e92zmyyfz_thb_0110(api):
    resp = api.get("/api/products/6E92ZMYYFZ", params={"currencyCode": "THB"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "6E92ZMYYFZ"
    assert product["name"] == 'Solar Filter'
    assert product["priceUsd"]["currencyCode"] == "THB"


def test_h03_hqtgwgpnh4_try_0111(api):
    resp = api.get("/api/products/HQTGWGPNH4", params={"currencyCode": "TRY"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "HQTGWGPNH4"
    assert product["name"] == 'The Comet Book'
    assert product["priceUsd"]["currencyCode"] == "TRY"


def test_h03_oljcespc7z_usd_0112(api):
    resp = api.get("/api/products/OLJCESPC7Z", params={"currencyCode": "USD"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "OLJCESPC7Z"
    assert product["name"] == 'National Park Foundation Explorascope'
    assert product["priceUsd"]["currencyCode"] == "USD"
    assert product["priceUsd"]["units"] == 101
    assert product["priceUsd"]["nanos"] == 960000000


def test_h03_66vchsjnup_zar_0113(api):
    resp = api.get("/api/products/66VCHSJNUP", params={"currencyCode": "ZAR"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "66VCHSJNUP"
    assert product["name"] == 'Starsense Explorer Refractor Telescope'
    assert product["priceUsd"]["currencyCode"] == "ZAR"


def test_h03_1ymwwn1n4o_aud_0114(api):
    resp = api.get("/api/products/1YMWWN1N4O", params={"currencyCode": "AUD"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "1YMWWN1N4O"
    assert product["name"] == 'Eclipsmart Travel Refractor Telescope'
    assert product["priceUsd"]["currencyCode"] == "AUD"


def test_h03_l9ecav7kim_bgn_0115(api):
    resp = api.get("/api/products/L9ECAV7KIM", params={"currencyCode": "BGN"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "L9ECAV7KIM"
    assert product["name"] == 'Lens Cleaning Kit'
    assert product["priceUsd"]["currencyCode"] == "BGN"


def test_h03_2zyfj3gm2n_brl_0116(api):
    resp = api.get("/api/products/2ZYFJ3GM2N", params={"currencyCode": "BRL"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "2ZYFJ3GM2N"
    assert product["name"] == 'Roof Binoculars'
    assert product["priceUsd"]["currencyCode"] == "BRL"


def test_h03_0puk6v6ev0_cad_0117(api):
    resp = api.get("/api/products/0PUK6V6EV0", params={"currencyCode": "CAD"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "0PUK6V6EV0"
    assert product["name"] == 'Solar System Color Imager'
    assert product["priceUsd"]["currencyCode"] == "CAD"


def test_h03_ls4psxunum_chf_0118(api):
    resp = api.get("/api/products/LS4PSXUNUM", params={"currencyCode": "CHF"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "LS4PSXUNUM"
    assert product["name"] == 'Red Flashlight'
    assert product["priceUsd"]["currencyCode"] == "CHF"


def test_h03_9siqt8tojo_cny_0119(api):
    resp = api.get("/api/products/9SIQT8TOJO", params={"currencyCode": "CNY"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "9SIQT8TOJO"
    assert product["name"] == 'Optical Tube Assembly'
    assert product["priceUsd"]["currencyCode"] == "CNY"


def test_h03_6e92zmyyfz_czk_0120(api):
    resp = api.get("/api/products/6E92ZMYYFZ", params={"currencyCode": "CZK"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "6E92ZMYYFZ"
    assert product["name"] == 'Solar Filter'
    assert product["priceUsd"]["currencyCode"] == "CZK"
