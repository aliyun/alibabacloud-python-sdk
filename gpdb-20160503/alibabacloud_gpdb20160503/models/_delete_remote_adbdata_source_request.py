# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteRemoteADBDataSourceRequest(DaraModel):
    def __init__(
        self,
        data_source_id: str = None,
        local_dbinstance_id: str = None,
        owner_id: int = None,
    ):
        # The service ID.
        # 
        # This parameter is required.
        self.data_source_id = data_source_id
        # The ID of the instance that uses the data provided by another instance.
        # 
        # This parameter is required.
        self.local_dbinstance_id = local_dbinstance_id
        self.owner_id = owner_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_source_id is not None:
            result['DataSourceId'] = self.data_source_id

        if self.local_dbinstance_id is not None:
            result['LocalDBInstanceId'] = self.local_dbinstance_id

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataSourceId') is not None:
            self.data_source_id = m.get('DataSourceId')

        if m.get('LocalDBInstanceId') is not None:
            self.local_dbinstance_id = m.get('LocalDBInstanceId')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        return self

