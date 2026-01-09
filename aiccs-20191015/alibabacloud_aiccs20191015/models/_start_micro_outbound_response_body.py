# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class StartMicroOutboundResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        customer_info: str = None,
        invoke_cmd_id: str = None,
        invoke_create_time: str = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.customer_info = customer_info
        self.invoke_cmd_id = invoke_cmd_id
        self.invoke_create_time = invoke_create_time
        self.message = message
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.customer_info is not None:
            result['CustomerInfo'] = self.customer_info

        if self.invoke_cmd_id is not None:
            result['InvokeCmdId'] = self.invoke_cmd_id

        if self.invoke_create_time is not None:
            result['InvokeCreateTime'] = self.invoke_create_time

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('CustomerInfo') is not None:
            self.customer_info = m.get('CustomerInfo')

        if m.get('InvokeCmdId') is not None:
            self.invoke_cmd_id = m.get('InvokeCmdId')

        if m.get('InvokeCreateTime') is not None:
            self.invoke_create_time = m.get('InvokeCreateTime')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

