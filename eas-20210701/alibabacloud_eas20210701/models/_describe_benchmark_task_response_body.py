# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeBenchmarkTaskResponseBody(DaraModel):
    def __init__(
        self,
        available_agent: int = None,
        caller_uid: str = None,
        desired_agent: int = None,
        endpoint: str = None,
        message: str = None,
        parent_uid: str = None,
        reason: str = None,
        request_id: str = None,
        service_name: str = None,
        status: str = None,
        task_id: str = None,
        task_name: str = None,
        token: str = None,
    ):
        # The number of instances that you can test.
        self.available_agent = available_agent
        # The ID of the operation caller.
        self.caller_uid = caller_uid
        # The number of instances that you want to test.
        self.desired_agent = desired_agent
        # The endpoint of the service gateway.
        self.endpoint = endpoint
        # The returned message.
        self.message = message
        # The ID of the Alibaba Cloud account that is used to call the operation.
        self.parent_uid = parent_uid
        # The event or reason that causes the current state of the stress testing task.
        self.reason = reason
        # The request ID.
        self.request_id = request_id
        # The name of the service that you want to test.
        self.service_name = service_name
        # The state of the stress testing task.
        # 
        # Valid values:
        # 
        # *   Creating
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   Starting
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   DeleteFailed
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   Running
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   Stopping
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   Error
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   Updating
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   Deleting
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   CreateFailed
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        self.status = status
        # The ID of the stress testing task.
        self.task_id = task_id
        # The name of the stress testing task.
        self.task_name = task_name
        # The token for authentication when a stress testing task is created.
        self.token = token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.available_agent is not None:
            result['AvailableAgent'] = self.available_agent

        if self.caller_uid is not None:
            result['CallerUid'] = self.caller_uid

        if self.desired_agent is not None:
            result['DesiredAgent'] = self.desired_agent

        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint

        if self.message is not None:
            result['Message'] = self.message

        if self.parent_uid is not None:
            result['ParentUid'] = self.parent_uid

        if self.reason is not None:
            result['Reason'] = self.reason

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.service_name is not None:
            result['ServiceName'] = self.service_name

        if self.status is not None:
            result['Status'] = self.status

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.task_name is not None:
            result['TaskName'] = self.task_name

        if self.token is not None:
            result['Token'] = self.token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AvailableAgent') is not None:
            self.available_agent = m.get('AvailableAgent')

        if m.get('CallerUid') is not None:
            self.caller_uid = m.get('CallerUid')

        if m.get('DesiredAgent') is not None:
            self.desired_agent = m.get('DesiredAgent')

        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('ParentUid') is not None:
            self.parent_uid = m.get('ParentUid')

        if m.get('Reason') is not None:
            self.reason = m.get('Reason')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')

        if m.get('Token') is not None:
            self.token = m.get('Token')

        return self

