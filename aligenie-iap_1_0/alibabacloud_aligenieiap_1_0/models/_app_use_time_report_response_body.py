# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AppUseTimeReportResponseBody(DaraModel):
    def __init__(
        self,
        ret_code: int = None,
        ret_msg: str = None,
        ret_value: bool = None,
    ):
        # Error code returned; `0` indicates success.
        self.ret_code = ret_code
        # Error message returned; no message is returned upon success.
        self.ret_msg = ret_msg
        # Result of invoking the API  
        # 
        # - true indicates success  
        # - false indicates failure
        self.ret_value = ret_value

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RetCode') is not None:
            self.ret_code = m.get('RetCode')

        if m.get('RetMsg') is not None:
            self.ret_msg = m.get('RetMsg')

        if m.get('RetValue') is not None:
            self.ret_value = m.get('RetValue')

        return self

