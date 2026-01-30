# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeGroupRequest(DaraModel):
    def __init__(
        self,
        id: str = None,
        include_stats: bool = None,
        owner_id: int = None,
    ):
        # This parameter is required.
        self.id = id
        self.include_stats = include_stats
        self.owner_id = owner_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.include_stats is not None:
            result['IncludeStats'] = self.include_stats

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('IncludeStats') is not None:
            self.include_stats = m.get('IncludeStats')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        return self

