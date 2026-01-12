# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpgradeMinorVersionRequest(DaraModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        upgrade_immediately: bool = None,
        upgrade_time: str = None,
        upgrade_version: str = None,
    ):
        # The cluster ID.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # Specifies whether to update the minor engine version of the ApsaraDB for ClickHouse cluster immediately. Valid values:
        # 
        # *   **true**: updates the minor engine version of the ApsaraDB for ClickHouse cluster immediately.
        # *   **false**: updates the minor engine version of the ApsaraDB for ClickHouse cluster at the specified time or within the specified maintenance window.
        # 
        # >  If you want to update the minor engine version of the ApsaraDB for ClickHouse cluster at the specified time, **UpgradeTime** is required.
        # 
        # This parameter is required.
        self.upgrade_immediately = upgrade_immediately
        # The update time. Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mmZ format. The time must be in Coordinated Universal Time (UTC).
        # 
        # >  If you do not set this parameter, the minor engine version of an ApsaraDB for ClickHouse cluster is updated within the specified maintenance window.
        self.upgrade_time = upgrade_time
        # The minor engine version to which you want to update.
        # 
        # >  By default, UpgradeVersion is not set and the minor engine version of the ApsaraDB for ClickHouse cluster is updated to the latest version.
        self.upgrade_version = upgrade_version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.upgrade_immediately is not None:
            result['UpgradeImmediately'] = self.upgrade_immediately

        if self.upgrade_time is not None:
            result['UpgradeTime'] = self.upgrade_time

        if self.upgrade_version is not None:
            result['UpgradeVersion'] = self.upgrade_version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('UpgradeImmediately') is not None:
            self.upgrade_immediately = m.get('UpgradeImmediately')

        if m.get('UpgradeTime') is not None:
            self.upgrade_time = m.get('UpgradeTime')

        if m.get('UpgradeVersion') is not None:
            self.upgrade_version = m.get('UpgradeVersion')

        return self

