# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dms_enterprise20181101 import models as main_models
from darabonba.model import DaraModel

class SearchDatabaseResponseBody(DaraModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        search_database_list: main_models.SearchDatabaseResponseBodySearchDatabaseList = None,
        success: bool = None,
        total_count: int = None,
    ):
        # The error code.
        self.error_code = error_code
        # The error message.
        self.error_message = error_message
        # The ID of the request.
        self.request_id = request_id
        # The information about the databases.
        self.search_database_list = search_database_list
        # Indicates whether the request is successful. Valid values:
        # 
        # *   **true**: The request is successful.
        # *   **false**: The request fails.
        self.success = success
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.search_database_list:
            self.search_database_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.search_database_list is not None:
            result['SearchDatabaseList'] = self.search_database_list.to_map()

        if self.success is not None:
            result['Success'] = self.success

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SearchDatabaseList') is not None:
            temp_model = main_models.SearchDatabaseResponseBodySearchDatabaseList()
            self.search_database_list = temp_model.from_map(m.get('SearchDatabaseList'))

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class SearchDatabaseResponseBodySearchDatabaseList(DaraModel):
    def __init__(
        self,
        search_database: List[main_models.SearchDatabaseResponseBodySearchDatabaseListSearchDatabase] = None,
    ):
        self.search_database = search_database

    def validate(self):
        if self.search_database:
            for v1 in self.search_database:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['SearchDatabase'] = []
        if self.search_database is not None:
            for k1 in self.search_database:
                result['SearchDatabase'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.search_database = []
        if m.get('SearchDatabase') is not None:
            for k1 in m.get('SearchDatabase'):
                temp_model = main_models.SearchDatabaseResponseBodySearchDatabaseListSearchDatabase()
                self.search_database.append(temp_model.from_map(k1))

        return self

class SearchDatabaseResponseBodySearchDatabaseListSearchDatabase(DaraModel):
    def __init__(
        self,
        alias: str = None,
        catalog_name: str = None,
        database_id: str = None,
        datalink_name: str = None,
        db_type: str = None,
        dba_id: str = None,
        encoding: str = None,
        env_type: str = None,
        host: str = None,
        logic: bool = None,
        owner_id_list: main_models.SearchDatabaseResponseBodySearchDatabaseListSearchDatabaseOwnerIdList = None,
        owner_name_list: main_models.SearchDatabaseResponseBodySearchDatabaseListSearchDatabaseOwnerNameList = None,
        port: int = None,
        schema_name: str = None,
        search_name: str = None,
        sid: str = None,
    ):
        # The alias of the database.
        self.alias = alias
        # The name of the catalog to which the database belongs.
        # 
        # > If the type of the database engine is PostgreSQL, the name of the database is displayed.
        self.catalog_name = catalog_name
        # The ID of the database.
        self.database_id = database_id
        # The name of the data link for cross-database queries.
        self.datalink_name = datalink_name
        # The type of the database engine.
        self.db_type = db_type
        # The ID of the user who assumes the database administrator (DBA) role.
        self.dba_id = dba_id
        # The encoding method of the database.
        self.encoding = encoding
        # The environment type of the database. For more information, see [Change the environment type of an instance](https://help.aliyun.com/document_detail/163309.html).
        self.env_type = env_type
        # The endpoint of the instance in which the database resides.
        self.host = host
        # Indicates whether the database is a logical database. Valid values:
        # 
        # *   **true**: The database is a logical database.
        # *   **false**: The database is not a logical database.
        self.logic = logic
        # The IDs of the owners of the databases.
        self.owner_id_list = owner_id_list
        # The nicknames of the database owners.
        self.owner_name_list = owner_name_list
        # The port of the instance in which the database resides.
        self.port = port
        # The name of the database.
        self.schema_name = schema_name
        # The name that is used to search for the database.
        self.search_name = search_name
        # The system ID (SID) of the instance in which the database resides.
        self.sid = sid

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
        if self.alias is not None:
            result['Alias'] = self.alias

        if self.catalog_name is not None:
            result['CatalogName'] = self.catalog_name

        if self.database_id is not None:
            result['DatabaseId'] = self.database_id

        if self.datalink_name is not None:
            result['DatalinkName'] = self.datalink_name

        if self.db_type is not None:
            result['DbType'] = self.db_type

        if self.dba_id is not None:
            result['DbaId'] = self.dba_id

        if self.encoding is not None:
            result['Encoding'] = self.encoding

        if self.env_type is not None:
            result['EnvType'] = self.env_type

        if self.host is not None:
            result['Host'] = self.host

        if self.logic is not None:
            result['Logic'] = self.logic

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Alias') is not None:
            self.alias = m.get('Alias')

        if m.get('CatalogName') is not None:
            self.catalog_name = m.get('CatalogName')

        if m.get('DatabaseId') is not None:
            self.database_id = m.get('DatabaseId')

        if m.get('DatalinkName') is not None:
            self.datalink_name = m.get('DatalinkName')

        if m.get('DbType') is not None:
            self.db_type = m.get('DbType')

        if m.get('DbaId') is not None:
            self.dba_id = m.get('DbaId')

        if m.get('Encoding') is not None:
            self.encoding = m.get('Encoding')

        if m.get('EnvType') is not None:
            self.env_type = m.get('EnvType')

        if m.get('Host') is not None:
            self.host = m.get('Host')

        if m.get('Logic') is not None:
            self.logic = m.get('Logic')

        if m.get('OwnerIdList') is not None:
            temp_model = main_models.SearchDatabaseResponseBodySearchDatabaseListSearchDatabaseOwnerIdList()
            self.owner_id_list = temp_model.from_map(m.get('OwnerIdList'))

        if m.get('OwnerNameList') is not None:
            temp_model = main_models.SearchDatabaseResponseBodySearchDatabaseListSearchDatabaseOwnerNameList()
            self.owner_name_list = temp_model.from_map(m.get('OwnerNameList'))

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('SchemaName') is not None:
            self.schema_name = m.get('SchemaName')

        if m.get('SearchName') is not None:
            self.search_name = m.get('SearchName')

        if m.get('Sid') is not None:
            self.sid = m.get('Sid')

        return self

class SearchDatabaseResponseBodySearchDatabaseListSearchDatabaseOwnerNameList(DaraModel):
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

class SearchDatabaseResponseBodySearchDatabaseListSearchDatabaseOwnerIdList(DaraModel):
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

