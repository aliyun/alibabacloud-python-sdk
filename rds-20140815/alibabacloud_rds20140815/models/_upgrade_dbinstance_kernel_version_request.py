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
        # The instance ID. You can invoke DescribeDBInstances to query the instance ID.
        # 
        # > * The storage type of the ApsaraDB RDS for PostgreSQL instance must be **cloud disks**. For an instance with Premium Local SSDs, you can invoke the [RestartDBInstance](https://help.aliyun.com/document_detail/26230.html) operation to restart the instance, which automatically upgrades the instance to the latest minor engine version.
        # > * Only the 2019 version of ApsaraDB RDS for SQL Server supports minor engine version upgrades.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The specified time. Format: <i>yyyy-MM-dd</i>T<i>HH:mm:ss</i>Z (UTC).
        # > This parameter takes effect only when **UpgradeTime** is set to **SpecifyTime**.
        self.switch_time = switch_time
        # The minor database engine version to which you want to upgrade. Format:
        # * **PostgreSQL**: `rds_postgres_<Major version number>00_<Minor version number>`. Example for version 12 with minor version 20200830: `rds_postgres_1200_20200830`.
        # * **MySQL**: `<Instance version>_<Minor version number>`. Examples: `rds_20200229`, `xcluster_20200229`, or `xcluster80_20200229`. The instance version can be one of the following:
        #     * **rds**: high-availability series or Basic Edition.
        #     * **xcluster**: MySQL 5.7 RDS Enterprise Edition.
        #     * **xcluster80**: MySQL 8.0 RDS Enterprise Edition.
        # * **SQLServer**: `<Minor version number>`. Example: `15.0.4073.23`.
        # 
        # If you do not specify this parameter, the instance is upgraded to the latest minor engine version by default.
        # > For minor engine version numbers, see [Release notes of ApsaraDB RDS for PostgreSQL minor engine versions](https://help.aliyun.com/document_detail/126002.html), [Release notes of ApsaraDB RDS for MySQL minor engine versions](https://help.aliyun.com/document_detail/96060.html), and [Release notes of ApsaraDB RDS for SQL Server minor engine versions](https://help.aliyun.com/document_detail/213577.html).
        self.target_minor_version = target_minor_version
        # The upgrade time. Valid values:
        # 
        # * **Immediate** (default): The upgrade takes effect immediately.
        # * **MaintainTime**: The upgrade takes effect during the maintenance window. To modify the maintenance window, call ModifyDBInstanceMaintainTime.
        # * **SpecifyTime**: The upgrade takes effect at a specified time.
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

