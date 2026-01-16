# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateAdminPasswordRequest(DaraModel):
    def __init__(
        self,
        es_admin_password: str = None,
        client_token: str = None,
    ):
        self.es_admin_password = es_admin_password
        # Indicates whether the password was updated. Valid values:
        # 
        # *   true: The call was successful.
        # *   false: The call failed.
        self.client_token = client_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.es_admin_password is not None:
            result['esAdminPassword'] = self.es_admin_password

        if self.client_token is not None:
            result['clientToken'] = self.client_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('esAdminPassword') is not None:
            self.es_admin_password = m.get('esAdminPassword')

        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')

        return self

