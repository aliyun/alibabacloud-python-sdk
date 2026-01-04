# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_eiam20211201 import models as main_models
from darabonba.model import DaraModel

class GetBrandResponseBody(DaraModel):
    def __init__(
        self,
        brand: main_models.GetBrandResponseBodyBrand = None,
        request_id: str = None,
    ):
        self.brand = brand
        self.request_id = request_id

    def validate(self):
        if self.brand:
            self.brand.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.brand is not None:
            result['Brand'] = self.brand.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Brand') is not None:
            temp_model = main_models.GetBrandResponseBodyBrand()
            self.brand = temp_model.from_map(m.get('Brand'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetBrandResponseBodyBrand(DaraModel):
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

