# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eds_user20210308 import models as main_models
from darabonba.model import DaraModel

class TransferResourcesOutofGroupRequest(DaraModel):
    def __init__(
        self,
        business_channel: str = None,
        platform: str = None,
        resource_group_id: str = None,
        resources: List[main_models.TransferResourcesOutofGroupRequestResources] = None,
        target_resource_group_id: str = None,
    ):
        self.business_channel = business_channel
        self.platform = platform
        self.resource_group_id = resource_group_id
        self.resources = resources
        self.target_resource_group_id = target_resource_group_id

    def validate(self):
        if self.resources:
            for v1 in self.resources:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.business_channel is not None:
            result['BusinessChannel'] = self.business_channel

        if self.platform is not None:
            result['Platform'] = self.platform

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        result['Resources'] = []
        if self.resources is not None:
            for k1 in self.resources:
                result['Resources'].append(k1.to_map() if k1 else None)

        if self.target_resource_group_id is not None:
            result['TargetResourceGroupId'] = self.target_resource_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BusinessChannel') is not None:
            self.business_channel = m.get('BusinessChannel')

        if m.get('Platform') is not None:
            self.platform = m.get('Platform')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        self.resources = []
        if m.get('Resources') is not None:
            for k1 in m.get('Resources'):
                temp_model = main_models.TransferResourcesOutofGroupRequestResources()
                self.resources.append(temp_model.from_map(k1))

        if m.get('TargetResourceGroupId') is not None:
            self.target_resource_group_id = m.get('TargetResourceGroupId')

        return self

class TransferResourcesOutofGroupRequestResources(DaraModel):
    def __init__(
        self,
        region_id: str = None,
        resource_id: str = None,
        resource_type: str = None,
    ):
        self.region_id = region_id
        self.resource_id = resource_id
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        return self

