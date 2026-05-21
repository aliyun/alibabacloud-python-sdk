# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateHoloWebLoginSettingRequest(DaraModel):
    def __init__(
        self,
        region_id: str = None,
        allow_external_accounts_login: bool = None,
    ):
        self.region_id = region_id
        self.allow_external_accounts_login = allow_external_accounts_login

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.allow_external_accounts_login is not None:
            result['allowExternalAccountsLogin'] = self.allow_external_accounts_login

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('allowExternalAccountsLogin') is not None:
            self.allow_external_accounts_login = m.get('allowExternalAccountsLogin')

        return self

