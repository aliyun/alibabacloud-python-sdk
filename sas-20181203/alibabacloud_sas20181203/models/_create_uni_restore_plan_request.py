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
        # The unique identifier of the database backup client on the destination server for restoration.
        # >Call the [DescribeUniBackupDatabase](~~DescribeUniBackupDatabase~~) operation to obtain this parameter.
        self.instance_uuid = instance_uuid
        # The ID of the database anti-ransomware backup policy.
        # >Call the [DescribeUniBackupPolicies](~~DescribeUniBackupPolicies~~) operation to obtain this parameter.
        # 
        # This parameter is required.
        self.policy_id = policy_id
        # The **reset_scn** value of the selected record from the recoverable points in time when you query backups for an Oracle database.
        # >Call the [DescribeUniRecoverableList](~~DescribeUniRecoverableList~~) operation to obtain this parameter.
        self.reset_scn = reset_scn
        # The **reset_time** value of the selected record from the recoverable points in time when you query backups for an Oracle database.
        # >Call the [DescribeUniRecoverableList](~~DescribeUniRecoverableList~~) operation to obtain this parameter.
        self.reset_time = reset_time
        # The database restoration information when the database type is MSSQL. The value is a JSON string. Valid values:
        # - **name**: the name of the database.
        # - **files**: the file path of the database.
        # >Call the [DescribeUniRecoverableList](~~DescribeUniRecoverableList~~) operation to obtain this parameter.
        self.restore_info = restore_info
        # The point in time to which you want to restore the database.
        # >Call the [DescribeRestorePlans](~~DescribeRestorePlans~~) operation to obtain this parameter.
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

