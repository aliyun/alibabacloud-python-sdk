# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteComponentAssetRequest(DaraModel):
    def __init__(
        self,
        asset_id: int = None,
        lang: str = None,
    ):
        # The ID of the asset.
        # 
        # >  You can call the [DescribeComponentAssets](~~DescribeComponentAssets~~) operation to query the ID.
        # 
        # This parameter is required.
        self.asset_id = asset_id
        # The language of the content within the request and the response. Valid values:
        # 
        # *   **zh** (default): Chinese
        # *   **en**: English
        self.lang = lang

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.asset_id is not None:
            result['AssetId'] = self.asset_id

        if self.lang is not None:
            result['Lang'] = self.lang

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssetId') is not None:
            self.asset_id = m.get('AssetId')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        return self

