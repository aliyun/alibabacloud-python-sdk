# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListUserAuthorizedResourcesRequest(DaraModel):
    def __init__(
        self,
        next_token: str = None,
        permission_code: str = None,
        resource_type: str = None,
    ):
        self.next_token = next_token
        self.permission_code = permission_code
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.permission_code is not None:
            result['PermissionCode'] = self.permission_code

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('PermissionCode') is not None:
            self.permission_code = m.get('PermissionCode')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        return self

