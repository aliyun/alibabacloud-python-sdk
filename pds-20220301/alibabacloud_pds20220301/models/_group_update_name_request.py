# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GroupUpdateNameRequest(DaraModel):
    def __init__(
        self,
        group_id: str = None,
        name: str = None,
    ):
        # This parameter is required.
        self.group_id = group_id
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.group_id is not None:
            result['group_id'] = self.group_id

        if self.name is not None:
            result['name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('group_id') is not None:
            self.group_id = m.get('group_id')

        if m.get('name') is not None:
            self.name = m.get('name')

        return self

