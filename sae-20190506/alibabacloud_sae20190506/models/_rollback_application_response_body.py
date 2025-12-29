# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_sae20190506 import models as main_models
from darabonba.model import DaraModel

class RollbackApplicationResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.RollbackApplicationResponseBodyData = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        # The HTTP status code. Take note of the following rules:
        # 
        # *   **2xx**: The call was successful.
        # *   **3xx**: The call was redirected.
        # *   **4xx**: The call failed.
        # *   **5xx**: A server error occurred.
        self.code = code
        # The response.
        self.data = data
        # The error code returned if the request failed. Take note of the following rules:
        # 
        # *   The **ErrorCode** parameter is not returned if the request succeeds.
        # *   If the call fails, the **ErrorCode** parameter is returned. For more information, see the "**Error codes**" section of this topic.
        self.error_code = error_code
        # The message returned for the operation.
        self.message = message
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the application is successfully rolled back. Take note of the following rules:
        # 
        # *   **true**
        # *   **false**
        self.success = success
        # The trace ID that is used to query the details of the request.
        self.trace_id = trace_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.trace_id is not None:
            result['TraceId'] = self.trace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.RollbackApplicationResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')

        return self

class RollbackApplicationResponseBodyData(DaraModel):
    def __init__(
        self,
        change_order_id: str = None,
        is_need_approval: bool = None,
    ):
        # The ID of the change process.
        self.change_order_id = change_order_id
        # Specifies whether approval is required when a RAM user performs release. Take note of the following rules:
        # 
        # *   **true**
        # *   **false**
        self.is_need_approval = is_need_approval

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.change_order_id is not None:
            result['ChangeOrderId'] = self.change_order_id

        if self.is_need_approval is not None:
            result['IsNeedApproval'] = self.is_need_approval

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChangeOrderId') is not None:
            self.change_order_id = m.get('ChangeOrderId')

        if m.get('IsNeedApproval') is not None:
            self.is_need_approval = m.get('IsNeedApproval')

        return self

