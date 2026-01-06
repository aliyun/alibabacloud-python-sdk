# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_adb20211201 import models as main_models
from darabonba.model import DaraModel

class DescribeAdbMySqlTableMetaResponseBody(DaraModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        table_meta: main_models.DescribeAdbMySqlTableMetaResponseBodyTableMeta = None,
    ):
        # The returned message. Valid values:
        # 
        # *   If the request was successful, a success message is returned.****
        # *   If the request failed, an error message is returned.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.success = success
        # The queried table metadata.
        self.table_meta = table_meta

    def validate(self):
        if self.table_meta:
            self.table_meta.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.table_meta is not None:
            result['TableMeta'] = self.table_meta.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TableMeta') is not None:
            temp_model = main_models.DescribeAdbMySqlTableMetaResponseBodyTableMeta()
            self.table_meta = temp_model.from_map(m.get('TableMeta'))

        return self

class DescribeAdbMySqlTableMetaResponseBodyTableMeta(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        distribute_column: str = None,
        distribute_type: str = None,
        is_all_index: bool = None,
        is_dict_encode: bool = None,
        is_full_text_dict: bool = None,
        is_hidden: bool = None,
        partition_column: str = None,
        partition_type: str = None,
        primary_key_column: str = None,
        table_engine: str = None,
        table_name: str = None,
        table_schema: str = None,
        table_type: str = None,
        update_time: str = None,
    ):
        # The time when the table was created.
        self.create_time = create_time
        # The distribution key column.
        self.distribute_column = distribute_column
        # The distribution type.
        self.distribute_type = distribute_type
        # Indicates whether full-column indexes are used.
        self.is_all_index = is_all_index
        # Indicates whether dictionary encoding is used.
        self.is_dict_encode = is_dict_encode
        # Indicates whether full-text indexes are used.
        self.is_full_text_dict = is_full_text_dict
        # Indicates whether pages are hidden.
        # 
        # *   **false**
        # *   **true**
        self.is_hidden = is_hidden
        # The partition key column.
        self.partition_column = partition_column
        # The type of the partition.
        self.partition_type = partition_type
        # The primary key column.
        self.primary_key_column = primary_key_column
        # The table engine.
        self.table_engine = table_engine
        # The name of the table.
        # 
        # **
        # 
        # ****
        self.table_name = table_name
        # The database to which the table belongs.
        self.table_schema = table_schema
        # The type of the table.
        self.table_type = table_type
        # The time when the table was updated.
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.distribute_column is not None:
            result['DistributeColumn'] = self.distribute_column

        if self.distribute_type is not None:
            result['DistributeType'] = self.distribute_type

        if self.is_all_index is not None:
            result['IsAllIndex'] = self.is_all_index

        if self.is_dict_encode is not None:
            result['IsDictEncode'] = self.is_dict_encode

        if self.is_full_text_dict is not None:
            result['IsFullTextDict'] = self.is_full_text_dict

        if self.is_hidden is not None:
            result['IsHidden'] = self.is_hidden

        if self.partition_column is not None:
            result['PartitionColumn'] = self.partition_column

        if self.partition_type is not None:
            result['PartitionType'] = self.partition_type

        if self.primary_key_column is not None:
            result['PrimaryKeyColumn'] = self.primary_key_column

        if self.table_engine is not None:
            result['TableEngine'] = self.table_engine

        if self.table_name is not None:
            result['TableName'] = self.table_name

        if self.table_schema is not None:
            result['TableSchema'] = self.table_schema

        if self.table_type is not None:
            result['TableType'] = self.table_type

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('DistributeColumn') is not None:
            self.distribute_column = m.get('DistributeColumn')

        if m.get('DistributeType') is not None:
            self.distribute_type = m.get('DistributeType')

        if m.get('IsAllIndex') is not None:
            self.is_all_index = m.get('IsAllIndex')

        if m.get('IsDictEncode') is not None:
            self.is_dict_encode = m.get('IsDictEncode')

        if m.get('IsFullTextDict') is not None:
            self.is_full_text_dict = m.get('IsFullTextDict')

        if m.get('IsHidden') is not None:
            self.is_hidden = m.get('IsHidden')

        if m.get('PartitionColumn') is not None:
            self.partition_column = m.get('PartitionColumn')

        if m.get('PartitionType') is not None:
            self.partition_type = m.get('PartitionType')

        if m.get('PrimaryKeyColumn') is not None:
            self.primary_key_column = m.get('PrimaryKeyColumn')

        if m.get('TableEngine') is not None:
            self.table_engine = m.get('TableEngine')

        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')

        if m.get('TableSchema') is not None:
            self.table_schema = m.get('TableSchema')

        if m.get('TableType') is not None:
            self.table_type = m.get('TableType')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

