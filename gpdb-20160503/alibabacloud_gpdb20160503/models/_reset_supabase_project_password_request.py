# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ResetSupabaseProjectPasswordRequest(DaraModel):
    def __init__(
        self,
        account_password: str = None,
        dashboard_password: str = None,
        project_id: str = None,
        region_id: str = None,
    ):
        # The password of the database account.
        # - The password must contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters.
        # - The supported special characters are: `!@#$%^&*()_+-=`
        # - The password must be 8 to 32 characters in length.
        self.account_password = account_password
        # The Supabase Dashboard password.
        self.dashboard_password = dashboard_password
        # The Supabase instance ID.
        # 
        # This parameter is required.
        self.project_id = project_id
        # The region ID of the instance.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_password is not None:
            result['AccountPassword'] = self.account_password

        if self.dashboard_password is not None:
            result['DashboardPassword'] = self.dashboard_password

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountPassword') is not None:
            self.account_password = m.get('AccountPassword')

        if m.get('DashboardPassword') is not None:
            self.dashboard_password = m.get('DashboardPassword')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

