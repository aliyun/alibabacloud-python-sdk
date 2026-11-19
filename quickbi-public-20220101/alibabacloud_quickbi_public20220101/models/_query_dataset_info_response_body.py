# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_quickbi_public20220101 import models as main_models
from darabonba.model import DaraModel

class QueryDatasetInfoResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result: main_models.QueryDatasetInfoResponseBodyResult = None,
        success: bool = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The dataset information.
        self.result = result
        # Specifies whether the request is successful. Valid values:
        # 
        # - true: The request is successful.
        # - false: The request fails.
        self.success = success

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.result is not None:
            result['Result'] = self.result.to_map()

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Result') is not None:
            temp_model = main_models.QueryDatasetInfoResponseBodyResult()
            self.result = temp_model.from_map(m.get('Result'))

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class QueryDatasetInfoResponseBodyResult(DaraModel):
    def __init__(
        self,
        cube_table_list: List[main_models.QueryDatasetInfoResponseBodyResultCubeTableList] = None,
        custimze_sql: bool = None,
        dataset_id: str = None,
        dataset_name: str = None,
        dimension_list: List[main_models.QueryDatasetInfoResponseBodyResultDimensionList] = None,
        directory: main_models.QueryDatasetInfoResponseBodyResultDirectory = None,
        ds_id: str = None,
        ds_name: str = None,
        ds_type: str = None,
        gmt_create: str = None,
        gmt_modify: str = None,
        measure_list: List[main_models.QueryDatasetInfoResponseBodyResultMeasureList] = None,
        open_offline_acceleration: bool = None,
        owner_id: str = None,
        owner_name: str = None,
        row_level: bool = None,
        workspace_id: str = None,
        workspace_name: str = None,
    ):
        # The list of tables used by the dataset.
        self.cube_table_list = cube_table_list
        # Specifies whether custom SQL is used. Valid values:
        # 
        # - true: Yes.
        # - false: No.
        self.custimze_sql = custimze_sql
        # The unique ID of the dataset.
        self.dataset_id = dataset_id
        # The dataset name.
        self.dataset_name = dataset_name
        # The list of all dimensions in the dataset.
        self.dimension_list = dimension_list
        # The folder information of the dataset.
        self.directory = directory
        # The unique ID of the data source.
        self.ds_id = ds_id
        # The data source name.
        self.ds_name = ds_name
        # The data source type. Valid values:
        # 
        # - mysql
        # - odps
        # - oracle
        # - Other data source types supported by Quick BI.
        self.ds_type = ds_type
        # The time when the dataset was created.
        self.gmt_create = gmt_create
        # The time when the dataset was last modified.
        self.gmt_modify = gmt_modify
        # The list of all measures in the dataset.
        self.measure_list = measure_list
        # Specifies whether extract acceleration is enabled. Valid values:
        # 
        # - true: Enabled.
        # - false: Disabled.
        self.open_offline_acceleration = open_offline_acceleration
        # The user ID of the dataset owner in Quick BI.
        self.owner_id = owner_id
        # The name of the dataset owner.
        self.owner_name = owner_name
        # Specifies whether row-level permissions are enabled. Valid values:
        # 
        # - true: Enabled.
        # - false: Disabled.
        self.row_level = row_level
        # The unique ID of the workspace to which the dataset belongs.
        self.workspace_id = workspace_id
        # The name of the workspace to which the dataset belongs.
        self.workspace_name = workspace_name

    def validate(self):
        if self.cube_table_list:
            for v1 in self.cube_table_list:
                 if v1:
                    v1.validate()
        if self.dimension_list:
            for v1 in self.dimension_list:
                 if v1:
                    v1.validate()
        if self.directory:
            self.directory.validate()
        if self.measure_list:
            for v1 in self.measure_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['CubeTableList'] = []
        if self.cube_table_list is not None:
            for k1 in self.cube_table_list:
                result['CubeTableList'].append(k1.to_map() if k1 else None)

        if self.custimze_sql is not None:
            result['CustimzeSql'] = self.custimze_sql

        if self.dataset_id is not None:
            result['DatasetId'] = self.dataset_id

        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name

        result['DimensionList'] = []
        if self.dimension_list is not None:
            for k1 in self.dimension_list:
                result['DimensionList'].append(k1.to_map() if k1 else None)

        if self.directory is not None:
            result['Directory'] = self.directory.to_map()

        if self.ds_id is not None:
            result['DsId'] = self.ds_id

        if self.ds_name is not None:
            result['DsName'] = self.ds_name

        if self.ds_type is not None:
            result['DsType'] = self.ds_type

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_modify is not None:
            result['GmtModify'] = self.gmt_modify

        result['MeasureList'] = []
        if self.measure_list is not None:
            for k1 in self.measure_list:
                result['MeasureList'].append(k1.to_map() if k1 else None)

        if self.open_offline_acceleration is not None:
            result['OpenOfflineAcceleration'] = self.open_offline_acceleration

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.owner_name is not None:
            result['OwnerName'] = self.owner_name

        if self.row_level is not None:
            result['RowLevel'] = self.row_level

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        if self.workspace_name is not None:
            result['WorkspaceName'] = self.workspace_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.cube_table_list = []
        if m.get('CubeTableList') is not None:
            for k1 in m.get('CubeTableList'):
                temp_model = main_models.QueryDatasetInfoResponseBodyResultCubeTableList()
                self.cube_table_list.append(temp_model.from_map(k1))

        if m.get('CustimzeSql') is not None:
            self.custimze_sql = m.get('CustimzeSql')

        if m.get('DatasetId') is not None:
            self.dataset_id = m.get('DatasetId')

        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')

        self.dimension_list = []
        if m.get('DimensionList') is not None:
            for k1 in m.get('DimensionList'):
                temp_model = main_models.QueryDatasetInfoResponseBodyResultDimensionList()
                self.dimension_list.append(temp_model.from_map(k1))

        if m.get('Directory') is not None:
            temp_model = main_models.QueryDatasetInfoResponseBodyResultDirectory()
            self.directory = temp_model.from_map(m.get('Directory'))

        if m.get('DsId') is not None:
            self.ds_id = m.get('DsId')

        if m.get('DsName') is not None:
            self.ds_name = m.get('DsName')

        if m.get('DsType') is not None:
            self.ds_type = m.get('DsType')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtModify') is not None:
            self.gmt_modify = m.get('GmtModify')

        self.measure_list = []
        if m.get('MeasureList') is not None:
            for k1 in m.get('MeasureList'):
                temp_model = main_models.QueryDatasetInfoResponseBodyResultMeasureList()
                self.measure_list.append(temp_model.from_map(k1))

        if m.get('OpenOfflineAcceleration') is not None:
            self.open_offline_acceleration = m.get('OpenOfflineAcceleration')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('OwnerName') is not None:
            self.owner_name = m.get('OwnerName')

        if m.get('RowLevel') is not None:
            self.row_level = m.get('RowLevel')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        if m.get('WorkspaceName') is not None:
            self.workspace_name = m.get('WorkspaceName')

        return self

