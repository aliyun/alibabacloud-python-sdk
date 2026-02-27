# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_resourcemanager20200331 import models as main_models
from darabonba.model import DaraModel

class GetResourceGroupResourceCountsRequest(DaraModel):
    def __init__(
        self,
        group_by_key: str = None,
        resource_group_id: str = None,
        resource_region_id: str = None,
        resource_types: List[main_models.GetResourceGroupResourceCountsRequestResourceTypes] = None,
    ):
        # The dimension by which resources are queried.
        # 
        # > If you do not specify a dimension, no results are returned.
        # 
        # Valid values:
        # 
        # *   ResourceGroupId
        # *   ResourceType
        self.group_by_key = group_by_key
        # The resource group ID.
        # 
        # You can call the [ListResourceGroups](https://help.aliyun.com/document_detail/2716558.html) operation to obtain the ID.
        self.resource_group_id = resource_group_id
        # The region ID of the resources.
        self.resource_region_id = resource_region_id
        # The resource types.
        self.resource_types = resource_types

    def validate(self):
        if self.resource_types:
            for v1 in self.resource_types:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.group_by_key is not None:
            result['GroupByKey'] = self.group_by_key

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.resource_region_id is not None:
            result['ResourceRegionId'] = self.resource_region_id

        result['ResourceTypes'] = []
        if self.resource_types is not None:
            for k1 in self.resource_types:
                result['ResourceTypes'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupByKey') is not None:
            self.group_by_key = m.get('GroupByKey')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ResourceRegionId') is not None:
            self.resource_region_id = m.get('ResourceRegionId')

        self.resource_types = []
        if m.get('ResourceTypes') is not None:
            for k1 in m.get('ResourceTypes'):
                temp_model = main_models.GetResourceGroupResourceCountsRequestResourceTypes()
                self.resource_types.append(temp_model.from_map(k1))

        return self

class GetResourceGroupResourceCountsRequestResourceTypes(DaraModel):
    def __init__(
        self,
        resource_type_code: str = None,
        service: str = None,
    ):
        # The resource type.
        # 
        # You can obtain the resource type from the **Resource type** column in [Services that work with Resource Group](https://help.aliyun.com/document_detail/94479.html).
        self.resource_type_code = resource_type_code
        # The service code.
        # 
        # You can obtain the code from the **Service code** column in [Services that work with Resource Group](https://help.aliyun.com/document_detail/94479.html).
        self.service = service

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.resource_type_code is not None:
            result['ResourceTypeCode'] = self.resource_type_code

        if self.service is not None:
            result['Service'] = self.service

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceTypeCode') is not None:
            self.resource_type_code = m.get('ResourceTypeCode')

        if m.get('Service') is not None:
            self.service = m.get('Service')

        return self

