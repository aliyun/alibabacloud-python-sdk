# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class FieldSchemaModel(DaraModel):
    def __init__(
        self,
        auto_increment: bool = None,
        column_raw_name: str = None,
        comment: str = None,
        compress_float_use_short: bool = None,
        compression: str = None,
        create_time: str = None,
        data_type: str = None,
        database_name: str = None,
        default_value: str = None,
        delimiter: str = None,
        encode: str = None,
        is_partition_key: bool = None,
        mapped_name: str = None,
        name: str = None,
        nullable: bool = None,
        on_update: str = None,
        ordinal_position: int = None,
        physical_column_name: str = None,
        pk_position: int = None,
        precision: int = None,
        primarykey: bool = None,
        scale: int = None,
        table_name: str = None,
        tokenizer: str = None,
        type: str = None,
        update_time: str = None,
        value_type: str = None,
    ):
        self.auto_increment = auto_increment
        self.column_raw_name = column_raw_name
        self.comment = comment
        self.compress_float_use_short = compress_float_use_short
        self.compression = compression
        self.create_time = create_time
        self.data_type = data_type
        self.database_name = database_name
        self.default_value = default_value
        self.delimiter = delimiter
        self.encode = encode
        self.is_partition_key = is_partition_key
        self.mapped_name = mapped_name
        self.name = name
        self.nullable = nullable
        self.on_update = on_update
        self.ordinal_position = ordinal_position
        self.physical_column_name = physical_column_name
        self.pk_position = pk_position
        self.precision = precision
        self.primarykey = primarykey
        self.scale = scale
        self.table_name = table_name
        self.tokenizer = tokenizer
        self.type = type
        self.update_time = update_time
        self.value_type = value_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_increment is not None:
            result['AutoIncrement'] = self.auto_increment

        if self.column_raw_name is not None:
            result['ColumnRawName'] = self.column_raw_name

        if self.comment is not None:
            result['Comment'] = self.comment

        if self.compress_float_use_short is not None:
            result['CompressFloatUseShort'] = self.compress_float_use_short

        if self.compression is not None:
            result['Compression'] = self.compression

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.data_type is not None:
            result['DataType'] = self.data_type

        if self.database_name is not None:
            result['DatabaseName'] = self.database_name

        if self.default_value is not None:
            result['DefaultValue'] = self.default_value

        if self.delimiter is not None:
            result['Delimiter'] = self.delimiter

        if self.encode is not None:
            result['Encode'] = self.encode

        if self.is_partition_key is not None:
            result['IsPartitionKey'] = self.is_partition_key

        if self.mapped_name is not None:
            result['MappedName'] = self.mapped_name

        if self.name is not None:
            result['Name'] = self.name

        if self.nullable is not None:
            result['Nullable'] = self.nullable

        if self.on_update is not None:
            result['OnUpdate'] = self.on_update

        if self.ordinal_position is not None:
            result['OrdinalPosition'] = self.ordinal_position

        if self.physical_column_name is not None:
            result['PhysicalColumnName'] = self.physical_column_name

        if self.pk_position is not None:
            result['PkPosition'] = self.pk_position

        if self.precision is not None:
            result['Precision'] = self.precision

        if self.primarykey is not None:
            result['Primarykey'] = self.primarykey

        if self.scale is not None:
            result['Scale'] = self.scale

        if self.table_name is not None:
            result['TableName'] = self.table_name

        if self.tokenizer is not None:
            result['Tokenizer'] = self.tokenizer

        if self.type is not None:
            result['Type'] = self.type

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        if self.value_type is not None:
            result['ValueType'] = self.value_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoIncrement') is not None:
            self.auto_increment = m.get('AutoIncrement')

        if m.get('ColumnRawName') is not None:
            self.column_raw_name = m.get('ColumnRawName')

        if m.get('Comment') is not None:
            self.comment = m.get('Comment')

        if m.get('CompressFloatUseShort') is not None:
            self.compress_float_use_short = m.get('CompressFloatUseShort')

        if m.get('Compression') is not None:
            self.compression = m.get('Compression')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('DataType') is not None:
            self.data_type = m.get('DataType')

        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')

        if m.get('DefaultValue') is not None:
            self.default_value = m.get('DefaultValue')

        if m.get('Delimiter') is not None:
            self.delimiter = m.get('Delimiter')

        if m.get('Encode') is not None:
            self.encode = m.get('Encode')

        if m.get('IsPartitionKey') is not None:
            self.is_partition_key = m.get('IsPartitionKey')

        if m.get('MappedName') is not None:
            self.mapped_name = m.get('MappedName')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Nullable') is not None:
            self.nullable = m.get('Nullable')

        if m.get('OnUpdate') is not None:
            self.on_update = m.get('OnUpdate')

        if m.get('OrdinalPosition') is not None:
            self.ordinal_position = m.get('OrdinalPosition')

        if m.get('PhysicalColumnName') is not None:
            self.physical_column_name = m.get('PhysicalColumnName')

        if m.get('PkPosition') is not None:
            self.pk_position = m.get('PkPosition')

        if m.get('Precision') is not None:
            self.precision = m.get('Precision')

        if m.get('Primarykey') is not None:
            self.primarykey = m.get('Primarykey')

        if m.get('Scale') is not None:
            self.scale = m.get('Scale')

        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')

        if m.get('Tokenizer') is not None:
            self.tokenizer = m.get('Tokenizer')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        if m.get('ValueType') is not None:
            self.value_type = m.get('ValueType')

        return self

