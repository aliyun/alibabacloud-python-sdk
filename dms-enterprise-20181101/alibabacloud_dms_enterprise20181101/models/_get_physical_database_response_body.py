# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dms_enterprise20181101 import models as main_models
from darabonba.model import DaraModel

class GetPhysicalDatabaseResponseBody(DaraModel):
    def __init__(
        self,
        database: main_models.GetPhysicalDatabaseResponseBodyDatabase = None,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The information about the physical database.
        self.database = database
        # The error code returned if the request failed.
        self.error_code = error_code
        # The error message returned if the request failed.
        self.error_message = error_message
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request is successful.
        self.success = success

    def validate(self):
        if self.database:
            self.database.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.database is not None:
            result['Database'] = self.database.to_map()

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Database') is not None:
            temp_model = main_models.GetPhysicalDatabaseResponseBodyDatabase()
            self.database = temp_model.from_map(m.get('Database'))

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetPhysicalDatabaseResponseBodyDatabase(DaraModel):
    def __init__(
        self,
        catalog_name: str = None,
        database_id: str = None,
        db_type: str = None,
        dba_id: str = None,
        dba_name: str = None,
        encoding: str = None,
        env_type: str = None,
        host: str = None,
        instance_alias: str = None,
        instance_id: str = None,
        owner_id_list: main_models.GetPhysicalDatabaseResponseBodyDatabaseOwnerIdList = None,
        owner_name_list: main_models.GetPhysicalDatabaseResponseBodyDatabaseOwnerNameList = None,
        port: int = None,
        schema_name: str = None,
        search_name: str = None,
        sid: str = None,
        state: str = None,
    ):
        # The name of the catalog to which the database belongs.
        # 
        # > : If the database is a PostgreSQL database, the name of the database is displayed.
        self.catalog_name = catalog_name
        # The ID of the physical database.
        self.database_id = database_id
        # The type of the database engine.
        self.db_type = db_type
        # The user ID of the DBA in the destination database.
        self.dba_id = dba_id
        # The nickname of the database administrator (DBA) in the destination database.
        self.dba_name = dba_name
        # The encoding format of the database.
        self.encoding = encoding
        # The type of the environment to which the database belongs. For more information, see [Change the environment type of an instance](https://help.aliyun.com/document_detail/163309.html).
        self.env_type = env_type
        # The endpoint that is used to connect to the database.
        self.host = host
        # The alias of the database instance.
        self.instance_alias = instance_alias
        # The instance ID of the destination database.
        self.instance_id = instance_id
        # The user IDs of the database owners.
        self.owner_id_list = owner_id_list
        # The nicknames of the database owners.
        self.owner_name_list = owner_name_list
        # The port that is used to connect to the database.
        self.port = port
        # The name of the database.
        # 
        # > : If the database is a PostgreSQL database, the name of the mode is displayed.
        self.schema_name = schema_name
        # The name that is used for searching the database.
        self.search_name = search_name
        # The system ID (SID) of the database.
        # 
        # > : The value of the parameter is returned only for Oracle databases.
        self.sid = sid
        # The state of the database. Valid values:
        # 
        # *   **NORMAL**: The database is normal.
        # *   **DISABLE**: The database is disabled.
        # *   **OFFLINE**: The database is unpublished.
        # *   **NOT_EXIST**: The database does not exist.
        self.state = state

    def validate(self):
        if self.owner_id_list:
            self.owner_id_list.validate()
        if self.owner_name_list:
            self.owner_name_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.catalog_name is not None:
            result['CatalogName'] = self.catalog_name

        if self.database_id is not None:
            result['DatabaseId'] = self.database_id

        if self.db_type is not None:
            result['DbType'] = self.db_type

        if self.dba_id is not None:
            result['DbaId'] = self.dba_id

        if self.dba_name is not None:
            result['DbaName'] = self.dba_name

        if self.encoding is not None:
            result['Encoding'] = self.encoding

        if self.env_type is not None:
            result['EnvType'] = self.env_type

        if self.host is not None:
            result['Host'] = self.host

        if self.instance_alias is not None:
            result['InstanceAlias'] = self.instance_alias

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.owner_id_list is not None:
            result['OwnerIdList'] = self.owner_id_list.to_map()

        if self.owner_name_list is not None:
            result['OwnerNameList'] = self.owner_name_list.to_map()

        if self.port is not None:
            result['Port'] = self.port

        if self.schema_name is not None:
            result['SchemaName'] = self.schema_name

        if self.search_name is not None:
            result['SearchName'] = self.search_name

        if self.sid is not None:
            result['Sid'] = self.sid

        if self.state is not None:
            result['State'] = self.state

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CatalogName') is not None:
            self.catalog_name = m.get('CatalogName')

        if m.get('DatabaseId') is not None:
            self.database_id = m.get('DatabaseId')

        if m.get('DbType') is not None:
            self.db_type = m.get('DbType')

        if m.get('DbaId') is not None:
            self.dba_id = m.get('DbaId')

        if m.get('DbaName') is not None:
            self.dba_name = m.get('DbaName')

        if m.get('Encoding') is not None:
            self.encoding = m.get('Encoding')

        if m.get('EnvType') is not None:
            self.env_type = m.get('EnvType')

        if m.get('Host') is not None:
            self.host = m.get('Host')

        if m.get('InstanceAlias') is not None:
            self.instance_alias = m.get('InstanceAlias')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('OwnerIdList') is not None:
            temp_model = main_models.GetPhysicalDatabaseResponseBodyDatabaseOwnerIdList()
            self.owner_id_list = temp_model.from_map(m.get('OwnerIdList'))

        if m.get('OwnerNameList') is not None:
            temp_model = main_models.GetPhysicalDatabaseResponseBodyDatabaseOwnerNameList()
            self.owner_name_list = temp_model.from_map(m.get('OwnerNameList'))

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('SchemaName') is not None:
            self.schema_name = m.get('SchemaName')

        if m.get('SearchName') is not None:
            self.search_name = m.get('SearchName')

        if m.get('Sid') is not None:
            self.sid = m.get('Sid')

        if m.get('State') is not None:
            self.state = m.get('State')

        return self

class GetPhysicalDatabaseResponseBodyDatabaseOwnerNameList(DaraModel):
    def __init__(
        self,
        owner_names: List[str] = None,
    ):
        self.owner_names = owner_names

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.owner_names is not None:
            result['OwnerNames'] = self.owner_names

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerNames') is not None:
            self.owner_names = m.get('OwnerNames')

        return self

class GetPhysicalDatabaseResponseBodyDatabaseOwnerIdList(DaraModel):
    def __init__(
        self,
        owner_ids: List[str] = None,
    ):
        self.owner_ids = owner_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.owner_ids is not None:
            result['OwnerIds'] = self.owner_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerIds') is not None:
            self.owner_ids = m.get('OwnerIds')

        return self

