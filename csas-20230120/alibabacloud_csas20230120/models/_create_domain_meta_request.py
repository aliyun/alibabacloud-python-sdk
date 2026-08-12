# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateDomainMetaRequest(DaraModel):
    def __init__(
        self,
        list_type: str = None,
        name: str = None,
    ):
        # The list type.
        self.list_type = list_type
        # The list name. Maximum length: 32 characters.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.list_type is not None:
            result['ListType'] = self.list_type

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ListType') is not None:
            self.list_type = m.get('ListType')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