class QueryDatasetInfoResponseBodyResultMeasureList(DaraModel):
    def __init__(
        self,
        caption: str = None,
        data_type: str = None,
        expression: str = None,
        expression_v2: str = None,
        fact_column: str = None,
        field_description: str = None,
        measure_type: str = None,
        table_unique_id: str = None,
        uid: str = None,
    ):
        # The display name of the measure.
        self.caption = caption
        # The data type. Valid values:
        # 
        # - string: String.
        # - number: Number.
        # - datetime: Datetime.
        self.data_type = data_type
        # The expression for the calculated measure. This parameter is valid only for calculated measures.
        self.expression = expression
        # The flattened expression for the calculated measure.
        self.expression_v2 = expression_v2
        # The actual physical field.
        self.fact_column = fact_column
        # The field description.
        self.field_description = field_description
        # The metric type. Valid values:
        # 
        # - standard_measure: Standard measure.
        # - calculate_measure: Calculated measure.
        self.measure_type = measure_type
        # The unique ID of the table to which the dimension belongs. This corresponds to the UniqueId in CubeTypeList.
        self.table_unique_id = table_unique_id
        # The unique ID of the measure.
        self.uid = uid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.caption is not None:
            result['Caption'] = self.caption

        if self.data_type is not None:
            result['DataType'] = self.data_type

        if self.expression is not None:
            result['Expression'] = self.expression

        if self.expression_v2 is not None:
            result['ExpressionV2'] = self.expression_v2

        if self.fact_column is not None:
            result['FactColumn'] = self.fact_column

        if self.field_description is not None:
            result['FieldDescription'] = self.field_description

        if self.measure_type is not None:
            result['MeasureType'] = self.measure_type

        if self.table_unique_id is not None:
            result['TableUniqueId'] = self.table_unique_id

        if self.uid is not None:
            result['Uid'] = self.uid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Caption') is not None:
            self.caption = m.get('Caption')

        if m.get('DataType') is not None:
            self.data_type = m.get('DataType')

        if m.get('Expression') is not None:
            self.expression = m.get('Expression')

        if m.get('ExpressionV2') is not None:
            self.expression_v2 = m.get('ExpressionV2')

        if m.get('FactColumn') is not None:
            self.fact_column = m.get('FactColumn')

        if m.get('FieldDescription') is not None:
            self.field_description = m.get('FieldDescription')

        if m.get('MeasureType') is not None:
            self.measure_type = m.get('MeasureType')

        if m.get('TableUniqueId') is not None:
            self.table_unique_id = m.get('TableUniqueId')

        if m.get('Uid') is not None:
            self.uid = m.get('Uid')

        return self

