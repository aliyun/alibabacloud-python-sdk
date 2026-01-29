# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

from alibabacloud_bssopenapi20171214 import models as main_models
from darabonba.model import DaraModel

class QuerySkuPriceListResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.QuerySkuPriceListResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The HTTP status code.
        self.code = code
        # The data that is returned.
        self.data = data
        # The message that is returned.
        self.message = message
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request is successful.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.QuerySkuPriceListResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class QuerySkuPriceListResponseBodyData(DaraModel):
    def __init__(
        self,
        sku_price_page: main_models.QuerySkuPriceListResponseBodyDataSkuPricePage = None,
    ):
        # The SKUs of the pricing object.
        self.sku_price_page = sku_price_page

    def validate(self):
        if self.sku_price_page:
            self.sku_price_page.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.sku_price_page is not None:
            result['SkuPricePage'] = self.sku_price_page.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SkuPricePage') is not None:
            temp_model = main_models.QuerySkuPriceListResponseBodyDataSkuPricePage()
            self.sku_price_page = temp_model.from_map(m.get('SkuPricePage'))

        return self

class QuerySkuPriceListResponseBodyDataSkuPricePage(DaraModel):
    def __init__(
        self,
        next_page_token: str = None,
        sku_price_list: List[main_models.QuerySkuPriceListResponseBodyDataSkuPricePageSkuPriceList] = None,
        total_count: int = None,
    ):
        # The token that is used to query the next page.
        self.next_page_token = next_page_token
        # The SKUs.
        self.sku_price_list = sku_price_list
        # The total number of SKUs.
        self.total_count = total_count

    def validate(self):
        if self.sku_price_list:
            for v1 in self.sku_price_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.next_page_token is not None:
            result['NextPageToken'] = self.next_page_token

        result['SkuPriceList'] = []
        if self.sku_price_list is not None:
            for k1 in self.sku_price_list:
                result['SkuPriceList'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextPageToken') is not None:
            self.next_page_token = m.get('NextPageToken')

        self.sku_price_list = []
        if m.get('SkuPriceList') is not None:
            for k1 in m.get('SkuPriceList'):
                temp_model = main_models.QuerySkuPriceListResponseBodyDataSkuPricePageSkuPriceList()
                self.sku_price_list.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class QuerySkuPriceListResponseBodyDataSkuPricePageSkuPriceList(DaraModel):
    def __init__(
        self,
        csku_price_list: List[main_models.QuerySkuPriceListResponseBodyDataSkuPricePageSkuPriceListCskuPriceList] = None,
        sku_code: str = None,
        sku_factor_map: Dict[str, str] = None,
    ):
        # The prices of the SKUs.
        self.csku_price_list = csku_price_list
        # The code of the SKU.
        self.sku_code = sku_code
        # The values of the pricing factors.
        self.sku_factor_map = sku_factor_map

    def validate(self):
        if self.csku_price_list:
            for v1 in self.csku_price_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['CskuPriceList'] = []
        if self.csku_price_list is not None:
            for k1 in self.csku_price_list:
                result['CskuPriceList'].append(k1.to_map() if k1 else None)

        if self.sku_code is not None:
            result['SkuCode'] = self.sku_code

        if self.sku_factor_map is not None:
            result['SkuFactorMap'] = self.sku_factor_map

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.csku_price_list = []
        if m.get('CskuPriceList') is not None:
            for k1 in m.get('CskuPriceList'):
                temp_model = main_models.QuerySkuPriceListResponseBodyDataSkuPricePageSkuPriceListCskuPriceList()
                self.csku_price_list.append(temp_model.from_map(k1))

        if m.get('SkuCode') is not None:
            self.sku_code = m.get('SkuCode')

        if m.get('SkuFactorMap') is not None:
            self.sku_factor_map = m.get('SkuFactorMap')

        return self

class QuerySkuPriceListResponseBodyDataSkuPricePageSkuPriceListCskuPriceList(DaraModel):
    def __init__(
        self,
        csku_code: str = None,
        currency: str = None,
        price: str = None,
        price_mode: str = None,
        price_type: str = None,
        price_unit: str = None,
        range_list: List[main_models.QuerySkuPriceListResponseBodyDataSkuPricePageSkuPriceListCskuPriceListRangeList] = None,
        usage_unit: str = None,
    ):
        # The unique code of the SKU price.
        self.csku_code = csku_code
        # The currency.
        self.currency = currency
        # The price.
        self.price = price
        # The pricing mode.
        self.price_mode = price_mode
        # The pricing type.
        self.price_type = price_type
        # The unit of the price.
        self.price_unit = price_unit
        # If the PriceMode parameter is set to STEP_ACCUMULATION or STEP_ARRIVE, the value of this field exists and specifies the range. If the PriceMode parameter is set to NORMAL_PRICE, the value of this field is null.
        self.range_list = range_list
        # The usage unit.
        self.usage_unit = usage_unit

    def validate(self):
        if self.range_list:
            for v1 in self.range_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.csku_code is not None:
            result['CskuCode'] = self.csku_code

        if self.currency is not None:
            result['Currency'] = self.currency

        if self.price is not None:
            result['Price'] = self.price

        if self.price_mode is not None:
            result['PriceMode'] = self.price_mode

        if self.price_type is not None:
            result['PriceType'] = self.price_type

        if self.price_unit is not None:
            result['PriceUnit'] = self.price_unit

        result['RangeList'] = []
        if self.range_list is not None:
            for k1 in self.range_list:
                result['RangeList'].append(k1.to_map() if k1 else None)

        if self.usage_unit is not None:
            result['UsageUnit'] = self.usage_unit

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CskuCode') is not None:
            self.csku_code = m.get('CskuCode')

        if m.get('Currency') is not None:
            self.currency = m.get('Currency')

        if m.get('Price') is not None:
            self.price = m.get('Price')

        if m.get('PriceMode') is not None:
            self.price_mode = m.get('PriceMode')

        if m.get('PriceType') is not None:
            self.price_type = m.get('PriceType')

        if m.get('PriceUnit') is not None:
            self.price_unit = m.get('PriceUnit')

        self.range_list = []
        if m.get('RangeList') is not None:
            for k1 in m.get('RangeList'):
                temp_model = main_models.QuerySkuPriceListResponseBodyDataSkuPricePageSkuPriceListCskuPriceListRangeList()
                self.range_list.append(temp_model.from_map(k1))

        if m.get('UsageUnit') is not None:
            self.usage_unit = m.get('UsageUnit')

        return self

class QuerySkuPriceListResponseBodyDataSkuPricePageSkuPriceListCskuPriceListRangeList(DaraModel):
    def __init__(
        self,
        factor_code: str = None,
        max: str = None,
        min: str = None,
        type: str = None,
    ):
        # The code of the pricing factor.
        self.factor_code = factor_code
        # The maximum value.
        self.max = max
        # The minimum value.
        self.min = min
        # The closure type of the interval.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.factor_code is not None:
            result['FactorCode'] = self.factor_code

        if self.max is not None:
            result['Max'] = self.max

        if self.min is not None:
            result['Min'] = self.min

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FactorCode') is not None:
            self.factor_code = m.get('FactorCode')

        if m.get('Max') is not None:
            self.max = m.get('Max')

        if m.get('Min') is not None:
            self.min = m.get('Min')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

