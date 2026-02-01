# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GenerateCopilotResponseResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
        massage: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.massage = massage
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.data is not None:
            result['data'] = self.data

        if self.massage is not None:
            result['massage'] = self.massage

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('data') is not None:
            self.data = m.get('data')

        if m.get('massage') is not None:
            self.massage = m.get('massage')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

