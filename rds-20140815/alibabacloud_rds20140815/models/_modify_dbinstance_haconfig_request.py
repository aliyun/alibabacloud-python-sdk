# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyDBInstanceHAConfigRequest(DaraModel):
    def __init__(
        self,
        db_instance_id: str = None,
        hamode: str = None,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        sync_mode: str = None,
    ):
        # The ID of the instance.
        # 
        # This parameter is required.
        self.db_instance_id = db_instance_id
        # The HA mode of the instance.
        # 
        # *   RPO: Data consistency is preferred. The instance ensures data reliability to minimize data losses. If you have high requirements on data consistency, select this mode.
        # *   RTO: Service availability is preferred. The instance restores the database service at the earliest opportunity to ensure service availability. If you have high requirements for service availability, select this mode.
        # 
        # This parameter is required.
        self.hamode = hamode
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The data replication mode of the instance. For more information, see [Data replication mode](https://help.aliyun.com/document_detail/96055.html).
        # 
        # *   Semi-sync: the semi-synchronous mode.
        # *   Sync: the synchronous mode.
        # *   gAsyncg: the asynchronous mode.
        # *   Mgr: the MySQL group replication (MGR) mode. This mode is available only for the China site (aliyun.com).
        # 
        # > This parameter is not supported for instances that run SQL Server 2017 on RDS Cluster Edition.
        # 
        # This parameter is required.
        self.sync_mode = sync_mode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.db_instance_id is not None:
            result['DbInstanceId'] = self.db_instance_id

        if self.hamode is not None:
            result['HAMode'] = self.hamode

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.sync_mode is not None:
            result['SyncMode'] = self.sync_mode

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DbInstanceId') is not None:
            self.db_instance_id = m.get('DbInstanceId')

        if m.get('HAMode') is not None:
            self.hamode = m.get('HAMode')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('SyncMode') is not None:
            self.sync_mode = m.get('SyncMode')

        return self

