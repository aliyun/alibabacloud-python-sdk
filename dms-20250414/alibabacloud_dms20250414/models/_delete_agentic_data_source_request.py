# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteAgenticDataSourceRequest(DaraModel):
    def __init__(
        self,
        data_source_uuid: str = None,
    ):
        # The UUID of the data source to delete. Ensure that no workloads are using the data source before deletion.
        # 
        # This parameter is required.
        self.data_source_uuid = data_source_uuid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_source_uuid is not None:
            result['DataSourceUuid'] = self.data_source_uuid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataSourceUuid') is not None:
            self.data_source_uuid = m.get('DataSourceUuid')

        return self

