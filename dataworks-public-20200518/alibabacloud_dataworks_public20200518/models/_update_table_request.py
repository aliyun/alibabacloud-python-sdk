# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataworks_public20200518 import models as main_models
from darabonba.model import DaraModel

class UpdateTableRequest(DaraModel):
    def __init__(
        self,
        app_guid: str = None,
        category_id: int = None,
        columns: List[main_models.UpdateTableRequestColumns] = None,
        comment: str = None,
        create_if_not_exists: bool = None,
        endpoint: str = None,
        env_type: int = None,
        external_table_type: str = None,
        has_part: int = None,
        is_view: int = None,
        life_cycle: int = None,
        location: str = None,
        logical_level_id: int = None,
        owner_id: str = None,
        physics_level_id: int = None,
        project_id: int = None,
        schema: str = None,
        table_name: str = None,
        themes: List[main_models.UpdateTableRequestThemes] = None,
        visibility: int = None,
    ):
        # The unique identifier of the MaxCompute project. Specify the GUID in the odps.{projectName} format.
        self.app_guid = app_guid
        # The ID of the associated category.
        self.category_id = category_id
        # The list of fields.
        self.columns = columns
        # The comment.
        self.comment = comment
        # Specifies whether the table exists. Valid values:
        # 
        # *   true: The table exists.
        # *   false: The table does not exist.
        # 
        # This parameter is deprecated. Do not use this parameter.
        self.create_if_not_exists = create_if_not_exists
        # The endpoint of MaxCompute. If you do not specify this parameter, the endpoint of the MaxCompute project is used.
        self.endpoint = endpoint
        # The environment of the DataWorks workspace. Valid values: 0 and 1. The value 0 indicates the development environment. The value 1 indicates the production environment.
        self.env_type = env_type
        # The type of the external table. Valid values: 0, 1, 2, and 3. The value 0 indicates that the external table is an OSS external table. The value 1 indicates that the external table is a Tablestore external table. The value 2 indicates that the external table is a volume external table. The value 3 indicates that the external table is a MySQL external table. This parameter is deprecated. Do not use this parameter.
        self.external_table_type = external_table_type
        # Specifies whether the table that you want to update is a partitioned table. Valid values: 0 and 1. The value 0 indicates that the table is not a partitioned table. The value 1 indicates that the table is a partitioned table. This parameter is deprecated. Do not use this parameter. The Column.N.isPartitionCol parameter is used instead of the HasPart parameter to specify whether the MaxCompute table is a partitioned table. If the Column.N.isPartitionCol parameter is set to 1, the MaxCompute table is a partitioned table.
        self.has_part = has_part
        # Specifies whether the table is a view. Valid values: 0 and 1. The value 0 indicates that the table is not a view. The value 1 indicates that the table is a view. This parameter is deprecated. Do not use this parameter.
        self.is_view = is_view
        # The lifecycle of the table. Unit: days. If this parameter is left empty, the table is permanently stored.
        self.life_cycle = life_cycle
        # The storage location of the external table. This parameter is deprecated. Do not use this parameter.
        self.location = location
        # The ID of the logical level.
        self.logical_level_id = logical_level_id
        self.owner_id = owner_id
        # The ID of the physical layer.
        self.physics_level_id = physics_level_id
        # The DataWorks workspace ID. You can log on to the DataWorks console to obtain the ID of the DataWorks workspace.
        self.project_id = project_id
        # The schema information of the table. You need to enter the schema information of the table if you enable the table schema in MaxCompute.
        self.schema = schema
        # The name of the MaxCompute table.
        # 
        # This parameter is required.
        self.table_name = table_name
        # The list of fields.
        self.themes = themes
        # The scope in which the table is visible. Valid values: 0, 1, and 2. The value 0 indicates that the table is invisible to all workspace members. The value 1 indicates that the table is visible to all workspace members. The value 2 indicates that the table is visible to workspace members.
        self.visibility = visibility

    def validate(self):
        if self.columns:
            for v1 in self.columns:
                 if v1:
                    v1.validate()
        if self.themes:
            for v1 in self.themes:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_guid is not None:
            result['AppGuid'] = self.app_guid

        if self.category_id is not None:
            result['CategoryId'] = self.category_id

        result['Columns'] = []
        if self.columns is not None:
            for k1 in self.columns:
                result['Columns'].append(k1.to_map() if k1 else None)

        if self.comment is not None:
            result['Comment'] = self.comment

        if self.create_if_not_exists is not None:
            result['CreateIfNotExists'] = self.create_if_not_exists

        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint

        if self.env_type is not None:
            result['EnvType'] = self.env_type

        if self.external_table_type is not None:
            result['ExternalTableType'] = self.external_table_type

        if self.has_part is not None:
            result['HasPart'] = self.has_part

        if self.is_view is not None:
            result['IsView'] = self.is_view

        if self.life_cycle is not None:
            result['LifeCycle'] = self.life_cycle

        if self.location is not None:
            result['Location'] = self.location

        if self.logical_level_id is not None:
            result['LogicalLevelId'] = self.logical_level_id

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.physics_level_id is not None:
            result['PhysicsLevelId'] = self.physics_level_id

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.schema is not None:
            result['Schema'] = self.schema

        if self.table_name is not None:
            result['TableName'] = self.table_name

        result['Themes'] = []
        if self.themes is not None:
            for k1 in self.themes:
                result['Themes'].append(k1.to_map() if k1 else None)

        if self.visibility is not None:
            result['Visibility'] = self.visibility

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppGuid') is not None:
            self.app_guid = m.get('AppGuid')

        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')

        self.columns = []
        if m.get('Columns') is not None:
            for k1 in m.get('Columns'):
                temp_model = main_models.UpdateTableRequestColumns()
                self.columns.append(temp_model.from_map(k1))

        if m.get('Comment') is not None:
            self.comment = m.get('Comment')

        if m.get('CreateIfNotExists') is not None:
            self.create_if_not_exists = m.get('CreateIfNotExists')

        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')

        if m.get('EnvType') is not None:
            self.env_type = m.get('EnvType')

        if m.get('ExternalTableType') is not None:
            self.external_table_type = m.get('ExternalTableType')

        if m.get('HasPart') is not None:
            self.has_part = m.get('HasPart')

        if m.get('IsView') is not None:
            self.is_view = m.get('IsView')

        if m.get('LifeCycle') is not None:
            self.life_cycle = m.get('LifeCycle')

        if m.get('Location') is not None:
            self.location = m.get('Location')

        if m.get('LogicalLevelId') is not None:
            self.logical_level_id = m.get('LogicalLevelId')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PhysicsLevelId') is not None:
            self.physics_level_id = m.get('PhysicsLevelId')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('Schema') is not None:
            self.schema = m.get('Schema')

        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')

        self.themes = []
        if m.get('Themes') is not None:
            for k1 in m.get('Themes'):
                temp_model = main_models.UpdateTableRequestThemes()
                self.themes.append(temp_model.from_map(k1))

        if m.get('Visibility') is not None:
            self.visibility = m.get('Visibility')

        return self

