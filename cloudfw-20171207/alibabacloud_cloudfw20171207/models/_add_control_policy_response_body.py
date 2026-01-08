# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AddControlPolicyResponseBody(DaraModel):
    def __init__(
        self,
        acl_uuid: str = None,
        request_id: str = None,
    ):
        # The ID of the access control policy that is created on the Internet firewall.
        self.acl_uuid = acl_uuid
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.acl_uuid is not None:
            result['AclUuid'] = self.acl_uuid

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AclUuid') is not None:
            self.acl_uuid = m.get('AclUuid')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

