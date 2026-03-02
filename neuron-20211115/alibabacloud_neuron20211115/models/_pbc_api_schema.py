# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class PbcApiSchema(DaraModel):
    def __init__(
        self,
        api_schema: str = None,
        id: int = None,
        pbc_version_id: int = None,
        request_id: str = None,
    ):
        # This parameter is required.
        self.api_schema = api_schema
        self.id = id
        self.pbc_version_id = pbc_version_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_schema is not None:
            result['apiSchema'] = self.api_schema

        if self.id is not None:
            result['id'] = self.id

        if self.pbc_version_id is not None:
            result['pbcVersionId'] = self.pbc_version_id

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apiSchema') is not None:
            self.api_schema = m.get('apiSchema')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('pbcVersionId') is not None:
            self.pbc_version_id = m.get('pbcVersionId')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

