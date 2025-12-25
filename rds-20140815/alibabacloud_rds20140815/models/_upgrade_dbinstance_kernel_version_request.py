# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpgradeDBInstanceKernelVersionRequest(DaraModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        switch_time: str = None,
        target_minor_version: str = None,
        upgrade_time: str = None,
    ):
        # The instance ID. You can call the DescribeDBInstances operation to query the instance ID.
        # 
        # > *   If your instance runs PostgreSQL, you must make sure that the instance uses **cloud disks**. If the instance uses local disks, you must call the [RestartDBInstance](https://help.aliyun.com/document_detail/26230.html) operation to restart the instance. The system automatically updates the minor engine version of the instance to the latest version during the restart.
        # > *   If your instance runs SQL Server, you must make sure that the instance runs SQL Server 2019.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The update time. Specify the time in the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time must be in UTC.
        # 
        # > This parameter takes effect only when you set **UpgradeTime** to **SpecifyTime**.
        self.switch_time = switch_time
        # The minor engine version to which you want to update. Format:
        # 
        # *   **PostgreSQL**: `rds_postgres_<Major engine version>00_<Minor engine version>`. Example: `rds_postgres_1200_20200830`.
        # 
        # *   **MySQL**: `<RDS edition and MySQL version>_<Minor engine version>`. Examples: `rds_20200229`, `xcluster_20200229`, and `xcluster80_20200229`. The following RDS editions and MySQL versions are supported:
        # 
        #     *   **rds**: RDS Basic Edition or RDS High-availability Edition
        #     *   **xcluster**: MySQL 5.7 on RDS Enterprise Edition
        #     *   **xcluster80**: MySQL 8.0 on RDS Enterprise Edition
        # 
        # *   **SQLServer**: `<Minor engine version>`. Example: `15.0.4073.23`.
        # 
        # If you do not specify this parameter, the instance is updated to the latest minor engine version.
        # 
        # >  For more information about minor engine versions, see [Release notes of AliPG](https://help.aliyun.com/document_detail/126002.html), [Release notes of AliSQL](https://help.aliyun.com/document_detail/96060.html), and [Release notes of minor engine versions of ApsaraDB RDS for SQL Server](https://help.aliyun.com/document_detail/213577.html).
        self.target_minor_version = target_minor_version
        # The time when the update takes effect. Valid values:
        # 
        # *   **Immediate** (default): The update takes effect immediately.
        # *   **MaintainTime**: The update takes effect during the maintenance window that you specify. For more information about how to change the maintenance window, see ModifyDBInstanceMaintainTime.
        # *   **SpecifyTime**: The update takes effect at the point in time you specify.
        self.upgrade_time = upgrade_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.switch_time is not None:
            result['SwitchTime'] = self.switch_time

        if self.target_minor_version is not None:
            result['TargetMinorVersion'] = self.target_minor_version

        if self.upgrade_time is not None:
            result['UpgradeTime'] = self.upgrade_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('SwitchTime') is not None:
            self.switch_time = m.get('SwitchTime')

        if m.get('TargetMinorVersion') is not None:
            self.target_minor_version = m.get('TargetMinorVersion')

        if m.get('UpgradeTime') is not None:
            self.upgrade_time = m.get('UpgradeTime')

        return self

