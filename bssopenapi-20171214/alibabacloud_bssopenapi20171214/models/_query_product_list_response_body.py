# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_bssopenapi20171214 import models as main_models
from darabonba.model import DaraModel

class QueryProductListResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.QueryProductListResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The HTTP status code returned.
        self.code = code
        # The information about all Alibaba Cloud services.
        self.data = data
        # The message returned.
        self.message = message
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request was successful.
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
            temp_model = main_models.QueryProductListResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class QueryProductListResponseBodyData(DaraModel):
    def __init__(
        self,
        page_num: int = None,
        page_size: int = None,
        product_list: main_models.QueryProductListResponseBodyDataProductList = None,
        total_count: int = None,
    ):
        # The page number of the returned page.
        self.page_num = page_num
        # The number of entries returned on each page.
        self.page_size = page_size
        # The service definitions.
        self.product_list = product_list
        # The total number of services.
        self.total_count = total_count

    def validate(self):
        if self.product_list:
            self.product_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_num is not None:
            result['PageNum'] = self.page_num

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.product_list is not None:
            result['ProductList'] = self.product_list.to_map()

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ProductList') is not None:
            temp_model = main_models.QueryProductListResponseBodyDataProductList()
            self.product_list = temp_model.from_map(m.get('ProductList'))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class QueryProductListResponseBodyDataProductList(DaraModel):
    def __init__(
        self,
        product: List[main_models.QueryProductListResponseBodyDataProductListProduct] = None,
    ):
        self.product = product

    def validate(self):
        if self.product:
            for v1 in self.product:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Product'] = []
        if self.product is not None:
            for k1 in self.product:
                result['Product'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.product = []
        if m.get('Product') is not None:
            for k1 in m.get('Product'):
                temp_model = main_models.QueryProductListResponseBodyDataProductListProduct()
                self.product.append(temp_model.from_map(k1))

        return self

class QueryProductListResponseBodyDataProductListProduct(DaraModel):
    def __init__(
        self,
        product_code: str = None,
        product_name: str = None,
        product_type: str = None,
        subscription_type: str = None,
    ):
        # The code of the service.
        self.product_code = product_code
        # The name of the service.
        self.product_name = product_name
        # The type of the service.
        self.product_type = product_type
        # The billing method. Valid values:
        # 
        # *   Subscription: subscription
        # *   PayAsYouGo: pay-as-you-go
        self.subscription_type = subscription_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.product_code is not None:
            result['ProductCode'] = self.product_code

        if self.product_name is not None:
            result['ProductName'] = self.product_name

        if self.product_type is not None:
            result['ProductType'] = self.product_type

        if self.subscription_type is not None:
            result['SubscriptionType'] = self.subscription_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')

        if m.get('ProductName') is not None:
            self.product_name = m.get('ProductName')

        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')

        if m.get('SubscriptionType') is not None:
            self.subscription_type = m.get('SubscriptionType')

        return self

