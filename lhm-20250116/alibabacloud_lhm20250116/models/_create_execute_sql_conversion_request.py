# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_lhm20250116 import models as main_models
from darabonba.model import DaraModel

class CreateExecuteSqlConversionRequest(DaraModel):
    def __init__(
        self,
        source_dialect: str = None,
        source_sql_script: List[main_models.CreateExecuteSqlConversionRequestSourceSqlScript] = None,
        target_dialect: str = None,
        task_description: str = None,
        task_name: str = None,
        type: int = None,
    ):
        # The source dialect.
        self.source_dialect = source_dialect
        # The list of source SQL scripts.
        self.source_sql_script = source_sql_script
        # The target dialect.
        self.target_dialect = target_dialect
        # The task description.
        self.task_description = task_description
        # The task name.
        # 
        # This parameter is required.
        self.task_name = task_name
        # The script type. Valid values: 0 (DDL) and 1 (DQL).
        self.type = type

    def validate(self):
        if self.source_sql_script:
            for v1 in self.source_sql_script:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.source_dialect is not None:
            result['sourceDialect'] = self.source_dialect

        result['sourceSqlScript'] = []
        if self.source_sql_script is not None:
            for k1 in self.source_sql_script:
                result['sourceSqlScript'].append(k1.to_map() if k1 else None)

        if self.target_dialect is not None:
            result['targetDialect'] = self.target_dialect

        if self.task_description is not None:
            result['taskDescription'] = self.task_description

        if self.task_name is not None:
            result['taskName'] = self.task_name

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('sourceDialect') is not None:
            self.source_dialect = m.get('sourceDialect')

        self.source_sql_script = []
        if m.get('sourceSqlScript') is not None:
            for k1 in m.get('sourceSqlScript'):
                temp_model = main_models.CreateExecuteSqlConversionRequestSourceSqlScript()
                self.source_sql_script.append(temp_model.from_map(k1))

        if m.get('targetDialect') is not None:
            self.target_dialect = m.get('targetDialect')

        if m.get('taskDescription') is not None:
            self.task_description = m.get('taskDescription')

        if m.get('taskName') is not None:
            self.task_name = m.get('taskName')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

class CreateExecuteSqlConversionRequestSourceSqlScript(DaraModel):
    def __init__(
        self,
        error_message: str = None,
        finish_time: str = None,
        script_id: int = None,
        script_name: str = None,
        script_transform_status: str = None,
        sql_result_content: str = None,
        sql_source_content: str = None,
        table_mapping_list: List[main_models.CreateExecuteSqlConversionRequestSourceSqlScriptTableMappingList] = None,
    ):
        # The error reason.
        self.error_message = error_message
        # The time when the conversion is completed.
        self.finish_time = finish_time
        # The script ID.
        self.script_id = script_id
        # The script name.
        self.script_name = script_name
        # The script conversion status. In conversion job scenarios, valid values: pass (conversion succeeded), turning (conversion in progress), fail (conversion failed). In some scenarios, the following values are used: success (succeeded), failed (failed), skipped (skipped).
        self.script_transform_status = script_transform_status
        # The converted script content.
        self.sql_result_content = sql_result_content
        # The original script content.
        self.sql_source_content = sql_source_content
        # The table name mappings for conversion.
        self.table_mapping_list = table_mapping_list

    def validate(self):
        if self.table_mapping_list:
            for v1 in self.table_mapping_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_message is not None:
            result['errorMessage'] = self.error_message

        if self.finish_time is not None:
            result['finishTime'] = self.finish_time

        if self.script_id is not None:
            result['scriptId'] = self.script_id

        if self.script_name is not None:
            result['scriptName'] = self.script_name

        if self.script_transform_status is not None:
            result['scriptTransformStatus'] = self.script_transform_status

        if self.sql_result_content is not None:
            result['sqlResultContent'] = self.sql_result_content

        if self.sql_source_content is not None:
            result['sqlSourceContent'] = self.sql_source_content

        result['tableMappingList'] = []
        if self.table_mapping_list is not None:
            for k1 in self.table_mapping_list:
                result['tableMappingList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')

        if m.get('finishTime') is not None:
            self.finish_time = m.get('finishTime')

        if m.get('scriptId') is not None:
            self.script_id = m.get('scriptId')

        if m.get('scriptName') is not None:
            self.script_name = m.get('scriptName')

        if m.get('scriptTransformStatus') is not None:
            self.script_transform_status = m.get('scriptTransformStatus')

        if m.get('sqlResultContent') is not None:
            self.sql_result_content = m.get('sqlResultContent')

        if m.get('sqlSourceContent') is not None:
            self.sql_source_content = m.get('sqlSourceContent')

        self.table_mapping_list = []
        if m.get('tableMappingList') is not None:
            for k1 in m.get('tableMappingList'):
                temp_model = main_models.CreateExecuteSqlConversionRequestSourceSqlScriptTableMappingList()
                self.table_mapping_list.append(temp_model.from_map(k1))

        return self

class CreateExecuteSqlConversionRequestSourceSqlScriptTableMappingList(DaraModel):
    def __init__(
        self,
        id: int = None,
        source_schema: str = None,
        source_table_name: str = None,
        target_table_name: str = None,
        target_type: str = None,
        task_id: int = None,
        tenant_id: str = None,
        uid: str = None,
    ):
        # The primary key.
        self.id = id
        # The source type. Valid values: DB and Schema.
        self.source_schema = source_schema
        # The source table name.
        self.source_table_name = source_table_name
        # The target table name.
        self.target_table_name = target_table_name
        # The target type. Valid values: DB and Schema.
        self.target_type = target_type
        # The SQL conversion task ID.
        self.task_id = task_id
        # The tenant ID.
        self.tenant_id = tenant_id
        # The user ID.
        self.uid = uid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['id'] = self.id

        if self.source_schema is not None:
            result['sourceSchema'] = self.source_schema

        if self.source_table_name is not None:
            result['sourceTableName'] = self.source_table_name

        if self.target_table_name is not None:
            result['targetTableName'] = self.target_table_name

        if self.target_type is not None:
            result['targetType'] = self.target_type

        if self.task_id is not None:
            result['taskId'] = self.task_id

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        if self.uid is not None:
            result['uid'] = self.uid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('sourceSchema') is not None:
            self.source_schema = m.get('sourceSchema')

        if m.get('sourceTableName') is not None:
            self.source_table_name = m.get('sourceTableName')

        if m.get('targetTableName') is not None:
            self.target_table_name = m.get('targetTableName')

        if m.get('targetType') is not None:
            self.target_type = m.get('targetType')

        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        if m.get('uid') is not None:
            self.uid = m.get('uid')

        return self

