# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateUniBackupPolicyShrinkRequest(DaraModel):
    def __init__(
        self,
        account_name: str = None,
        account_password: str = None,
        database_add_by_user: str = None,
        database_type: str = None,
        full_plan_shrink: str = None,
        inc_plan_shrink: str = None,
        instance_id: str = None,
        policy_name: str = None,
        retention: int = None,
        speed_limiter: int = None,
        uni_region_id: str = None,
        uuid: str = None,
    ):
        # The username of the database account.
        self.account_name = account_name
        # The password of the database account.
        self.account_password = account_password
        # Specifies whether the database is manually added by the user. Valid values:
        # 
        # - **true**: The database is manually added.
        # - **false**: The database is not manually added.
        self.database_add_by_user = database_add_by_user
        # The type of the database. Valid values:
        # 
        # - **MYSQL**
        # - **ORACLE**
        # - **MSSQL**
        # 
        # This parameter is required.
        self.database_type = database_type
        # The full backup policy. The value is in JSON format and contains the following fields:
        # 
        # - **start**: the start time of the backup.
        # - **interval**: the interval between backups.
        # - **type**: the unit of the interval.
        # - **days**: the days of the week on which backups are performed.
        # 
        # This parameter is required.
        self.full_plan_shrink = full_plan_shrink
        # The incremental backup policy. The value is in JSON format and contains the following fields:
        # - **start**: the start time of the backup.
        # - **interval**: the interval between backups.
        # - **type**: the unit of the interval.
        # - **days**: the days of the week on which backups are performed.
        # 
        # This parameter is required.
        self.inc_plan_shrink = inc_plan_shrink
        # The ID of the ECS instance.
        # >You can call the [DescribeUniBackupDatabase](~~DescribeUniBackupDatabase~~) operation to obtain this parameter.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The name of the anti-ransomware backup policy.
        # 
        # This parameter is required.
        self.policy_name = policy_name
        # The number of days for which backup data is retained.
        # 
        # This parameter is required.
        self.retention = retention
        # The network bandwidth throttling for backup network bandwidth. Unit: bytes.
        # 
        # This parameter is required.
        self.speed_limiter = speed_limiter
        # The region in which the server protected by the backup policy resides.
        # 
        # This parameter is required.
        self.uni_region_id = uni_region_id
        # The UUID of the server that is backed up by the database anti-ransomware feature.
        # > You can call the [DescribeCloudCenterInstances](https://help.aliyun.com/document_detail/141932.html) operation to obtain the UUID of the server.
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_name is not None:
            result['AccountName'] = self.account_name

        if self.account_password is not None:
            result['AccountPassword'] = self.account_password

        if self.database_add_by_user is not None:
            result['DatabaseAddByUser'] = self.database_add_by_user

        if self.database_type is not None:
            result['DatabaseType'] = self.database_type

        if self.full_plan_shrink is not None:
            result['FullPlan'] = self.full_plan_shrink

        if self.inc_plan_shrink is not None:
            result['IncPlan'] = self.inc_plan_shrink

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.policy_name is not None:
            result['PolicyName'] = self.policy_name

        if self.retention is not None:
            result['Retention'] = self.retention

        if self.speed_limiter is not None:
            result['SpeedLimiter'] = self.speed_limiter

        if self.uni_region_id is not None:
            result['UniRegionId'] = self.uni_region_id

        if self.uuid is not None:
            result['Uuid'] = self.uuid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')

        if m.get('AccountPassword') is not None:
            self.account_password = m.get('AccountPassword')

        if m.get('DatabaseAddByUser') is not None:
            self.database_add_by_user = m.get('DatabaseAddByUser')

        if m.get('DatabaseType') is not None:
            self.database_type = m.get('DatabaseType')

        if m.get('FullPlan') is not None:
            self.full_plan_shrink = m.get('FullPlan')

        if m.get('IncPlan') is not None:
            self.inc_plan_shrink = m.get('IncPlan')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')

        if m.get('Retention') is not None:
            self.retention = m.get('Retention')

        if m.get('SpeedLimiter') is not None:
            self.speed_limiter = m.get('SpeedLimiter')

        if m.get('UniRegionId') is not None:
            self.uni_region_id = m.get('UniRegionId')

        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')

        return self

