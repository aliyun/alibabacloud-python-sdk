# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateSignalResponseBody(DaraModel):
    def __init__(
        self,
        job_id: str = None,
        request_id: str = None,
        signal: str = None,
        signal_id: str = None,
        status: str = None,
    ):
        self.job_id = job_id
        self.request_id = request_id
        self.signal = signal
        self.signal_id = signal_id
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.signal is not None:
            result['Signal'] = self.signal

        if self.signal_id is not None:
            result['SignalId'] = self.signal_id

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Signal') is not None:
            self.signal = m.get('Signal')

        if m.get('SignalId') is not None:
            self.signal_id = m.get('SignalId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

