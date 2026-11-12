# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_agentcore20260804 import models as main_models
from darabonba.model import DaraModel

class RebuildSandboxResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.RebuildSandboxResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # Task result code of this API request. A successful request returns SUCCESS. Query task result of the asynchronous task separately.
        self.code = code
        # The acceptance result of the rebuild request.
        self.data = data
        # The HTTP status code corresponding to this API request.
        self.http_status_code = http_status_code
        # The result description of this API request. This does not indicate that the asynchronous rebuild task is complete.
        self.message = message
        # The request ID used to trace this API call.
        self.request_id = request_id
        # Indicates whether this API request is successful. A value of true does not indicate that the sandbox rebuild is complete.
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
            temp_model = main_models.RebuildSandboxResponseBodyData()
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

class RebuildSandboxResponseBodyData(DaraModel):
    def __init__(
        self,
        incarnation: int = None,
        operation_id: str = None,
        sandbox_id: str = None,
    ):
        # The target instance incarnation for this rebuild. The rebuild increases the incarnation. The returned value only indicates that the request is accepted, not that the new instance is ready.
        self.incarnation = incarnation
        # The initial rebuild task ID. Use the operationId returned by RebuildSandbox. Always use this ID to query the overall result. You do not need to switch to the IDs of subsequently created tasks.
        self.operation_id = operation_id
        # The logical sandbox ID corresponding to this rebuild. The logical ID remains unchanged after the rebuild.
        self.sandbox_id = sandbox_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.incarnation is not None:
            result['incarnation'] = self.incarnation

        if self.operation_id is not None:
            result['operationId'] = self.operation_id

        if self.sandbox_id is not None:
            result['sandboxId'] = self.sandbox_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('incarnation') is not None:
            self.incarnation = m.get('incarnation')

        if m.get('operationId') is not None:
            self.operation_id = m.get('operationId')

        if m.get('sandboxId') is not None:
            self.sandbox_id = m.get('sandboxId')

        return self

