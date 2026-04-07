# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataworks_public20200518 import models as main_models
from darabonba.model import DaraModel

class ListDeploymentsResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.ListDeploymentsResponseBodyData = None,
        request_id: str = None,
    ):
        # The data returned.
        self.data = data
        # The request ID.
        self.request_id = request_id

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.ListDeploymentsResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListDeploymentsResponseBodyData(DaraModel):
    def __init__(
        self,
        deployments: List[main_models.ListDeploymentsResponseBodyDataDeployments] = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # The deployment packages.
        self.deployments = deployments
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.deployments:
            for v1 in self.deployments:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Deployments'] = []
        if self.deployments is not None:
            for k1 in self.deployments:
                result['Deployments'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.deployments = []
        if m.get('Deployments') is not None:
            for k1 in m.get('Deployments'):
                temp_model = main_models.ListDeploymentsResponseBodyDataDeployments()
                self.deployments.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListDeploymentsResponseBodyDataDeployments(DaraModel):
    def __init__(
        self,
        create_time: int = None,
        creator: str = None,
        error_message: str = None,
        execute_time: int = None,
        executor: str = None,
        id: int = None,
        name: str = None,
        status: int = None,
    ):
        # The time when the deployment package was created.
        self.create_time = create_time
        # The ID of the Alibaba Cloud account used by the user who created the deployment package.
        self.creator = creator
        # The error message returned when the deployment package failed.
        self.error_message = error_message
        # The time when the deployment package was run. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.execute_time = execute_time
        # The ID of the Alibaba Cloud account used by the user who ran the deployment package.
        self.executor = executor
        # The deployment package ID. You can call the [GetDeployment](https://help.aliyun.com/document_detail/173950.html) operation to obtain the ID.
        self.id = id
        # The name of the deployment package.
        self.name = name
        # The status of the deployment package. Valid values:
        # 
        # *   0: The deployment package is ready.
        # *   1: The deployment package is deployed.
        # *   2: The deployment package fails to be deployed.
        # *   6: The deployment package is rejected.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.creator is not None:
            result['Creator'] = self.creator

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.execute_time is not None:
            result['ExecuteTime'] = self.execute_time

        if self.executor is not None:
            result['Executor'] = self.executor

        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Creator') is not None:
            self.creator = m.get('Creator')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('ExecuteTime') is not None:
            self.execute_time = m.get('ExecuteTime')

        if m.get('Executor') is not None:
            self.executor = m.get('Executor')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

