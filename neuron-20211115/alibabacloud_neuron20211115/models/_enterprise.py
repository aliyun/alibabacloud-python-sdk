# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class Enterprise(DaraModel):
    def __init__(
        self,
        account_id: str = None,
        description: str = None,
        id: int = None,
        identification: str = None,
        name: str = None,
        request_id: str = None,
        type: str = None,
    ):
        # This parameter is required.
        self.account_id = account_id
        self.description = description
        # This parameter is required.
        self.id = id
        self.identification = identification
        # This parameter is required.
        self.name = name
        self.request_id = request_id
        # This parameter is required.
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

        if self.description is not None:
            result['description'] = self.description

        if self.id is not None:
            result['id'] = self.id

        if self.identification is not None:
            result['identification'] = self.identification

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

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('identification') is not None:
            self.identification = m.get('identification')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

