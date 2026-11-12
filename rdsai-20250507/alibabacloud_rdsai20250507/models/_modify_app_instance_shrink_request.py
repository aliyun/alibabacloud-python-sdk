# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyAppInstanceShrinkRequest(DaraModel):
    def __init__(
        self,
        branch_name: str = None,
        client_token: str = None,
        components_shrink: str = None,
        dbinstance_name: str = None,
        instance_class: str = None,
        instance_name: str = None,
        migration_mode: str = None,
        region_id: str = None,
    ):
        # The reserved parameter.
        self.branch_name = branch_name
        # The idempotency parameter.
        self.client_token = client_token
        # The list of modules.
        self.components_shrink = components_shrink
        # The instance ID of the ApsaraDB RDS for PostgreSQL database connected to the AI application.
        # 
        # <notice>Only **newly purchased empty ApsaraDB RDS for PostgreSQL instances** are supported. The major engine version must be **17**, and the minor engine version must be **20250630 or later**.</notice>
        self.dbinstance_name = dbinstance_name
        # The instance type. Only **rdsai.supabase.basic** is supported.
        self.instance_class = instance_class
        # The instance ID of the AI application.
        self.instance_name = instance_name
        # The reserved parameter.
        self.migration_mode = migration_mode
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

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.components_shrink is not None:
            result['Components'] = self.components_shrink

        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name

        if self.instance_class is not None:
            result['InstanceClass'] = self.instance_class

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.migration_mode is not None:
            result['MigrationMode'] = self.migration_mode

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BranchName') is not None:
            self.branch_name = m.get('BranchName')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('Components') is not None:
            self.components_shrink = m.get('Components')

        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')

        if m.get('InstanceClass') is not None:
            self.instance_class = m.get('InstanceClass')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('MigrationMode') is not None:
            self.migration_mode = m.get('MigrationMode')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

