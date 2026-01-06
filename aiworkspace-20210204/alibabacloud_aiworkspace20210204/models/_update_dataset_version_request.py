# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateDatasetVersionRequest(DaraModel):
    def __init__(
        self,
        data_count: int = None,
        data_size: int = None,
        description: str = None,
        options: str = None,
    ):
        self.data_count = data_count
        self.data_size = data_size
        self.description = description
        self.options = options

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_count is not None:
            result['DataCount'] = self.data_count

        if self.data_size is not None:
            result['DataSize'] = self.data_size

        if self.description is not None:
            result['Description'] = self.description

        if self.options is not None:
            result['Options'] = self.options

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataCount') is not None:
            self.data_count = m.get('DataCount')

        if m.get('DataSize') is not None:
            self.data_size = m.get('DataSize')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Options') is not None:
            self.options = m.get('Options')

        return self

