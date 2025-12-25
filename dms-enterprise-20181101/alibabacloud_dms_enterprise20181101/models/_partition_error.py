# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class PartitionError(DaraModel):
    def __init__(
        self,
        error_detail: str = None,
        values: List[str] = None,
    ):
        self.error_detail = error_detail
        self.values = values

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_detail is not None:
            result['ErrorDetail'] = self.error_detail

        if self.values is not None:
            result['Values'] = self.values

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorDetail') is not None:
            self.error_detail = m.get('ErrorDetail')

        if m.get('Values') is not None:
            self.values = m.get('Values')

        return self

