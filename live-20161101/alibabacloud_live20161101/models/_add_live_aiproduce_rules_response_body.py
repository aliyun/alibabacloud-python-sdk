# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AddLiveAIProduceRulesResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        rules_id: str = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The ID of the subtitle rule.
        self.rules_id = rules_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.rules_id is not None:
            result['RulesId'] = self.rules_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('RulesId') is not None:
            self.rules_id = m.get('RulesId')

        return self

