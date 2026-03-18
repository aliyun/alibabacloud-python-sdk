# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class TriggerStackExecutionResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        trigger_id: str = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.trigger_id = trigger_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.trigger_id is not None:
            result['triggerId'] = self.trigger_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('triggerId') is not None:
            self.trigger_id = m.get('triggerId')

        return self

