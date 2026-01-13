# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_pairecservice20221213 import models as main_models
from darabonba.model import DaraModel

class ListRecallManagementServiceVersionsResponseBody(DaraModel):
    def __init__(
        self,
        recall_management_service_versions: List[main_models.ListRecallManagementServiceVersionsResponseBodyRecallManagementServiceVersions] = None,
        request_id: str = None,
        total_count: str = None,
    ):
        self.recall_management_service_versions = recall_management_service_versions
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.recall_management_service_versions:
            for v1 in self.recall_management_service_versions:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['RecallManagementServiceVersions'] = []
        if self.recall_management_service_versions is not None:
            for k1 in self.recall_management_service_versions:
                result['RecallManagementServiceVersions'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.recall_management_service_versions = []
        if m.get('RecallManagementServiceVersions') is not None:
            for k1 in m.get('RecallManagementServiceVersions'):
                temp_model = main_models.ListRecallManagementServiceVersionsResponseBodyRecallManagementServiceVersions()
                self.recall_management_service_versions.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListRecallManagementServiceVersionsResponseBodyRecallManagementServiceVersions(DaraModel):
    def __init__(
        self,
        gmt_create_time: str = None,
        gmt_modified_time: str = None,
        is_default: str = None,
        name: str = None,
        recall_management_service_version_id: str = None,
    ):
        self.gmt_create_time = gmt_create_time
        self.gmt_modified_time = gmt_modified_time
        self.is_default = is_default
        self.name = name
        self.recall_management_service_version_id = recall_management_service_version_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time

        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time

        if self.is_default is not None:
            result['IsDefault'] = self.is_default

        if self.name is not None:
            result['Name'] = self.name

        if self.recall_management_service_version_id is not None:
            result['RecallManagementServiceVersionId'] = self.recall_management_service_version_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')

        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')

        if m.get('IsDefault') is not None:
            self.is_default = m.get('IsDefault')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('RecallManagementServiceVersionId') is not None:
            self.recall_management_service_version_id = m.get('RecallManagementServiceVersionId')

        return self

