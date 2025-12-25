# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class GetCloudResourceDataResponseBody(DaraModel):
    def __init__(
        self,
        data: List[List[str]] = None,
        header: List[str] = None,
        request_id: str = None,
    ):
        self.data = data
        self.header = header
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['data'] = self.data

        if self.header is not None:
            result['header'] = self.header

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            self.data = m.get('data')

        if m.get('header') is not None:
            self.header = m.get('header')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

