# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListRemoteADBDataSourcesRequest(DaraModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        data_source_id: str = None,
        owner_id: int = None,
    ):
        # Instance name.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # Data source ID.
        self.data_source_id = data_source_id
        self.owner_id = owner_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.data_source_id is not None:
            result['DataSourceId'] = self.data_source_id

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('DataSourceId') is not None:
            self.data_source_id = m.get('DataSourceId')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        return self

