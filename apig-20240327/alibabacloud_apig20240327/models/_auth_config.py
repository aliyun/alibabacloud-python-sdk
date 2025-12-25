# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AuthConfig(DaraModel):
    def __init__(
        self,
        auth_mode: str = None,
        auth_type: str = None,
    ):
        self.auth_mode = auth_mode
        self.auth_type = auth_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auth_mode is not None:
            result['authMode'] = self.auth_mode

        if self.auth_type is not None:
            result['authType'] = self.auth_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('authMode') is not None:
            self.auth_mode = m.get('authMode')

        if m.get('authType') is not None:
            self.auth_type = m.get('authType')

        return self

