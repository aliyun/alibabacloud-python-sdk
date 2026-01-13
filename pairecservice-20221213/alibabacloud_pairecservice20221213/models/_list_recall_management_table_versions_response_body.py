# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_pairecservice20221213 import models as main_models
from darabonba.model import DaraModel

class ListRecallManagementTableVersionsResponseBody(DaraModel):
    def __init__(
        self,
        recall_management_table_versions: List[main_models.ListRecallManagementTableVersionsResponseBodyRecallManagementTableVersions] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.recall_management_table_versions = recall_management_table_versions
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.recall_management_table_versions:
            for v1 in self.recall_management_table_versions:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['RecallManagementTableVersions'] = []
        if self.recall_management_table_versions is not None:
            for k1 in self.recall_management_table_versions:
                result['RecallManagementTableVersions'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.recall_management_table_versions = []
        if m.get('RecallManagementTableVersions') is not None:
            for k1 in m.get('RecallManagementTableVersions'):
                temp_model = main_models.ListRecallManagementTableVersionsResponseBodyRecallManagementTableVersions()
                self.recall_management_table_versions.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListRecallManagementTableVersionsResponseBodyRecallManagementTableVersions(DaraModel):
    def __init__(
        self,
        data_version: str = None,
        effective_time: str = None,
        publish_end_time: str = None,
        publish_start_time: str = None,
        recall_management_table_version_id: str = None,
        source_table_data_size: int = None,
        source_table_row_count: int = None,
        status: str = None,
    ):
        self.data_version = data_version
        self.effective_time = effective_time
        self.publish_end_time = publish_end_time
        self.publish_start_time = publish_start_time
        self.recall_management_table_version_id = recall_management_table_version_id
        self.source_table_data_size = source_table_data_size
        self.source_table_row_count = source_table_row_count
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_version is not None:
            result['DataVersion'] = self.data_version

        if self.effective_time is not None:
            result['EffectiveTime'] = self.effective_time

        if self.publish_end_time is not None:
            result['PublishEndTime'] = self.publish_end_time

        if self.publish_start_time is not None:
            result['PublishStartTime'] = self.publish_start_time

        if self.recall_management_table_version_id is not None:
            result['RecallManagementTableVersionId'] = self.recall_management_table_version_id

        if self.source_table_data_size is not None:
            result['SourceTableDataSize'] = self.source_table_data_size

        if self.source_table_row_count is not None:
            result['SourceTableRowCount'] = self.source_table_row_count

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataVersion') is not None:
            self.data_version = m.get('DataVersion')

        if m.get('EffectiveTime') is not None:
            self.effective_time = m.get('EffectiveTime')

        if m.get('PublishEndTime') is not None:
            self.publish_end_time = m.get('PublishEndTime')

        if m.get('PublishStartTime') is not None:
            self.publish_start_time = m.get('PublishStartTime')

        if m.get('RecallManagementTableVersionId') is not None:
            self.recall_management_table_version_id = m.get('RecallManagementTableVersionId')

        if m.get('SourceTableDataSize') is not None:
            self.source_table_data_size = m.get('SourceTableDataSize')

        if m.get('SourceTableRowCount') is not None:
            self.source_table_row_count = m.get('SourceTableRowCount')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

