# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_agentcore20260804 import models as main_models
from darabonba.model import DaraModel

class CreateIdentityProviderSyncJobResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.CreateIdentityProviderSyncJobResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The business status code of the API request. SUCCESS indicates that the request is successful, but does not indicate that the asynchronous synchronization task is completed.
        self.code = code
        # The business data returned in the response.
        self.data = data
        # The HTTP status code of the API request, which does not indicate the execution result of the asynchronous task.
        self.http_status_code = http_status_code
        # The response message of the API request.
        self.message = message
        # The unique identifier of the request. Provide this value when troubleshooting issues.
        self.request_id = request_id
        # Indicates whether the API request is successful. To check whether the asynchronous task is completed, query the task status.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.data is not None:
            result['data'] = self.data.to_map()

        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.success is not None:
            result['success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('data') is not None:
            temp_model = main_models.CreateIdentityProviderSyncJobResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        return self

class CreateIdentityProviderSyncJobResponseBodyData(DaraModel):
    def __init__(
        self,
        current_step: str = None,
        failure_reason: str = None,
        status: str = None,
        synced_user_count: int = None,
        synchronization_job_id: str = None,
        task_id: str = None,
    ):
        # The current execution step of the AgentCore asynchronous task. This field may not be returned if the task has not started.
        self.current_step = current_step
        # The failure summary of the asynchronous task. This field is not returned if no failure information is available. You can use this field along with the taskId and requestId for troubleshooting.
        self.failure_reason = failure_reason
        # The status of the synchronization task. Valid values: PENDING: pending. RUNNING: running. PAUSED: paused. SUCCESS: successful. FAILED: failed. CANCELED: canceled. The first three are non-terminal states, and the last three are terminal states. Query the status until a terminal state is reached to determine the result.
        self.status = status
        # The number of user entries that have been read locally and written or updated, including existing users. This does not represent the number of newly added users or the synchronization percentage. This field is not returned when no statistics are available.
        self.synced_user_count = synced_user_count
        # The ID of the downstream synchronization task in AgentIdentity. This field is not returned if the task has not been created. You cannot use this ID in place of taskId to call GetIdentityProviderSyncJob.
        self.synchronization_job_id = synchronization_job_id
        # The local task ID in AgentCore returned by CreateIdentityProviderSyncJob, which is different from the synchronizationJobId in AgentIdentity. You must use the same workspace and identity provider when querying the task.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_step is not None:
            result['currentStep'] = self.current_step

        if self.failure_reason is not None:
            result['failureReason'] = self.failure_reason

        if self.status is not None:
            result['status'] = self.status

        if self.synced_user_count is not None:
            result['syncedUserCount'] = self.synced_user_count

        if self.synchronization_job_id is not None:
            result['synchronizationJobId'] = self.synchronization_job_id

        if self.task_id is not None:
            result['taskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('currentStep') is not None:
            self.current_step = m.get('currentStep')

        if m.get('failureReason') is not None:
            self.failure_reason = m.get('failureReason')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('syncedUserCount') is not None:
            self.synced_user_count = m.get('syncedUserCount')

        if m.get('synchronizationJobId') is not None:
            self.synchronization_job_id = m.get('synchronizationJobId')

        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')

        return self

