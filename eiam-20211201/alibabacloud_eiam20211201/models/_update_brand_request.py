# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateBrandRequest(DaraModel):
    def __init__(
        self,
        brand_id: str = None,
        brand_name: str = None,
        instance_id: str = None,
    ):
        # 品牌化Id
        # 
        # This parameter is required.
        self.brand_id = brand_id
        # 品牌名称
        # 
        # This parameter is required.
        self.brand_name = brand_name
        # IDaaS EIAM实例的ID。
        # 
        # This parameter is required.
        self.instance_id = instance_id

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

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BrandId') is not None:
            self.brand_id = m.get('BrandId')

        if m.get('BrandName') is not None:
            self.brand_name = m.get('BrandName')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        return self

