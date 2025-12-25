# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CheckInstanceExistResponseBody(DaraModel):
    def __init__(
        self,
        is_exist_instance: bool = None,
        request_id: str = None,
    ):
        self.is_exist_instance = is_exist_instance
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.is_exist_instance is not None:
            result['IsExistInstance'] = self.is_exist_instance

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsExistInstance') is not None:
            self.is_exist_instance = m.get('IsExistInstance')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

