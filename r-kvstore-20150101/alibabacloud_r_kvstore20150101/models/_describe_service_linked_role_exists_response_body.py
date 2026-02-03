# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeServiceLinkedRoleExistsResponseBody(DaraModel):
    def __init__(
        self,
        exists_service_linked_role: bool = None,
        request_id: str = None,
    ):
        # Indicates whether the service-linked role is created for Tair (Redis OSS-compatible) in the current account. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.exists_service_linked_role = exists_service_linked_role
        # The unique ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.exists_service_linked_role is not None:
            result['ExistsServiceLinkedRole'] = self.exists_service_linked_role

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExistsServiceLinkedRole') is not None:
            self.exists_service_linked_role = m.get('ExistsServiceLinkedRole')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

