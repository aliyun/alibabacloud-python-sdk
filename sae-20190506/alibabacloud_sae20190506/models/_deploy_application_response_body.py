# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_sae20190506 import models as main_models
from darabonba.model import DaraModel

class DeployApplicationResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.DeployApplicationResponseBodyData = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        # The API status or POP error code. Values:
        # 
        # - **2xx**: Success.
        # 
        # - **3xx**: Redirection.
        # 
        # - **4xx**: Request error.
        # 
        # - **5xx**: Server error.
        self.code = code
        # The response data.
        self.data = data
        # The error code. Values:
        # 
        # - On success: This field is not returned.
        # 
        # - On failure: This field is returned. For details, see the **Error codes** section in this topic.
        self.error_code = error_code
        # Additional information. Values:
        # 
        # - On success, returns **success**.
        # 
        # - On failure, returns a specific error code.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Whether the deployment succeeded. Values:
        # 
        # - **true**: Deployment succeeded.
        # 
        # - **false**: Deployment failed.
        self.success = success
        # The trace ID for precise query of call information.
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
            temp_model = main_models.DeployApplicationResponseBodyData()
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

class DeployApplicationResponseBodyData(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        change_order_id: str = None,
        is_need_approval: bool = None,
    ):
        # The application ID.
        self.app_id = app_id
        # The returned change order ID. Use it to query task execution status.
        self.change_order_id = change_order_id
        # Whether RAM users need approval to deploy changes. Values:
        # 
        # - **true**: Approval required.
        # 
        # - **false**: No approval required.
        self.is_need_approval = is_need_approval

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.change_order_id is not None:
            result['ChangeOrderId'] = self.change_order_id

        if self.is_need_approval is not None:
            result['IsNeedApproval'] = self.is_need_approval

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('ChangeOrderId') is not None:
            self.change_order_id = m.get('ChangeOrderId')

        if m.get('IsNeedApproval') is not None:
            self.is_need_approval = m.get('IsNeedApproval')

        return self

