# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_pairecservice20221213 import models as main_models
from darabonba.model import DaraModel

class GetRecallManagementJobResponseBody(DaraModel):
    def __init__(
        self,
        end_time: str = None,
        log: str = None,
        recall_management_job_id: str = None,
        recall_manager_table_info: main_models.GetRecallManagementJobResponseBodyRecallManagerTableInfo = None,
        request_id: str = None,
        start_time: str = None,
        status: str = None,
    ):
        self.end_time = end_time
        self.log = log
        self.recall_management_job_id = recall_management_job_id
        self.recall_manager_table_info = recall_manager_table_info
        self.request_id = request_id
        self.start_time = start_time
        self.status = status

    def validate(self):
        if self.recall_manager_table_info:
            self.recall_manager_table_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.log is not None:
            result['Log'] = self.log

        if self.recall_management_job_id is not None:
            result['RecallManagementJobId'] = self.recall_management_job_id

        if self.recall_manager_table_info is not None:
            result['RecallManagerTableInfo'] = self.recall_manager_table_info.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Log') is not None:
            self.log = m.get('Log')

        if m.get('RecallManagementJobId') is not None:
            self.recall_management_job_id = m.get('RecallManagementJobId')

        if m.get('RecallManagerTableInfo') is not None:
            temp_model = main_models.GetRecallManagementJobResponseBodyRecallManagerTableInfo()
            self.recall_manager_table_info = temp_model.from_map(m.get('RecallManagerTableInfo'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class GetRecallManagementJobResponseBodyRecallManagerTableInfo(DaraModel):
    def __init__(
        self,
        data_version: str = None,
        recall_manager_table_version_id: str = None,
        source_table_data_size: str = None,
        source_table_row_count: str = None,
    ):
        self.data_version = data_version
        self.recall_manager_table_version_id = recall_manager_table_version_id
        self.source_table_data_size = source_table_data_size
        self.source_table_row_count = source_table_row_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_version is not None:
            result['DataVersion'] = self.data_version

        if self.recall_manager_table_version_id is not None:
            result['RecallManagerTableVersionId'] = self.recall_manager_table_version_id

        if self.source_table_data_size is not None:
            result['SourceTableDataSize'] = self.source_table_data_size

        if self.source_table_row_count is not None:
            result['SourceTableRowCount'] = self.source_table_row_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataVersion') is not None:
            self.data_version = m.get('DataVersion')

        if m.get('RecallManagerTableVersionId') is not None:
            self.recall_manager_table_version_id = m.get('RecallManagerTableVersionId')

        if m.get('SourceTableDataSize') is not None:
            self.source_table_data_size = m.get('SourceTableDataSize')

        if m.get('SourceTableRowCount') is not None:
            self.source_table_row_count = m.get('SourceTableRowCount')

        return self

