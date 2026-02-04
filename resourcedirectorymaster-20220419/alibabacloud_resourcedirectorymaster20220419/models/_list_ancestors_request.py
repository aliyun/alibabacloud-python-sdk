# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListAncestorsRequest(DaraModel):
    def __init__(
        self,
        child_id: str = None,
    ):
        # The ID of the subfolder.
        # 
        # This parameter is required.
        self.child_id = child_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.child_id is not None:
            result['ChildId'] = self.child_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChildId') is not None:
            self.child_id = m.get('ChildId')

        return self

