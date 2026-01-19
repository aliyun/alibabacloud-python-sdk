# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyBackendRequest(DaraModel):
    def __init__(
        self,
        backend_id: str = None,
        backend_name: str = None,
        backend_type: str = None,
        description: str = None,
        security_token: str = None,
    ):
        # This parameter is required.
        self.backend_id = backend_id
        # This parameter is required.
        self.backend_name = backend_name
        # This parameter is required.
        self.backend_type = backend_type
        self.description = description
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.backend_id is not None:
            result['BackendId'] = self.backend_id

        if self.backend_name is not None:
            result['BackendName'] = self.backend_name

        if self.backend_type is not None:
            result['BackendType'] = self.backend_type

        if self.description is not None:
            result['Description'] = self.description

        if self.security_token is not None:
            result['SecurityToken'] = self.security_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackendId') is not None:
            self.backend_id = m.get('BackendId')

        if m.get('BackendName') is not None:
            self.backend_name = m.get('BackendName')

        if m.get('BackendType') is not None:
            self.backend_type = m.get('BackendType')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')

        return self

