# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CheckRdsCustomInitResponseBody(DaraModel):
    def __init__(
        self,
        has_service_linked_role: str = None,
        register_uid_success: bool = None,
        request_id: str = None,
        require_service_linked_role: str = None,
    ):
        self.has_service_linked_role = has_service_linked_role
        self.register_uid_success = register_uid_success
        self.request_id = request_id
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

        if self.register_uid_success is not None:
            result['RegisterUidSuccess'] = self.register_uid_success

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.require_service_linked_role is not None:
            result['RequireServiceLinkedRole'] = self.require_service_linked_role

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HasServiceLinkedRole') is not None:
            self.has_service_linked_role = m.get('HasServiceLinkedRole')

        if m.get('RegisterUidSuccess') is not None:
            self.register_uid_success = m.get('RegisterUidSuccess')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('RequireServiceLinkedRole') is not None:
            self.require_service_linked_role = m.get('RequireServiceLinkedRole')

        return self

