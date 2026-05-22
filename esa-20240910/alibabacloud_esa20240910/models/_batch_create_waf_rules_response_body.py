# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class BatchCreateWafRulesResponseBody(DaraModel):
    def __init__(
        self,
        ids: List[int] = None,
        request_id: str = None,
        ruleset_id: int = None,
    ):
        # ID of the WAF rule, which can be obtained by calling the [ListWafRules](https://help.aliyun.com/document_detail/2878257.html) interface.
        self.ids = ids
        # Request ID.
        self.request_id = request_id
        # ID of the WAF ruleset, which can be obtained by calling the [ListWafRulesets](https://help.aliyun.com/document_detail/2878359.html) interface.
        self.ruleset_id = ruleset_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ids is not None:
            result['Ids'] = self.ids

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.ruleset_id is not None:
            result['RulesetId'] = self.ruleset_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ids') is not None:
            self.ids = m.get('Ids')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('RulesetId') is not None:
            self.ruleset_id = m.get('RulesetId')

        return self

