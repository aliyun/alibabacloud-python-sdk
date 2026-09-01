# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ChangeCheckScopeConfigInstanceRequest(DaraModel):
    def __init__(
        self,
        add_asset_uuids: List[str] = None,
        config_id: str = None,
        delete_asset_uuids: List[str] = None,
    ):
        # The list of unique IDs of cloud assets to add.
        self.add_asset_uuids = add_asset_uuids
        # The ID of the scan scope configuration.
        # >Call the [GetCheckScopeConfig](~~GetCheckScopeConfig~~) operation to obtain this parameter.
        # 
        # This parameter is required.
        self.config_id = config_id
        # The list of unique IDs of cloud assets to delete.
        self.delete_asset_uuids = delete_asset_uuids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.add_asset_uuids is not None:
            result['AddAssetUuids'] = self.add_asset_uuids

        if self.config_id is not None:
            result['ConfigId'] = self.config_id

        if self.delete_asset_uuids is not None:
            result['DeleteAssetUuids'] = self.delete_asset_uuids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddAssetUuids') is not None:
            self.add_asset_uuids = m.get('AddAssetUuids')

        if m.get('ConfigId') is not None:
            self.config_id = m.get('ConfigId')

        if m.get('DeleteAssetUuids') is not None:
            self.delete_asset_uuids = m.get('DeleteAssetUuids')

        return self

