# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AddDatasetDataResponseBody(DaraModel):
    def __init__(
        self,
        affected_rows: int = None,
        request_id: str = None,
    ):
        self.affected_rows = affected_rows
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.affected_rows is not None:
            result['affectedRows'] = self.affected_rows

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('affectedRows') is not None:
            self.affected_rows = m.get('affectedRows')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

