# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_edas20170801 import models as main_models
from darabonba.model import DaraModel

class RollbackChangeOrderResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: main_models.RollbackChangeOrderResponseBodyData = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        trace_id: str = None,
    ):
        # The HTTP status code that is returned.
        self.code = code
        # The information about the change process.
        self.data = data
        # The error code that is returned.
        self.error_code = error_code
        # The additional information that is returned.
        self.message = message
        # The ID of the request.
        self.request_id = request_id
        # The ID of the trace.
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

        if self.trace_id is not None:
            result['TraceId'] = self.trace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.RollbackChangeOrderResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')

        return self

class RollbackChangeOrderResponseBodyData(DaraModel):
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

