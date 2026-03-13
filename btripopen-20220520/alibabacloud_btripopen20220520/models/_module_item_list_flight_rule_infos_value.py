# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModuleItemListFlightRuleInfosValue(DaraModel):
    def __init__(
        self,
        refund_change_rule_desc: str = None,
        baggage_desc: str = None,
    ):
        self.refund_change_rule_desc = refund_change_rule_desc
        self.baggage_desc = baggage_desc

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.refund_change_rule_desc is not None:
            result['refund_change_rule_desc'] = self.refund_change_rule_desc

        if self.baggage_desc is not None:
            result['baggage_desc'] = self.baggage_desc

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('refund_change_rule_desc') is not None:
            self.refund_change_rule_desc = m.get('refund_change_rule_desc')

        if m.get('baggage_desc') is not None:
            self.baggage_desc = m.get('baggage_desc')

        return self

