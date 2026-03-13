# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DepartmentSaveShrinkRequest(DaraModel):
    def __init__(
        self,
        depart_list_shrink: str = None,
    ):
        self.depart_list_shrink = depart_list_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.depart_list_shrink is not None:
            result['depart_list'] = self.depart_list_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('depart_list') is not None:
            self.depart_list_shrink = m.get('depart_list')

        return self

