# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecs20140526 import models as main_models
from darabonba.model import DaraModel

class DescribeImageComponentsRequest(DaraModel):
    def __init__(
        self,
        component_type: str = None,
        component_version: str = None,
        image_component_id: List[str] = None,
        max_results: int = None,
        name: str = None,
        next_token: str = None,
        owner: str = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_group_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        system_type: str = None,
        tag: List[main_models.DescribeImageComponentsRequestTag] = None,
    ):
        # The type of the image component.
        # 
        # Valid values:
        # 
        # *   Build
        # *   Test
        self.component_type = component_type
        # The version number of the image component in the \\<major>.\\<minor>.\\<patch> format. You can set \\<major>, \\<minor>, and \\<patch> to non-negative integers, or set one of \\<major>, \\<minor>, and \\<patch> to the wildcard (\\*) and the other two to non-negative integers.
        # 
        # >  This parameter takes effect only if you specify Name.
        self.component_version = component_version
        # The IDs of image components. Valid values of N: 1 to 20.
        self.image_component_id = image_component_id
        # The maximum number of entries per page. Valid values: 1 to 500.
        # 
        # Default value: 50.
        self.max_results = max_results
        # The name of the image component. You must specify an exact name to search for the image component.
        self.name = name
        # The pagination token that is used in the next request to retrieve a new page of results. You do not need to specify this parameter for the first request. You must specify the token that is obtained from the previous query as the value of `NextToken`.
        self.next_token = next_token
        # The type of the image component. Valid values:
        # 
        # *   SELF: the custom component that you created.
        # *   ALIYUN: the system component provided by Alibaba Cloud.
        self.owner = owner
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The region ID of the image component. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/25609.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the resource group. If this parameter is specified to query resources, up to 1,000 resources that belong to the specified resource group can be displayed in the response.
        # 
        # >  Resources in the default resource group are displayed in the response regardless of how this parameter is set.
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The type of the operating system supported by the image component.
        # 
        # Valid values:
        # 
        # *   Linux
        # *   Windows
        self.system_type = system_type
        # The tags of the image component.
        self.tag = tag

    def validate(self):
        if self.tag:
            for v1 in self.tag:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.component_type is not None:
            result['ComponentType'] = self.component_type

        if self.component_version is not None:
            result['ComponentVersion'] = self.component_version

        if self.image_component_id is not None:
            result['ImageComponentId'] = self.image_component_id

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.name is not None:
            result['Name'] = self.name

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.owner is not None:
            result['Owner'] = self.owner

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.system_type is not None:
            result['SystemType'] = self.system_type

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComponentType') is not None:
            self.component_type = m.get('ComponentType')

        if m.get('ComponentVersion') is not None:
            self.component_version = m.get('ComponentVersion')

        if m.get('ImageComponentId') is not None:
            self.image_component_id = m.get('ImageComponentId')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('Owner') is not None:
            self.owner = m.get('Owner')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('SystemType') is not None:
            self.system_type = m.get('SystemType')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.DescribeImageComponentsRequestTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class DescribeImageComponentsRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of tag N. Valid values of N: 1 to 20.
        self.key = key
        # The value of tag N. Valid values of N: 1 to 20.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

