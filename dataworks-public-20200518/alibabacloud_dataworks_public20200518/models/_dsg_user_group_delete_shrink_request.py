# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DsgUserGroupDeleteShrinkRequest(DaraModel):
    def __init__(
        self,
        ids_shrink: str = None,
    ):
        # The information about the user group.
        self.ids_shrink = ids_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ids_shrink is not None:
            result['Ids'] = self.ids_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ids') is not None:
            self.ids_shrink = m.get('Ids')

        return self

