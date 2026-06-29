# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class BatchRevokeSeatsShrinkRequest(DaraModel):
    def __init__(
        self,
        items_shrink: str = None,
        locale: str = None,
    ):
        # The list of revocation items. This parameter is required.
        self.items_shrink = items_shrink
        # The language. Valid values: zh-CN and en-US.
        self.locale = locale

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.items_shrink is not None:
            result['Items'] = self.items_shrink

        if self.locale is not None:
            result['Locale'] = self.locale

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Items') is not None:
            self.items_shrink = m.get('Items')

        if m.get('Locale') is not None:
            self.locale = m.get('Locale')

        return self

