# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ChangeResourceGroupRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        new_resource_group_id: str = None,
        region_id: str = None,
        resource_id: str = None,
        resource_type: str = None,
    ):
        # The client token that is used to ensure the idempotence of a request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The **ClientToken** value can contain only ASCII characters.
        # 
        # > If you do not specify this parameter, the system automatically uses the **RequestId** of the API request as the **ClientToken**. The **RequestId** may be different for each API request.
        self.client_token = client_token
        # The ID of the new resource group.
        # 
        # This parameter is required.
        self.new_resource_group_id = new_resource_group_id
        # The region ID of the Alibaba Cloud Global Accelerator (GA) instance. Set the value to **ap-southeast-1**.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The instance ID of the Global Accelerator resource for which you want to modify the resource group.
        # - If **ResourceType** is set to **accelerator**, set this parameter to the instance ID of a standard Global Accelerator instance.
        # - If **ResourceType** is set to **basicaccelerator**, set this parameter to the instance ID of a basic Global Accelerator instance.
        # - If **ResourceType** is set to **bandwidthpackage**, set this parameter to the ID of a bandwidth plan.
        # - If **ResourceType** is set to **acl**, set this parameter to the ID of an access control policy group.
        # 
        # This parameter is required.
        self.resource_id = resource_id
        # The type of the Global Accelerator resource for which you want to modify the resource group. Valid values:
        # - **accelerator**: a standard Alibaba Cloud Global Accelerator (GA) instance.
        # - **basicaccelerator**: a basic Alibaba Cloud Global Accelerator (GA) instance.
        # - **bandwidthpackage**: a bandwidth plan.
        # - **acl**: an access control policy group.
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
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

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
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('NewResourceGroupId') is not None:
            self.new_resource_group_id = m.get('NewResourceGroupId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        return self