class QueryDatasetInfoResponseBodyResultDirectory(DaraModel):
    def __init__(
        self,
        id: str = None,
        name: str = None,
        path_id: str = None,
        path_name: str = None,
    ):
        # The folder ID.
        self.id = id
        # The folder name.
        self.name = name
        # The path of the folder ID, such as aa/bb/cc/dd.
        self.path_id = path_id
        # The path name of the folder ID, such as Level 1 folder/Level 2 folder.
        self.path_name = path_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        if self.path_id is not None:
            result['PathId'] = self.path_id

        if self.path_name is not None:
            result['PathName'] = self.path_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('PathId') is not None:
            self.path_id = m.get('PathId')

        if m.get('PathName') is not None:
            self.path_name = m.get('PathName')

        return self

class QueryDatasetInfoResponseBodyResultDimensionList(DaraModel):
    def __init__(
        self,
        caption: str = None,
        data_type: str = None,
        dimension_type: str = None,
        expression: str = None,
        expression_v2: str = None,
        fact_column: str = None,
        field_description: str = None,
        granularity: str = None,
        ref_uid: str = None,
        table_unique_id: str = None,
        uid: str = None,
    ):
        # The display name of the dimension.
        self.caption = caption
        # The data type. Valid values:
        # 
        # - string: String.
        # - number: Number.
        # - datetime: Datetime.
        self.data_type = data_type
        # The dimension type. Valid values:
        # 
        # - standard_dimension: Standard dimension.
        # - calculate_dimension: Calculated dimension.
        # - group_dimension: Grouped dimension.
        self.dimension_type = dimension_type
        # The expression for the calculated dimension. This parameter is valid only for calculated dimensions.
        self.expression = expression
        # The flattened expression for the calculated dimension.
        self.expression_v2 = expression_v2
        # The actual physical field.
        self.fact_column = fact_column
        # The field description.
        self.field_description = field_description
        # The granularity.
        self.granularity = granularity
        # The unique ID of the referenced field for a grouped measure. This parameter is not null only when the measure is a grouped measure.
        self.ref_uid = ref_uid
        # The unique ID of the table to which the dimension belongs. This corresponds to the UniqueId in CubeTypeList.
        self.table_unique_id = table_unique_id
        # The unique ID.
        self.uid = uid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.caption is not None:
            result['Caption'] = self.caption

        if self.data_type is not None:
            result['DataType'] = self.data_type

        if self.dimension_type is not None:
            result['DimensionType'] = self.dimension_type

        if self.expression is not None:
            result['Expression'] = self.expression

        if self.expression_v2 is not None:
            result['ExpressionV2'] = self.expression_v2

        if self.fact_column is not None:
            result['FactColumn'] = self.fact_column

        if self.field_description is not None:
            result['FieldDescription'] = self.field_description

        if self.granularity is not None:
            result['Granularity'] = self.granularity

        if self.ref_uid is not None:
            result['RefUid'] = self.ref_uid

        if self.table_unique_id is not None:
            result['TableUniqueId'] = self.table_unique_id

        if self.uid is not None:
            result['Uid'] = self.uid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Caption') is not None:
            self.caption = m.get('Caption')

        if m.get('DataType') is not None:
            self.data_type = m.get('DataType')

        if m.get('DimensionType') is not None:
            self.dimension_type = m.get('DimensionType')

        if m.get('Expression') is not None:
            self.expression = m.get('Expression')

        if m.get('ExpressionV2') is not None:
            self.expression_v2 = m.get('ExpressionV2')

        if m.get('FactColumn') is not None:
            self.fact_column = m.get('FactColumn')

        if m.get('FieldDescription') is not None:
            self.field_description = m.get('FieldDescription')

        if m.get('Granularity') is not None:
            self.granularity = m.get('Granularity')

        if m.get('RefUid') is not None:
            self.ref_uid = m.get('RefUid')

        if m.get('TableUniqueId') is not None:
            self.table_unique_id = m.get('TableUniqueId')

        if m.get('Uid') is not None:
            self.uid = m.get('Uid')

        return self

