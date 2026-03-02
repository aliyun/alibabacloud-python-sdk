# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ProductUpdateCmd(DaraModel):
    def __init__(
        self,
        alias: str = None,
        company_id: int = None,
        description: str = None,
        id: int = None,
        request_id: str = None,
    ):
        self.alias = alias
        self.company_id = company_id
        self.description = description
        self.id = id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alias is not None:
            result['alias'] = self.alias

        if self.company_id is not None:
            result['companyId'] = self.company_id

        if self.description is not None:
            result['description'] = self.description

        if self.id is not None:
            result['id'] = self.id

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('alias') is not None:
            self.alias = m.get('alias')

        if m.get('companyId') is not None:
            self.company_id = m.get('companyId')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

