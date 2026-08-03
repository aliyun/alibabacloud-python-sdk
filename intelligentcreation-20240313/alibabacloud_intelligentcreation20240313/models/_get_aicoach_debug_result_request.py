# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetAICoachDebugResultRequest(DaraModel):
    def __init__(
        self,
        data_id: str = None,
        data_type: str = None,
        script_debug_id: str = None,
        script_record_id: str = None,
        script_snapshot_id: str = None,
        task_id: str = None,
    ):
        self.data_id = data_id
        self.data_type = data_type
        self.script_debug_id = script_debug_id
        self.script_record_id = script_record_id
        self.script_snapshot_id = script_snapshot_id
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_id is not None:
            result['dataId'] = self.data_id

        if self.data_type is not None:
            result['dataType'] = self.data_type

        if self.script_debug_id is not None:
            result['scriptDebugId'] = self.script_debug_id

        if self.script_record_id is not None:
            result['scriptRecordId'] = self.script_record_id

        if self.script_snapshot_id is not None:
            result['scriptSnapshotId'] = self.script_snapshot_id

        if self.task_id is not None:
            result['taskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dataId') is not None:
            self.data_id = m.get('dataId')

        if m.get('dataType') is not None:
            self.data_type = m.get('dataType')

        if m.get('scriptDebugId') is not None:
            self.script_debug_id = m.get('scriptDebugId')

        if m.get('scriptRecordId') is not None:
            self.script_record_id = m.get('scriptRecordId')

        if m.get('scriptSnapshotId') is not None:
            self.script_snapshot_id = m.get('scriptSnapshotId')

        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')

        return self

