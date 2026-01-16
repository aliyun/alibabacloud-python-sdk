# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateUserSuppressionResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        suppression_id: str = None,
    ):
        # Request ID
        self.request_id = request_id
        # Invalid address number
        self.suppression_id = suppression_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.suppression_id is not None:
            result['SuppressionId'] = self.suppression_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SuppressionId') is not None:
            self.suppression_id = m.get('SuppressionId')

        return self

