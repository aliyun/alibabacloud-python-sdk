# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class TagResourcesRequest(DaraModel):
    def __init__(
        self,
        resource_ids: str = None,
        resource_region_id: str = None,
        resource_type: str = None,
        tags: str = None,
    ):
        # The IDs of the resources. You can specify up to 20 IDs in the format of a JSON array.
        # 
        # This parameter is required.
        self.resource_ids = resource_ids
        # The region in which the resource resides.
        # 
        # This parameter is required.
        self.resource_region_id = resource_region_id
        # The type of the resource. Valid values:
        # 
        # - **application**: Enterprise Distributed Application Service (EDAS) application
        # 
        # - **cluster**: EDAS cluster
        # 
        # This parameter is required.
        self.resource_type = resource_type
        # The key-value pairs. When you set this parameter, take note of the following limits:
        # 
        # - You can add up to 20 tags to a resource.
        # 
        # - The tag key cannot start with **aliyun** or **acs:**. It cannot contain **http\\://** or **https\\://**.
        # 
        # - The tag key or tag value can be up to 128 characters in length, and can contain letters, digits, hyphens (-), commas (,), asterisks (\\*), forward slashes (/), question marks (?), and colons (:).
        # 
        # - Set this parameter to a JSON array.
        # 
        # This parameter is required.
        self.tags = tags

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.resource_ids is not None:
            result['ResourceIds'] = self.resource_ids

        if self.resource_region_id is not None:
            result['ResourceRegionId'] = self.resource_region_id

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.tags is not None:
            result['Tags'] = self.tags

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceIds') is not None:
            self.resource_ids = m.get('ResourceIds')

        if m.get('ResourceRegionId') is not None:
            self.resource_region_id = m.get('ResourceRegionId')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('Tags') is not None:
            self.tags = m.get('Tags')

        return self

