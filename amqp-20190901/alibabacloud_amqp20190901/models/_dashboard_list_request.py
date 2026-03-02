# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DashboardListRequest(DaraModel):
    def __init__(
        self,
        console_session_id: str = None,
        dashboard_name: str = None,
    ):
        self.console_session_id = console_session_id
        # This parameter is required.
        self.dashboard_name = dashboard_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.console_session_id is not None:
            result['ConsoleSessionId'] = self.console_session_id

        if self.dashboard_name is not None:
            result['DashboardName'] = self.dashboard_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConsoleSessionId') is not None:
            self.console_session_id = m.get('ConsoleSessionId')

        if m.get('DashboardName') is not None:
            self.dashboard_name = m.get('DashboardName')

        return self

