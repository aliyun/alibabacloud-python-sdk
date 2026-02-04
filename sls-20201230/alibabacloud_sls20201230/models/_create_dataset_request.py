# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_sls20201230 import models as main_models
from darabonba.model import DaraModel

class CreateDatasetRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        schema: Dict[str, main_models.IndexKey] = None,
    ):
        self.description = description
        self.name = name
        self.schema = schema

    def validate(self):
        if self.schema:
            for v1 in self.schema.values():
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['description'] = self.description

        if self.name is not None:
            result['name'] = self.name

        result['schema'] = {}
        if self.schema is not None:
            for k1, v1 in self.schema.items():
                result['schema'][k1] = v1.to_map() if v1 else None

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('name') is not None:
            self.name = m.get('name')

        self.schema = {}
        if m.get('schema') is not None:
            for k1, v1 in m.get('schema').items():
                temp_model = main_models.IndexKey()
                self.schema[k1] = temp_model.from_map(v1)

        return self

