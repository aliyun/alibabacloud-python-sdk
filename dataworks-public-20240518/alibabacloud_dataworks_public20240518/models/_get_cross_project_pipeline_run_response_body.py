# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dataworks_public20240518 import models as main_models
from darabonba.model import DaraModel

class GetCrossProjectPipelineRunResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.GetCrossProjectPipelineRunResponseBodyData = None,
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
            temp_model = main_models.GetCrossProjectPipelineRunResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetCrossProjectPipelineRunResponseBodyData(DaraModel):
    def __init__(
        self,
        abolish_time: int = None,
        abolisher: str = None,
        change_type: str = None,
        create_time: int = None,
        creator: str = None,
        deployment_environment_id: int = None,
        description: str = None,
        error_code: str = None,
        error_message: str = None,
        execute_time: int = None,
        executor: str = None,
        finish_time: int = None,
        object_id: str = None,
        object_name: str = None,
        object_type: str = None,
        object_version: str = None,
        pipeline_run_id: str = None,
        request_id: str = None,
        status: str = None,
    ):
        # The termination time. This value is a UNIX timestamp in milliseconds. This parameter is returned only after the flow is terminated.
        self.abolish_time = abolish_time
        # The user who terminated the flow.
        self.abolisher = abolisher
        # The change type.
        self.change_type = change_type
        # The creation time. This value is a UNIX timestamp in milliseconds.
        self.create_time = create_time
        # The creator.
        self.creator = creator
        # The cross-workspace deployment environment ID.
        self.deployment_environment_id = deployment_environment_id
        # The deployment description.
        self.description = description
        # The error code.
        self.error_code = error_code
        # The error message.
        self.error_message = error_message
        # The execution time. This value is a UNIX timestamp in milliseconds.
        self.execute_time = execute_time
        # The executor.
        self.executor = executor
        # The completion time. This value is a UNIX timestamp in milliseconds.
        self.finish_time = finish_time
        # The ID of the deployment object.
        self.object_id = object_id
        # The name of the deployment object.
        self.object_name = object_name
        # The object type of the publish object.
        self.object_type = object_type
        # The version of the deployment object.
        self.object_version = object_version
        # The cross-workspace deployment flow ID.
        self.pipeline_run_id = pipeline_run_id
        # The request ID.
        self.request_id = request_id
        # The status of the deployment flow. Valid values:
        # - Building: Building.
        # - Ready: Ready and waiting for execution.
        # - Running: Running.
        # - Termination: Terminated.
        # - Success: Execution succeeded.
        # - Fail: Execution failed.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.abolish_time is not None:
            result['AbolishTime'] = self.abolish_time

        if self.abolisher is not None:
            result['Abolisher'] = self.abolisher

        if self.change_type is not None:
            result['ChangeType'] = self.change_type

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.creator is not None:
            result['Creator'] = self.creator

        if self.deployment_environment_id is not None:
            result['DeploymentEnvironmentId'] = self.deployment_environment_id

        if self.description is not None:
            result['Description'] = self.description

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.execute_time is not None:
            result['ExecuteTime'] = self.execute_time

        if self.executor is not None:
            result['Executor'] = self.executor

        if self.finish_time is not None:
            result['FinishTime'] = self.finish_time

        if self.object_id is not None:
            result['ObjectId'] = self.object_id

        if self.object_name is not None:
            result['ObjectName'] = self.object_name

        if self.object_type is not None:
            result['ObjectType'] = self.object_type

        if self.object_version is not None:
            result['ObjectVersion'] = self.object_version

        if self.pipeline_run_id is not None:
            result['PipelineRunId'] = self.pipeline_run_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AbolishTime') is not None:
            self.abolish_time = m.get('AbolishTime')

        if m.get('Abolisher') is not None:
            self.abolisher = m.get('Abolisher')

        if m.get('ChangeType') is not None:
            self.change_type = m.get('ChangeType')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Creator') is not None:
            self.creator = m.get('Creator')

        if m.get('DeploymentEnvironmentId') is not None:
            self.deployment_environment_id = m.get('DeploymentEnvironmentId')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('ExecuteTime') is not None:
            self.execute_time = m.get('ExecuteTime')

        if m.get('Executor') is not None:
            self.executor = m.get('Executor')

        if m.get('FinishTime') is not None:
            self.finish_time = m.get('FinishTime')

        if m.get('ObjectId') is not None:
            self.object_id = m.get('ObjectId')

        if m.get('ObjectName') is not None:
            self.object_name = m.get('ObjectName')

        if m.get('ObjectType') is not None:
            self.object_type = m.get('ObjectType')

        if m.get('ObjectVersion') is not None:
            self.object_version = m.get('ObjectVersion')

        if m.get('PipelineRunId') is not None:
            self.pipeline_run_id = m.get('PipelineRunId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

