# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_pairecservice20221213 import models as main_models
from darabonba.model import DaraModel

class ListRecallManagementServicesResponseBody(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        recall_management_services: List[main_models.ListRecallManagementServicesResponseBodyRecallManagementServices] = None,
        request_id: str = None,
        total_count: str = None,
    ):
        self.max_results = max_results
        self.next_token = next_token
        self.recall_management_services = recall_management_services
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.recall_management_services:
            for v1 in self.recall_management_services:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        result['RecallManagementServices'] = []
        if self.recall_management_services is not None:
            for k1 in self.recall_management_services:
                result['RecallManagementServices'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        self.recall_management_services = []
        if m.get('RecallManagementServices') is not None:
            for k1 in m.get('RecallManagementServices'):
                temp_model = main_models.ListRecallManagementServicesResponseBodyRecallManagementServices()
                self.recall_management_services.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListRecallManagementServicesResponseBodyRecallManagementServices(DaraModel):
    def __init__(
        self,
        current_recall_management_service_version_id: str = None,
        current_recall_management_service_version_name: str = None,
        description: str = None,
        gmt_create_time: str = None,
        gmt_modified_time: str = None,
        name: str = None,
        recall_management_service_id: str = None,
        status: str = None,
    ):
        self.current_recall_management_service_version_id = current_recall_management_service_version_id
        self.current_recall_management_service_version_name = current_recall_management_service_version_name
        self.description = description
        self.gmt_create_time = gmt_create_time
        self.gmt_modified_time = gmt_modified_time
        self.name = name
        self.recall_management_service_id = recall_management_service_id
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_recall_management_service_version_id is not None:
            result['CurrentRecallManagementServiceVersionId'] = self.current_recall_management_service_version_id

        if self.current_recall_management_service_version_name is not None:
            result['CurrentRecallManagementServiceVersionName'] = self.current_recall_management_service_version_name

        if self.description is not None:
            result['Description'] = self.description

        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time

        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time

        if self.name is not None:
            result['Name'] = self.name

        if self.recall_management_service_id is not None:
            result['RecallManagementServiceId'] = self.recall_management_service_id

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentRecallManagementServiceVersionId') is not None:
            self.current_recall_management_service_version_id = m.get('CurrentRecallManagementServiceVersionId')

        if m.get('CurrentRecallManagementServiceVersionName') is not None:
            self.current_recall_management_service_version_name = m.get('CurrentRecallManagementServiceVersionName')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')

        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('RecallManagementServiceId') is not None:
            self.recall_management_service_id = m.get('RecallManagementServiceId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

