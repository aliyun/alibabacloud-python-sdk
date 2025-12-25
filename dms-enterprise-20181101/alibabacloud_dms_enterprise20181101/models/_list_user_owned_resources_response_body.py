# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dms_enterprise20181101 import models as main_models
from darabonba.model import DaraModel

class ListUserOwnedResourcesResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.ListUserOwnedResourcesResponseBodyData = None,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        # Indicates whether the request was successful. Valid values:
        self.data = data
        # The error code returned if the request failed.
        self.error_code = error_code
        # The error message that is returned if the request failed.
        self.error_message = error_message
        # The request ID. You can use the request ID to locate logs and troubleshoot issues.
        self.request_id = request_id
        # Indicates whether the request was successful.
        self.success = success
        # The total number of entries returned. By default, this parameter is not returned.
        self.total_count = total_count

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.ListUserOwnedResourcesResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListUserOwnedResourcesResponseBodyData(DaraModel):
    def __init__(
        self,
        resource_list: List[main_models.ListUserOwnedResourcesResponseBodyDataResourceList] = None,
    ):
        self.resource_list = resource_list

    def validate(self):
        if self.resource_list:
            for v1 in self.resource_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['resourceList'] = []
        if self.resource_list is not None:
            for k1 in self.resource_list:
                result['resourceList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.resource_list = []
        if m.get('resourceList') is not None:
            for k1 in m.get('resourceList'):
                temp_model = main_models.ListUserOwnedResourcesResponseBodyDataResourceList()
                self.resource_list.append(temp_model.from_map(k1))

        return self

class ListUserOwnedResourcesResponseBodyDataResourceList(DaraModel):
    def __init__(
        self,
        alias: str = None,
        db_id: str = None,
        db_instance_id: str = None,
        db_type: str = None,
        env_type: str = None,
        host: str = None,
        instance_id: str = None,
        logic: bool = None,
        port: int = None,
        schema_name: str = None,
        search_name: str = None,
        table_id: str = None,
        table_name: str = None,
    ):
        # The alias of the instance.
        self.alias = alias
        # The ID of the database in DMS.
        self.db_id = db_id
        # The ID of the instance to which the database belongs.
        self.db_instance_id = db_instance_id
        # The database engine type. For more information about the valid values of the DbType parameter, see [DbType parameter](https://help.aliyun.com/document_detail/198106.html).
        self.db_type = db_type
        # The type of the environment to which the database instance belongs.
        self.env_type = env_type
        # The endpoint of the instance to which the database belongs.
        self.host = host
        # The ID of the instance.
        self.instance_id = instance_id
        # Indicates whether the database is a logical database. Valid values:
        # 
        # *   **true**: The database is a logical database
        # *   **false**: The database is a physical database.
        self.logic = logic
        # The connection port of the instance to which the database belongs.
        self.port = port
        # The name of the database.
        self.schema_name = schema_name
        # The query name of the database.
        self.search_name = search_name
        # The table ID.
        self.table_id = table_id
        # The table name.
        self.table_name = table_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alias is not None:
            result['Alias'] = self.alias

        if self.db_id is not None:
            result['DbId'] = self.db_id

        if self.db_instance_id is not None:
            result['DbInstanceId'] = self.db_instance_id

        if self.db_type is not None:
            result['DbType'] = self.db_type

        if self.env_type is not None:
            result['EnvType'] = self.env_type

        if self.host is not None:
            result['Host'] = self.host

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.logic is not None:
            result['Logic'] = self.logic

        if self.port is not None:
            result['Port'] = self.port

        if self.schema_name is not None:
            result['SchemaName'] = self.schema_name

        if self.search_name is not None:
            result['SearchName'] = self.search_name

        if self.table_id is not None:
            result['TableId'] = self.table_id

        if self.table_name is not None:
            result['TableName'] = self.table_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Alias') is not None:
            self.alias = m.get('Alias')

        if m.get('DbId') is not None:
            self.db_id = m.get('DbId')

        if m.get('DbInstanceId') is not None:
            self.db_instance_id = m.get('DbInstanceId')

        if m.get('DbType') is not None:
            self.db_type = m.get('DbType')

        if m.get('EnvType') is not None:
            self.env_type = m.get('EnvType')

        if m.get('Host') is not None:
            self.host = m.get('Host')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Logic') is not None:
            self.logic = m.get('Logic')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('SchemaName') is not None:
            self.schema_name = m.get('SchemaName')

        if m.get('SearchName') is not None:
            self.search_name = m.get('SearchName')

        if m.get('TableId') is not None:
            self.table_id = m.get('TableId')

        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')

        return self

