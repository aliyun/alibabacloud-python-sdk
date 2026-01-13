# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_emr_serverless_spark20230808 import models as main_models
from darabonba.model import DaraModel

class SqlOutput(DaraModel):
    def __init__(
        self,
        rows: List[main_models.SqlOutputRows] = None,
        schema: main_models.SqlOutputSchema = None,
    ):
        self.rows = rows
        self.schema = schema

    def validate(self):
        if self.rows:
            for v1 in self.rows:
                 if v1:
                    v1.validate()
        if self.schema:
            self.schema.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['rows'] = []
        if self.rows is not None:
            for k1 in self.rows:
                result['rows'].append(k1.to_map() if k1 else None)

        if self.schema is not None:
            result['schema'] = self.schema.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.rows = []
        if m.get('rows') is not None:
            for k1 in m.get('rows'):
                temp_model = main_models.SqlOutputRows()
                self.rows.append(temp_model.from_map(k1))

        if m.get('schema') is not None:
            temp_model = main_models.SqlOutputSchema()
            self.schema = temp_model.from_map(m.get('schema'))

        return self

class SqlOutputSchema(DaraModel):
    def __init__(
        self,
        fields: List[main_models.SqlOutputSchemaFields] = None,
    ):
        self.fields = fields

    def validate(self):
        if self.fields:
            for v1 in self.fields:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['fields'] = []
        if self.fields is not None:
            for k1 in self.fields:
                result['fields'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.fields = []
        if m.get('fields') is not None:
            for k1 in m.get('fields'):
                temp_model = main_models.SqlOutputSchemaFields()
                self.fields.append(temp_model.from_map(k1))

        return self

class SqlOutputSchemaFields(DaraModel):
    def __init__(
        self,
        name: str = None,
        nullable: bool = None,
        type: str = None,
    ):
        self.name = name
        self.nullable = nullable
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['name'] = self.name

        if self.nullable is not None:
            result['nullable'] = self.nullable

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('nullable') is not None:
            self.nullable = m.get('nullable')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

class SqlOutputRows(DaraModel):
    def __init__(
        self,
        values: List[str] = None,
    ):
        self.values = values

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.values is not None:
            result['values'] = self.values

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('values') is not None:
            self.values = m.get('values')

        return self

