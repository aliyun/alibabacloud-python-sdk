# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dataworks_public20200518 import models as main_models
from darabonba.model import DaraModel

class GetMetaTableBasicInfoResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.GetMetaTableBasicInfoResponseBodyData = None,
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
            temp_model = main_models.GetMetaTableBasicInfoResponseBodyData()
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

class GetMetaTableBasicInfoResponseBodyData(DaraModel):
    def __init__(
        self,
        caption: str = None,
        cluster_id: str = None,
        column_count: int = None,
        comment: str = None,
        create_time: int = None,
        data_size: int = None,
        database_name: str = None,
        env_type: int = None,
        favorite_count: int = None,
        is_partition_table: bool = None,
        is_view: bool = None,
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
        read_count: int = None,
        schema: str = None,
        table_guid: str = None,
        table_name: str = None,
        tenant_id: int = None,
        view_count: int = None,
    ):
        # The display name of the metatable.
        self.caption = caption
        # The ID of the EMR cluster.
        self.cluster_id = cluster_id
        # The number of fields.
        self.column_count = column_count
        # The comment of the metatable.
        self.comment = comment
        # The time when the metatable was created.
        self.create_time = create_time
        # The size of storage space that is occupied by the metatable. Unit: bytes.
        self.data_size = data_size
        # The name of the metadatabase.
        self.database_name = database_name
        # The type of the environment. Valid values:
        # 
        # *   0: development environment
        # *   1: production environment
        self.env_type = env_type
        # The number of times the metatable was added to a favorite list. This parameter is returned only if you set the Extension parameter to true and takes effect only if you set the DataSourceType parameter to odps.
        self.favorite_count = favorite_count
        # Indicates whether the metatable is a partitioned table. Valid values:
        # 
        # *   true
        # *   false
        self.is_partition_table = is_partition_table
        # Indicates whether the metatable is a view. Valid values:
        # 
        # *   true
        # *   false
        self.is_view = is_view
        # The scope in which the metatable is visible. Valid values:
        # 
        # *   0: The metatable is visible to workspace members.
        # *   1: The metatable is visible to users within the tenant.
        # *   2: The metatable is visible to all tenants.
        # *   3: The metatable is visible only to the metatable owner.
        self.is_visible = is_visible
        # The time when the metatable was last accessed.
        self.last_access_time = last_access_time
        # The time when the schema of the metatable was last changed.
        self.last_ddl_time = last_ddl_time
        # The time when the metatable was last updated.
        self.last_modify_time = last_modify_time
        # The lifecycle of the table. Unit: day.
        # 
        # >  If the lifecycle is not set for a MaxCompute table, the return value is 0, indicating that the table is permanently valid.
        self.life_cycle = life_cycle
        # The storage path of the Hive metadatabase.
        self.location = location
        # The ID of the metatable owner.
        self.owner_id = owner_id
        # The partition key of the Hive metatable.
        self.partition_keys = partition_keys
        # The workspace ID.
        self.project_id = project_id
        # The name of the workspace.
        self.project_name = project_name
        # The number of times the metatable was read. This parameter is returned only if you set the Extension parameter to true and takes effect only if you set the DataSourceType parameter to odps.
        self.read_count = read_count
        # The schema information of the metatable. This parameter is returned if the three-layer model of MaxCompute is enabled.
        self.schema = schema
        # The GUID of the metatable.
        self.table_guid = table_guid
        # The name of the metatable.
        self.table_name = table_name
        # The tenant ID.
        self.tenant_id = tenant_id
        # The number of times the metatable was viewed. This parameter is returned only if you set the Extension parameter to true and takes effect only if you set the DataSourceType parameter to odps.
        self.view_count = view_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.caption is not None:
            result['Caption'] = self.caption

        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.column_count is not None:
            result['ColumnCount'] = self.column_count

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

        if self.favorite_count is not None:
            result['FavoriteCount'] = self.favorite_count

        if self.is_partition_table is not None:
            result['IsPartitionTable'] = self.is_partition_table

        if self.is_view is not None:
            result['IsView'] = self.is_view

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

        if self.read_count is not None:
            result['ReadCount'] = self.read_count

        if self.schema is not None:
            result['Schema'] = self.schema

        if self.table_guid is not None:
            result['TableGuid'] = self.table_guid

        if self.table_name is not None:
            result['TableName'] = self.table_name

        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id

        if self.view_count is not None:
            result['ViewCount'] = self.view_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Caption') is not None:
            self.caption = m.get('Caption')

        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('ColumnCount') is not None:
            self.column_count = m.get('ColumnCount')

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

        if m.get('FavoriteCount') is not None:
            self.favorite_count = m.get('FavoriteCount')

        if m.get('IsPartitionTable') is not None:
            self.is_partition_table = m.get('IsPartitionTable')

        if m.get('IsView') is not None:
            self.is_view = m.get('IsView')

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

        if m.get('ReadCount') is not None:
            self.read_count = m.get('ReadCount')

        if m.get('Schema') is not None:
            self.schema = m.get('Schema')

        if m.get('TableGuid') is not None:
            self.table_guid = m.get('TableGuid')

        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')

        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')

        if m.get('ViewCount') is not None:
            self.view_count = m.get('ViewCount')

        return self

