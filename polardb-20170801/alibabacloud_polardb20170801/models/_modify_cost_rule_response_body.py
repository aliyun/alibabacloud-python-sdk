# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyCostRuleResponseBody(DaraModel):
    def __init__(
        self,
        cost_rule_id: str = None,
        request_id: str = None,
    ):
        self.cost_rule_id = cost_rule_id
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cost_rule_id is not None:
            result['CostRuleId'] = self.cost_rule_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CostRuleId') is not None:
            self.cost_rule_id = m.get('CostRuleId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

