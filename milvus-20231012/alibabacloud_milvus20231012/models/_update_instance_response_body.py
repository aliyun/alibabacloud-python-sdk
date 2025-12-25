# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateInstanceResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        data: bool = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.data = data
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.data is not None:
            result['data'] = self.data

        if self.success is not None:
            result['success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('data') is not None:
            self.data = m.get('data')

        if m.get('success') is not None:
            self.success = m.get('success')

        return self

