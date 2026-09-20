# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeBackupStatusResponseBody(DaraModel):
    def __init__(
        self,
        backup_status: str = None,
        bds_cluster_id: str = None,
        cluster_id: str = None,
        request_id: str = None,
    ):
        # The enabling status of backup. Valid values:
        # - closed: not enabled.
        # - opened: enabled.
        # - opening: being enabled.
        self.backup_status = backup_status
        # The instance ID of the BDS instance used for backup.
        self.bds_cluster_id = bds_cluster_id
        # The ID of the backup cluster.
        self.cluster_id = cluster_id
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.backup_status is not None:
            result['BackupStatus'] = self.backup_status

        if self.bds_cluster_id is not None:
            result['BdsClusterId'] = self.bds_cluster_id

        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupStatus') is not None:
            self.backup_status = m.get('BackupStatus')

        if m.get('BdsClusterId') is not None:
            self.bds_cluster_id = m.get('BdsClusterId')

        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

