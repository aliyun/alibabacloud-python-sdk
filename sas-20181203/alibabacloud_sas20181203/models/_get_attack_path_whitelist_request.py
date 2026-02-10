# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetAttackPathWhitelistRequest(DaraModel):
    def __init__(
        self,
        attack_path_whitelist_id: str = None,
    ):
        # Attack path whitelist ID.
        # > You can call [ListAttackPathWhitelist](~~ListAttackPathWhitelist~~) to query the attack path whitelist ID.
        # 
        # This parameter is required.
        self.attack_path_whitelist_id = attack_path_whitelist_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.attack_path_whitelist_id is not None:
            result['AttackPathWhitelistId'] = self.attack_path_whitelist_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AttackPathWhitelistId') is not None:
            self.attack_path_whitelist_id = m.get('AttackPathWhitelistId')

        return self

