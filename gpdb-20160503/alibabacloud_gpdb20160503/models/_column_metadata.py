# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ColumnMetadata(DaraModel):
    def __init__(
        self,
        column_default: str = None,
        comment: str = None,
        data_type: str = None,
        is_case_sensitive: bool = None,
        is_currency: bool = None,
        is_primary_key: bool = None,
        is_signed: bool = None,
        max_length: int = None,
        name: str = None,
        nullable: bool = None,
        precision: int = None,
        scale: int = None,
        schema_name: str = None,
        table_name: str = None,
        udt_name: str = None,
    ):
        self.column_default = column_default
        self.comment = comment
        self.data_type = data_type
        self.is_case_sensitive = is_case_sensitive
        self.is_currency = is_currency
        self.is_primary_key = is_primary_key
        self.is_signed = is_signed
        self.max_length = max_length
        self.name = name
        self.nullable = nullable
        self.precision = precision
        self.scale = scale
        self.schema_name = schema_name
        self.table_name = table_name
        self.udt_name = udt_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.column_default is not None:
            result['ColumnDefault'] = self.column_default

        if self.comment is not None:
            result['Comment'] = self.comment

        if self.data_type is not None:
            result['DataType'] = self.data_type

        if self.is_case_sensitive is not None:
            result['IsCaseSensitive'] = self.is_case_sensitive

        if self.is_currency is not None:
            result['IsCurrency'] = self.is_currency

        if self.is_primary_key is not None:
            result['IsPrimaryKey'] = self.is_primary_key

        if self.is_signed is not None:
            result['IsSigned'] = self.is_signed

        if self.max_length is not None:
            result['MaxLength'] = self.max_length

        if self.name is not None:
            result['Name'] = self.name

        if self.nullable is not None:
            result['Nullable'] = self.nullable

        if self.precision is not None:
            result['Precision'] = self.precision

        if self.scale is not None:
            result['Scale'] = self.scale

        if self.schema_name is not None:
            result['SchemaName'] = self.schema_name

        if self.table_name is not None:
            result['TableName'] = self.table_name

        if self.udt_name is not None:
            result['UdtName'] = self.udt_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ColumnDefault') is not None:
            self.column_default = m.get('ColumnDefault')

        if m.get('Comment') is not None:
            self.comment = m.get('Comment')

        if m.get('DataType') is not None:
            self.data_type = m.get('DataType')

        if m.get('IsCaseSensitive') is not None:
            self.is_case_sensitive = m.get('IsCaseSensitive')

        if m.get('IsCurrency') is not None:
            self.is_currency = m.get('IsCurrency')

        if m.get('IsPrimaryKey') is not None:
            self.is_primary_key = m.get('IsPrimaryKey')

        if m.get('IsSigned') is not None:
            self.is_signed = m.get('IsSigned')

        if m.get('MaxLength') is not None:
            self.max_length = m.get('MaxLength')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Nullable') is not None:
            self.nullable = m.get('Nullable')

        if m.get('Precision') is not None:
            self.precision = m.get('Precision')

        if m.get('Scale') is not None:
            self.scale = m.get('Scale')

        if m.get('SchemaName') is not None:
            self.schema_name = m.get('SchemaName')

        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')

        if m.get('UdtName') is not None:
            self.udt_name = m.get('UdtName')

        return self

