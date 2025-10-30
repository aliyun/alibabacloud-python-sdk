# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyRemoteADBDataSourceRequest(DaraModel):
    def __init__(
        self,
        data_source_id: str = None,
        data_source_name: str = None,
        local_dbinstance_id: str = None,
        owner_id: int = None,
        user_name: str = None,
        user_password: str = None,
    ):
        # Service ID
        # 
        # This parameter is required.
        self.data_source_id = data_source_id
        # Specified dataSourceName.
        self.data_source_name = data_source_name
        # The ID of the local data instance being used.
        # 
        # This parameter is required.
        self.local_dbinstance_id = local_dbinstance_id
        self.owner_id = owner_id
        # New user name.
        # 
        # This parameter is required.
        self.user_name = user_name
        # New user password, which must be transmitted in encrypted form.
        # 
        # This parameter is required.
        self.user_password = user_password

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_source_id is not None:
            result['DataSourceId'] = self.data_source_id

        if self.data_source_name is not None:
            result['DataSourceName'] = self.data_source_name

        if self.local_dbinstance_id is not None:
            result['LocalDBInstanceId'] = self.local_dbinstance_id

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.user_name is not None:
            result['UserName'] = self.user_name

        if self.user_password is not None:
            result['UserPassword'] = self.user_password

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataSourceId') is not None:
            self.data_source_id = m.get('DataSourceId')

        if m.get('DataSourceName') is not None:
            self.data_source_name = m.get('DataSourceName')

        if m.get('LocalDBInstanceId') is not None:
            self.local_dbinstance_id = m.get('LocalDBInstanceId')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')

        if m.get('UserPassword') is not None:
            self.user_password = m.get('UserPassword')

        return self

