# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class ListStreamOpsRecordsResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: List[main_models.ListStreamOpsRecordsResponseBodyData] = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The backend response code.
        self.code = code
        # The start and stop operation records of real-time tasks.
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
                temp_model = main_models.ListStreamOpsRecordsResponseBodyData()
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

class ListStreamOpsRecordsResponseBodyData(DaraModel):
    def __init__(
        self,
        deployment_id: str = None,
        deployment_instance_id: str = None,
        end_time: str = None,
        log_content: str = None,
        operate: str = None,
        ops_record_id: str = None,
        start_time: str = None,
    ):
        # deploymentId
        self.deployment_id = deployment_id
        # deploymentInstanceId
        self.deployment_instance_id = deployment_instance_id
        # The end time.
        self.end_time = end_time
        # The log content.
        self.log_content = log_content
        # The instance status. Valid values: START, PAUSE, RESUME, and STOP. Displayed as Start, Pause, Recover, or Stop.
        self.operate = operate
        # opsRecordId
        self.ops_record_id = ops_record_id
        # The start time.
        self.start_time = start_time

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

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.log_content is not None:
            result['LogContent'] = self.log_content

        if self.operate is not None:
            result['Operate'] = self.operate

        if self.ops_record_id is not None:
            result['OpsRecordId'] = self.ops_record_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeploymentId') is not None:
            self.deployment_id = m.get('DeploymentId')

        if m.get('DeploymentInstanceId') is not None:
            self.deployment_instance_id = m.get('DeploymentInstanceId')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('LogContent') is not None:
            self.log_content = m.get('LogContent')

        if m.get('Operate') is not None:
            self.operate = m.get('Operate')

        if m.get('OpsRecordId') is not None:
            self.ops_record_id = m.get('OpsRecordId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

