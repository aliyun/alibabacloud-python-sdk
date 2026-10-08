# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_domain20180129 import models as main_models
from darabonba.model import DaraModel

class QueryIntlFixedPriceOrderListResponseBody(DaraModel):
    def __init__(
        self,
        module: main_models.QueryIntlFixedPriceOrderListResponseBodyModule = None,
        request_id: str = None,
    ):
        # The response object.
        self.module = module
        # The request ID.
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
            temp_model = main_models.QueryIntlFixedPriceOrderListResponseBodyModule()
            self.module = temp_model.from_map(m.get('Module'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class QueryIntlFixedPriceOrderListResponseBodyModule(DaraModel):
    def __init__(
        self,
        current_page_num: int = None,
        data: List[main_models.QueryIntlFixedPriceOrderListResponseBodyModuleData] = None,
        page_size: int = None,
        total_item_num: int = None,
        total_page_num: int = None,
    ):
        # The current page number.
        self.current_page_num = current_page_num
        # The order list data.
        self.data = data
        # The number of entries per page.
        self.page_size = page_size
        # The total number of entries.
        self.total_item_num = total_item_num
        # The total number of pages.
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
                temp_model = main_models.QueryIntlFixedPriceOrderListResponseBodyModuleData()
                self.data.append(temp_model.from_map(k1))

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalItemNum') is not None:
            self.total_item_num = m.get('TotalItemNum')

        if m.get('TotalPageNum') is not None:
            self.total_page_num = m.get('TotalPageNum')

        return self

class QueryIntlFixedPriceOrderListResponseBodyModuleData(DaraModel):
    def __init__(
        self,
        biz_id: str = None,
        create_time: int = None,
        domain: str = None,
        order_type: int = None,
        price: int = None,
        status: int = None,
        update_time: int = None,
        user_id: str = None,
    ):
        # The business ID.
        self.biz_id = biz_id
        # The creation time.
        self.create_time = create_time
        # The domain name.
        self.domain = domain
        # The order type. Valid values:
        # - 11: international fixed-price.
        self.order_type = order_type
        # The price.
        self.price = price
        # The order status. Valid values:
        # - 5: Transaction closed.
        # - 6: Paid.
        # - 7: Pending production.
        # - 9: Transaction completed.
        self.status = status
        # The update time.
        self.update_time = update_time
        # The user ID.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_id is not None:
            result['BizId'] = self.biz_id

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.domain is not None:
            result['Domain'] = self.domain

        if self.order_type is not None:
            result['OrderType'] = self.order_type

        if self.price is not None:
            result['Price'] = self.price

        if self.status is not None:
            result['Status'] = self.status

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Domain') is not None:
            self.domain = m.get('Domain')

        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')

        if m.get('Price') is not None:
            self.price = m.get('Price')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

