# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteSDGShrinkRequest(DaraModel):
    def __init__(
        self,
        sdgid_shrink: str = None,
    ):
        # The IDs of the SDGs that you want to delete.
        # 
        # This parameter is required.
        self.sdgid_shrink = sdgid_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.sdgid_shrink is not None:
            result['SDGId'] = self.sdgid_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SDGId') is not None:
            self.sdgid_shrink = m.get('SDGId')

        return self

