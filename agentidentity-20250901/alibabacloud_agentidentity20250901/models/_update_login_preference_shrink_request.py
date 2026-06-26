# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateLoginPreferenceShrinkRequest(DaraModel):
    def __init__(
        self,
        login_preference_shrink: str = None,
        user_pool_name: str = None,
    ):
        self.login_preference_shrink = login_preference_shrink
        self.user_pool_name = user_pool_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.login_preference_shrink is not None:
            result['LoginPreference'] = self.login_preference_shrink

        if self.user_pool_name is not None:
            result['UserPoolName'] = self.user_pool_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LoginPreference') is not None:
            self.login_preference_shrink = m.get('LoginPreference')

        if m.get('UserPoolName') is not None:
            self.user_pool_name = m.get('UserPoolName')

        return self

