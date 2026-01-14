# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetInstanceAclRequest(DaraModel):
    def __init__(
        self,
        resource_name: str = None,
        resource_type: str = None,
    ):
        # The name of the resource on which you want to grant permissions.
        # 
        # This parameter is required.
        self.resource_name = resource_name
        # The type of the resource on which you want to grant permissions.
        # 
        # Valid values:
        # 
        # *   Group
        # *   Topic
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
        if self.resource_name is not None:
            result['resourceName'] = self.resource_name

        if self.resource_type is not None:
            result['resourceType'] = self.resource_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('resourceName') is not None:
            self.resource_name = m.get('resourceName')

        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')

        return self

