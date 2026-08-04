# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AuthLoginTicketRequest(DaraModel):
    def __init__(
        self,
        app_name: str = None,
        auth_code: str = None,
        minor_auth_code: str = None,
        scene: str = None,
    ):
        # This parameter is required.
        self.app_name = app_name
        # This parameter is required.
        self.auth_code = auth_code
        # This parameter is required.
        self.minor_auth_code = minor_auth_code
        # This parameter is required.
        self.scene = scene

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.auth_code is not None:
            result['AuthCode'] = self.auth_code

        if self.minor_auth_code is not None:
            result['MinorAuthCode'] = self.minor_auth_code

        if self.scene is not None:
            result['Scene'] = self.scene

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('AuthCode') is not None:
            self.auth_code = m.get('AuthCode')

        if m.get('MinorAuthCode') is not None:
            self.minor_auth_code = m.get('MinorAuthCode')

        if m.get('Scene') is not None:
            self.scene = m.get('Scene')

        return self

