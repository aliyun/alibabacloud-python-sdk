# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpgradeDBProxyInstanceKernelVersionRequest(DaraModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        dbproxy_engine_type: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        switch_time: str = None,
        target_minor_version: str = None,
        upgrade_time: str = None,
    ):
        # The instance ID. You can call the DescribeDBInstances operation to query the instance ID.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # A reserved parameter. You do not need to specify this parameter.
        self.dbproxy_engine_type = dbproxy_engine_type
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The specific point in time when you want to perform the upgrade. Specify the time in the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time must be in UTC.
        # 
        # >  If you set **UpgradeTime** to **SpecifyTime**, you must specify SwitchTime.
        self.switch_time = switch_time
        self.target_minor_version = target_minor_version
        # The time when you want to upgrade the database proxy version of the instance. Valid values:
        # 
        # *   **MaintainTime** (default): performs the upgrade during the maintenance window that you specified. For more information, see [Modify the maintenance window](https://help.aliyun.com/document_detail/610402.html).
        # *   **Immediate**: performs the upgrade immediately.
        # *   **SpecifyTime**: performs the upgrade at a specified point in time.
        # 
        # > *   **If the instance runs MySQL, you can set this parameter to **MaintainTime**, **Immediate**, or SpecifyTime**.
        # > *   If the instance runs PostgreSQL, you can set this parameter to **MaintainTime** or **Immediate**.
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

        if self.dbproxy_engine_type is not None:
            result['DBProxyEngineType'] = self.dbproxy_engine_type

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

        if m.get('DBProxyEngineType') is not None:
            self.dbproxy_engine_type = m.get('DBProxyEngineType')

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

