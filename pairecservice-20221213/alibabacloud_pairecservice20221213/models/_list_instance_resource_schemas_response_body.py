# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_pairecservice20221213 import models as main_models
from darabonba.model import DaraModel

class ListInstanceResourceSchemasResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        schemas: List[main_models.ListInstanceResourceSchemasResponseBodySchemas] = None,
        total_count: int = None,
    ):
        self.request_id = request_id
        self.schemas = schemas
        self.total_count = total_count

    def validate(self):
        if self.schemas:
            for v1 in self.schemas:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Schemas'] = []
        if self.schemas is not None:
            for k1 in self.schemas:
                result['Schemas'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.schemas = []
        if m.get('Schemas') is not None:
            for k1 in m.get('Schemas'):
                temp_model = main_models.ListInstanceResourceSchemasResponseBodySchemas()
                self.schemas.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListInstanceResourceSchemasResponseBodySchemas(DaraModel):
    def __init__(
        self,
        schema_name: str = None,
    ):
        self.schema_name = schema_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.schema_name is not None:
            result['SchemaName'] = self.schema_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SchemaName') is not None:
            self.schema_name = m.get('SchemaName')

        return self

