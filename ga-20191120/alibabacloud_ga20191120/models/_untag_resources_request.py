# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class UntagResourcesRequest(DaraModel):
    def __init__(
        self,
        all: bool = None,
        client_token: str = None,
        region_id: str = None,
        resource_id: List[str] = None,
        resource_type: str = None,
        tag_key: List[str] = None,
    ):
        # Specifies whether to remove all tags of the specified resource. Valid values:
        # 
        # *   **true**: yes
        # *   **false** (default): no
        self.all = all
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters.
        # 
        # >  If you do not specify this parameter, the system automatically uses the **request ID** as the **client token**. The **request ID** may be different for each request.
        self.client_token = client_token
        # The ID of the region where the GA instance is deployed. Set the value to **cn-hangzhou**.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The IDs of the resources whose tags you want to remove.
        # 
        # *   If you set **ResourceType** to **accelerator**, set the value of ResourceId to the ID of a standard GA instance.
        # *   If you set **ResourceType** to **basicaccelerator**, set the value of ResourceId to the ID of a basic GA instance.
        # *   If you set **ResourceType** to **bandwidthpackage**, set the value of ResourceId to the ID of a bandwidth plan.
        # *   If you set **ResourceType** to **acl**, set the value of ResourceId to the ID of an ACL.
        # *   If you set **ResourceType** to **endpointgroup**, set the value of ResourceId to the ID of an endpoint group.
        # 
        # You can specify up to 50 GA resource IDs.
        # 
        # This parameter is required.
        self.resource_id = resource_id
        # The type of the resource whose tags you want to remove. Valid values:
        # 
        # *   **accelerator**: a standard GA instance
        # *   **basicaccelerator**: a basic GA instance
        # *   **bandwidthpackage**: a bandwidth plan
        # *   **acl**: an access control list (ACL).
        # *   **endpointgroup**: an endpoint group
        # 
        # This parameter is required.
        self.resource_type = resource_type
        # The key of the tag to be removed.
        # 
        # The system removes all tags with this tag key.
        # 
        # You can specify up to 20 tag keys.
        # 
        # >  If the **All** parameter is set to **true**, this parameter does not take effect.
        self.tag_key = tag_key

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.all is not None:
            result['All'] = self.all

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.tag_key is not None:
            result['TagKey'] = self.tag_key

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('All') is not None:
            self.all = m.get('All')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')

        return self

