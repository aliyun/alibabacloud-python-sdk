# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ValidateUserTokenRequest(DaraModel):
    def __init__(
        self,
        auth_message: str = None,
        auth_type: str = None,
        dbcluster_id: str = None,
    ):
        # This parameter is required.
        self.auth_message = auth_message
        # This parameter is required.
        self.auth_type = auth_type
        # This parameter is required.
        self.dbcluster_id = dbcluster_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auth_message is not None:
            result['AuthMessage'] = self.auth_message

        if self.auth_type is not None:
            result['AuthType'] = self.auth_type

        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthMessage') is not None:
            self.auth_message = m.get('AuthMessage')

        if m.get('AuthType') is not None:
            self.auth_type = m.get('AuthType')

        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        return self

