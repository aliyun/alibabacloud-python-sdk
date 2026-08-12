# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateDomainMetaRequest(DaraModel):
    def __init__(
        self,
        list_id: str = None,
        list_type: str = None,
        name: str = None,
    ):
        # The list ID. This is a unique business identifier used for policy references and add, delete, or modify operations.
        self.list_id = list_id
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
        if self.list_id is not None:
            result['ListId'] = self.list_id

        if self.list_type is not None:
            result['ListType'] = self.list_type

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ListId') is not None:
            self.list_id = m.get('ListId')

        if m.get('ListType') is not None:
            self.list_type = m.get('ListType')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

