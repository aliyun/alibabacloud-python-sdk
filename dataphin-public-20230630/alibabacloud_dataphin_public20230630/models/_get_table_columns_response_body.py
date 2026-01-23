# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class GetTableColumnsResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        column_list: List[main_models.GetTableColumnsResponseBodyColumnList] = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.column_list = column_list
        self.http_status_code = http_status_code
        self.message = message
        # Id of the request
        self.request_id = request_id
        self.success = success

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
        if self.code is not None:
            result['Code'] = self.code

        result['ColumnList'] = []
        if self.column_list is not None:
            for k1 in self.column_list:
                result['ColumnList'].append(k1.to_map() if k1 else None)

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        self.column_list = []
        if m.get('ColumnList') is not None:
            for k1 in m.get('ColumnList'):
                temp_model = main_models.GetTableColumnsResponseBodyColumnList()
                self.column_list.append(temp_model.from_map(k1))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetTableColumnsResponseBodyColumnList(DaraModel):
    def __init__(
        self,
        classify_id: int = None,
        classify_name: str = None,
        comment: str = None,
        create_time: str = None,
        creator: str = None,
        data_source_id: int = None,
        data_source_type: str = None,
        data_type: str = None,
        default_value: str = None,
        display_name: str = None,
        env: str = None,
        guid: str = None,
        is_foreign_key: bool = None,
        is_partition_column: bool = None,
        is_primary_key: bool = None,
        last_modifier: str = None,
        level_abbreviation: str = None,
        modify_time: str = None,
        name: str = None,
        nullable: bool = None,
        seq_number: int = None,
        table_guid: str = None,
        table_name: str = None,
        visit_count_30d: int = None,
    ):
        self.classify_id = classify_id
        self.classify_name = classify_name
        self.comment = comment
        self.create_time = create_time
        self.creator = creator
        self.data_source_id = data_source_id
        self.data_source_type = data_source_type
        self.data_type = data_type
        self.default_value = default_value
        self.display_name = display_name
        self.env = env
        self.guid = guid
        self.is_foreign_key = is_foreign_key
        self.is_partition_column = is_partition_column
        self.is_primary_key = is_primary_key
        self.last_modifier = last_modifier
        self.level_abbreviation = level_abbreviation
        self.modify_time = modify_time
        self.name = name
        self.nullable = nullable
        self.seq_number = seq_number
        self.table_guid = table_guid
        self.table_name = table_name
        self.visit_count_30d = visit_count_30d

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.classify_id is not None:
            result['ClassifyId'] = self.classify_id

        if self.classify_name is not None:
            result['ClassifyName'] = self.classify_name

        if self.comment is not None:
            result['Comment'] = self.comment

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.creator is not None:
            result['Creator'] = self.creator

        if self.data_source_id is not None:
            result['DataSourceId'] = self.data_source_id

        if self.data_source_type is not None:
            result['DataSourceType'] = self.data_source_type

        if self.data_type is not None:
            result['DataType'] = self.data_type

        if self.default_value is not None:
            result['DefaultValue'] = self.default_value

        if self.display_name is not None:
            result['DisplayName'] = self.display_name

        if self.env is not None:
            result['Env'] = self.env

        if self.guid is not None:
            result['Guid'] = self.guid

        if self.is_foreign_key is not None:
            result['IsForeignKey'] = self.is_foreign_key

        if self.is_partition_column is not None:
            result['IsPartitionColumn'] = self.is_partition_column

        if self.is_primary_key is not None:
            result['IsPrimaryKey'] = self.is_primary_key

        if self.last_modifier is not None:
            result['LastModifier'] = self.last_modifier

        if self.level_abbreviation is not None:
            result['LevelAbbreviation'] = self.level_abbreviation

        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time

        if self.name is not None:
            result['Name'] = self.name

        if self.nullable is not None:
            result['Nullable'] = self.nullable

        if self.seq_number is not None:
            result['SeqNumber'] = self.seq_number

        if self.table_guid is not None:
            result['TableGuid'] = self.table_guid

        if self.table_name is not None:
            result['TableName'] = self.table_name

        if self.visit_count_30d is not None:
            result['VisitCount30d'] = self.visit_count_30d

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClassifyId') is not None:
            self.classify_id = m.get('ClassifyId')

        if m.get('ClassifyName') is not None:
            self.classify_name = m.get('ClassifyName')

        if m.get('Comment') is not None:
            self.comment = m.get('Comment')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Creator') is not None:
            self.creator = m.get('Creator')

        if m.get('DataSourceId') is not None:
            self.data_source_id = m.get('DataSourceId')

        if m.get('DataSourceType') is not None:
            self.data_source_type = m.get('DataSourceType')

        if m.get('DataType') is not None:
            self.data_type = m.get('DataType')

        if m.get('DefaultValue') is not None:
            self.default_value = m.get('DefaultValue')

        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        if m.get('Env') is not None:
            self.env = m.get('Env')

        if m.get('Guid') is not None:
            self.guid = m.get('Guid')

        if m.get('IsForeignKey') is not None:
            self.is_foreign_key = m.get('IsForeignKey')

        if m.get('IsPartitionColumn') is not None:
            self.is_partition_column = m.get('IsPartitionColumn')

        if m.get('IsPrimaryKey') is not None:
            self.is_primary_key = m.get('IsPrimaryKey')

        if m.get('LastModifier') is not None:
            self.last_modifier = m.get('LastModifier')

        if m.get('LevelAbbreviation') is not None:
            self.level_abbreviation = m.get('LevelAbbreviation')

        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Nullable') is not None:
            self.nullable = m.get('Nullable')

        if m.get('SeqNumber') is not None:
            self.seq_number = m.get('SeqNumber')

        if m.get('TableGuid') is not None:
            self.table_guid = m.get('TableGuid')

        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')

        if m.get('VisitCount30d') is not None:
            self.visit_count_30d = m.get('VisitCount30d')

        return self

