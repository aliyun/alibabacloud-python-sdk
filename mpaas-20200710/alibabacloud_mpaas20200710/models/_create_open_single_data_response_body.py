# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateOpenSingleDataResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result: bool = None,
        result_code: str = None,
        result_message: str = None,
    ):
        self.request_id = request_id
        self.result = result
        self.result_code = result_code
        self.result_message = result_message

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.result is not None:
            result['Result'] = self.result

        if self.result_code is not None:
            result['ResultCode'] = self.result_code

        if self.result_message is not None:
            result['ResultMessage'] = self.result_message

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Result') is not None:
            self.result = m.get('Result')

        if m.get('ResultCode') is not None:
            self.result_code = m.get('ResultCode')

        if m.get('ResultMessage') is not None:
            self.result_message = m.get('ResultMessage')

        return self

