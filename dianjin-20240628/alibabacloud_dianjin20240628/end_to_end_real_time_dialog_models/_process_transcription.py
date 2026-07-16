# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ProcessTranscription(DaraModel):
    def __init__(
        self,
        data_source_type: str = None,
        data: List[int] = None,
    ):
        self.data_source_type = data_source_type
        # This parameter is required.
        self.data = data

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_source_type is not None:
            result['dataSourceType'] = self.data_source_type

        if self.data is not None:
            result['data'] = self.data

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dataSourceType') is not None:
            self.data_source_type = m.get('dataSourceType')

        if m.get('data') is not None:
            self.data = m.get('data')

        return self

