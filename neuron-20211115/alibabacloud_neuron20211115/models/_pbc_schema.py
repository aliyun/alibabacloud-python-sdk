# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class PbcSchema(DaraModel):
    def __init__(
        self,
        id: int = None,
        pbc_version_id: int = None,
        request_id: str = None,
        schema: str = None,
    ):
        self.id = id
        self.pbc_version_id = pbc_version_id
        self.request_id = request_id
        # This parameter is required.
        self.schema = schema

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['id'] = self.id

        if self.pbc_version_id is not None:
            result['pbcVersionId'] = self.pbc_version_id

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.schema is not None:
            result['schema'] = self.schema

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('pbcVersionId') is not None:
            self.pbc_version_id = m.get('pbcVersionId')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('schema') is not None:
            self.schema = m.get('schema')

        return self

