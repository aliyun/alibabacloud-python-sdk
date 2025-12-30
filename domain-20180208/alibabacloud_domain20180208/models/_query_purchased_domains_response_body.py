# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_domain20180208 import models as main_models
from darabonba.model import DaraModel

class QueryPurchasedDomainsResponseBody(DaraModel):
    def __init__(
        self,
        current_page_num: int = None,
        data: List[main_models.QueryPurchasedDomainsResponseBodyData] = None,
        page_size: int = None,
        request_id: str = None,
        total_item_num: int = None,
        total_page_num: int = None,
    ):
        self.current_page_num = current_page_num
        self.data = data
        self.page_size = page_size
        self.request_id = request_id
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

        if self.request_id is not None:
            result['RequestId'] = self.request_id

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
                temp_model = main_models.QueryPurchasedDomainsResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalItemNum') is not None:
            self.total_item_num = m.get('TotalItemNum')

        if m.get('TotalPageNum') is not None:
            self.total_page_num = m.get('TotalPageNum')

        return self

class QueryPurchasedDomainsResponseBodyData(DaraModel):
    def __init__(
        self,
        delivery_time: str = None,
        domain_name: str = None,
        operation_status: str = None,
        operation_time: str = None,
        product_type: str = None,
        trade_money: float = None,
    ):
        self.delivery_time = delivery_time
        self.domain_name = domain_name
        self.operation_status = operation_status
        self.operation_time = operation_time
        self.product_type = product_type
        self.trade_money = trade_money

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.delivery_time is not None:
            result['DeliveryTime'] = self.delivery_time

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.operation_status is not None:
            result['OperationStatus'] = self.operation_status

        if self.operation_time is not None:
            result['OperationTime'] = self.operation_time

        if self.product_type is not None:
            result['ProductType'] = self.product_type

        if self.trade_money is not None:
            result['TradeMoney'] = self.trade_money

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeliveryTime') is not None:
            self.delivery_time = m.get('DeliveryTime')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('OperationStatus') is not None:
            self.operation_status = m.get('OperationStatus')

        if m.get('OperationTime') is not None:
            self.operation_time = m.get('OperationTime')

        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')

        if m.get('TradeMoney') is not None:
            self.trade_money = m.get('TradeMoney')

        return self

