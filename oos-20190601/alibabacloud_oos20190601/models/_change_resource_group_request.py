# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ChangeResourceGroupRequest(DaraModel):
    def __init__(
        self,
        new_resource_group_id: str = None,
        region_id: str = None,
        resource_id: str = None,
        resource_type: str = None,
    ):
        # The ID of the resource group to which the cloud resource is to be moved. You can use resource groups to manage resources owned by your Alibaba Cloud account. Resource groups simplify the resource and permission management of your Alibaba Cloud account. For more information, see [What is Resource Management?](https://help.aliyun.com/document_detail/94475.html)
        # 
        # This parameter is required.
        self.new_resource_group_id = new_resource_group_id
        # The ID of the region.
        self.region_id = region_id
        # The ID of the cloud resource that you want to move to another resource group.
        # 
        # *   If the ResourceType parameter is set to template, set the ResourceId parameter to the name of the template.
        # *   If the ResourceType parameter is set to parameter, set the ResourceId parameter to the name of the parameter.
        # *   If the ResourceType parameter is set to secretparameter, set the ResourceId parameter to the name of the encryption parameter.
        # *   If the ResourceType parameter is set to stateconfiguration, set the ResourceId parameter to the ID of the desired-state configuration.
        # *   If the ResourceType parameter is set to application, set the ResourceId parameter to the name of the application.
        # 
        # This parameter is required.
        self.resource_id = resource_id
        # The type of the cloud resource. Valid values:
        # 
        # *   template: template
        # *   parameter: parameter
        # *   secretparameter: encryption parameter
        # *   stateconfiguration: desired-state configuration
        # *   application: application
        # 
        # This parameter is required.
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.new_resource_group_id is not None:
            result['NewResourceGroupId'] = self.new_resource_group_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NewResourceGroupId') is not None:
            self.new_resource_group_id = m.get('NewResourceGroupId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        return self

