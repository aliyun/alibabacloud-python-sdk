# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataworks_public20240518 import models as main_models
from darabonba.model import DaraModel

class GetDeploymentPackageResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.GetDeploymentPackageResponseBodyData = None,
        error_code: str = None,
        error_message: str = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The deployment package details.
        self.data = data
        # The error code.
        self.error_code = error_code
        # The error message.
        self.error_message = error_message
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The request ID. Use this ID to locate logs and troubleshoot issues.
        self.request_id = request_id
        # Indicates whether the call succeeded. Valid values:
        # 
        # *   **true**
        # *   **false**
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

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.GetDeploymentPackageResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetDeploymentPackageResponseBodyData(DaraModel):
    def __init__(
        self,
        deployed_items: List[main_models.GetDeploymentPackageResponseBodyDataDeployedItems] = None,
        deployment: main_models.GetDeploymentPackageResponseBodyDataDeployment = None,
    ):
        # The deployment item details.
        self.deployed_items = deployed_items
        # The deployment package details.
        self.deployment = deployment

    def validate(self):
        if self.deployed_items:
            for v1 in self.deployed_items:
                 if v1:
                    v1.validate()
        if self.deployment:
            self.deployment.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DeployedItems'] = []
        if self.deployed_items is not None:
            for k1 in self.deployed_items:
                result['DeployedItems'].append(k1.to_map() if k1 else None)

        if self.deployment is not None:
            result['Deployment'] = self.deployment.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.deployed_items = []
        if m.get('DeployedItems') is not None:
            for k1 in m.get('DeployedItems'):
                temp_model = main_models.GetDeploymentPackageResponseBodyDataDeployedItems()
                self.deployed_items.append(temp_model.from_map(k1))

        if m.get('Deployment') is not None:
            temp_model = main_models.GetDeploymentPackageResponseBodyDataDeployment()
            self.deployment = temp_model.from_map(m.get('Deployment'))

        return self

class GetDeploymentPackageResponseBodyDataDeployment(DaraModel):
    def __init__(
        self,
        checking_status: int = None,
        create_time: int = None,
        creator_id: str = None,
        error_message: str = None,
        execute_time: int = None,
        from_environment: int = None,
        handler_id: str = None,
        name: str = None,
        status: int = None,
        to_environment: int = None,
    ):
        # The validation status of nodes in the deployment package. For packages deployed to the development environment (toEnviroment=1), you can only proceed to deploy to production if the package Status is 1 (succeeded) and CheckingStatus is empty (validation complete).
        # 
        # *   7: Validation failed
        # *   8: Validation in progress
        self.checking_status = checking_status
        # The timestamp (in milliseconds) when the deployment package was created.
        self.create_time = create_time
        # The Alibaba Cloud account ID of the user who created the deployment package.
        self.creator_id = creator_id
        # The detailed error message when the deployment package fails (status is 2).
        self.error_message = error_message
        # The timestamp (in milliseconds) when the deployment started.
        self.execute_time = execute_time
        # The environment where the deployment is executed. Valid values: 0 (local) and 1 (development).
        self.from_environment = from_environment
        # The Alibaba Cloud account ID of the user who executed the deployment.
        self.handler_id = handler_id
        # The deployment package name, displayed on the Deploy Center > Deployment Packages page.
        self.name = name
        # The current status of the deployment package. Valid values: 0 (ready), 1 (succeeded), and 2 (failed).
        self.status = status
        # The target environment for the deployment. Valid values: 1 (development) and 2 (production).
        self.to_environment = to_environment

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.checking_status is not None:
            result['CheckingStatus'] = self.checking_status

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.creator_id is not None:
            result['CreatorId'] = self.creator_id

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.execute_time is not None:
            result['ExecuteTime'] = self.execute_time

        if self.from_environment is not None:
            result['FromEnvironment'] = self.from_environment

        if self.handler_id is not None:
            result['HandlerId'] = self.handler_id

        if self.name is not None:
            result['Name'] = self.name

        if self.status is not None:
            result['Status'] = self.status

        if self.to_environment is not None:
            result['ToEnvironment'] = self.to_environment

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckingStatus') is not None:
            self.checking_status = m.get('CheckingStatus')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('CreatorId') is not None:
            self.creator_id = m.get('CreatorId')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('ExecuteTime') is not None:
            self.execute_time = m.get('ExecuteTime')

        if m.get('FromEnvironment') is not None:
            self.from_environment = m.get('FromEnvironment')

        if m.get('HandlerId') is not None:
            self.handler_id = m.get('HandlerId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('ToEnvironment') is not None:
            self.to_environment = m.get('ToEnvironment')

        return self

class GetDeploymentPackageResponseBodyDataDeployedItems(DaraModel):
    def __init__(
        self,
        file_id: int = None,
        file_version: int = None,
        status: int = None,
    ):
        # The file ID.
        self.file_id = file_id
        # The file version.
        self.file_version = file_version
        # *   UNPUBLISHED(0)
        # *   SUCCESS(1)
        # *   ERROR(2)
        # *   CLONED(3)
        # *   DEPLOY_ERROR(4)
        # *   CLONING(5)
        # *   REJECT(6)
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.file_id is not None:
            result['FileId'] = self.file_id

        if self.file_version is not None:
            result['FileVersion'] = self.file_version

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileId') is not None:
            self.file_id = m.get('FileId')

        if m.get('FileVersion') is not None:
            self.file_version = m.get('FileVersion')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

