# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class BatchCreateVodPackagingAssetShrinkRequest(DaraModel):
    def __init__(
        self,
        assets_shrink: str = None,
        group_name: str = None,
    ):
        # The assets that you want to ingest.
        self.assets_shrink = assets_shrink
        # The name of the packaging group.
        self.group_name = group_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.assets_shrink is not None:
            result['Assets'] = self.assets_shrink

        if self.group_name is not None:
            result['GroupName'] = self.group_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Assets') is not None:
            self.assets_shrink = m.get('Assets')

        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')

        return self

