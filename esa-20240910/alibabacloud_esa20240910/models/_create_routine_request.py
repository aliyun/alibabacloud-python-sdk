# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateRoutineRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        has_assets: bool = None,
        name: str = None,
    ):
        # The routine description.
        self.description = description
        self.has_assets = has_assets
        # The routine name, which must be unique in the same account.
        # 
        # This parameter is required.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.has_assets is not None:
            result['HasAssets'] = self.has_assets

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('HasAssets') is not None:
            self.has_assets = m.get('HasAssets')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

