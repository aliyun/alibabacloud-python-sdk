# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ResetAppCodeRequest(DaraModel):
    def __init__(
        self,
        app_code: str = None,
        new_app_code: str = None,
        security_token: str = None,
    ):
        # The AppCode of the app.
        # 
        # This parameter is required.
        self.app_code = app_code
        # The new AppCode of the app.
        self.new_app_code = new_app_code
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_code is not None:
            result['AppCode'] = self.app_code

        if self.new_app_code is not None:
            result['NewAppCode'] = self.new_app_code

        if self.security_token is not None:
            result['SecurityToken'] = self.security_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')

        if m.get('NewAppCode') is not None:
            self.new_app_code = m.get('NewAppCode')

        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')

        return self

