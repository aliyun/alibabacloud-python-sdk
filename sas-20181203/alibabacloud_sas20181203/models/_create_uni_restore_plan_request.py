# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateUniRestorePlanRequest(DaraModel):
    def __init__(
        self,
        database: str = None,
        instance_uuid: str = None,
        policy_id: int = None,
        reset_scn: str = None,
        reset_time: str = None,
        restore_info: str = None,
        time_point: int = None,
    ):
        # The name of the database.
        self.database = database
        # The UUID of the Hybrid Backup Recovery (HBR) agent that is used to restore the data of the database on your server.
        # 
        # >  You can call the [DescribeUniBackupDatabase](~~DescribeUniBackupDatabase~~) operation to query the UUID.
        self.instance_uuid = instance_uuid
        # The ID of the anti-ransomware policy.
        # 
        # >  You can call the [DescribeUniBackupPolicies](~~DescribeUniBackupPolicies~~) operation to query the ID.
        # 
        # This parameter is required.
        self.policy_id = policy_id
        # The identifier of the point in time for restoration in the backup version that you want to use. The database is an Oracle database.****
        # 
        # >  You can call the [DescribeUniRecoverableList](~~DescribeUniRecoverableList~~) operation to query the value.
        self.reset_scn = reset_scn
        # The point in time for restoration in the backup version that you want to use. The database is an Oracle database.****
        # 
        # >  You can call the [DescribeUniRecoverableList](~~DescribeUniRecoverableList~~) operation to query the value.
        self.reset_time = reset_time
        # The information about the database. This parameter is available when the database is a Microsoft SQL Server (MSSQL) database. The value is a JSON string. Valid values:
        # 
        # *   **name**: the name of the database
        # *   **files**: the path to the database files
        # 
        # >  You can call the [DescribeUniRecoverableList](~~DescribeUniRecoverableList~~) operation to query the information.
        self.restore_info = restore_info
        # The point in time to which you want to restore data.
        # 
        # >  You can call the [DescribeRestorePlans](~~DescribeRestorePlans~~) operation to query the point in time.
        # 
        # This parameter is required.
        self.time_point = time_point

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.database is not None:
            result['Database'] = self.database

        if self.instance_uuid is not None:
            result['InstanceUuid'] = self.instance_uuid

        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id

        if self.reset_scn is not None:
            result['ResetScn'] = self.reset_scn

        if self.reset_time is not None:
            result['ResetTime'] = self.reset_time

        if self.restore_info is not None:
            result['RestoreInfo'] = self.restore_info

        if self.time_point is not None:
            result['TimePoint'] = self.time_point

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Database') is not None:
            self.database = m.get('Database')

        if m.get('InstanceUuid') is not None:
            self.instance_uuid = m.get('InstanceUuid')

        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')

        if m.get('ResetScn') is not None:
            self.reset_scn = m.get('ResetScn')

        if m.get('ResetTime') is not None:
            self.reset_time = m.get('ResetTime')

        if m.get('RestoreInfo') is not None:
            self.restore_info = m.get('RestoreInfo')

        if m.get('TimePoint') is not None:
            self.time_point = m.get('TimePoint')

        return self

