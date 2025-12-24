# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecd20200930 import models as main_models
from darabonba.model import DaraModel

class UnbindConfigGroupRequest(DaraModel):
    def __init__(
        self,
        region_id: str = None,
        resource_infos: List[main_models.UnbindConfigGroupRequestResourceInfos] = None,
        type: str = None,
    ):
        # The ID of the region. Set the value to `cn-shanghai`.
        self.region_id = region_id
        # The resources from which you want to unbind the configuration group.
        # 
        # This parameter is required.
        self.resource_infos = resource_infos
        # The type of the configuration group.
        # 
        # Valid value:
        # 
        # *   Timer: the scheduled task type.
        # 
        # This parameter is required.
        self.type = type

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
        if self.region_id is not None:
            result['RegionId'] = self.region_id

        result['ResourceInfos'] = []
        if self.resource_infos is not None:
            for k1 in self.resource_infos:
                result['ResourceInfos'].append(k1.to_map() if k1 else None)

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        self.resource_infos = []
        if m.get('ResourceInfos') is not None:
            for k1 in m.get('ResourceInfos'):
                temp_model = main_models.UnbindConfigGroupRequestResourceInfos()
                self.resource_infos.append(temp_model.from_map(k1))

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class UnbindConfigGroupRequestResourceInfos(DaraModel):
    def __init__(
        self,
        product_type: str = None,
        resource_id: str = None,
        resource_region_id: str = None,
        resource_type: str = None,
    ):
        # The service type of the resource.
        # 
        # Valid value:
        # 
        # *   CLOUD_DESKTOP: the cloud computer service.
        self.product_type = product_type
        # The ID of the resource.
        self.resource_id = resource_id
        # The region ID of the resource.
        self.resource_region_id = resource_region_id
        # The type of the resource.
        # 
        # Valid values:
        # 
        # *   RESOURCE_GROUP: the resource group.
        # *   CLOUD_DESKTOP: the cloud computer service.
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

