# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyBlackListStrategyShrinkRequest(DaraModel):
    def __init__(
        self,
        black_list_strategy_shrink: str = None,
        region_id: str = None,
    ):
        # Blacklist rule.
        self.black_list_strategy_shrink = black_list_strategy_shrink
        # Region ID
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.black_list_strategy_shrink is not None:
            result['BlackListStrategy'] = self.black_list_strategy_shrink

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BlackListStrategy') is not None:
            self.black_list_strategy_shrink = m.get('BlackListStrategy')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

