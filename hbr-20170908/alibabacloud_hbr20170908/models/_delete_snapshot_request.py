# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteSnapshotRequest(DaraModel):
    def __init__(
        self,
        client_id: str = None,
        force: bool = None,
        instance_id: str = None,
        snapshot_id: str = None,
        source_type: str = None,
        token: str = None,
        vault_id: str = None,
    ):
        # The client ID. When deleting a backup snapshot of ECS File Backup Essential Edition, you must specify either this parameter or **InstanceId**.
        self.client_id = client_id
        # Deprecated.
        self.force = force
        # The ECS instance ID. When deleting a backup snapshot of ECS File Backup Essential Edition, you must specify either this parameter or **ClientId**.
        self.instance_id = instance_id
        # The backup snapshot ID.
        # 
        # This parameter is required.
        self.snapshot_id = snapshot_id
        # The backup source type. Valid values:
        # 
        # * **ECS_FILE**: backup snapshot of ECS File Backup Essential Edition.
        # * **OSS**: backup snapshot of Alibaba Cloud OSS.
        # * **NAS**: backup snapshot of Alibaba Cloud NAS.
        # * **UDM_ECS**: backup snapshot of an entire ECS instance.
        self.source_type = source_type
        # The token for the deletion.
        self.token = token
        # The backup vault ID.
        self.vault_id = vault_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_id is not None:
            result['ClientId'] = self.client_id

        if self.force is not None:
            result['Force'] = self.force

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.snapshot_id is not None:
            result['SnapshotId'] = self.snapshot_id

        if self.source_type is not None:
            result['SourceType'] = self.source_type

        if self.token is not None:
            result['Token'] = self.token

        if self.vault_id is not None:
            result['VaultId'] = self.vault_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')

        if m.get('Force') is not None:
            self.force = m.get('Force')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('SnapshotId') is not None:
            self.snapshot_id = m.get('SnapshotId')

        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')

        if m.get('Token') is not None:
            self.token = m.get('Token')

        if m.get('VaultId') is not None:
            self.vault_id = m.get('VaultId')

        return self

