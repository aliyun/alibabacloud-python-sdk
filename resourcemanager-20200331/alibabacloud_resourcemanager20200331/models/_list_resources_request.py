# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_resourcemanager20200331 import models as main_models
from darabonba.model import DaraModel

class ListResourcesRequest(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        region: str = None,
        resource_group_id: str = None,
        resource_id: str = None,
        resource_type: str = None,
        resource_types: List[main_models.ListResourcesRequestResourceTypes] = None,
        service: str = None,
    ):
        # The page number.
        # 
        # Pages start from page 1. Default value: 1.
        self.page_number = page_number
        # The number of entries per page.
        # 
        # Valid values: 1 to 100. Default value: 10.
        self.page_size = page_size
        # The region ID.
        self.region = region
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The ID of the resource.
        self.resource_id = resource_id
        # The resource type.
        # 
        # For more information about the supported resource types, see the **Resource type** column in [Services that work with Resource Group](https://help.aliyun.com/document_detail/94479.html).
        self.resource_type = resource_type
        # The resource types. A maximum of 50 resource types are supported.
        # 
        # >  If you configure `ResourceTypes`, you must configure both `Service` and `ResourceType`. Otherwise, the configured Service or ResourceType does not take effect.
        self.resource_types = resource_types
        # The ID of the Alibaba Cloud service.
        # 
        # You can obtain the ID from the **Service code** column in [Services that work with Resource Group](https://help.aliyun.com/document_detail/94479.html).
        self.service = service

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
        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region is not None:
            result['Region'] = self.region

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        result['ResourceTypes'] = []
        if self.resource_types is not None:
            for k1 in self.resource_types:
                result['ResourceTypes'].append(k1.to_map() if k1 else None)

        if self.service is not None:
            result['Service'] = self.service

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        self.resource_types = []
        if m.get('ResourceTypes') is not None:
            for k1 in m.get('ResourceTypes'):
                temp_model = main_models.ListResourcesRequestResourceTypes()
                self.resource_types.append(temp_model.from_map(k1))

        if m.get('Service') is not None:
            self.service = m.get('Service')

        return self

class ListResourcesRequestResourceTypes(DaraModel):
    def __init__(
        self,
        resource_type: str = None,
        service: str = None,
    ):
        # The resource type.
        # 
        # Valid values of N: 1 to 50.
        # 
        # For more information about the supported resource types, see the **Resource type** column in [Services that work with Resource Group](https://help.aliyun.com/document_detail/94479.html).
        # 
        # >  You must configure both `Service` and `ResourceType` in `ResourceTypes`. Otherwise, the two parameters do not take effect.
        self.resource_type = resource_type
        # The ID of the Alibaba Cloud service.
        # 
        # Valid values of N: 1 to 50.
        # 
        # You can obtain the ID from the **Service code** column in [Services that work with Resource Group](https://help.aliyun.com/document_detail/94479.html).
        # 
        # >  You must configure both `Service` and `ResourceType` in `ResourceTypes`. Otherwise, the two parameters do not take effect.
        self.service = service

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.service is not None:
            result['Service'] = self.service

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('Service') is not None:
            self.service = m.get('Service')

        return self

