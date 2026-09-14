# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataworks_public20240518 import models as main_models
from darabonba.model import DaraModel

class ListCrossProjectDeploymentEnvironmentsResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.ListCrossProjectDeploymentEnvironmentsResponseBodyData = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The business response.
        self.data = data
        # The request ID, which is used to locate and troubleshoot this API call.
        self.request_id = request_id
        # Indicates whether the request was successful.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.ListCrossProjectDeploymentEnvironmentsResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListCrossProjectDeploymentEnvironmentsResponseBodyData(DaraModel):
    def __init__(
        self,
        deployment_environments: List[main_models.ListCrossProjectDeploymentEnvironmentsResponseBodyDataDeploymentEnvironments] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The list of enabled cross-workspace deployment environments in the source project.
        self.deployment_environments = deployment_environments
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of records.
        self.total_count = total_count

    def validate(self):
        if self.deployment_environments:
            for v1 in self.deployment_environments:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DeploymentEnvironments'] = []
        if self.deployment_environments is not None:
            for k1 in self.deployment_environments:
                result['DeploymentEnvironments'].append(k1.to_map() if k1 else None)

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
        self.deployment_environments = []
        if m.get('DeploymentEnvironments') is not None:
            for k1 in m.get('DeploymentEnvironments'):
                temp_model = main_models.ListCrossProjectDeploymentEnvironmentsResponseBodyDataDeploymentEnvironments()
                self.deployment_environments.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListCrossProjectDeploymentEnvironmentsResponseBodyDataDeploymentEnvironments(DaraModel):
    def __init__(
        self,
        deployment_environment_id: int = None,
        name: str = None,
        source_project_id: int = None,
        status: str = None,
        target_project_id: int = None,
        target_project_name: str = None,
    ):
        # The cross-workspace deployment environment ID.
        self.deployment_environment_id = deployment_environment_id
        # The environment name.
        self.name = name
        # The source project workspace ID.
        self.source_project_id = source_project_id
        # The environment status.
        self.status = status
        # The target project workspace ID.
        self.target_project_id = target_project_id
        # The target project workspace name.
        self.target_project_name = target_project_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.deployment_environment_id is not None:
            result['DeploymentEnvironmentId'] = self.deployment_environment_id

        if self.name is not None:
            result['Name'] = self.name

        if self.source_project_id is not None:
            result['SourceProjectId'] = self.source_project_id

        if self.status is not None:
            result['Status'] = self.status

        if self.target_project_id is not None:
            result['TargetProjectId'] = self.target_project_id

        if self.target_project_name is not None:
            result['TargetProjectName'] = self.target_project_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeploymentEnvironmentId') is not None:
            self.deployment_environment_id = m.get('DeploymentEnvironmentId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('SourceProjectId') is not None:
            self.source_project_id = m.get('SourceProjectId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TargetProjectId') is not None:
            self.target_project_id = m.get('TargetProjectId')

        if m.get('TargetProjectName') is not None:
            self.target_project_name = m.get('TargetProjectName')

        return self

