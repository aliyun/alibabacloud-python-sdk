# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CallBackThirdRightSendPlanResponseBody(DaraModel):
    def __init__(
        self,
        ret_code: str = None,
        ret_msg: str = None,
        ret_value: bool = None,
        request_id: str = None,
    ):
        # fault status code
        self.ret_code = ret_code
        # error message
        self.ret_msg = ret_msg
        # Return Result true/false
        self.ret_value = ret_value
        # Request ID
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ret_code is not None:
            result['RetCode'] = self.ret_code

        if self.ret_msg is not None:
            result['RetMsg'] = self.ret_msg

        if self.ret_value is not None:
            result['RetValue'] = self.ret_value

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RetCode') is not None:
            self.ret_code = m.get('RetCode')

        if m.get('RetMsg') is not None:
            self.ret_msg = m.get('RetMsg')

        if m.get('RetValue') is not None:
            self.ret_value = m.get('RetValue')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

