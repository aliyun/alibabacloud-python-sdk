# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RefreshContainerAssetsRequest(DaraModel):
    def __init__(
        self,
        asset_type: str = None,
    ):
        # The Asset Type of the container asset to refresh. Valid values:
        # - **IMAGE**: container image.
        # - **CONTAINER**: container.
        # 
        # This parameter is required.
        self.asset_type = asset_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.asset_type is not None:
            result['AssetType'] = self.asset_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssetType') is not None:
            self.asset_type = m.get('AssetType')

        return self

