# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteRtcAsrTaskResponseBody(DaraModel):
    def __init__(
        self,
        description: str = None,
        request_id: str = None,
        ret_code: int = None,
    ):
        # The result of the request. If success is returned, the request is successful. If an error message is returned, the request failed.
        self.description = description
        # The ID of the request.
        self.request_id = request_id
        # The returned HTTP status code. HTTP status code 2000 indicates that the request is successful. If another HTTP status code is returned, the request failed.
        self.ret_code = ret_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.ret_code is not None:
            result['RetCode'] = self.ret_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('RetCode') is not None:
            self.ret_code = m.get('RetCode')

        return self

