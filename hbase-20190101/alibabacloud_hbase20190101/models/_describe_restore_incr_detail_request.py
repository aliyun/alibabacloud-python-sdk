# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeRestoreIncrDetailRequest(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        restore_record_id: str = None,
    ):
        # The ID of the cluster for backup and recovery.
        # 
        # This parameter is required.
        self.cluster_id = cluster_id
        # The ID of the restoration record. You can call the DescribeRestoreSummary operation to obtain the ID.
        # 
        # This parameter is required.
        self.restore_record_id = restore_record_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.restore_record_id is not None:
            result['RestoreRecordId'] = self.restore_record_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('RestoreRecordId') is not None:
            self.restore_record_id = m.get('RestoreRecordId')

        return self

