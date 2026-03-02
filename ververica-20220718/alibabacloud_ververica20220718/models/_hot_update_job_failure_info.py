# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class HotUpdateJobFailureInfo(DaraModel):
    def __init__(
        self,
        failure_severity: str = None,
        message: str = None,
        reason: str = None,
    ):
        self.failure_severity = failure_severity
        self.message = message
        self.reason = reason

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.failure_severity is not None:
            result['failureSeverity'] = self.failure_severity

        if self.message is not None:
            result['message'] = self.message

        if self.reason is not None:
            result['reason'] = self.reason

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('failureSeverity') is not None:
            self.failure_severity = m.get('failureSeverity')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('reason') is not None:
            self.reason = m.get('reason')

        return self

