# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dlfnext20250310 import models as main_models
from darabonba.model import DaraModel

class CreateTableRequest(DaraModel):
    def __init__(
        self,
        identifier: main_models.Identifier = None,
        schema: main_models.Schema = None,
    ):
        self.identifier = identifier
        self.schema = schema

    def validate(self):
        if self.identifier:
            self.identifier.validate()
        if self.schema:
            self.schema.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.identifier is not None:
            result['identifier'] = self.identifier.to_map()

        if self.schema is not None:
            result['schema'] = self.schema.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('identifier') is not None:
            temp_model = main_models.Identifier()
            self.identifier = temp_model.from_map(m.get('identifier'))

        if m.get('schema') is not None:
            temp_model = main_models.Schema()
            self.schema = temp_model.from_map(m.get('schema'))

        return self

