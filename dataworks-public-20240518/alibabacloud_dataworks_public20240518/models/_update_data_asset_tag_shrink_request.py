# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateDataAssetTagShrinkRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        key: str = None,
        managers_shrink: str = None,
        values_shrink: str = None,
    ):
        # The description of the tag.
        self.description = description
        # The tag key.
        # 
        # This parameter is required.
        self.key = key
        # The tag administrators.
        self.managers_shrink = managers_shrink
        # The tag values.
        self.values_shrink = values_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.key is not None:
            result['Key'] = self.key

        if self.managers_shrink is not None:
            result['Managers'] = self.managers_shrink

        if self.values_shrink is not None:
            result['Values'] = self.values_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Managers') is not None:
            self.managers_shrink = m.get('Managers')

        if m.get('Values') is not None:
            self.values_shrink = m.get('Values')

        return self

