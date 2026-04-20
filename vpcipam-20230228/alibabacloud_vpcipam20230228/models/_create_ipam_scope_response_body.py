# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateIpamScopeResponseBody(DaraModel):
    def __init__(
        self,
        ipam_scope_id: str = None,
        request_id: str = None,
    ):
        # The ID of the IPAM scope.
        self.ipam_scope_id = ipam_scope_id
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ipam_scope_id is not None:
            result['IpamScopeId'] = self.ipam_scope_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IpamScopeId') is not None:
            self.ipam_scope_id = m.get('IpamScopeId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

