# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class VerifySiteResponseBody(DaraModel):
    def __init__(
        self,
        passed: bool = None,
        request_id: str = None,
    ):
        # Indicates whether the verification passed. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.passed = passed
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.passed is not None:
            result['Passed'] = self.passed

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Passed') is not None:
            self.passed = m.get('Passed')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

