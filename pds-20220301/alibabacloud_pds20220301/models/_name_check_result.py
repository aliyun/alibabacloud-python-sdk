# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class NameCheckResult(DaraModel):
    def __init__(
        self,
        exist_file_id: str = None,
        exist_file_type: str = None,
    ):
        self.exist_file_id = exist_file_id
        self.exist_file_type = exist_file_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.exist_file_id is not None:
            result['exist_file_id'] = self.exist_file_id

        if self.exist_file_type is not None:
            result['exist_file_type'] = self.exist_file_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('exist_file_id') is not None:
            self.exist_file_id = m.get('exist_file_id')

        if m.get('exist_file_type') is not None:
            self.exist_file_type = m.get('exist_file_type')

        return self

