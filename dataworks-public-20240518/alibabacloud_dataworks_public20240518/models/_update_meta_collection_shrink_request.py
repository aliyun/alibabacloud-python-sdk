# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateMetaCollectionShrinkRequest(DaraModel):
    def __init__(
        self,
        administrators_shrink: str = None,
        description: str = None,
        id: str = None,
        name: str = None,
    ):
        # The collection administrator IDs. This parameter is available only for data albums. The administrator must be an account within the same tenant.
        self.administrators_shrink = administrators_shrink
        self.description = description
        # The collection ID.
        # 
        # This parameter is required.
        self.id = id
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.administrators_shrink is not None:
            result['Administrators'] = self.administrators_shrink

        if self.description is not None:
            result['Description'] = self.description

        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Administrators') is not None:
            self.administrators_shrink = m.get('Administrators')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

