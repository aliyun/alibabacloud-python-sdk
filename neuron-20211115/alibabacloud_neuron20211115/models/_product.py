# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class Product(DaraModel):
    def __init__(
        self,
        account_id: str = None,
        alias: str = None,
        company_id: int = None,
        creator: str = None,
        description: str = None,
        gmt_create: str = None,
        id: int = None,
        name: str = None,
        request_id: str = None,
        type: str = None,
    ):
        self.account_id = account_id
        self.alias = alias
        self.company_id = company_id
        self.creator = creator
        self.description = description
        self.gmt_create = gmt_create
        self.id = id
        self.name = name
        self.request_id = request_id
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_id is not None:
            result['accountId'] = self.account_id

        if self.alias is not None:
            result['alias'] = self.alias

        if self.company_id is not None:
            result['companyId'] = self.company_id

        if self.creator is not None:
            result['creator'] = self.creator

        if self.description is not None:
            result['description'] = self.description

        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create

        if self.id is not None:
            result['id'] = self.id

        if self.name is not None:
            result['name'] = self.name

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accountId') is not None:
            self.account_id = m.get('accountId')

        if m.get('alias') is not None:
            self.alias = m.get('alias')

        if m.get('companyId') is not None:
            self.company_id = m.get('companyId')

        if m.get('creator') is not None:
            self.creator = m.get('creator')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

