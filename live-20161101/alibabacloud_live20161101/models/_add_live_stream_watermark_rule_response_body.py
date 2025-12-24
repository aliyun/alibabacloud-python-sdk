# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AddLiveStreamWatermarkRuleResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        rule_id: str = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The ID of the watermark rule.
        self.rule_id = rule_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.rule_id is not None:
            result['RuleId'] = self.rule_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')

        return self

