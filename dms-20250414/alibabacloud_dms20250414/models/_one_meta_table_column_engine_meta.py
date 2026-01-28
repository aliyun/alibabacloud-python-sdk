# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class OneMetaTableColumnEngineMeta(DaraModel):
    def __init__(
        self,
        auto_increment: bool = None,
        data_length: int = None,
        data_precision: int = None,
        data_scale: int = None,
        default_value: str = None,
        encoding: str = None,
        extra: str = None,
        generation_column: bool = None,
        generation_expression: str = None,
        nullable: bool = None,
    ):
        self.auto_increment = auto_increment
        self.data_length = data_length
        self.data_precision = data_precision
        self.data_scale = data_scale
        self.default_value = default_value
        self.encoding = encoding
        self.extra = extra
        self.generation_column = generation_column
        self.generation_expression = generation_expression
        self.nullable = nullable

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_increment is not None:
            result['AutoIncrement'] = self.auto_increment

        if self.data_length is not None:
            result['DataLength'] = self.data_length

        if self.data_precision is not None:
            result['DataPrecision'] = self.data_precision

        if self.data_scale is not None:
            result['DataScale'] = self.data_scale

        if self.default_value is not None:
            result['DefaultValue'] = self.default_value

        if self.encoding is not None:
            result['Encoding'] = self.encoding

        if self.extra is not None:
            result['Extra'] = self.extra

        if self.generation_column is not None:
            result['GenerationColumn'] = self.generation_column

        if self.generation_expression is not None:
            result['GenerationExpression'] = self.generation_expression

        if self.nullable is not None:
            result['Nullable'] = self.nullable

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoIncrement') is not None:
            self.auto_increment = m.get('AutoIncrement')

        if m.get('DataLength') is not None:
            self.data_length = m.get('DataLength')

        if m.get('DataPrecision') is not None:
            self.data_precision = m.get('DataPrecision')

        if m.get('DataScale') is not None:
            self.data_scale = m.get('DataScale')

        if m.get('DefaultValue') is not None:
            self.default_value = m.get('DefaultValue')

        if m.get('Encoding') is not None:
            self.encoding = m.get('Encoding')

        if m.get('Extra') is not None:
            self.extra = m.get('Extra')

        if m.get('GenerationColumn') is not None:
            self.generation_column = m.get('GenerationColumn')

        if m.get('GenerationExpression') is not None:
            self.generation_expression = m.get('GenerationExpression')

        if m.get('Nullable') is not None:
            self.nullable = m.get('Nullable')

        return self

