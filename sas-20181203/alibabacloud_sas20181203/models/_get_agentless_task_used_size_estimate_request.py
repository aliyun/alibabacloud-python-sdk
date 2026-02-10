# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetAgentlessTaskUsedSizeEstimateRequest(DaraModel):
    def __init__(
        self,
        asset_selection_type: str = None,
    ):
        # Asset selection identifier.
        # 
        # This parameter is required.
        self.asset_selection_type = asset_selection_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.asset_selection_type is not None:
            result['AssetSelectionType'] = self.asset_selection_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssetSelectionType') is not None:
            self.asset_selection_type = m.get('AssetSelectionType')

        return self

