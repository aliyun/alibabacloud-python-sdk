# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class ListStreamInstanceRecordsResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: List[main_models.ListStreamInstanceRecordsResponseBodyData] = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The backend response code.
        self.code = code
        # The historical running instance records of the real-time task. You can use the deploymentInstanceId to query the logs of a specific run.
        self.data = data
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The details of the backend response exception.
        self.message = message
        # Id of the request
        self.request_id = request_id
        # Indicates whether the request is successful.
        self.success = success

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.ListStreamInstanceRecordsResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListStreamInstanceRecordsResponseBodyData(DaraModel):
    def __init__(
        self,
        deployment_id: str = None,
        deployment_instance_id: str = None,
        error_data_path: str = None,
        start_time: str = None,
        state: str = None,
    ):
        # The deployment ID of the task. A single deployment can be associated with multiple running instances.
        self.deployment_id = deployment_id
        # The instance ID of the deployment running instance. This value corresponds to the DeploymentInstanceId request parameter in the log and TaskManager query operations.
        self.deployment_instance_id = deployment_instance_id
        # The relative path for dirty data storage in this run, excluding the storage service domain name. A value of null indicates that no dirty data path exists.
        self.error_data_path = error_data_path
        # The start time of this run. Format: yyyy-MM-dd HH:mm:ss.
        self.start_time = start_time
        # The running instance status returned by the engine, such as RUNNING, FINISHED, and TRANSITIONING. This status uses a different enumeration from the TaskStatusEnum returned by the GetStreamTask operation.
        self.state = state

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.deployment_id is not None:
            result['DeploymentId'] = self.deployment_id

        if self.deployment_instance_id is not None:
            result['DeploymentInstanceId'] = self.deployment_instance_id

        if self.error_data_path is not None:
            result['ErrorDataPath'] = self.error_data_path

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.state is not None:
            result['State'] = self.state

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeploymentId') is not None:
            self.deployment_id = m.get('DeploymentId')

        if m.get('DeploymentInstanceId') is not None:
            self.deployment_instance_id = m.get('DeploymentInstanceId')

        if m.get('ErrorDataPath') is not None:
            self.error_data_path = m.get('ErrorDataPath')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('State') is not None:
            self.state = m.get('State')

        return self

