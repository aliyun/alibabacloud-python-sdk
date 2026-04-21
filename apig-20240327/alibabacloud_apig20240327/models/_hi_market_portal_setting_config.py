# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class HiMarketPortalSettingConfig(DaraModel):
    def __init__(
        self,
        auto_approve_developers: bool = None,
        auto_approve_subscriptions: bool = None,
        builtin_auth_enabled: bool = None,
    ):
        self.auto_approve_developers = auto_approve_developers
        self.auto_approve_subscriptions = auto_approve_subscriptions
        self.builtin_auth_enabled = builtin_auth_enabled

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_approve_developers is not None:
            result['autoApproveDevelopers'] = self.auto_approve_developers

        if self.auto_approve_subscriptions is not None:
            result['autoApproveSubscriptions'] = self.auto_approve_subscriptions

        if self.builtin_auth_enabled is not None:
            result['builtinAuthEnabled'] = self.builtin_auth_enabled

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('autoApproveDevelopers') is not None:
            self.auto_approve_developers = m.get('autoApproveDevelopers')

        if m.get('autoApproveSubscriptions') is not None:
            self.auto_approve_subscriptions = m.get('autoApproveSubscriptions')

        if m.get('builtinAuthEnabled') is not None:
            self.builtin_auth_enabled = m.get('builtinAuthEnabled')

        return self

