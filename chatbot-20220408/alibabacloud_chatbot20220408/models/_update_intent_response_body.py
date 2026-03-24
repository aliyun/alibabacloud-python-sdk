# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateIntentResponseBody(DaraModel):
    def __init__(
        self,
        intent_id: int = None,
        request_id: str = None,
    ):
        self.intent_id = intent_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.intent_id is not None:
            result['IntentId'] = self.intent_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IntentId') is not None:
            self.intent_id = m.get('IntentId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

