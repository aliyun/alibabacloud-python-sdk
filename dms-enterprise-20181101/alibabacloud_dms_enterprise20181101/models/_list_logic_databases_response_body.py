# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dms_enterprise20181101 import models as main_models
from darabonba.model import DaraModel

class ListLogicDatabasesResponseBody(DaraModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        logic_database_list: main_models.ListLogicDatabasesResponseBodyLogicDatabaseList = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        # The error code that is returned.
        self.error_code = error_code
        # The error message that is returned.
        self.error_message = error_message
        # The details of logical databases.
        self.logic_database_list = logic_database_list
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request is successful. Valid values:
        # 
        # - **true**: The request is successful.
        # - **false**: The request fails.
        self.success = success
        # The total number of logical databases.
        self.total_count = total_count

    def validate(self):
        if self.logic_database_list:
            self.logic_database_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.logic_database_list is not None:
            result['LogicDatabaseList'] = self.logic_database_list.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

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

        if m.get('LogicDatabaseList') is not None:
            temp_model = main_models.ListLogicDatabasesResponseBodyLogicDatabaseList()
            self.logic_database_list = temp_model.from_map(m.get('LogicDatabaseList'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListLogicDatabasesResponseBodyLogicDatabaseList(DaraModel):
    def __init__(
        self,
        logic_database: List[main_models.ListLogicDatabasesResponseBodyLogicDatabaseListLogicDatabase] = None,
    ):
        self.logic_database = logic_database

    def validate(self):
        if self.logic_database:
            for v1 in self.logic_database:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['LogicDatabase'] = []
        if self.logic_database is not None:
            for k1 in self.logic_database:
                result['LogicDatabase'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.logic_database = []
        if m.get('LogicDatabase') is not None:
            for k1 in m.get('LogicDatabase'):
                temp_model = main_models.ListLogicDatabasesResponseBodyLogicDatabaseListLogicDatabase()
                self.logic_database.append(temp_model.from_map(k1))

        return self

class ListLogicDatabasesResponseBodyLogicDatabaseListLogicDatabase(DaraModel):
    def __init__(
        self,
        alias: str = None,
        database_id: str = None,
        database_ids: main_models.ListLogicDatabasesResponseBodyLogicDatabaseListLogicDatabaseDatabaseIds = None,
        db_type: str = None,
        env_type: str = None,
        logic: bool = None,
        owner_id_list: main_models.ListLogicDatabasesResponseBodyLogicDatabaseListLogicDatabaseOwnerIdList = None,
        owner_name_list: main_models.ListLogicDatabasesResponseBodyLogicDatabaseListLogicDatabaseOwnerNameList = None,
        schema_name: str = None,
        search_name: str = None,
    ):
        # The alias of the logical database.
        self.alias = alias
        # The ID of the logical database.
        self.database_id = database_id
        # Logical database sub-ID list.
        self.database_ids = database_ids
        # The type of the logical database. For more information about the valid values of this parameter, see [DbType parameter](https://www.alibabacloud.com/help/en/data-management-service/latest/dbtype-parameter).
        self.db_type = db_type
        # The type of the environment to which the logical database belongs. Valid values:
        # 
        # - **product**: production environment
        # - **dev**: development environment
        # - **pre**: staging environment
        # - **test**: test environment
        # - **sit**: system integration testing (SIT) environment
        # - **uat**: user acceptance testing (UAT) environment
        # - **pet**: stress testing environment
        # - **stag**: STAG environment
        self.env_type = env_type
        # Indicates whether the database is a logical database. The return value is true.
        self.logic = logic
        # The IDs of the owners of the logical database.
        self.owner_id_list = owner_id_list
        # The names of the owners of the logical database.
        self.owner_name_list = owner_name_list
        # The name of the logical database.
        self.schema_name = schema_name
        # The name that is used to search for the logical database.
        # 
        # > We recommend that you do not use this parameter for business development. The format of the parameter value may be modified in later versions.
        self.search_name = search_name

    def validate(self):
        if self.database_ids:
            self.database_ids.validate()
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

        if self.database_id is not None:
            result['DatabaseId'] = self.database_id

        if self.database_ids is not None:
            result['DatabaseIds'] = self.database_ids.to_map()

        if self.db_type is not None:
            result['DbType'] = self.db_type

        if self.env_type is not None:
            result['EnvType'] = self.env_type

        if self.logic is not None:
            result['Logic'] = self.logic

        if self.owner_id_list is not None:
            result['OwnerIdList'] = self.owner_id_list.to_map()

        if self.owner_name_list is not None:
            result['OwnerNameList'] = self.owner_name_list.to_map()

        if self.schema_name is not None:
            result['SchemaName'] = self.schema_name

        if self.search_name is not None:
            result['SearchName'] = self.search_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Alias') is not None:
            self.alias = m.get('Alias')

        if m.get('DatabaseId') is not None:
            self.database_id = m.get('DatabaseId')

        if m.get('DatabaseIds') is not None:
            temp_model = main_models.ListLogicDatabasesResponseBodyLogicDatabaseListLogicDatabaseDatabaseIds()
            self.database_ids = temp_model.from_map(m.get('DatabaseIds'))

        if m.get('DbType') is not None:
            self.db_type = m.get('DbType')

        if m.get('EnvType') is not None:
            self.env_type = m.get('EnvType')

        if m.get('Logic') is not None:
            self.logic = m.get('Logic')

        if m.get('OwnerIdList') is not None:
            temp_model = main_models.ListLogicDatabasesResponseBodyLogicDatabaseListLogicDatabaseOwnerIdList()
            self.owner_id_list = temp_model.from_map(m.get('OwnerIdList'))

        if m.get('OwnerNameList') is not None:
            temp_model = main_models.ListLogicDatabasesResponseBodyLogicDatabaseListLogicDatabaseOwnerNameList()
            self.owner_name_list = temp_model.from_map(m.get('OwnerNameList'))

        if m.get('SchemaName') is not None:
            self.schema_name = m.get('SchemaName')

        if m.get('SearchName') is not None:
            self.search_name = m.get('SearchName')

        return self

class ListLogicDatabasesResponseBodyLogicDatabaseListLogicDatabaseOwnerNameList(DaraModel):
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

class ListLogicDatabasesResponseBodyLogicDatabaseListLogicDatabaseOwnerIdList(DaraModel):
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

class ListLogicDatabasesResponseBodyLogicDatabaseListLogicDatabaseDatabaseIds(DaraModel):
    def __init__(
        self,
        database_ids: List[int] = None,
    ):
        self.database_ids = database_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.database_ids is not None:
            result['DatabaseIds'] = self.database_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatabaseIds') is not None:
            self.database_ids = m.get('DatabaseIds')

        return self

