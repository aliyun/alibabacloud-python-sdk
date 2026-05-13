# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeTairSkvDdbTableSchemaResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        schema: str = None,
        ttl_spec: str = None,
    ):
        self.request_id = request_id
        self.schema = schema
        self.ttl_spec = ttl_spec

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.schema is not None:
            result['Schema'] = self.schema

        if self.ttl_spec is not None:
            result['TtlSpec'] = self.ttl_spec

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Schema') is not None:
            self.schema = m.get('Schema')

        if m.get('TtlSpec') is not None:
            self.ttl_spec = m.get('TtlSpec')

        return self

