# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateResourceServerScopeResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        resource_server_scope_id: str = None,
    ):
        self.request_id = request_id
        self.resource_server_scope_id = resource_server_scope_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.resource_server_scope_id is not None:
            result['ResourceServerScopeId'] = self.resource_server_scope_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResourceServerScopeId') is not None:
            self.resource_server_scope_id = m.get('ResourceServerScopeId')

        return self

