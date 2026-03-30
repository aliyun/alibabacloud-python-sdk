# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class UntagResourcesRequest(DaraModel):
    def __init__(
        self,
        all: bool = None,
        resource_id: List[str] = None,
        resource_principal_name: List[str] = None,
        resource_type: str = None,
        tag_key: List[str] = None,
    ):
        # Specifies whether to remove all tags from the resource. Valid values:
        # 
        # *   true: remove all tags from the resources.
        # *   false (default): does not remove all tags from the resources.
        # 
        # > This parameter takes effect only when TagKey.N is not set in the request.
        self.all = all
        # The IDs of resources.
        # 
        # Valid values of N: 1 to 50. If the ResourceType parameter is set to user, the resource ID is the ID of the RAM user.
        # 
        # > You must specify only one of the following parameters: ResourceId and ResourcePrincipalName.
        self.resource_id = resource_id
        # The names of resources.
        # 
        # Valid values of N: 1 to 50. If the ResourceType parameter is set to user, the resource name is the name of the RAM user.
        # 
        # > You must specify only one of the following parameters: ResourceId and ResourcePrincipalName.
        self.resource_principal_name = resource_principal_name
        # The type of the resource. Valid value:
        # 
        # *   user: a RAM user
        self.resource_type = resource_type
        # The tag keys of resources.
        # 
        # Valid values of N: 1 to 20. N must be consecutive.
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

        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        if self.resource_principal_name is not None:
            result['ResourcePrincipalName'] = self.resource_principal_name

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.tag_key is not None:
            result['TagKey'] = self.tag_key

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('All') is not None:
            self.all = m.get('All')

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('ResourcePrincipalName') is not None:
            self.resource_principal_name = m.get('ResourcePrincipalName')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')

        return self

