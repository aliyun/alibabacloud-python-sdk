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
        # Request ID, which can be used for end-to-end Diagnosis
        self.request_id = request_id
        # Status code  
        # - `code == Success` indicates that authorization Succeeded.  
        # - Any other status code indicates Failed to Authorize. When authorization fails, View the `message` field to obtain the detailed error message.
        self.code = code
        # Returned Data.
        self.data = data
        # Error message  
        # - If `code == Success`, this field is empty;  
        # - Otherwise, this field contains the Request error message.
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
        # List of sub-Jobs
        self.jobs = jobs
        self.status = status
        # Job ID.
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
        # When Job execution fails, this field contains the error message indicating the cause of the failure.
        self.error = error
        # The error code indicating the reason for sub-job failure. Possible values:
        # * empty: The job executed normally.
        # * INSTANCE_NOT_SUPPORTED: The instance type is not supported.
        # * INSTANCE_NOT_EXISTS: The instance does not exist.
        # * INSTANCE_RELEASED: The instance has been released.
        # * INSTANCE_NOT_RUNNING: The instance is not running.
        # * INSTANCE_NOT_OWNED: The instance does not belong to the current account.
        # * AGENT_ALREADY_INSTALLED: The agent is already installed.
        # * AGENT_NOT_INSTALLED: The agent is not installed.
        # * AGENT_SAME_VERSION: The version is the same.
        # * HAS_RUNNING_JOB: There is a running job.
        # * RPM_LOCK_HELD: The RPM lock is held.
        # * DISK_SPACE_INSUFFICIENT: Insufficient disk space.
        # * NODE_LOAD_HIGH: High edge zone load.
        # * COMMAND_FAILED: Command execution failed.
        # * CLIENT_NOT_RUNNING: The Cloud Assistant agent is not running.
        # * CLIENT_NOT_RESPONSE: The Cloud Assistant agent is unresponsive.
        # * DELIVERY_TIMEOUT: Command delivery timeout.
        # * EXECUTION_TIMEOUT: Command execution timeout.
        # * TASK_CONCURRENCY_LIMIT: Task concurrency limit reached.
        self.error_code = error_code
        # Detailed reason for subtask execution failure. Possible values:  
        # * Instance type is not supported  
        # * Instance does not exist  
        # * Instance has been released  
        # * Instance is not running  
        # * Instance does not belong to the current account  
        # * Agent is already installed  
        # * Agent is not installed  
        # * Agent version is the same; no upgrade is required  
        # * A task is currently running; please retry later  
        # * RPM lock is occupied; please retry later  
        # * Insufficient disk space  
        # * Edge zone payload is too high; please retry later  
        # * Command execution failed; please retry later  
        # * Cloud Assistant Agent is not running  
        # * Cloud Assistant Agent is unresponsive  
        # * Command sending timeout  
        # * Command execution timeout  
        # * Task concurrency limit has been reached
        self.error_message = error_message
        # Instance ID.
        self.instance = instance
        # Parameters of the sub-Job
        self.params = params
        # Region ID.
        self.region = region
        # Result of sub-Job execution
        self.result = result
        # Sub-Job status:  
        # - Created: Created  
        # - Running: Running  
        # - Success: Job Run Succeeded  
        # - Fail: Job Run failed
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

