# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyDashboardNl2sqlStatusRequest(DaraModel):
    def __init__(
        self,
        dashboard_ids: str = None,
        status: int = None,
    ):
        # This parameter is required.
        self.dashboard_ids = dashboard_ids
        # This parameter is required.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dashboard_ids is not None:
            result['DashboardIds'] = self.dashboard_ids

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DashboardIds') is not None:
            self.dashboard_ids = m.get('DashboardIds')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

