# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListLogContentsRequest(DaraModel):
    def __init__(
        self,
        file_name: str = None,
        length: int = None,
        offset: int = None,
        region_id: str = None,
    ):
        # Full path of the file.
        self.file_name = file_name
        # Length of the log.
        self.length = length
        # Start line for query.
        self.offset = offset
        # Region ID.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.file_name is not None:
            result['fileName'] = self.file_name

        if self.length is not None:
            result['length'] = self.length

        if self.offset is not None:
            result['offset'] = self.offset

        if self.region_id is not None:
            result['regionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('fileName') is not None:
            self.file_name = m.get('fileName')

        if m.get('length') is not None:
            self.length = m.get('length')

        if m.get('offset') is not None:
            self.offset = m.get('offset')

        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')

        return self

