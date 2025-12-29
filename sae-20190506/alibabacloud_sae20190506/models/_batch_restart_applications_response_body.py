# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_sae20190506 import models as main_models
from darabonba.model import DaraModel

class BatchRestartApplicationsResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.BatchRestartApplicationsResponseBodyData = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        # The API status or POP error code. Value description:
        # 
        # 2xx: The request was successful. 3xx: The request was redirected. 4xx: The request was invalid. 5xx: A server error occurred.
        self.code = code
        # The response.
        self.data = data
        # The error code. Value description:
        # 
        # If the request succeeds, this field is not returned. It is returned only if the request fails. For more information, see the "Error codes" section in this topic.
        self.error_code = error_code
        # The additional information. Value description:
        # 
        # If the request succeeds, a success message is returned. If the request fails, an error code is returned.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the applications were started. Valid values:
        # 
        # true and false
        self.success = success
        # The ID of the trace, which is used to query the exact call information.
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
            temp_model = main_models.BatchRestartApplicationsResponseBodyData()
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

class BatchRestartApplicationsResponseBodyData(DaraModel):
    def __init__(
        self,
        change_order_id: str = None,
    ):
        # The ID of the change process.
        self.change_order_id = change_order_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.change_order_id is not None:
            result['ChangeOrderId'] = self.change_order_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChangeOrderId') is not None:
            self.change_order_id = m.get('ChangeOrderId')

        return self

