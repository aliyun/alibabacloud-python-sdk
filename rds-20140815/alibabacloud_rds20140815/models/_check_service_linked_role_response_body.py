# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CheckServiceLinkedRoleResponseBody(DaraModel):
    def __init__(
        self,
        has_service_linked_role: str = None,
        request_id: str = None,
        require_service_linked_role: str = None,
    ):
        # Indicates whether an SLR is created.
        self.has_service_linked_role = has_service_linked_role
        # The request ID.
        self.request_id = request_id
        # Indicates whether the service-linked role is required. Default value: true.
        self.require_service_linked_role = require_service_linked_role

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.has_service_linked_role is not None:
            result['HasServiceLinkedRole'] = self.has_service_linked_role

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.require_service_linked_role is not None:
            result['RequireServiceLinkedRole'] = self.require_service_linked_role

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HasServiceLinkedRole') is not None:
            self.has_service_linked_role = m.get('HasServiceLinkedRole')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('RequireServiceLinkedRole') is not None:
            self.require_service_linked_role = m.get('RequireServiceLinkedRole')

        return self

