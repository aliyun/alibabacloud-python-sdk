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
        # The ID of the instance. You can call the DescribeDBInstances operation to query the instance ID.
        # 
        # > * The storage type of the ApsaraDB RDS for PostgreSQL instance must be **cloud disk**. You can call the [restart the instance](https://help.aliyun.com/document_detail/26230.html) operation to restart an instance with Premium Local SSDs to automatically upgrade the instance to the latest minor engine version.
        # > * Only ApsaraDB RDS for SQL Server 2019 instances support minor engine version upgrades.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The specified time when the upgrade is performed. Specify the time in the <i>yyyy-MM-dd</i>T<i>HH:mm:ss</i>Z format. The time must be in UTC.
        # >This parameter takes effect only when **UpgradeTime** is set to **SpecifyTime**.
        self.switch_time = switch_time
        # The target minor database version. Format:
        # * **PostgreSQL**: `rds_postgres_<Major version number>00_<Minor version number>`. Example: `rds_postgres_1200_20200830` for PostgreSQL 12 version 20200830.
        # * **MySQL**: `<Instance edition>_<Minor version number>`. Examples: `rds_20200229`, `xcluster_20200229`, and `xcluster80_20200229`. The instance editions are as follows:
        #     * **rds**: high availability series or Basic Edition.
        #     * **xcluster**: MySQL 5.7 RDS Enterprise Edition.
        #     * **xcluster80**: MySQL 8.0 RDS Enterprise Edition.
        # * **SQL Server**: `<Minor version number>`. Example: `15.0.4073.23`.
        # 
        # If you do not specify this parameter, the instance is upgraded to the latest minor database version by default.
        # > For more information about minor database versions, see [Release notes for minor engine versions of ApsaraDB RDS for PostgreSQL](https://help.aliyun.com/document_detail/126002.html), [Release notes for minor engine versions of ApsaraDB RDS for MySQL](https://help.aliyun.com/document_detail/96060.html), and [Release notes for minor engine versions of ApsaraDB RDS for SQL Server](https://help.aliyun.com/document_detail/213577.html).
        self.target_minor_version = target_minor_version
        # The time when the upgrade is performed. Valid values:
        # 
        # * **Immediate**: The upgrade is immediately performed. This is the default value.
        # * **MaintainTime**: The upgrade is performed within the specified maintenance window. For more information about how to modify the maintenance window, see ModifyDBInstanceMaintainTime.
        # * **SpecifyTime**: The upgrade is performed at the specified time.
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

