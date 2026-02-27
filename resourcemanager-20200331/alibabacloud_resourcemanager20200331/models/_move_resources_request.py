# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_resourcemanager20200331 import models as main_models
from darabonba.model import DaraModel

class MoveResourcesRequest(DaraModel):
    def __init__(
        self,
        resource_group_id: str = None,
        resources: List[main_models.MoveResourcesRequestResources] = None,
    ):
        # The ID of the resource group to which you want to move the resources.
        # 
        # This parameter is required.
        self.resource_group_id = resource_group_id
        # The resources that you want to move.
        # 
        # >  You can move a maximum of 10 resources at a time. If you want to move more than 10 resources, move them in batches.
        # 
        # This parameter is required.
        self.resources = resources

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
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        result['Resources'] = []
        if self.resources is not None:
            for k1 in self.resources:
                result['Resources'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        self.resources = []
        if m.get('Resources') is not None:
            for k1 in m.get('Resources'):
                temp_model = main_models.MoveResourcesRequestResources()
                self.resources.append(temp_model.from_map(k1))

        return self

class MoveResourcesRequestResources(DaraModel):
    def __init__(
        self,
        region_id: str = None,
        resource_id: str = None,
        resource_type: str = None,
        service: str = None,
    ):
        # The region ID of the resource.
        self.region_id = region_id
        # The ID of the resource.
        self.resource_id = resource_id
        # The type of the resource.
        self.resource_type = resource_type
        # The ID of the Alibaba Cloud service to which the resource belongs.
        self.service = service

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

        if self.service is not None:
            result['Service'] = self.service

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('Service') is not None:
            self.service = m.get('Service')

        return self

