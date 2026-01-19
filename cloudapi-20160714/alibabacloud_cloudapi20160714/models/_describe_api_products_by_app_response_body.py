# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudapi20160714 import models as main_models
from darabonba.model import DaraModel

class DescribeApiProductsByAppResponseBody(DaraModel):
    def __init__(
        self,
        api_product_info_list: main_models.DescribeApiProductsByAppResponseBodyApiProductInfoList = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The information about API products.
        self.api_product_info_list = api_product_info_list
        # The page number. Default value: 1.
        self.page_number = page_number
        # The number of entries per page. Default value: 10.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of returned entries.
        self.total_count = total_count

    def validate(self):
        if self.api_product_info_list:
            self.api_product_info_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_product_info_list is not None:
            result['ApiProductInfoList'] = self.api_product_info_list.to_map()

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiProductInfoList') is not None:
            temp_model = main_models.DescribeApiProductsByAppResponseBodyApiProductInfoList()
            self.api_product_info_list = temp_model.from_map(m.get('ApiProductInfoList'))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeApiProductsByAppResponseBodyApiProductInfoList(DaraModel):
    def __init__(
        self,
        api_product_info: List[main_models.DescribeApiProductsByAppResponseBodyApiProductInfoListApiProductInfo] = None,
    ):
        self.api_product_info = api_product_info

    def validate(self):
        if self.api_product_info:
            for v1 in self.api_product_info:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ApiProductInfo'] = []
        if self.api_product_info is not None:
            for k1 in self.api_product_info:
                result['ApiProductInfo'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.api_product_info = []
        if m.get('ApiProductInfo') is not None:
            for k1 in m.get('ApiProductInfo'):
                temp_model = main_models.DescribeApiProductsByAppResponseBodyApiProductInfoListApiProductInfo()
                self.api_product_info.append(temp_model.from_map(k1))

        return self

class DescribeApiProductsByAppResponseBodyApiProductInfoListApiProductInfo(DaraModel):
    def __init__(
        self,
        api_product_id: str = None,
    ):
        # The ID of the API product.
        self.api_product_id = api_product_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_product_id is not None:
            result['ApiProductId'] = self.api_product_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiProductId') is not None:
            self.api_product_id = m.get('ApiProductId')

        return self

