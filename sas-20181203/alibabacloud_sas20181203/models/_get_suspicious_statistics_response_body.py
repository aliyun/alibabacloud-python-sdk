# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetSuspiciousStatisticsResponseBody(DaraModel):
    def __init__(
        self,
        remind_count: int = None,
        request_id: str = None,
        serious_count: int = None,
        suspicious_count: int = None,
        total_count: int = None,
    ):
        # The number of security alerts whose alert level is Reminder.
        self.remind_count = remind_count
        # The request ID. Alibaba Cloud generates a unique identifier for each API request. You can use this ID to troubleshoot issues.
        self.request_id = request_id
        # The number of security alerts whose alert level is Urgent.
        self.serious_count = serious_count
        # The number of security alerts whose alert level is Suspicious.
        self.suspicious_count = suspicious_count
        # The total number of security alerts.
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.remind_count is not None:
            result['RemindCount'] = self.remind_count

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.serious_count is not None:
            result['SeriousCount'] = self.serious_count

        if self.suspicious_count is not None:
            result['SuspiciousCount'] = self.suspicious_count

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RemindCount') is not None:
            self.remind_count = m.get('RemindCount')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SeriousCount') is not None:
            self.serious_count = m.get('SeriousCount')

        if m.get('SuspiciousCount') is not None:
            self.suspicious_count = m.get('SuspiciousCount')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

