# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class LogReservePolicy(DaraModel):
    def __init__(
        self,
        expiration_days: int = None,
        open_history: bool = None,
    ):
        # The number of days for which logs are retained after you enable the
        # log archiving feature.
        self.expiration_days = expiration_days
        # Specifies whether to enable the log archiving feature.
        self.open_history = open_history

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.expiration_days is not None:
            result['expirationDays'] = self.expiration_days

        if self.open_history is not None:
            result['openHistory'] = self.open_history

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('expirationDays') is not None:
            self.expiration_days = m.get('expirationDays')

        if m.get('openHistory') is not None:
            self.open_history = m.get('openHistory')

        return self

