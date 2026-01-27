# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListApprovalProcessesForApprovalSchemasRequest(DaraModel):
    def __init__(
        self,
        schema_ids: List[str] = None,
    ):
        # This parameter is required.
        self.schema_ids = schema_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.schema_ids is not None:
            result['SchemaIds'] = self.schema_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SchemaIds') is not None:
            self.schema_ids = m.get('SchemaIds')

        return self

