# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetAttackPathSensitiveAssetConfigRequest(DaraModel):
    def __init__(
        self,
        attack_path_sensitive_asset_config_id: str = None,
        config_type: str = None,
    ):
        # ID of the created attack path sensitive asset setting.
        self.attack_path_sensitive_asset_config_id = attack_path_sensitive_asset_config_id
        # Configuration type. Possible values:
        # - asset_instance: Asset.
        # 
        # This parameter is required.
        self.config_type = config_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.attack_path_sensitive_asset_config_id is not None:
            result['AttackPathSensitiveAssetConfigId'] = self.attack_path_sensitive_asset_config_id

        if self.config_type is not None:
            result['ConfigType'] = self.config_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AttackPathSensitiveAssetConfigId') is not None:
            self.attack_path_sensitive_asset_config_id = m.get('AttackPathSensitiveAssetConfigId')

        if m.get('ConfigType') is not None:
            self.config_type = m.get('ConfigType')

        return self

