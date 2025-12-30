# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateMediaLiveInputResponseBody(DaraModel):
    def __init__(
        self,
        input_id: str = None,
        request_id: str = None,
    ):
        # The ID of the input.
        self.input_id = input_id
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.input_id is not None:
            result['InputId'] = self.input_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InputId') is not None:
            self.input_id = m.get('InputId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

