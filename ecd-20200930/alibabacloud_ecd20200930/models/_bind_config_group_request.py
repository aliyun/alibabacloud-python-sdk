# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecd20200930 import models as main_models
from darabonba.model import DaraModel

class BindConfigGroupRequest(DaraModel):
    def __init__(
        self,
        group_id: str = None,
        region_id: str = None,
        resource_infos: List[main_models.BindConfigGroupRequestResourceInfos] = None,
    ):
        # The configuration group ID.
        # 
        # This parameter is required.
        self.group_id = group_id
        # The region ID. This operation is not region-specific. Set this parameter to `cn-shanghai`.
        self.region_id = region_id
        # The resource information to associate.
        # 
        # This parameter is required.
        self.resource_infos = resource_infos

    def validate(self):
        if self.resource_infos:
            for v1 in self.resource_infos:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        result['ResourceInfos'] = []
        if self.resource_infos is not None:
            for k1 in self.resource_infos:
                result['ResourceInfos'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        self.resource_infos = []
        if m.get('ResourceInfos') is not None:
            for k1 in m.get('ResourceInfos'):
                temp_model = main_models.BindConfigGroupRequestResourceInfos()
                self.resource_infos.append(temp_model.from_map(k1))

        return self

class BindConfigGroupRequestResourceInfos(DaraModel):
    def __init__(
        self,
        product_type: str = None,
        resource_id: str = None,
        resource_region_id: str = None,
        resource_type: str = None,
    ):
        # The product type to which the resource belongs.
        self.product_type = product_type
        # The resource ID.
        self.resource_id = resource_id
        # The region where the resource resides.
        self.resource_region_id = resource_region_id
        # The resource type.
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.product_type is not None:
            result['ProductType'] = self.product_type

        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        if self.resource_region_id is not None:
            result['ResourceRegionId'] = self.resource_region_id

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('ResourceRegionId') is not None:
            self.resource_region_id = m.get('ResourceRegionId')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        return self

