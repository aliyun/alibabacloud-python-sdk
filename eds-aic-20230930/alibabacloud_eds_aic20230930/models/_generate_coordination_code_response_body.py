# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GenerateCoordinationCodeResponseBody(DaraModel):
    def __init__(
        self,
        coordinator_code: str = None,
        request_id: str = None,
    ):
        # The collaboration code.
        self.coordinator_code = coordinator_code
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.coordinator_code is not None:
            result['CoordinatorCode'] = self.coordinator_code

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CoordinatorCode') is not None:
            self.coordinator_code = m.get('CoordinatorCode')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

