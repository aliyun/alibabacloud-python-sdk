# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class JobFailure(DaraModel):
    def __init__(
        self,
        failed_at: int = None,
        message: str = None,
        reason: str = None,
    ):
        # The time when the deployment fails.
        self.failed_at = failed_at
        # The details of the failure.
        self.message = message
        # The reason for the failure.
        self.reason = reason

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.failed_at is not None:
            result['failedAt'] = self.failed_at

        if self.message is not None:
            result['message'] = self.message

        if self.reason is not None:
            result['reason'] = self.reason

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('failedAt') is not None:
            self.failed_at = m.get('failedAt')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('reason') is not None:
            self.reason = m.get('reason')

        return self

