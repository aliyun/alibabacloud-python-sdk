# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_domain20180208 import models as main_models
from darabonba.model import DaraModel

class QueryBuyerDomainTradeRecordsResponseBody(DaraModel):
    def __init__(
        self,
        module: main_models.QueryBuyerDomainTradeRecordsResponseBodyModule = None,
        request_id: str = None,
    ):
        self.module = module
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.module:
            self.module.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.module is not None:
            result['Module'] = self.module.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Module') is not None:
            temp_model = main_models.QueryBuyerDomainTradeRecordsResponseBodyModule()
            self.module = temp_model.from_map(m.get('Module'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class QueryBuyerDomainTradeRecordsResponseBodyModule(DaraModel):
    def __init__(
        self,
        current_page_num: int = None,
        data: List[main_models.QueryBuyerDomainTradeRecordsResponseBodyModuleData] = None,
        page_size: int = None,
        total_item_num: int = None,
        total_page_num: int = None,
    ):
        self.current_page_num = current_page_num
        self.data = data
        self.page_size = page_size
        self.total_item_num = total_item_num
        self.total_page_num = total_page_num

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page_num is not None:
            result['CurrentPageNum'] = self.current_page_num

        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_item_num is not None:
            result['TotalItemNum'] = self.total_item_num

        if self.total_page_num is not None:
            result['TotalPageNum'] = self.total_page_num

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPageNum') is not None:
            self.current_page_num = m.get('CurrentPageNum')

        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.QueryBuyerDomainTradeRecordsResponseBodyModuleData()
                self.data.append(temp_model.from_map(k1))

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalItemNum') is not None:
            self.total_item_num = m.get('TotalItemNum')

        if m.get('TotalPageNum') is not None:
            self.total_page_num = m.get('TotalPageNum')

        return self

class QueryBuyerDomainTradeRecordsResponseBodyModuleData(DaraModel):
    def __init__(
        self,
        biz_id: str = None,
        currency: str = None,
        delivery_time: str = None,
        domain_name: str = None,
        pay_time: str = None,
        status: str = None,
        trade_id: str = None,
        trade_price: float = None,
        trade_type: str = None,
    ):
        self.biz_id = biz_id
        self.currency = currency
        self.delivery_time = delivery_time
        self.domain_name = domain_name
        self.pay_time = pay_time
        self.status = status
        self.trade_id = trade_id
        self.trade_price = trade_price
        self.trade_type = trade_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_id is not None:
            result['BizId'] = self.biz_id

        if self.currency is not None:
            result['Currency'] = self.currency

        if self.delivery_time is not None:
            result['DeliveryTime'] = self.delivery_time

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.pay_time is not None:
            result['PayTime'] = self.pay_time

        if self.status is not None:
            result['Status'] = self.status

        if self.trade_id is not None:
            result['TradeId'] = self.trade_id

        if self.trade_price is not None:
            result['TradePrice'] = self.trade_price

        if self.trade_type is not None:
            result['TradeType'] = self.trade_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')

        if m.get('Currency') is not None:
            self.currency = m.get('Currency')

        if m.get('DeliveryTime') is not None:
            self.delivery_time = m.get('DeliveryTime')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('PayTime') is not None:
            self.pay_time = m.get('PayTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TradeId') is not None:
            self.trade_id = m.get('TradeId')

        if m.get('TradePrice') is not None:
            self.trade_price = m.get('TradePrice')

        if m.get('TradeType') is not None:
            self.trade_type = m.get('TradeType')

        return self

