# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Any

from darabonba.model import DaraModel

class GetFundAccountLowAvailableAmountAlarmResponseBody(DaraModel):
    def __init__(
        self,
        alarm_enabled: bool = None,
        metadata: Any = None,
        request_id: str = None,
        threshold_amount: str = None,
    ):
        self.alarm_enabled = alarm_enabled
        self.metadata = metadata
        self.request_id = request_id
        self.threshold_amount = threshold_amount

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alarm_enabled is not None:
            result['AlarmEnabled'] = self.alarm_enabled

        if self.metadata is not None:
            result['Metadata'] = self.metadata

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.threshold_amount is not None:
            result['ThresholdAmount'] = self.threshold_amount

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlarmEnabled') is not None:
            self.alarm_enabled = m.get('AlarmEnabled')

        if m.get('Metadata') is not None:
            self.metadata = m.get('Metadata')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ThresholdAmount') is not None:
            self.threshold_amount = m.get('ThresholdAmount')

        return self

