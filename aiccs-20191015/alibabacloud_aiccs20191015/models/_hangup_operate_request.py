# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class HangupOperateRequest(DaraModel):
    def __init__(
        self,
        call_id: str = None,
        immediate_hangup: bool = None,
    ):
        # This parameter is required.
        self.call_id = call_id
        self.immediate_hangup = immediate_hangup

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.call_id is not None:
            result['CallId'] = self.call_id

        if self.immediate_hangup is not None:
            result['ImmediateHangup'] = self.immediate_hangup

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CallId') is not None:
            self.call_id = m.get('CallId')

        if m.get('ImmediateHangup') is not None:
            self.immediate_hangup = m.get('ImmediateHangup')

        return self

