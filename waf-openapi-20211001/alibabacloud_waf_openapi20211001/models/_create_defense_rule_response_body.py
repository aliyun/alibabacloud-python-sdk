# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateDefenseRuleResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        rule_ids: str = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The IDs of the protection rules. Multiple IDs are separated by commas (,).
        self.rule_ids = rule_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.rule_ids is not None:
            result['RuleIds'] = self.rule_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('RuleIds') is not None:
            self.rule_ids = m.get('RuleIds')

        return self

