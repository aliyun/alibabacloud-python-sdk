# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_nas20170626 import models as main_models
from darabonba.model import DaraModel

class DescribeAutoSnapshotTasksResponseBody(DaraModel):
    def __init__(
        self,
        auto_snapshot_tasks: main_models.DescribeAutoSnapshotTasksResponseBodyAutoSnapshotTasks = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The queried automatic snapshot tasks.
        self.auto_snapshot_tasks = auto_snapshot_tasks
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of automatic snapshot tasks.
        self.total_count = total_count

    def validate(self):
        if self.auto_snapshot_tasks:
            self.auto_snapshot_tasks.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_snapshot_tasks is not None:
            result['AutoSnapshotTasks'] = self.auto_snapshot_tasks.to_map()

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoSnapshotTasks') is not None:
            temp_model = main_models.DescribeAutoSnapshotTasksResponseBodyAutoSnapshotTasks()
            self.auto_snapshot_tasks = temp_model.from_map(m.get('AutoSnapshotTasks'))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeAutoSnapshotTasksResponseBodyAutoSnapshotTasks(DaraModel):
    def __init__(
        self,
        auto_snapshot_task: List[main_models.DescribeAutoSnapshotTasksResponseBodyAutoSnapshotTasksAutoSnapshotTask] = None,
    ):
        self.auto_snapshot_task = auto_snapshot_task

    def validate(self):
        if self.auto_snapshot_task:
            for v1 in self.auto_snapshot_task:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AutoSnapshotTask'] = []
        if self.auto_snapshot_task is not None:
            for k1 in self.auto_snapshot_task:
                result['AutoSnapshotTask'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.auto_snapshot_task = []
        if m.get('AutoSnapshotTask') is not None:
            for k1 in m.get('AutoSnapshotTask'):
                temp_model = main_models.DescribeAutoSnapshotTasksResponseBodyAutoSnapshotTasksAutoSnapshotTask()
                self.auto_snapshot_task.append(temp_model.from_map(k1))

        return self

class DescribeAutoSnapshotTasksResponseBodyAutoSnapshotTasksAutoSnapshotTask(DaraModel):
    def __init__(
        self,
        auto_snapshot_policy_id: str = None,
        source_file_system_id: str = None,
    ):
        # The ID of the automatic snapshot policy.
        self.auto_snapshot_policy_id = auto_snapshot_policy_id
        # The ID of the file system.
        self.source_file_system_id = source_file_system_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_snapshot_policy_id is not None:
            result['AutoSnapshotPolicyId'] = self.auto_snapshot_policy_id

        if self.source_file_system_id is not None:
            result['SourceFileSystemId'] = self.source_file_system_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoSnapshotPolicyId') is not None:
            self.auto_snapshot_policy_id = m.get('AutoSnapshotPolicyId')

        if m.get('SourceFileSystemId') is not None:
            self.source_file_system_id = m.get('SourceFileSystemId')

        return self