class QueryDatasetInfoResponseBodyResultCubeTableList(DaraModel):
    def __init__(
        self,
        caption: str = None,
        child_tables: List[main_models.QueryDatasetInfoResponseBodyResultCubeTableListChildTables] = None,
        customsql: bool = None,
        datasource_id: str = None,
        ds_type: str = None,
        fact_table: bool = None,
        sql: str = None,
        table_name: str = None,
        unique_id: str = None,
    ):
        # The display name of the table.
        self.caption = caption
        # The actual physical tables used by the merged table.
        self.child_tables = child_tables
        # Specifies whether the table is a custom SQL table. Valid values:
        # 
        # - true: The table is a custom SQL table.
        # - false: The table is not a custom SQL table.
        self.customsql = customsql
        # The data source ID.
        self.datasource_id = datasource_id
        # The data source type. Valid values:
        # 
        # - mysql
        # - odps
        # - oracle
        # - Other data source types supported by Quick BI.
        self.ds_type = ds_type
        # Specifies whether the table is a data source table. Valid values:
        # 
        # - true: The table is a data source table.
        # - false: The table is a custom table.
        self.fact_table = fact_table
        # The specific SQL statement when the table is a custom SQL table.
        self.sql = sql
        # The table name.
        self.table_name = table_name
        # The unique ID of the table.
        self.unique_id = unique_id

    def validate(self):
        if self.child_tables:
            for v1 in self.child_tables:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.caption is not None:
            result['Caption'] = self.caption

        result['ChildTables'] = []
        if self.child_tables is not None:
            for k1 in self.child_tables:
                result['ChildTables'].append(k1.to_map() if k1 else None)

        if self.customsql is not None:
            result['Customsql'] = self.customsql

        if self.datasource_id is not None:
            result['DatasourceId'] = self.datasource_id

        if self.ds_type is not None:
            result['DsType'] = self.ds_type

        if self.fact_table is not None:
            result['FactTable'] = self.fact_table

        if self.sql is not None:
            result['Sql'] = self.sql

        if self.table_name is not None:
            result['TableName'] = self.table_name

        if self.unique_id is not None:
            result['UniqueId'] = self.unique_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Caption') is not None:
            self.caption = m.get('Caption')

        self.child_tables = []
        if m.get('ChildTables') is not None:
            for k1 in m.get('ChildTables'):
                temp_model = main_models.QueryDatasetInfoResponseBodyResultCubeTableListChildTables()
                self.child_tables.append(temp_model.from_map(k1))

        if m.get('Customsql') is not None:
            self.customsql = m.get('Customsql')

        if m.get('DatasourceId') is not None:
            self.datasource_id = m.get('DatasourceId')

        if m.get('DsType') is not None:
            self.ds_type = m.get('DsType')

        if m.get('FactTable') is not None:
            self.fact_table = m.get('FactTable')

        if m.get('Sql') is not None:
            self.sql = m.get('Sql')

        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')

        if m.get('UniqueId') is not None:
            self.unique_id = m.get('UniqueId')

        return self

class QueryDatasetInfoResponseBodyResultCubeTableListChildTables(DaraModel):
    def __init__(
        self,
        caption: str = None,
        customsql: bool = None,
        datasource_id: str = None,
        ds_type: str = None,
        fact_table: bool = None,
        sql: str = None,
        table_name: str = None,
        unique_id: str = None,
    ):
        # The display name.
        self.caption = caption
        # Specifies whether the table is a custom dataset.
        self.customsql = customsql
        # The data source ID.
        self.datasource_id = datasource_id
        # The data source type.
        self.ds_type = ds_type
        # Specifies whether the table is the primary table.
        self.fact_table = fact_table
        # The SQL statement for the custom SQL dataset.
        self.sql = sql
        # The physical table name.
        self.table_name = table_name
        # The unique ID.
        self.unique_id = unique_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.caption is not None:
            result['Caption'] = self.caption

        if self.customsql is not None:
            result['Customsql'] = self.customsql

        if self.datasource_id is not None:
            result['DatasourceId'] = self.datasource_id

        if self.ds_type is not None:
            result['DsType'] = self.ds_type

        if self.fact_table is not None:
            result['FactTable'] = self.fact_table

        if self.sql is not None:
            result['Sql'] = self.sql

        if self.table_name is not None:
            result['TableName'] = self.table_name

        if self.unique_id is not None:
            result['UniqueId'] = self.unique_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Caption') is not None:
            self.caption = m.get('Caption')

        if m.get('Customsql') is not None:
            self.customsql = m.get('Customsql')

        if m.get('DatasourceId') is not None:
            self.datasource_id = m.get('DatasourceId')

        if m.get('DsType') is not None:
            self.ds_type = m.get('DsType')

        if m.get('FactTable') is not None:
            self.fact_table = m.get('FactTable')

        if m.get('Sql') is not None:
            self.sql = m.get('Sql')

        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')

        if m.get('UniqueId') is not None:
            self.unique_id = m.get('UniqueId')

        return self

