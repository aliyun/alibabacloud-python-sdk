# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetEventRuleRequest(DaraModel):
    def __init__(
        self,
        product_name: str = None,
        rule_name: str = None,
    ):
        # The name of the Alibaba Cloud product that triggers the event notification.
        # 
        # This parameter is required.
        self.product_name = product_name
        # The name of the event notification rule.
        # 
        # This parameter is required.
        self.rule_name = rule_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.product_name is not None:
            result['ProductName'] = self.product_name

        if self.rule_name is not None:
            result['RuleName'] = self.rule_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProductName') is not None:
            self.product_name = m.get('ProductName')

        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')

        return self

