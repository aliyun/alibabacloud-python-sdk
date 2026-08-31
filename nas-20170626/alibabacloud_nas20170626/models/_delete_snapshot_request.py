# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteSnapshotRequest(DaraModel):
    def __init__(
        self,
        snapshot_id: str = None,
    ):
        # The snapshot ID. After you successfully create a snapshot for an Advanced Extreme NAS file system by calling [CreateSnapshot](https://www.alibabacloud.com/help/en/nas/developer-reference/api-nas-2017-06-26-createsnapshot), call [DescribeSnapshots](https://www.alibabacloud.com/help/en/nas/developer-reference/api-nas-2017-06-26-describesnapshots) (with FileSystemType set to extreme) to query the snapshot list and obtain the snapshot ID.
        # 
        # This parameter is required.
        self.snapshot_id = snapshot_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.snapshot_id is not None:
            result['SnapshotId'] = self.snapshot_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SnapshotId') is not None:
            self.snapshot_id = m.get('SnapshotId')

        return self

