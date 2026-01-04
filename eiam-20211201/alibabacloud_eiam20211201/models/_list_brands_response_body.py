# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eiam20211201 import models as main_models
from darabonba.model import DaraModel

class ListBrandsResponseBody(DaraModel):
    def __init__(
        self,
        brands: List[main_models.ListBrandsResponseBodyBrands] = None,
        max_results: int = None,
        next_token: str = None,
        previous_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.brands = brands
        # 分页查询时每页行数。
        self.max_results = max_results
        # 本次调用返回的查询凭证（Token）值，用于下一次翻页查询。
        self.next_token = next_token
        # 本次调用返回的查询凭证（Token）值，用于上一次翻页查询。
        self.previous_token = previous_token
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.brands:
            for v1 in self.brands:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Brands'] = []
        if self.brands is not None:
            for k1 in self.brands:
                result['Brands'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.previous_token is not None:
            result['PreviousToken'] = self.previous_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.brands = []
        if m.get('Brands') is not None:
            for k1 in m.get('Brands'):
                temp_model = main_models.ListBrandsResponseBodyBrands()
                self.brands.append(temp_model.from_map(k1))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('PreviousToken') is not None:
            self.previous_token = m.get('PreviousToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListBrandsResponseBodyBrands(DaraModel):
    def __init__(
        self,
        brand_id: str = None,
        brand_name: str = None,
        brand_type: str = None,
        instance_id: str = None,
        status: str = None,
    ):
        # 品牌ID
        self.brand_id = brand_id
        # 品牌名称
        self.brand_name = brand_name
        # 品牌类型
        self.brand_type = brand_type
        # 实例ID。
        self.instance_id = instance_id
        # 品牌状态
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.brand_id is not None:
            result['BrandId'] = self.brand_id

        if self.brand_name is not None:
            result['BrandName'] = self.brand_name

        if self.brand_type is not None:
            result['BrandType'] = self.brand_type

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BrandId') is not None:
            self.brand_id = m.get('BrandId')

        if m.get('BrandName') is not None:
            self.brand_name = m.get('BrandName')

        if m.get('BrandType') is not None:
            self.brand_type = m.get('BrandType')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

