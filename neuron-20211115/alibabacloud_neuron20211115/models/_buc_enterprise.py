# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class BucEnterprise(DaraModel):
    def __init__(
        self,
        account_id: str = None,
        codeup_enterprise_id: str = None,
        codeup_namespace_id: int = None,
        description: str = None,
        id: int = None,
        name: str = None,
        type: str = None,
    ):
        self.account_id = account_id
        self.codeup_enterprise_id = codeup_enterprise_id
        self.codeup_namespace_id = codeup_namespace_id
        self.description = description
        self.id = id
        self.name = name
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

        if self.codeup_enterprise_id is not None:
            result['codeupEnterpriseId'] = self.codeup_enterprise_id

        if self.codeup_namespace_id is not None:
            result['codeupNamespaceId'] = self.codeup_namespace_id

        if self.description is not None:
            result['description'] = self.description

        if self.id is not None:
            result['id'] = self.id

        if self.name is not None:
            result['name'] = self.name

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accountId') is not None:
            self.account_id = m.get('accountId')

        if m.get('codeupEnterpriseId') is not None:
            self.codeup_enterprise_id = m.get('codeupEnterpriseId')

        if m.get('codeupNamespaceId') is not None:
            self.codeup_namespace_id = m.get('codeupNamespaceId')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

