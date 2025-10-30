# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateRemoteADBDataSourceRequest(DaraModel):
    def __init__(
        self,
        data_source_name: str = None,
        local_dbinstance_id: str = None,
        local_database: str = None,
        manager_user_name: str = None,
        manager_user_password: str = None,
        owner_id: int = None,
        remote_dbinstance_id: str = None,
        remote_database: str = None,
        user_name: str = None,
        user_password: str = None,
    ):
        # Customer-specified DataSourceName.
        self.data_source_name = data_source_name
        # Instance ID of the data being used (required).
        # 
        # This parameter is required.
        self.local_dbinstance_id = local_dbinstance_id
        # Database name of the data being used (required)
        # 
        # This parameter is required.
        self.local_database = local_database
        # Management account of the data-using instance.
        # 
        # This parameter is required.
        self.manager_user_name = manager_user_name
        # Password of the management account of the data-using instance.
        # 
        # This parameter is required.
        self.manager_user_password = manager_user_password
        self.owner_id = owner_id
        # Instance ID providing the data (required).
        # 
        # This parameter is required.
        self.remote_dbinstance_id = remote_dbinstance_id
        # Database name providing the data (required).
        # 
        # This parameter is required.
        self.remote_database = remote_database
        # Account name of the data-providing instance used for user mapping (required).
        # 
        # This parameter is required.
        self.user_name = user_name
        # Password of the data-providing instance account used for user mapping.
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
        if self.data_source_name is not None:
            result['DataSourceName'] = self.data_source_name

        if self.local_dbinstance_id is not None:
            result['LocalDBInstanceId'] = self.local_dbinstance_id

        if self.local_database is not None:
            result['LocalDatabase'] = self.local_database

        if self.manager_user_name is not None:
            result['ManagerUserName'] = self.manager_user_name

        if self.manager_user_password is not None:
            result['ManagerUserPassword'] = self.manager_user_password

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.remote_dbinstance_id is not None:
            result['RemoteDBInstanceId'] = self.remote_dbinstance_id

        if self.remote_database is not None:
            result['RemoteDatabase'] = self.remote_database

        if self.user_name is not None:
            result['UserName'] = self.user_name

        if self.user_password is not None:
            result['UserPassword'] = self.user_password

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataSourceName') is not None:
            self.data_source_name = m.get('DataSourceName')

        if m.get('LocalDBInstanceId') is not None:
            self.local_dbinstance_id = m.get('LocalDBInstanceId')

        if m.get('LocalDatabase') is not None:
            self.local_database = m.get('LocalDatabase')

        if m.get('ManagerUserName') is not None:
            self.manager_user_name = m.get('ManagerUserName')

        if m.get('ManagerUserPassword') is not None:
            self.manager_user_password = m.get('ManagerUserPassword')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RemoteDBInstanceId') is not None:
            self.remote_dbinstance_id = m.get('RemoteDBInstanceId')

        if m.get('RemoteDatabase') is not None:
            self.remote_database = m.get('RemoteDatabase')

        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')

        if m.get('UserPassword') is not None:
            self.user_password = m.get('UserPassword')

        return self

