# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class HangupOperateResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        mesage: str = None,
        request_id: str = None,
        result: bool = None,
    ):
        # The status code. A value of \\"OK\\" indicates that the request was successful.
        self.code = code
        # The status message.
        self.mesage = mesage
        # The request ID.
        self.request_id = request_id
        # The result of the operation. Valid values:
        # 
        # - **true**: The hang-up was successful.
        # 
        # - **false**: The hang-up operation failed.
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.mesage is not None:
            result['Mesage'] = self.mesage

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.result is not None:
            result['Result'] = self.result

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Mesage') is not None:
            self.mesage = m.get('Mesage')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Result') is not None:
            self.result = m.get('Result')

        return self

