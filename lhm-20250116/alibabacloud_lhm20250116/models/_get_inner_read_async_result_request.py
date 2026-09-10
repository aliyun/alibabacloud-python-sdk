# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetInnerReadAsyncResultRequest(DaraModel):
    def __init__(
        self,
        data_source_name: str = None,
    ):
        # The data source name. The probe task uses this field as its dimension identifier.
        self.data_source_name = data_source_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_source_name is not None:
            result['dataSourceName'] = self.data_source_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dataSourceName') is not None:
            self.data_source_name = m.get('dataSourceName')

        return self

