# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteDataAssetTagShrinkRequest(DaraModel):
    def __init__(
        self,
        key: str = None,
        values_shrink: str = None,
    ):
        # The tag key.
        # 
        # This parameter is required.
        self.key = key
        # The tag values.
        self.values_shrink = values_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.values_shrink is not None:
            result['Values'] = self.values_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Values') is not None:
            self.values_shrink = m.get('Values')

        return self

