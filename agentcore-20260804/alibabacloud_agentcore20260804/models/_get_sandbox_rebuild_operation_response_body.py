# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_agentcore20260804 import models as main_models
from darabonba.model import DaraModel

class GetSandboxRebuildOperationResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetSandboxRebuildOperationResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The result code of the API request. A successful request returns SUCCESS. Query the asynchronous task result separately.
        self.code = code
        # The overall result of the rebuild task.
        self.data = data
        # The HTTP status code of the API request.
        self.http_status_code = http_status_code
        # The result message of the API request. This message does not indicate that the asynchronous rebuild task is completed.
        self.message = message
        # The request ID used to trace the API call.
        self.request_id = request_id
        # Indicates whether the API request is successful. A value of true does not indicate that the sandbox rebuild is completed.
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
            temp_model = main_models.GetSandboxRebuildOperationResponseBodyData()
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

class GetSandboxRebuildOperationResponseBodyData(DaraModel):
    def __init__(
        self,
        error: main_models.GetSandboxRebuildOperationResponseBodyDataError = None,
        operation_id: str = None,
        sandbox_id: str = None,
        status: str = None,
    ):
        # The publicly accessible node error. This error is returned when the node fails, is canceled, or subsequent operations override it. It can be empty in other states.
        self.error = error
        # The initial rebuild task ID. Use the operationId returned by RebuildSandbox. Always use this ID to query the overall result. You do not need to switch to the ID of a subsequent creation task.
        self.operation_id = operation_id
        # The logical sandbox ID corresponding to this rebuild. The logical ID remains unchanged after the rebuild.
        self.sandbox_id = sandbox_id
        # The overall rebuild status. Valid values:
        # - PENDING: Waiting to be processed.
        # - RUNNING: execute in progress.
        # - SUCCEEDED: Overall success.
        # - FAILED: Failed.
        # - CANCELED: Canceled.
        # - SUPERSEDED: override by subsequent operations.
        # - UNKNOWN: Unconfirmed.
        # Only SUCCEEDED indicates completion. Do not treat UNKNOWN, missing status, or query exceptions as success, and do not automatically resubmit the rebuild.
        self.status = status

    def validate(self):
        if self.error:
            self.error.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error is not None:
            result['error'] = self.error.to_map()

        if self.operation_id is not None:
            result['operationId'] = self.operation_id

        if self.sandbox_id is not None:
            result['sandboxId'] = self.sandbox_id

        if self.status is not None:
            result['status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('error') is not None:
            temp_model = main_models.GetSandboxRebuildOperationResponseBodyDataError()
            self.error = temp_model.from_map(m.get('error'))

        if m.get('operationId') is not None:
            self.operation_id = m.get('operationId')

        if m.get('sandboxId') is not None:
            self.sandbox_id = m.get('sandboxId')

        if m.get('status') is not None:
            self.status = m.get('status')

        return self

class GetSandboxRebuildOperationResponseBodyDataError(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
    ):
        # The task error code. This code is used to distinguish between rebuild failures, subsequent instance creation failures, cancellations, or supersessions.
        self.code = code
        # The publicly accessible task error message. Keep the task ID for troubleshooting.
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.message is not None:
            result['message'] = self.message

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('message') is not None:
            self.message = m.get('message')

        return self

