# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_adb20211201 import models as main_models
from darabonba.model import DaraModel

class DescribeApsActionLogsResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        action_logs: List[main_models.DescribeApsActionLogsResponseBodyActionLogs] = None,
        dbcluster_id: str = None,
        page_number: str = None,
        page_size: str = None,
        request_id: str = None,
        total_count: str = None,
        workload_id: str = None,
    ):
        # The information about the request denial.
        self.access_denied_detail = access_denied_detail
        # The queried logs.
        self.action_logs = action_logs
        # The ID of the AnalyticDB for MySQL Data Lakehouse Edition (V3.0) cluster.
        self.dbcluster_id = dbcluster_id
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count
        # The ID of the real-time data ingestion job.
        self.workload_id = workload_id

    def validate(self):
        if self.action_logs:
            for v1 in self.action_logs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail

        result['ActionLogs'] = []
        if self.action_logs is not None:
            for k1 in self.action_logs:
                result['ActionLogs'].append(k1.to_map() if k1 else None)

        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        if self.workload_id is not None:
            result['WorkloadId'] = self.workload_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')

        self.action_logs = []
        if m.get('ActionLogs') is not None:
            for k1 in m.get('ActionLogs'):
                temp_model = main_models.DescribeApsActionLogsResponseBodyActionLogs()
                self.action_logs.append(temp_model.from_map(k1))

        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        if m.get('WorkloadId') is not None:
            self.workload_id = m.get('WorkloadId')

        return self

class DescribeApsActionLogsResponseBodyActionLogs(DaraModel):
    def __init__(
        self,
        context: str = None,
        stage: str = None,
        state: str = None,
        time: str = None,
    ):
        # The content of the log.
        self.context = context
        # The phase during which the log was generated. Valid values:
        # 
        # *   **StructureMigrate**: schema migration.
        # *   **FullDataSync**: full data synchronization.
        # *   **IncrementalSync**: incremental data synchronization.
        self.stage = stage
        # The type of the log. Multiple log types are separated by commas (,). Valid values:
        # 
        # *   **INFO**
        # *   **WARN**
        # *   **ERROR**
        self.state = state
        # The time when the log was generated. The time follows the ISO 8601 standard in the **yyyy-MM-ddTHH:mm:ssZ** format. The time is displayed in UTC.
        self.time = time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.context is not None:
            result['Context'] = self.context

        if self.stage is not None:
            result['Stage'] = self.stage

        if self.state is not None:
            result['State'] = self.state

        if self.time is not None:
            result['Time'] = self.time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Context') is not None:
            self.context = m.get('Context')

        if m.get('Stage') is not None:
            self.stage = m.get('Stage')

        if m.get('State') is not None:
            self.state = m.get('State')

        if m.get('Time') is not None:
            self.time = m.get('Time')

        return self

