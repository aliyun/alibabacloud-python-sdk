# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_agentidentity20250901 import models as main_models
from darabonba.model import DaraModel

class UpdateLoginPreferenceRequest(DaraModel):
    def __init__(
        self,
        login_preference: main_models.UpdateLoginPreferenceRequestLoginPreference = None,
        user_pool_name: str = None,
    ):
        self.login_preference = login_preference
        self.user_pool_name = user_pool_name

    def validate(self):
        if self.login_preference:
            self.login_preference.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.login_preference is not None:
            result['LoginPreference'] = self.login_preference.to_map()

        if self.user_pool_name is not None:
            result['UserPoolName'] = self.user_pool_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LoginPreference') is not None:
            temp_model = main_models.UpdateLoginPreferenceRequestLoginPreference()
            self.login_preference = temp_model.from_map(m.get('LoginPreference'))

        if m.get('UserPoolName') is not None:
            self.user_pool_name = m.get('UserPoolName')

        return self

class UpdateLoginPreferenceRequestLoginPreference(DaraModel):
    def __init__(
        self,
        enable_password_login: bool = None,
    ):
        self.enable_password_login = enable_password_login

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enable_password_login is not None:
            result['EnablePasswordLogin'] = self.enable_password_login

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnablePasswordLogin') is not None:
            self.enable_password_login = m.get('EnablePasswordLogin')

        return self