class UpdateTableRequestThemes(DaraModel):
    def __init__(
        self,
        theme_id: int = None,
        theme_level: int = None,
    ):
        # The ID of the associated topic.
        self.theme_id = theme_id
        # The level that corresponds to the topic ID.
        self.theme_level = theme_level

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.theme_id is not None:
            result['ThemeId'] = self.theme_id

        if self.theme_level is not None:
            result['ThemeLevel'] = self.theme_level

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ThemeId') is not None:
            self.theme_id = m.get('ThemeId')

        if m.get('ThemeLevel') is not None:
            self.theme_level = m.get('ThemeLevel')

        return self

class UpdateTableRequestColumns(DaraModel):
    def __init__(
        self,
        column_name: str = None,
        column_name_cn: str = None,
        column_type: str = None,
        comment: str = None,
        is_partition_col: bool = None,
        length: int = None,
        seq_number: int = None,
    ):
        # The name of the field.
        # 
        # This parameter is required.
        self.column_name = column_name
        # The display name of the field.
        self.column_name_cn = column_name_cn
        # The type of the field. For more information, see MaxCompute field types.
        # 
        # This parameter is required.
        self.column_type = column_type
        # The comment of the field.
        self.comment = comment
        # Specifies whether the field is a partition field. Valid values: 0 and 1. The value 0 indicates that the field is not a partition field. The value 1 indicates that the field is a partition field.
        self.is_partition_col = is_partition_col
        # The length of the field.
        self.length = length
        # The sequence number of the field. If the field is a partition field, this parameter is not supported.
        self.seq_number = seq_number

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.column_name is not None:
            result['ColumnName'] = self.column_name

        if self.column_name_cn is not None:
            result['ColumnNameCn'] = self.column_name_cn

        if self.column_type is not None:
            result['ColumnType'] = self.column_type

        if self.comment is not None:
            result['Comment'] = self.comment

        if self.is_partition_col is not None:
            result['IsPartitionCol'] = self.is_partition_col

        if self.length is not None:
            result['Length'] = self.length

        if self.seq_number is not None:
            result['SeqNumber'] = self.seq_number

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ColumnName') is not None:
            self.column_name = m.get('ColumnName')

        if m.get('ColumnNameCn') is not None:
            self.column_name_cn = m.get('ColumnNameCn')

        if m.get('ColumnType') is not None:
            self.column_type = m.get('ColumnType')

        if m.get('Comment') is not None:
            self.comment = m.get('Comment')

        if m.get('IsPartitionCol') is not None:
            self.is_partition_col = m.get('IsPartitionCol')

        if m.get('Length') is not None:
            self.length = m.get('Length')

        if m.get('SeqNumber') is not None:
            self.seq_number = m.get('SeqNumber')

        return self

