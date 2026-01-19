# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ResetAppSecretRequest(DaraModel):
    def __init__(
        self,
        app_key: str = None,
        new_app_key: str = None,
        new_app_secret: str = None,
        security_token: str = None,
    ):
        # The key of the application that is used to make an API call.
        # 
        # This parameter is required.
        self.app_key = app_key
        # The new AppKey that you set must be globally unique.
        self.new_app_key = new_app_key
        # The new key of the application. To improve compatibility, we recommend that you use other parameters.
        self.new_app_secret = new_app_secret
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_key is not None:
            result['AppKey'] = self.app_key

        if self.new_app_key is not None:
            result['NewAppKey'] = self.new_app_key

        if self.new_app_secret is not None:
            result['NewAppSecret'] = self.new_app_secret

        if self.security_token is not None:
            result['SecurityToken'] = self.security_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')

        if m.get('NewAppKey') is not None:
            self.new_app_key = m.get('NewAppKey')

        if m.get('NewAppSecret') is not None:
            self.new_app_secret = m.get('NewAppSecret')

        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')

        return self

