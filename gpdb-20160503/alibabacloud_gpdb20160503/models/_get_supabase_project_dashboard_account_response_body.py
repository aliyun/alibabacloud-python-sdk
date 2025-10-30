# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetSupabaseProjectDashboardAccountResponseBody(DaraModel):
    def __init__(
        self,
        dashboard_password: str = None,
        dashboard_username: str = None,
        project_id: str = None,
        project_name: str = None,
        request_id: str = None,
    ):
        self.dashboard_password = dashboard_password
        self.dashboard_username = dashboard_username
        self.project_id = project_id
        self.project_name = project_name
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dashboard_password is not None:
            result['DashboardPassword'] = self.dashboard_password

        if self.dashboard_username is not None:
            result['DashboardUsername'] = self.dashboard_username

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.project_name is not None:
            result['ProjectName'] = self.project_name

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DashboardPassword') is not None:
            self.dashboard_password = m.get('DashboardPassword')

        if m.get('DashboardUsername') is not None:
            self.dashboard_username = m.get('DashboardUsername')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

