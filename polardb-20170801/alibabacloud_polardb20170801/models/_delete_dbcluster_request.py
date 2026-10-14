# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteDBClusterRequest(DaraModel):
    def __init__(
        self,
        backup_retention_policy_on_cluster_deletion: str = None,
        cloud_provider: str = None,
        dbcluster_id: str = None,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The backup data retention policy when the cluster is deleted. Valid values:
        # * **ALL**: Long-term retention (LTR) of all backups.
        # * **LATEST**: Long-term retention (LTR) of the last backup (automatic backup before deletion).
        # * **NONE**: Does not retain any backups when the cluster is deleted.
        self.backup_retention_policy_on_cluster_deletion = backup_retention_policy_on_cluster_deletion
        # The cloud service provider to which the instance belongs.
        self.cloud_provider = cloud_provider
        # The cluster ID.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.backup_retention_policy_on_cluster_deletion is not None:
            result['BackupRetentionPolicyOnClusterDeletion'] = self.backup_retention_policy_on_cluster_deletion

        if self.cloud_provider is not None:
            result['CloudProvider'] = self.cloud_provider

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupRetentionPolicyOnClusterDeletion') is not None:
            self.backup_retention_policy_on_cluster_deletion = m.get('BackupRetentionPolicyOnClusterDeletion')

        if m.get('CloudProvider') is not None:
            self.cloud_provider = m.get('CloudProvider')

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

        return self

