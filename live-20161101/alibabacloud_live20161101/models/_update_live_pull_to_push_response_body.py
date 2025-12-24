# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateLivePullToPushResponseBody(DaraModel):
    def __init__(
        self,
        description: str = None,
        request_id: str = None,
        ret_code: int = None,
    ):
        # The error description.
        self.description = description
        # The request ID.
        self.request_id = request_id
        # The code that is returned for the request.
        # 
        # > 
        # 
        # *   0 is returned if the request is normal.
        # 
        # *   For information about codes that are returned when exceptions occur, see the following Error codes table.
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

