# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateSlrRoleResponseBody(DaraModel):
    def __init__(
        self,
        has_permission: bool = None,
        request_id: str = None,
    ):
        # Indicates whether the service-linked role was created. Valid values:
        # 
        # *   **true**: yes
        # *   **false**: no
        self.has_permission = has_permission
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.has_permission is not None:
            result['HasPermission'] = self.has_permission

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HasPermission') is not None:
            self.has_permission = m.get('HasPermission')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

