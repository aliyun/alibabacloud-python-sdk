# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribeSafConsoleResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        biz_data: List[str] = None,
    ):
        # Request ID.
        self.request_id = request_id
        # Returned result.
        self.biz_data = biz_data

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.biz_data is not None:
            result['bizData'] = self.biz_data

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('bizData') is not None:
            self.biz_data = m.get('bizData')

        return self

