# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AddCustomLineResponseBody(DaraModel):
    def __init__(
        self,
        line_code: str = None,
        line_id: int = None,
        request_id: str = None,
    ):
        # The code of the custom line.
        self.line_code = line_code
        # The unique ID of the custom line.
        self.line_id = line_id
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.line_code is not None:
            result['LineCode'] = self.line_code

        if self.line_id is not None:
            result['LineId'] = self.line_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LineCode') is not None:
            self.line_code = m.get('LineCode')

        if m.get('LineId') is not None:
            self.line_id = m.get('LineId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

