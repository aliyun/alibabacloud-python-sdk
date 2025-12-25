# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_workorder20210610 import models as main_models
from darabonba.model import DaraModel

class ListProductsResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: List[main_models.ListProductsResponseBodyData] = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The return code of the request result.
        self.code = code
        # Return value, that is, product list
        self.data = data
        # The error message. If success is set to false, the message is returned.
        self.message = message
        # The unique ID of the API request. The requestID is unique for each call.
        self.request_id = request_id
        # Indicates whether the call is successful. A value of true indicates that the call is normal.
        self.success = success

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
        if self.code is not None:
            result['Code'] = self.code

        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

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

        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.ListProductsResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListProductsResponseBodyData(DaraModel):
    def __init__(
        self,
        directory_id: int = None,
        directory_name: str = None,
        product_list: List[main_models.ListProductsResponseBodyDataProductList] = None,
    ):
        # The ID of the product catalog, which represents the product category, such as elastic computing
        self.directory_id = directory_id
        # The name of the product catalog, which represents the product category, such as elastic computing
        self.directory_name = directory_name
        # List of Alibaba Cloud products
        self.product_list = product_list

    def validate(self):
        if self.product_list:
            for v1 in self.product_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id

        if self.directory_name is not None:
            result['DirectoryName'] = self.directory_name

        result['ProductList'] = []
        if self.product_list is not None:
            for k1 in self.product_list:
                result['ProductList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')

        if m.get('DirectoryName') is not None:
            self.directory_name = m.get('DirectoryName')

        self.product_list = []
        if m.get('ProductList') is not None:
            for k1 in m.get('ProductList'):
                temp_model = main_models.ListProductsResponseBodyDataProductList()
                self.product_list.append(temp_model.from_map(k1))

        return self

class ListProductsResponseBodyDataProductList(DaraModel):
    def __init__(
        self,
        product_id: int = None,
        product_name: str = None,
    ):
        # Alibaba Cloud product ID
        self.product_id = product_id
        # Alibaba Cloud product name
        self.product_name = product_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.product_id is not None:
            result['ProductId'] = self.product_id

        if self.product_name is not None:
            result['ProductName'] = self.product_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')

        if m.get('ProductName') is not None:
            self.product_name = m.get('ProductName')

        return self

