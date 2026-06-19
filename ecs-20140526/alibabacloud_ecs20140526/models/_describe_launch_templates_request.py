# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecs20140526 import models as main_models
from darabonba.model import DaraModel

class DescribeLaunchTemplatesRequest(DaraModel):
    def __init__(
        self,
        launch_template_id: List[str] = None,
        launch_template_name: List[str] = None,
        owner_account: str = None,
        owner_id: int = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        template_resource_group_id: str = None,
        template_tag: List[main_models.DescribeLaunchTemplatesRequestTemplateTag] = None,
    ):
        # An array of one or more launch template IDs.
        # 
        # - You can query up to 100 launch templates at a time.
        # 
        # - You must specify LaunchTemplateId or LaunchTemplateName to determine the templates.
        self.launch_template_id = launch_template_id
        # An array of one or more launch template names.
        # 
        # - You can query up to 100 launch templates at a time.
        # 
        # - You must specify LaunchTemplateId or LaunchTemplateName to determine the templates.
        self.launch_template_name = launch_template_name
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The page number of the launch template list. Minimum value: 1.
        # 
        # Default value: 1.
        self.page_number = page_number
        # The number of entries per page for a paginated query.
        # 
        # Default value: 10.
        self.page_size = page_size
        # The region ID. You can call [DescribeRegions](https://help.aliyun.com/document_detail/25609.html) to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The ID of the resource group to which the launch template belongs. When you use this parameter to filter resources, the number of resources cannot exceed 1000.
        # 
        # > Filtering by the default resource group is not supported.
        self.template_resource_group_id = template_resource_group_id
        # The list of tag key-value pairs of the launch template.
        # > Currently, you can create and query launch template tags only by calling API operations. The console does not support creating or viewing launch template tags.
        self.template_tag = template_tag

    def validate(self):
        if self.template_tag:
            for v1 in self.template_tag:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.launch_template_id is not None:
            result['LaunchTemplateId'] = self.launch_template_id

        if self.launch_template_name is not None:
            result['LaunchTemplateName'] = self.launch_template_name

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.template_resource_group_id is not None:
            result['TemplateResourceGroupId'] = self.template_resource_group_id

        result['TemplateTag'] = []
        if self.template_tag is not None:
            for k1 in self.template_tag:
                result['TemplateTag'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LaunchTemplateId') is not None:
            self.launch_template_id = m.get('LaunchTemplateId')

        if m.get('LaunchTemplateName') is not None:
            self.launch_template_name = m.get('LaunchTemplateName')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('TemplateResourceGroupId') is not None:
            self.template_resource_group_id = m.get('TemplateResourceGroupId')

        self.template_tag = []
        if m.get('TemplateTag') is not None:
            for k1 in m.get('TemplateTag'):
                temp_model = main_models.DescribeLaunchTemplatesRequestTemplateTag()
                self.template_tag.append(temp_model.from_map(k1))

        return self

class DescribeLaunchTemplatesRequestTemplateTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key of the launch template. Valid values of N: 1 to 20.
        # 
        # If you use a single tag to filter resources, the number of resources with the specified tag cannot exceed 1000. If you use multiple tags to filter resources, the number of resources that are bound with all the specified tags cannot exceed 1000. If the number of resources exceeds 1000, call the [ListTagResources](https://help.aliyun.com/document_detail/110425.html) operation to query them.
        self.key = key
        # The tag value of the launch template. Valid values of N: 1 to 20.
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

