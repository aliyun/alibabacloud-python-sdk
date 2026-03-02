# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RemoveAssetWatchRequest(DaraModel):
    def __init__(
        self,
        asset_type: str = None,
        company_id: int = None,
    ):
        # This parameter is required.
        self.asset_type = asset_type
        self.company_id = company_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.asset_type is not None:
            result['assetType'] = self.asset_type

        if self.company_id is not None:
            result['companyId'] = self.company_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('assetType') is not None:
            self.asset_type = m.get('assetType')

        if m.get('companyId') is not None:
            self.company_id = m.get('companyId')

        return self

