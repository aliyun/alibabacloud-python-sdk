# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from darabonba.model import DaraModel

class RemoveHotelResponseBody(DaraModel):
    def __init__(
        self,
        extentions: Dict[str, Any] = None,
        message: str = None,
        request_id: str = None,
        result: bool = None,
        status_code: int = None,
    ):
        self.extentions = extentions
        self.message = message
        # The ID of the request.
        self.request_id = request_id
        self.result = result
        self.status_code = status_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.extentions is not None:
            result['Extentions'] = self.extentions

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.result is not None:
            result['Result'] = self.result

        if self.status_code is not None:
            result['StatusCode'] = self.status_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Extentions') is not None:
            self.extentions = m.get('Extentions')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Result') is not None:
            self.result = m.get('Result')

        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')

        return self

