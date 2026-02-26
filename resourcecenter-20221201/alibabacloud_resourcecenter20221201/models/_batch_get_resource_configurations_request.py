# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_resourcecenter20221201 import models as main_models
from darabonba.model import DaraModel

class BatchGetResourceConfigurationsRequest(DaraModel):
    def __init__(
        self,
        resources: List[main_models.BatchGetResourceConfigurationsRequestResources] = None,
    ):
        # The list of resources.
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
        result['Resources'] = []
        if self.resources is not None:
            for k1 in self.resources:
                result['Resources'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.resources = []
        if m.get('Resources') is not None:
            for k1 in m.get('Resources'):
                temp_model = main_models.BatchGetResourceConfigurationsRequestResources()
                self.resources.append(temp_model.from_map(k1))

        return self



class BatchGetResourceConfigurationsRequestResources(DaraModel):
    def __init__(
        self,
        region_id: str = None,
        resource_id: str = None,
        resource_type: str = None,
    ):
        # The region ID of the resource.
        self.region_id = region_id
        # The resource ID.
        self.resource_id = resource_id
        # The resource type.
        # 
        # For a list of resource types supported by Resource Center, see [Alibaba Cloud services and resource types that are supported by Resource Center](https://help.aliyun.com/document_detail/477798.html).
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

