# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_maxcompute20220104 import models as main_models
from darabonba.model import DaraModel

class ListMmsTablesResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.ListMmsTablesResponseBodyData = None,
        request_id: str = None,
    ):
        # The returned data.
        self.data = data
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['data'] = self.data.to_map()

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = main_models.ListMmsTablesResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class ListMmsTablesResponseBodyData(DaraModel):
    def __init__(
        self,
        object_list: List[main_models.ListMmsTablesResponseBodyDataObjectList] = None,
        page_num: int = None,
        page_size: int = None,
        total: int = None,
    ):
        # The list of tables.
        self.object_list = object_list
        # The page number.
        self.page_num = page_num
        # The number of entries per page.
        self.page_size = page_size
        # The total number of records.
        self.total = total

    def validate(self):
        if self.object_list:
            for v1 in self.object_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['objectList'] = []
        if self.object_list is not None:
            for k1 in self.object_list:
                result['objectList'].append(k1.to_map() if k1 else None)

        if self.page_num is not None:
            result['pageNum'] = self.page_num

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.total is not None:
            result['total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.object_list = []
        if m.get('objectList') is not None:
            for k1 in m.get('objectList'):
                temp_model = main_models.ListMmsTablesResponseBodyDataObjectList()
                self.object_list.append(temp_model.from_map(k1))

        if m.get('pageNum') is not None:
            self.page_num = m.get('pageNum')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('total') is not None:
            self.total = m.get('total')

        return self

class ListMmsTablesResponseBodyDataObjectList(DaraModel):
    def __init__(
        self,
        db_id: int = None,
        db_name: str = None,
        dst_name: str = None,
        dst_project_name: str = None,
        dst_schema_name: str = None,
        extra: str = None,
        has_partitions: bool = None,
        id: int = None,
        input_format: str = None,
        last_ddl_time: str = None,
        location: str = None,
        name: str = None,
        num_rows: int = None,
        output_format: str = None,
        owner: str = None,
        partitions: int = None,
        partitions_doing: int = None,
        partitions_done: int = None,
        partitions_failed: int = None,
        schema: main_models.ListMmsTablesResponseBodyDataObjectListSchema = None,
        serde: str = None,
        size: int = None,
        source_id: int = None,
        source_name: str = None,
        status: str = None,
        type: str = None,
        updated: bool = None,
    ):
        # The database ID.
        self.db_id = db_id
        # The database name.
        self.db_name = db_name
        # The name of the destination MaxCompute table. By default, this name is the same as the source table name.
        self.dst_name = dst_name
        # The name of the destination MaxCompute project.
        self.dst_project_name = dst_project_name
        # The name of the destination MaxCompute schema. This parameter is null if the destination MaxCompute project does not have a schema layer.
        self.dst_schema_name = dst_schema_name
        # Other information stored in JSON format.
        self.extra = extra
        # Indicates whether the table is a partitioned table.
        self.has_partitions = has_partitions
        # The table ID.
        self.id = id
        # The input format.
        self.input_format = input_format
        # The last DDL time.
        self.last_ddl_time = last_ddl_time
        # The storage location of the table.
        self.location = location
        # The table name.
        self.name = name
        # The number of rows.
        self.num_rows = num_rows
        # The output format.
        self.output_format = output_format
        # The owner of the table.
        self.owner = owner
        # The number of partitions.
        self.partitions = partitions
        # The number of partitions that are being migrated.
        self.partitions_doing = partitions_doing
        # The number of partitions that are migrated.
        self.partitions_done = partitions_done
        # The number of partitions that failed to be migrated.
        self.partitions_failed = partitions_failed
        # The table schema.
        self.schema = schema
        # The serializer/deserializer (SerDe).
        self.serde = serde
        # The data size in bytes.
        self.size = size
        # The ID of the data source.
        self.source_id = source_id
        # The name of the data source.
        self.source_name = source_name
        # The migration status.
        self.status = status
        # The table type.
        self.type = type
        # Indicates whether the metadata is updated.
        self.updated = updated

    def validate(self):
        if self.schema:
            self.schema.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.db_id is not None:
            result['dbId'] = self.db_id

        if self.db_name is not None:
            result['dbName'] = self.db_name

        if self.dst_name is not None:
            result['dstName'] = self.dst_name

        if self.dst_project_name is not None:
            result['dstProjectName'] = self.dst_project_name

        if self.dst_schema_name is not None:
            result['dstSchemaName'] = self.dst_schema_name

        if self.extra is not None:
            result['extra'] = self.extra

        if self.has_partitions is not None:
            result['hasPartitions'] = self.has_partitions

        if self.id is not None:
            result['id'] = self.id

        if self.input_format is not None:
            result['inputFormat'] = self.input_format

        if self.last_ddl_time is not None:
            result['lastDdlTime'] = self.last_ddl_time

        if self.location is not None:
            result['location'] = self.location

        if self.name is not None:
            result['name'] = self.name

        if self.num_rows is not None:
            result['numRows'] = self.num_rows

        if self.output_format is not None:
            result['outputFormat'] = self.output_format

        if self.owner is not None:
            result['owner'] = self.owner

        if self.partitions is not None:
            result['partitions'] = self.partitions

        if self.partitions_doing is not None:
            result['partitionsDoing'] = self.partitions_doing

        if self.partitions_done is not None:
            result['partitionsDone'] = self.partitions_done

        if self.partitions_failed is not None:
            result['partitionsFailed'] = self.partitions_failed

        if self.schema is not None:
            result['schema'] = self.schema.to_map()

        if self.serde is not None:
            result['serde'] = self.serde

        if self.size is not None:
            result['size'] = self.size

        if self.source_id is not None:
            result['sourceId'] = self.source_id

        if self.source_name is not None:
            result['sourceName'] = self.source_name

        if self.status is not None:
            result['status'] = self.status

        if self.type is not None:
            result['type'] = self.type

        if self.updated is not None:
            result['updated'] = self.updated

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dbId') is not None:
            self.db_id = m.get('dbId')

        if m.get('dbName') is not None:
            self.db_name = m.get('dbName')

        if m.get('dstName') is not None:
            self.dst_name = m.get('dstName')

        if m.get('dstProjectName') is not None:
            self.dst_project_name = m.get('dstProjectName')

        if m.get('dstSchemaName') is not None:
            self.dst_schema_name = m.get('dstSchemaName')

        if m.get('extra') is not None:
            self.extra = m.get('extra')

        if m.get('hasPartitions') is not None:
            self.has_partitions = m.get('hasPartitions')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('inputFormat') is not None:
            self.input_format = m.get('inputFormat')

        if m.get('lastDdlTime') is not None:
            self.last_ddl_time = m.get('lastDdlTime')

        if m.get('location') is not None:
            self.location = m.get('location')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('numRows') is not None:
            self.num_rows = m.get('numRows')

        if m.get('outputFormat') is not None:
            self.output_format = m.get('outputFormat')

        if m.get('owner') is not None:
            self.owner = m.get('owner')

        if m.get('partitions') is not None:
            self.partitions = m.get('partitions')

        if m.get('partitionsDoing') is not None:
            self.partitions_doing = m.get('partitionsDoing')

        if m.get('partitionsDone') is not None:
            self.partitions_done = m.get('partitionsDone')

        if m.get('partitionsFailed') is not None:
            self.partitions_failed = m.get('partitionsFailed')

        if m.get('schema') is not None:
            temp_model = main_models.ListMmsTablesResponseBodyDataObjectListSchema()
            self.schema = temp_model.from_map(m.get('schema'))

        if m.get('serde') is not None:
            self.serde = m.get('serde')

        if m.get('size') is not None:
            self.size = m.get('size')

        if m.get('sourceId') is not None:
            self.source_id = m.get('sourceId')

        if m.get('sourceName') is not None:
            self.source_name = m.get('sourceName')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('updated') is not None:
            self.updated = m.get('updated')

        return self

class ListMmsTablesResponseBodyDataObjectListSchema(DaraModel):
    def __init__(
        self,
        columns: List[main_models.ListMmsTablesResponseBodyDataObjectListSchemaColumns] = None,
        comment: str = None,
        name: str = None,
        partitions: List[main_models.ListMmsTablesResponseBodyDataObjectListSchemaPartitions] = None,
    ):
        # All non-partition key columns of the table.
        self.columns = columns
        # The comment on the table.
        self.comment = comment
        # The table name.
        self.name = name
        # All partition key columns.
        self.partitions = partitions

    def validate(self):
        if self.columns:
            for v1 in self.columns:
                 if v1:
                    v1.validate()
        if self.partitions:
            for v1 in self.partitions:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['columns'] = []
        if self.columns is not None:
            for k1 in self.columns:
                result['columns'].append(k1.to_map() if k1 else None)

        if self.comment is not None:
            result['comment'] = self.comment

        if self.name is not None:
            result['name'] = self.name

        result['partitions'] = []
        if self.partitions is not None:
            for k1 in self.partitions:
                result['partitions'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.columns = []
        if m.get('columns') is not None:
            for k1 in m.get('columns'):
                temp_model = main_models.ListMmsTablesResponseBodyDataObjectListSchemaColumns()
                self.columns.append(temp_model.from_map(k1))

        if m.get('comment') is not None:
            self.comment = m.get('comment')

        if m.get('name') is not None:
            self.name = m.get('name')

        self.partitions = []
        if m.get('partitions') is not None:
            for k1 in m.get('partitions'):
                temp_model = main_models.ListMmsTablesResponseBodyDataObjectListSchemaPartitions()
                self.partitions.append(temp_model.from_map(k1))

        return self

class ListMmsTablesResponseBodyDataObjectListSchemaPartitions(DaraModel):
    def __init__(
        self,
        comment: str = None,
        default_value: str = None,
        name: str = None,
        nullable: bool = None,
        type: str = None,
    ):
        # The comment on the column.
        self.comment = comment
        # The default value of the column.
        self.default_value = default_value
        # The column name.
        self.name = name
        # Indicates whether the column can be null.
        self.nullable = nullable
        # The column type.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.comment is not None:
            result['comment'] = self.comment

        if self.default_value is not None:
            result['defaultValue'] = self.default_value

        if self.name is not None:
            result['name'] = self.name

        if self.nullable is not None:
            result['nullable'] = self.nullable

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('comment') is not None:
            self.comment = m.get('comment')

        if m.get('defaultValue') is not None:
            self.default_value = m.get('defaultValue')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('nullable') is not None:
            self.nullable = m.get('nullable')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

class ListMmsTablesResponseBodyDataObjectListSchemaColumns(DaraModel):
    def __init__(
        self,
        comment: str = None,
        default_value: str = None,
        name: str = None,
        nullable: bool = None,
        type: str = None,
    ):
        # The comment on the column.
        self.comment = comment
        # The default value of the column.
        self.default_value = default_value
        # The column name.
        self.name = name
        # Indicates whether the column can be null.
        self.nullable = nullable
        # The column type.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.comment is not None:
            result['comment'] = self.comment

        if self.default_value is not None:
            result['defaultValue'] = self.default_value

        if self.name is not None:
            result['name'] = self.name

        if self.nullable is not None:
            result['nullable'] = self.nullable

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('comment') is not None:
            self.comment = m.get('comment')

        if m.get('defaultValue') is not None:
            self.default_value = m.get('defaultValue')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('nullable') is not None:
            self.nullable = m.get('nullable')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

