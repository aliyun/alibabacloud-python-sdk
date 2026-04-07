# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataworks_public20200518 import models as main_models
from darabonba.model import DaraModel

class GetMetaTableFullInfoResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.GetMetaTableFullInfoResponseBodyData = None,
        error_code: str = None,
        error_message: str = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The business data.
        self.data = data
        # The error code.
        self.error_code = error_code
        # The error message.
        self.error_message = error_message
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful.
        self.success = success

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

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.GetMetaTableFullInfoResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetMetaTableFullInfoResponseBodyData(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        column_list: List[main_models.GetMetaTableFullInfoResponseBodyDataColumnList] = None,
        comment: str = None,
        create_time: int = None,
        data_size: int = None,
        database_name: str = None,
        env_type: int = None,
        is_visible: int = None,
        last_access_time: int = None,
        last_ddl_time: int = None,
        last_modify_time: int = None,
        life_cycle: int = None,
        location: str = None,
        owner_id: str = None,
        partition_keys: str = None,
        project_id: int = None,
        project_name: str = None,
        schema: str = None,
        table_guid: str = None,
        table_name: str = None,
        tenant_id: int = None,
        total_column_count: int = None,
    ):
        # The EMR cluster ID.
        self.cluster_id = cluster_id
        # The fields in the table.
        self.column_list = column_list
        # The comment on the table.
        self.comment = comment
        # The time when the table was created. A timestamp is returned for this parameter. You can convert the timestamp to the related date based on the time zone that you use.
        self.create_time = create_time
        # The size of the storage space that is consumed by the table. Unit: bytes.
        self.data_size = data_size
        # The name of the database.
        self.database_name = database_name
        # The type of the environment. Valid values:
        # 
        # *   0: indicates that the table resides in the development environment.
        # *   1: indicates that the table resides in the production environment.
        self.env_type = env_type
        # The scope in which the table is visible. Valid values:
        # 
        # *   0: indicates that the table is visible to workspace members.
        # *   1: indicates that the table is visible to users within a tenant.
        # *   2: indicates that the table is visible to all tenants.
        # *   3: indicates that the table is visible only to the table owner.
        self.is_visible = is_visible
        # The time when the table was last accessed. A timestamp is returned for this parameter. You can convert the timestamp to the related date based on the time zone that you use.
        self.last_access_time = last_access_time
        # The time when the schema of the table was last changed. A timestamp is returned for this parameter. You can convert the timestamp to the related date based on the time zone that you use.
        self.last_ddl_time = last_ddl_time
        # The time when the table was last updated. A timestamp is returned for this parameter. You can convert the timestamp to the related date based on the time zone that you use.
        self.last_modify_time = last_modify_time
        # The lifecycle of the table. Unit: days.
        self.life_cycle = life_cycle
        # The storage path of the Hive table.
        self.location = location
        # The ID of the table owner.
        self.owner_id = owner_id
        # The partition key column.
        self.partition_keys = partition_keys
        # The ID of the workspace to which the table belongs.
        self.project_id = project_id
        # The name of the workspace to which the table belongs.
        self.project_name = project_name
        # The schema information of the table.
        self.schema = schema
        # The unique identifier of the table.
        self.table_guid = table_guid
        # The name of the table.
        self.table_name = table_name
        # The tenant ID.
        self.tenant_id = tenant_id
        # The total number of fields.
        self.total_column_count = total_column_count

    def validate(self):
        if self.column_list:
            for v1 in self.column_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        result['ColumnList'] = []
        if self.column_list is not None:
            for k1 in self.column_list:
                result['ColumnList'].append(k1.to_map() if k1 else None)

        if self.comment is not None:
            result['Comment'] = self.comment

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.data_size is not None:
            result['DataSize'] = self.data_size

        if self.database_name is not None:
            result['DatabaseName'] = self.database_name

        if self.env_type is not None:
            result['EnvType'] = self.env_type

        if self.is_visible is not None:
            result['IsVisible'] = self.is_visible

        if self.last_access_time is not None:
            result['LastAccessTime'] = self.last_access_time

        if self.last_ddl_time is not None:
            result['LastDdlTime'] = self.last_ddl_time

        if self.last_modify_time is not None:
            result['LastModifyTime'] = self.last_modify_time

        if self.life_cycle is not None:
            result['LifeCycle'] = self.life_cycle

        if self.location is not None:
            result['Location'] = self.location

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.partition_keys is not None:
            result['PartitionKeys'] = self.partition_keys

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.project_name is not None:
            result['ProjectName'] = self.project_name

        if self.schema is not None:
            result['Schema'] = self.schema

        if self.table_guid is not None:
            result['TableGuid'] = self.table_guid

        if self.table_name is not None:
            result['TableName'] = self.table_name

        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id

        if self.total_column_count is not None:
            result['TotalColumnCount'] = self.total_column_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        self.column_list = []
        if m.get('ColumnList') is not None:
            for k1 in m.get('ColumnList'):
                temp_model = main_models.GetMetaTableFullInfoResponseBodyDataColumnList()
                self.column_list.append(temp_model.from_map(k1))

        if m.get('Comment') is not None:
            self.comment = m.get('Comment')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('DataSize') is not None:
            self.data_size = m.get('DataSize')

        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')

        if m.get('EnvType') is not None:
            self.env_type = m.get('EnvType')

        if m.get('IsVisible') is not None:
            self.is_visible = m.get('IsVisible')

        if m.get('LastAccessTime') is not None:
            self.last_access_time = m.get('LastAccessTime')

        if m.get('LastDdlTime') is not None:
            self.last_ddl_time = m.get('LastDdlTime')

        if m.get('LastModifyTime') is not None:
            self.last_modify_time = m.get('LastModifyTime')

        if m.get('LifeCycle') is not None:
            self.life_cycle = m.get('LifeCycle')

        if m.get('Location') is not None:
            self.location = m.get('Location')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PartitionKeys') is not None:
            self.partition_keys = m.get('PartitionKeys')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        if m.get('Schema') is not None:
            self.schema = m.get('Schema')

        if m.get('TableGuid') is not None:
            self.table_guid = m.get('TableGuid')

        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')

        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')

        if m.get('TotalColumnCount') is not None:
            self.total_column_count = m.get('TotalColumnCount')

        return self

