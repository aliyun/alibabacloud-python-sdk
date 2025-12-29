# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class PmsEventReportRequest(DaraModel):
    def __init__(
        self,
        payload: str = None,
    ):
        # This parameter is required.
        self.payload = payload

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.payload is not None:
            result['Payload'] = self.payload

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Payload') is not None:
            self.payload = m.get('Payload')

        return self

