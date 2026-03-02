# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ScheduledPlanExecutedStatus(DaraModel):
    def __init__(
        self,
        restart_type: str = None,
        status_state: str = None,
    ):
        self.restart_type = restart_type
        self.status_state = status_state

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.restart_type is not None:
            result['restartType'] = self.restart_type

        if self.status_state is not None:
            result['statusState'] = self.status_state

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('restartType') is not None:
            self.restart_type = m.get('restartType')

        if m.get('statusState') is not None:
            self.status_state = m.get('statusState')

        return self

