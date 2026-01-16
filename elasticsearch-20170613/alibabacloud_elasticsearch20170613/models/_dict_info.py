# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DictInfo(DaraModel):
    def __init__(
        self,
        file_size: int = None,
        name: str = None,
        source_type: str = None,
        type: str = None,
    ):
        self.file_size = file_size
        self.name = name
        self.source_type = source_type
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.file_size is not None:
            result['fileSize'] = self.file_size

        if self.name is not None:
            result['name'] = self.name

        if self.source_type is not None:
            result['sourceType'] = self.source_type

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('fileSize') is not None:
            self.file_size = m.get('fileSize')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('sourceType') is not None:
            self.source_type = m.get('sourceType')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

