# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ValidateSlrPermissionRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        rolename: str = None,
    ):
        self.client_token = client_token
        # This parameter is required.
        self.rolename = rolename

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.rolename is not None:
            result['rolename'] = self.rolename

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('rolename') is not None:
            self.rolename = m.get('rolename')

        return self

