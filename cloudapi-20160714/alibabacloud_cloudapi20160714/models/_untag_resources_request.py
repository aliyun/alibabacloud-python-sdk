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
        resource_type: str = None,
        security_token: str = None,
        tag_key: List[str] = None,
    ):
        # Specifies whether to delete all tags. This parameter is valid only when the **TagKey.N**parameter is not specified. Default value: false. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.all = all
        # The resource IDs.
        # 
        # This parameter is required.
        self.resource_id = resource_id
        # The type of the resource. Tags are bound to API groups, plug-ins, and applications. You can use tags to manage cloud resources by group. Valid values:
        # 
        # *   **apiGroup**
        # *   **plugin**
        # *   **app**
        # 
        # This parameter is required.
        self.resource_type = resource_type
        # The security token included in the WebSocket request header. The system uses this token to authenticate the request.
        self.security_token = security_token
        # The tag keys of the resource.
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

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.security_token is not None:
            result['SecurityToken'] = self.security_token

        if self.tag_key is not None:
            result['TagKey'] = self.tag_key

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('All') is not None:
            self.all = m.get('All')

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')

        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')

        return self

