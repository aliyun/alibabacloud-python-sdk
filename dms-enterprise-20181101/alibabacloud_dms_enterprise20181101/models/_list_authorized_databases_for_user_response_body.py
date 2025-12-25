# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dms_enterprise20181101 import models as main_models
from darabonba.model import DaraModel

class ListAuthorizedDatabasesForUserResponseBody(DaraModel):
    def __init__(
        self,
        databases: List[main_models.ListAuthorizedDatabasesForUserResponseBodyDatabases] = None,
        request_id: str = None,
    ):
        # The names of the databases on which the user has permissions.
        self.databases = databases
        # The request ID. You can use the ID to query logs and troubleshoot issues.
        self.request_id = request_id

    def validate(self):
        if self.databases:
            for v1 in self.databases:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Databases'] = []
        if self.databases is not None:
            for k1 in self.databases:
                result['Databases'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.databases = []
        if m.get('Databases') is not None:
            for k1 in m.get('Databases'):
                temp_model = main_models.ListAuthorizedDatabasesForUserResponseBodyDatabases()
                self.databases.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListAuthorizedDatabasesForUserResponseBodyDatabases(DaraModel):
    def __init__(
        self,
        db_id: str = None,
        db_type: str = None,
        env_type: str = None,
        instance_id: str = None,
        logic: bool = None,
        permission_detail: main_models.ListAuthorizedDatabasesForUserResponseBodyDatabasesPermissionDetail = None,
        schema_name: str = None,
        search_name: str = None,
        user_id: str = None,
    ):
        # The database ID.
        self.db_id = db_id
        # The engine of the database.
        self.db_type = db_type
        # The type of the environment in which the database instance is deployed.
        self.env_type = env_type
        # The ID of the instance.
        self.instance_id = instance_id
        # Indicates whether the database is a logical database. Valid values:
        # 
        # *   **true.**: The database is a logical database
        # *   **false**: The database is a physical database.
        self.logic = logic
        # The details of permissions. The format of the permission details varies with the permission source. For example, if the permission source is a normal permission, the following parameters are returned.
        self.permission_detail = permission_detail
        # The database name.
        self.schema_name = schema_name
        # The name that is used to search for the database.
        self.search_name = search_name
        # The user IDs.
        self.user_id = user_id

    def validate(self):
        if self.permission_detail:
            self.permission_detail.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.db_id is not None:
            result['DbId'] = self.db_id

        if self.db_type is not None:
            result['DbType'] = self.db_type

        if self.env_type is not None:
            result['EnvType'] = self.env_type

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.logic is not None:
            result['Logic'] = self.logic

        if self.permission_detail is not None:
            result['PermissionDetail'] = self.permission_detail.to_map()

        if self.schema_name is not None:
            result['SchemaName'] = self.schema_name

        if self.search_name is not None:
            result['SearchName'] = self.search_name

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DbId') is not None:
            self.db_id = m.get('DbId')

        if m.get('DbType') is not None:
            self.db_type = m.get('DbType')

        if m.get('EnvType') is not None:
            self.env_type = m.get('EnvType')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Logic') is not None:
            self.logic = m.get('Logic')

        if m.get('PermissionDetail') is not None:
            temp_model = main_models.ListAuthorizedDatabasesForUserResponseBodyDatabasesPermissionDetail()
            self.permission_detail = temp_model.from_map(m.get('PermissionDetail'))

        if m.get('SchemaName') is not None:
            self.schema_name = m.get('SchemaName')

        if m.get('SearchName') is not None:
            self.search_name = m.get('SearchName')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

class ListAuthorizedDatabasesForUserResponseBodyDatabasesPermissionDetail(DaraModel):
    def __init__(
        self,
        ds_type: str = None,
        expire_date: str = None,
        message: str = None,
        perm_type: str = None,
    ):
        # The type of object on which the operation is performed.
        self.ds_type = ds_type
        # The time when the permissions expire.
        self.expire_date = expire_date
        # If the permission source is a permission policy, the value of this parameter includes the policy name and the operations that are allowed for the user.
        self.message = message
        # The type of the permission. Valid values:
        # 
        # *   **QUERY**: the query permission
        # *   **EXPORT**: the data export permission
        # *   **CORRECT**: the data change permission
        self.perm_type = perm_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ds_type is not None:
            result['DsType'] = self.ds_type

        if self.expire_date is not None:
            result['ExpireDate'] = self.expire_date

        if self.message is not None:
            result['Message'] = self.message

        if self.perm_type is not None:
            result['PermType'] = self.perm_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DsType') is not None:
            self.ds_type = m.get('DsType')

        if m.get('ExpireDate') is not None:
            self.expire_date = m.get('ExpireDate')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('PermType') is not None:
            self.perm_type = m.get('PermType')

        return self

