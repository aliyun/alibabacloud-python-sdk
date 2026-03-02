# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ververica20220718 import models as main_models
from darabonba.model import DaraModel

class SubmitPreviewResult(DaraModel):
    def __init__(
        self,
        query_id: str = None,
        session_id: str = None,
        table_schemas: List[main_models.TableSchema] = None,
    ):
        self.query_id = query_id
        self.session_id = session_id
        self.table_schemas = table_schemas

    def validate(self):
        if self.table_schemas:
            for v1 in self.table_schemas:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.query_id is not None:
            result['queryId'] = self.query_id

        if self.session_id is not None:
            result['sessionId'] = self.session_id

        result['tableSchemas'] = []
        if self.table_schemas is not None:
            for k1 in self.table_schemas:
                result['tableSchemas'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('queryId') is not None:
            self.query_id = m.get('queryId')

        if m.get('sessionId') is not None:
            self.session_id = m.get('sessionId')

        self.table_schemas = []
        if m.get('tableSchemas') is not None:
            for k1 in m.get('tableSchemas'):
                temp_model = main_models.TableSchema()
                self.table_schemas.append(temp_model.from_map(k1))

        return self

