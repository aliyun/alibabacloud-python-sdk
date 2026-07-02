# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Any

from alibabacloud_sysom20231230 import models as main_models
from darabonba.model import DaraModel

class GetAgentTaskResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        code: str = None,
        data: main_models.GetAgentTaskResponseBodyData = None,
        message: str = None,
    ):
        # The request ID, which can be used for end-to-end diagnostics.
        self.request_id = request_id
        # The status code.
        # - `code == Success` indicates that the authorization is successful.
        # - Other status codes indicate that the authorization failed. Check the `message` field for the detailed fault message.
        self.code = code
        # The returned data.
        self.data = data
        # The error message.
        # - If `code == Success`, this field is empty.
        # - Otherwise, this field contains the request error information.
        self.message = message

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.code is not None:
            result['code'] = self.code

        if self.data is not None:
            result['data'] = self.data.to_map()

        if self.message is not None:
            result['message'] = self.message

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('data') is not None:
            temp_model = main_models.GetAgentTaskResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('message') is not None:
            self.message = m.get('message')

        return self

class GetAgentTaskResponseBodyData(DaraModel):
    def __init__(
        self,
        jobs: List[main_models.GetAgentTaskResponseBodyDataJobs] = None,
        status: str = None,
        task_id: str = None,
    ):
        # The list of subtasks.
        self.jobs = jobs
        self.status = status
        # The task ID.
        self.task_id = task_id

    def validate(self):
        if self.jobs:
            for v1 in self.jobs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['jobs'] = []
        if self.jobs is not None:
            for k1 in self.jobs:
                result['jobs'].append(k1.to_map() if k1 else None)

        if self.status is not None:
            result['status'] = self.status

        if self.task_id is not None:
            result['task_id'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.jobs = []
        if m.get('jobs') is not None:
            for k1 in m.get('jobs'):
                temp_model = main_models.GetAgentTaskResponseBodyDataJobs()
                self.jobs.append(temp_model.from_map(k1))

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('task_id') is not None:
            self.task_id = m.get('task_id')

        return self

class GetAgentTaskResponseBodyDataJobs(DaraModel):
    def __init__(
        self,
        error: str = None,
        error_code: str = None,
        error_message: str = None,
        instance: str = None,
        params: Any = None,
        region: str = None,
        result: str = None,
        status: str = None,
    ):
        # The cause of the task failure. This field is returned only when the task fails.
        self.error = error
        # The error code of the subtask failure. Valid values:
        # * Empty: The task is executed normally.
        # * INSTANCE_NOT_SUPPORTED: The instance type is not supported.
        # * INSTANCE_NOT_EXISTS: The instance does not exist.
        # * INSTANCE_RELEASED: The instance has been released.
        # * INSTANCE_NOT_RUNNING: The instance is not running.
        # * INSTANCE_NOT_OWNED: The instance does not belong to the current account.
        # * AGENT_ALREADY_INSTALLED: The Agent is already installed.
        # * AGENT_NOT_INSTALLED: The Agent is not installed.
        # * AGENT_SAME_VERSION: The version is the same.
        # * HAS_RUNNING_JOB: A running task exists.
        # * RPM_LOCK_HELD: The RPM lock is held.
        # * DISK_SPACE_INSUFFICIENT: Insufficient disk space.
        # * NODE_LOAD_HIGH: The node load is high.
        # * COMMAND_FAILED: Command execution failed.
        # * CLIENT_NOT_RUNNING: The Cloud Assistant Agent is not running.
        # * CLIENT_NOT_RESPONSE: The Cloud Assistant Agent is not responding.
        # * DELIVERY_TIMEOUT: Command delivery timed out.
        # * EXECUTION_TIMEOUT: Command execution timed out.
        # * TASK_CONCURRENCY_LIMIT: The task concurrency limit is reached.
        self.error_code = error_code
        # The detailed description of the subtask failure. Valid values:
        # * The instance type is not supported.
        # * The instance does not exist.
        # * The instance has been released.
        # * The instance is not running.
        # * The instance does not belong to the current account.
        # * The Agent is already installed.
        # * The Agent is not installed.
        # * The Agent version is the same. No upgrade is required.
        # * A running task exists. Try again later.
        # * The RPM lock is held. Try again later.
        # * Insufficient disk space.
        # * The node load is too high. Try again later.
        # * Command execution failed. Try again later.
        # * The Cloud Assistant Agent is not running.
        # * The Cloud Assistant Agent is not responding.
        # * Command delivery timed out.
        # * Command execution timed out.
        # * The task concurrency limit is reached.
        self.error_message = error_message
        # The instance ID.
        self.instance = instance
        # The subtask parameters.
        self.params = params
        # The region ID.
        self.region = region
        # The subtask execution result.
        self.result = result
        # The subtask status. Valid values:
        # - Created: Created.
        # - Running: Running.
        # - Success: The task succeeded.
        # - Fail: The task failed.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error is not None:
            result['error'] = self.error

        if self.error_code is not None:
            result['errorCode'] = self.error_code

        if self.error_message is not None:
            result['errorMessage'] = self.error_message

        if self.instance is not None:
            result['instance'] = self.instance

        if self.params is not None:
            result['params'] = self.params

        if self.region is not None:
            result['region'] = self.region

        if self.result is not None:
            result['result'] = self.result

        if self.status is not None:
            result['status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('error') is not None:
            self.error = m.get('error')

        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')

        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')

        if m.get('instance') is not None:
            self.instance = m.get('instance')

        if m.get('params') is not None:
            self.params = m.get('params')

        if m.get('region') is not None:
            self.region = m.get('region')

        if m.get('result') is not None:
            self.result = m.get('result')

        if m.get('status') is not None:
            self.status = m.get('status')

        return self

