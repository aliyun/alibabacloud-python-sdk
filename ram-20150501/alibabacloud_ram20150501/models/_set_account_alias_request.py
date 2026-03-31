# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SetAccountAliasRequest(DaraModel):
    def __init__(
        self,
        account_alias: str = None,
    ):
        # The alias of the Alibaba Cloud account.
        # 
        # The alias must be 3 to 32 characters in length, and can contain lowercase letters, digits, and hyphens (-).
        # 
        # >  It cannot start or end with a hyphen (-), and cannot contain consecutive hyphens (-).
        self.account_alias = account_alias

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_alias is not None:
            result['AccountAlias'] = self.account_alias

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountAlias') is not None:
            self.account_alias = m.get('AccountAlias')

        return self

