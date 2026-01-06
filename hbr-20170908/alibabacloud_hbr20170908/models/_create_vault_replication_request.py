# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateVaultReplicationRequest(DaraModel):
    def __init__(
        self,
        replication_source_region_id: str = None,
        replication_source_vault_id: str = None,
        replication_target_vault_id: str = None,
    ):
        self.replication_source_region_id = replication_source_region_id
        # This parameter is required.
        self.replication_source_vault_id = replication_source_vault_id
        # This parameter is required.
        self.replication_target_vault_id = replication_target_vault_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.replication_source_region_id is not None:
            result['ReplicationSourceRegionId'] = self.replication_source_region_id

        if self.replication_source_vault_id is not None:
            result['ReplicationSourceVaultId'] = self.replication_source_vault_id

        if self.replication_target_vault_id is not None:
            result['ReplicationTargetVaultId'] = self.replication_target_vault_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ReplicationSourceRegionId') is not None:
            self.replication_source_region_id = m.get('ReplicationSourceRegionId')

        if m.get('ReplicationSourceVaultId') is not None:
            self.replication_source_vault_id = m.get('ReplicationSourceVaultId')

        if m.get('ReplicationTargetVaultId') is not None:
            self.replication_target_vault_id = m.get('ReplicationTargetVaultId')

        return self

