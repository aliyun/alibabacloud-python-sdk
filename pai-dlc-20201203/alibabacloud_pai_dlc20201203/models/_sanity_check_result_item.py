# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SanityCheckResultItem(DaraModel):
    def __init__(
        self,
        check_number: int = None,
        finished_at: str = None,
        message: str = None,
        phase: str = None,
        started_at: str = None,
        status: str = None,
    ):
        self.check_number = check_number
        self.finished_at = finished_at
        self.message = message
        self.phase = phase
        self.started_at = started_at
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.check_number is not None:
            result['CheckNumber'] = self.check_number

        if self.finished_at is not None:
            result['FinishedAt'] = self.finished_at

        if self.message is not None:
            result['Message'] = self.message

        if self.phase is not None:
            result['Phase'] = self.phase

        if self.started_at is not None:
            result['StartedAt'] = self.started_at

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckNumber') is not None:
            self.check_number = m.get('CheckNumber')

        if m.get('FinishedAt') is not None:
            self.finished_at = m.get('FinishedAt')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('Phase') is not None:
            self.phase = m.get('Phase')

        if m.get('StartedAt') is not None:
            self.started_at = m.get('StartedAt')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

