# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RevokeTablePermissionResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        revoke_success: bool = None,
    ):
        # The request ID.
        self.request_id = request_id
        # Indicates whether the permissions are revoked.
        self.revoke_success = revoke_success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.revoke_success is not None:
            result['RevokeSuccess'] = self.revoke_success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('RevokeSuccess') is not None:
            self.revoke_success = m.get('RevokeSuccess')

        return self

