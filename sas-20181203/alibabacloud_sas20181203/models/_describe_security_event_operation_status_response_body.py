# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class DescribeSecurityEventOperationStatusResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        security_event_operation_status_response: main_models.DescribeSecurityEventOperationStatusResponseBodySecurityEventOperationStatusResponse = None,
    ):
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id
        # The information about the task that handles the alert events.
        self.security_event_operation_status_response = security_event_operation_status_response

    def validate(self):
        if self.security_event_operation_status_response:
            self.security_event_operation_status_response.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.security_event_operation_status_response is not None:
            result['SecurityEventOperationStatusResponse'] = self.security_event_operation_status_response.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SecurityEventOperationStatusResponse') is not None:
            temp_model = main_models.DescribeSecurityEventOperationStatusResponseBodySecurityEventOperationStatusResponse()
            self.security_event_operation_status_response = temp_model.from_map(m.get('SecurityEventOperationStatusResponse'))

        return self

class DescribeSecurityEventOperationStatusResponseBodySecurityEventOperationStatusResponse(DaraModel):
    def __init__(
        self,
        security_event_operation_statuses: List[main_models.DescribeSecurityEventOperationStatusResponseBodySecurityEventOperationStatusResponseSecurityEventOperationStatuses] = None,
        task_status: str = None,
    ):
        # An array consisting of the status of the alert events handled by the task.
        self.security_event_operation_statuses = security_event_operation_statuses
        # The status of the task that handles the alert events. Valid values:
        # 
        # *   **Processing**: The task is running.
        # *   **Success**: The task is successful.
        # *   **Failure**: The task failed.
        # *   **Pending**: The task is pending.
        self.task_status = task_status

    def validate(self):
        if self.security_event_operation_statuses:
            for v1 in self.security_event_operation_statuses:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['SecurityEventOperationStatuses'] = []
        if self.security_event_operation_statuses is not None:
            for k1 in self.security_event_operation_statuses:
                result['SecurityEventOperationStatuses'].append(k1.to_map() if k1 else None)

        if self.task_status is not None:
            result['TaskStatus'] = self.task_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.security_event_operation_statuses = []
        if m.get('SecurityEventOperationStatuses') is not None:
            for k1 in m.get('SecurityEventOperationStatuses'):
                temp_model = main_models.DescribeSecurityEventOperationStatusResponseBodySecurityEventOperationStatusResponseSecurityEventOperationStatuses()
                self.security_event_operation_statuses.append(temp_model.from_map(k1))

        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')

        return self

class DescribeSecurityEventOperationStatusResponseBodySecurityEventOperationStatusResponseSecurityEventOperationStatuses(DaraModel):
    def __init__(
        self,
        error_code: str = None,
        security_event_id: str = None,
        status: str = None,
    ):
        # The code that indicates the handling result of the alert event.
        self.error_code = error_code
        # The ID of the alert event.
        self.security_event_id = security_event_id
        # The handling status of the alert event. Valid values:
        # 
        # *   **Processing**: The alert event is being handled.
        # *   **Success**: The alert event is handled.
        # *   **Failed**: The alert event failed to be handled.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.security_event_id is not None:
            result['SecurityEventId'] = self.security_event_id

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('SecurityEventId') is not None:
            self.security_event_id = m.get('SecurityEventId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

