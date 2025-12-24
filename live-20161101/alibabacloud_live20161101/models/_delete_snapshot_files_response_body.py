# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_live20161101 import models as main_models
from darabonba.model import DaraModel

class DeleteSnapshotFilesResponseBody(DaraModel):
    def __init__(
        self,
        failure_count: int = None,
        request_id: str = None,
        snapshot_delete_info_list: main_models.DeleteSnapshotFilesResponseBodySnapshotDeleteInfoList = None,
        success_count: int = None,
    ):
        # The number of snapshots that failed to be deleted.
        self.failure_count = failure_count
        # The request ID.
        self.request_id = request_id
        # The information about the snapshots.
        self.snapshot_delete_info_list = snapshot_delete_info_list
        # The number of successful screenshot deletions.
        self.success_count = success_count

    def validate(self):
        if self.snapshot_delete_info_list:
            self.snapshot_delete_info_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.failure_count is not None:
            result['FailureCount'] = self.failure_count

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.snapshot_delete_info_list is not None:
            result['SnapshotDeleteInfoList'] = self.snapshot_delete_info_list.to_map()

        if self.success_count is not None:
            result['SuccessCount'] = self.success_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FailureCount') is not None:
            self.failure_count = m.get('FailureCount')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SnapshotDeleteInfoList') is not None:
            temp_model = main_models.DeleteSnapshotFilesResponseBodySnapshotDeleteInfoList()
            self.snapshot_delete_info_list = temp_model.from_map(m.get('SnapshotDeleteInfoList'))

        if m.get('SuccessCount') is not None:
            self.success_count = m.get('SuccessCount')

        return self

class DeleteSnapshotFilesResponseBodySnapshotDeleteInfoList(DaraModel):
    def __init__(
        self,
        snapshot_delete_info: List[main_models.DeleteSnapshotFilesResponseBodySnapshotDeleteInfoListSnapshotDeleteInfo] = None,
    ):
        self.snapshot_delete_info = snapshot_delete_info

    def validate(self):
        if self.snapshot_delete_info:
            for v1 in self.snapshot_delete_info:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['SnapshotDeleteInfo'] = []
        if self.snapshot_delete_info is not None:
            for k1 in self.snapshot_delete_info:
                result['SnapshotDeleteInfo'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.snapshot_delete_info = []
        if m.get('SnapshotDeleteInfo') is not None:
            for k1 in m.get('SnapshotDeleteInfo'):
                temp_model = main_models.DeleteSnapshotFilesResponseBodySnapshotDeleteInfoListSnapshotDeleteInfo()
                self.snapshot_delete_info.append(temp_model.from_map(k1))

        return self

class DeleteSnapshotFilesResponseBodySnapshotDeleteInfoListSnapshotDeleteInfo(DaraModel):
    def __init__(
        self,
        create_timestamp: int = None,
        message: str = None,
    ):
        # The timestamp when the snapshot was captured. Unit: milliseconds.
        self.create_timestamp = create_timestamp
        # The processing result of the snapshot. Valid values:
        # 
        # *   **OK**: The snapshot was deleted.
        # *   **FileNotFound**: The snapshot was not found.
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_timestamp is not None:
            result['CreateTimestamp'] = self.create_timestamp

        if self.message is not None:
            result['Message'] = self.message

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTimestamp') is not None:
            self.create_timestamp = m.get('CreateTimestamp')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        return self

