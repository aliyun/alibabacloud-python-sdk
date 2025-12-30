# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetVodPackagingAssetRequest(DaraModel):
    def __init__(
        self,
        asset_name: str = None,
    ):
        # The name of the VOD packaging asset.
        self.asset_name = asset_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.asset_name is not None:
            result['AssetName'] = self.asset_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssetName') is not None:
            self.asset_name = m.get('AssetName')

        return self

