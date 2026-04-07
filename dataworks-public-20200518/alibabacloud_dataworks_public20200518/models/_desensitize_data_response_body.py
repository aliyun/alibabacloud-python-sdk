# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DesensitizeDataResponseBody(DaraModel):
    def __init__(
        self,
        desensitize_data: str = None,
        request_id: str = None,
    ):
        # The data returned after masking.
        self.desensitize_data = desensitize_data
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.desensitize_data is not None:
            result['DesensitizeData'] = self.desensitize_data

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DesensitizeData') is not None:
            self.desensitize_data = m.get('DesensitizeData')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