class GetMetaTableFullInfoResponseBodyDataColumnList(DaraModel):
    def __init__(
        self,
        caption: str = None,
        column_guid: str = None,
        column_name: str = None,
        column_type: str = None,
        comment: str = None,
        is_foreign_key: bool = None,
        is_partition_column: bool = None,
        is_primary_key: bool = None,
        position: int = None,
    ):
        # The description of the field.
        self.caption = caption
        # The unique identifier of the field.
        self.column_guid = column_guid
        # The name of the field.
        self.column_name = column_name
        # The data type of the field.
        self.column_type = column_type
        # The remarks of the field.
        self.comment = comment
        # Indicates whether the field is a foreign key. Valid values:
        # 
        # *   true
        # *   false
        self.is_foreign_key = is_foreign_key
        # Indicates whether the field is a partition field. Valid values:
        # 
        # *   true
        # *   false
        self.is_partition_column = is_partition_column
        # Indicates whether the field is a primary key. Valid values:
        # 
        # *   true
        # *   false
        self.is_primary_key = is_primary_key
        # The sequence number of the field.
        self.position = position

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.caption is not None:
            result['Caption'] = self.caption

        if self.column_guid is not None:
            result['ColumnGuid'] = self.column_guid

        if self.column_name is not None:
            result['ColumnName'] = self.column_name

        if self.column_type is not None:
            result['ColumnType'] = self.column_type

        if self.comment is not None:
            result['Comment'] = self.comment

        if self.is_foreign_key is not None:
            result['IsForeignKey'] = self.is_foreign_key

        if self.is_partition_column is not None:
            result['IsPartitionColumn'] = self.is_partition_column

        if self.is_primary_key is not None:
            result['IsPrimaryKey'] = self.is_primary_key

        if self.position is not None:
            result['Position'] = self.position

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Caption') is not None:
            self.caption = m.get('Caption')

        if m.get('ColumnGuid') is not None:
            self.column_guid = m.get('ColumnGuid')

        if m.get('ColumnName') is not None:
            self.column_name = m.get('ColumnName')

        if m.get('ColumnType') is not None:
            self.column_type = m.get('ColumnType')

        if m.get('Comment') is not None:
            self.comment = m.get('Comment')

        if m.get('IsForeignKey') is not None:
            self.is_foreign_key = m.get('IsForeignKey')

        if m.get('IsPartitionColumn') is not None:
            self.is_partition_column = m.get('IsPartitionColumn')

        if m.get('IsPrimaryKey') is not None:
            self.is_primary_key = m.get('IsPrimaryKey')

        if m.get('Position') is not None:
            self.position = m.get('Position')

        return self

