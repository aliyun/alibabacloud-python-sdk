# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteAttackPathSensitiveAssetConfigRequest(DaraModel):
    def __init__(
        self,
        attack_path_sensitive_asset_config_id: str = None,
    ):
        # ID of the attack path sensitive asset configuration.
        # 
        # This parameter is required.
        self.attack_path_sensitive_asset_config_id = attack_path_sensitive_asset_config_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.attack_path_sensitive_asset_config_id is not None:
            result['AttackPathSensitiveAssetConfigId'] = self.attack_path_sensitive_asset_config_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AttackPathSensitiveAssetConfigId') is not None:
            self.attack_path_sensitive_asset_config_id = m.get('AttackPathSensitiveAssetConfigId')

        return self

