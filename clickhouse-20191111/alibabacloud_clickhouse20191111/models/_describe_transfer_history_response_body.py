# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_clickhouse20191111 import models as main_models
from darabonba.model import DaraModel

class DescribeTransferHistoryResponseBody(DaraModel):
    def __init__(
        self,
        history_details: main_models.DescribeTransferHistoryResponseBodyHistoryDetails = None,
        request_id: str = None,
    ):
        # The migration information.
        self.history_details = history_details
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.history_details:
            self.history_details.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.history_details is not None:
            result['HistoryDetails'] = self.history_details.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HistoryDetails') is not None:
            temp_model = main_models.DescribeTransferHistoryResponseBodyHistoryDetails()
            self.history_details = temp_model.from_map(m.get('HistoryDetails'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeTransferHistoryResponseBodyHistoryDetails(DaraModel):
    def __init__(
        self,
        history_detail: List[main_models.DescribeTransferHistoryResponseBodyHistoryDetailsHistoryDetail] = None,
    ):
        self.history_detail = history_detail

    def validate(self):
        if self.history_detail:
            for v1 in self.history_detail:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['HistoryDetail'] = []
        if self.history_detail is not None:
            for k1 in self.history_detail:
                result['HistoryDetail'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.history_detail = []
        if m.get('HistoryDetail') is not None:
            for k1 in m.get('HistoryDetail'):
                temp_model = main_models.DescribeTransferHistoryResponseBodyHistoryDetailsHistoryDetail()
                self.history_detail.append(temp_model.from_map(k1))

        return self

class DescribeTransferHistoryResponseBodyHistoryDetailsHistoryDetail(DaraModel):
    def __init__(
        self,
        bytes_per_minute: int = None,
        disable_write_windows: str = None,
        parts_per_minute: float = None,
        progress: str = None,
        source_control_version: str = None,
        source_dbcluster: str = None,
        status: str = None,
        sub_job: str = None,
        sub_job_message: str = None,
        sub_job_status: str = None,
        target_control_version: str = None,
        target_dbcluster: str = None,
        unsynced_bytes: int = None,
        unsynced_parts: int = None,
    ):
        # The amount of data that is migrated per minute.
        self.bytes_per_minute = bytes_per_minute
        # The time window during which write operations are stopped.
        self.disable_write_windows = disable_write_windows
        # The number of parts that are migrated per minute.
        self.parts_per_minute = parts_per_minute
        # The progress of the data migration.
        self.progress = progress
        # The control version of the source cluster.
        self.source_control_version = source_control_version
        # The ID of the source cluster.
        self.source_dbcluster = source_dbcluster
        # The status of the data migration task. Valid values:
        # 
        # *   **Finished**: The data migration task is complete.
        # *   **Processing**: The data migration task is in progress.
        self.status = status
        # The running subtask.
        self.sub_job = sub_job
        self.sub_job_message = sub_job_message
        # The subtask status.
        self.sub_job_status = sub_job_status
        # The control version of the destination cluster.
        self.target_control_version = target_control_version
        # The ID of the destination cluster.
        self.target_dbcluster = target_dbcluster
        # The amount of data that is not migrated.
        self.unsynced_bytes = unsynced_bytes
        # The number of parts that are not migrated.
        self.unsynced_parts = unsynced_parts

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bytes_per_minute is not None:
            result['BytesPerMinute'] = self.bytes_per_minute

        if self.disable_write_windows is not None:
            result['DisableWriteWindows'] = self.disable_write_windows

        if self.parts_per_minute is not None:
            result['PartsPerMinute'] = self.parts_per_minute

        if self.progress is not None:
            result['Progress'] = self.progress

        if self.source_control_version is not None:
            result['SourceControlVersion'] = self.source_control_version

        if self.source_dbcluster is not None:
            result['SourceDBCluster'] = self.source_dbcluster

        if self.status is not None:
            result['Status'] = self.status

        if self.sub_job is not None:
            result['SubJob'] = self.sub_job

        if self.sub_job_message is not None:
            result['SubJobMessage'] = self.sub_job_message

        if self.sub_job_status is not None:
            result['SubJobStatus'] = self.sub_job_status

        if self.target_control_version is not None:
            result['TargetControlVersion'] = self.target_control_version

        if self.target_dbcluster is not None:
            result['TargetDBCluster'] = self.target_dbcluster

        if self.unsynced_bytes is not None:
            result['UnsyncedBytes'] = self.unsynced_bytes

        if self.unsynced_parts is not None:
            result['UnsyncedParts'] = self.unsynced_parts

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BytesPerMinute') is not None:
            self.bytes_per_minute = m.get('BytesPerMinute')

        if m.get('DisableWriteWindows') is not None:
            self.disable_write_windows = m.get('DisableWriteWindows')

        if m.get('PartsPerMinute') is not None:
            self.parts_per_minute = m.get('PartsPerMinute')

        if m.get('Progress') is not None:
            self.progress = m.get('Progress')

        if m.get('SourceControlVersion') is not None:
            self.source_control_version = m.get('SourceControlVersion')

        if m.get('SourceDBCluster') is not None:
            self.source_dbcluster = m.get('SourceDBCluster')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('SubJob') is not None:
            self.sub_job = m.get('SubJob')

        if m.get('SubJobMessage') is not None:
            self.sub_job_message = m.get('SubJobMessage')

        if m.get('SubJobStatus') is not None:
            self.sub_job_status = m.get('SubJobStatus')

        if m.get('TargetControlVersion') is not None:
            self.target_control_version = m.get('TargetControlVersion')

        if m.get('TargetDBCluster') is not None:
            self.target_dbcluster = m.get('TargetDBCluster')

        if m.get('UnsyncedBytes') is not None:
            self.unsynced_bytes = m.get('UnsyncedBytes')

        if m.get('UnsyncedParts') is not None:
            self.unsynced_parts = m.get('UnsyncedParts')

        return self

