# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_agentloop20260520 import models as main_models
from darabonba.model import DaraModel

class UpdateDatasetRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        schema: Dict[str, main_models.IndexKey] = None,
        client_token: str = None,
    ):
        self.description = description
        self.schema = schema
        self.client_token = client_token

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

        result['schema'] = {}
        if self.schema is not None:
            for k1, v1 in self.schema.items():
                result['schema'][k1] = v1.to_map() if v1 else None

        if self.client_token is not None:
            result['clientToken'] = self.client_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')

        self.schema = {}
        if m.get('schema') is not None:
            for k1, v1 in m.get('schema').items():
                temp_model = main_models.IndexKey()
                self.schema[k1] = temp_model.from_map(v1)

        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')

        return self

