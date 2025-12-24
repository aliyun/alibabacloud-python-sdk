# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribePriceForModifyDesktopOversoldGroupSaleRequest(DaraModel):
    def __init__(
        self,
        concurrence_count: int = None,
        oversold_group_id: str = None,
        oversold_user_count: int = None,
    ):
        self.concurrence_count = concurrence_count
        self.oversold_group_id = oversold_group_id
        self.oversold_user_count = oversold_user_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.concurrence_count is not None:
            result['ConcurrenceCount'] = self.concurrence_count

        if self.oversold_group_id is not None:
            result['OversoldGroupId'] = self.oversold_group_id

        if self.oversold_user_count is not None:
            result['OversoldUserCount'] = self.oversold_user_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConcurrenceCount') is not None:
            self.concurrence_count = m.get('ConcurrenceCount')

        if m.get('OversoldGroupId') is not None:
            self.oversold_group_id = m.get('OversoldGroupId')

        if m.get('OversoldUserCount') is not None:
            self.oversold_user_count = m.get('OversoldUserCount')

        return self

