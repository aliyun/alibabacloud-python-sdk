# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyComponentAssetRequest(DaraModel):
    def __init__(
        self,
        asset_config: str = None,
        lang: str = None,
    ):
        # The configuration of the asset. The value is a JSON object.
        # 
        # This parameter is required.
        self.asset_config = asset_config
        # The language of the content within the request and response.
        # 
        # *   **zh**: Chinese (default)
        # *   **en**: English
        self.lang = lang

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.asset_config is not None:
            result['AssetConfig'] = self.asset_config

        if self.lang is not None:
            result['Lang'] = self.lang

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssetConfig') is not None:
            self.asset_config = m.get('AssetConfig')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        return self

