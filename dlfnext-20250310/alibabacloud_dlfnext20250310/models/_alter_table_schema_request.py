# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dlfnext20250310 import models as main_models
from darabonba.model import DaraModel

class AlterTableSchemaRequest(DaraModel):
    def __init__(
        self,
        schema: main_models.Schema = None,
    ):
        # The table schema.
        self.schema = schema

    def validate(self):
        if self.schema:
            self.schema.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.schema is not None:
            result['schema'] = self.schema.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('schema') is not None:
            temp_model = main_models.Schema()
            self.schema = temp_model.from_map(m.get('schema'))

        return self

