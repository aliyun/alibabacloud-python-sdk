# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ResetInstancePasswordRequest(DaraModel):
    def __init__(
        self,
        branch_name: str = None,
        dashboard_password: str = None,
        database_password: str = None,
        instance_name: str = None,
        region_id: str = None,
    ):
        # The reserved parameter.
        self.branch_name = branch_name
        # The password for the Supabase Dashboard.
        # 
        # The password must be 8 to 32 characters in length and must contain at least three of the following character types: uppercase letters, lowercase letters, digits, and underscores (_).
        self.dashboard_password = dashboard_password
        # The access password for the RDS database.
        # 
        # The password must be 8 to 32 characters in length and must contain at least three of the following character types: uppercase letters, lowercase letters, digits, and underscores (_).
        # 
        # >Notice: This password is synchronized to update the access passwords of the following accounts (all required by Supabase) on the associated PostgreSQL instance: postgres, supabase_admin, supabase_auth_admin, supabase_functions_admin, supabase_storage_admin, authenticator, and pgbouncer.
        # </notice>
        self.database_password = database_password
        # The instance ID of the AI application.
        # 
        # This parameter is required.
        self.instance_name = instance_name
        # The region ID.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.branch_name is not None:
            result['BranchName'] = self.branch_name

        if self.dashboard_password is not None:
            result['DashboardPassword'] = self.dashboard_password

        if self.database_password is not None:
            result['DatabasePassword'] = self.database_password

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BranchName') is not None:
            self.branch_name = m.get('BranchName')

        if m.get('DashboardPassword') is not None:
            self.dashboard_password = m.get('DashboardPassword')

        if m.get('DatabasePassword') is not None:
            self.database_password = m.get('DatabasePassword')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

