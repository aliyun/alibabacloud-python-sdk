# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyCustomizeFlowStrategyListShrinkRequest(DaraModel):
    def __init__(
        self,
        product_type: str = None,
        strategy_object_shrink: str = None,
    ):
        # Product type, currently only supports **ANT_CLOUD_AUTH** (Financial-grade real person), all others have been phased out.
        self.product_type = product_type
        # Strategy list.
        self.strategy_object_shrink = strategy_object_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.product_type is not None:
            result['ProductType'] = self.product_type

        if self.strategy_object_shrink is not None:
            result['StrategyObject'] = self.strategy_object_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')

        if m.get('StrategyObject') is not None:
            self.strategy_object_shrink = m.get('StrategyObject')

        return self

