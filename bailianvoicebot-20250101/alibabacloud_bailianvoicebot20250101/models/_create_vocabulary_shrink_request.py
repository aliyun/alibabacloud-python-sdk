# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateVocabularyShrinkRequest(DaraModel):
    def __init__(
        self,
        business_unit_id: str = None,
        description: str = None,
        name: str = None,
        words_shrink: str = None,
    ):
        self.business_unit_id = business_unit_id
        self.description = description
        self.name = name
        self.words_shrink = words_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.business_unit_id is not None:
            result['BusinessUnitId'] = self.business_unit_id

        if self.description is not None:
            result['Description'] = self.description

        if self.name is not None:
            result['Name'] = self.name

        if self.words_shrink is not None:
            result['Words'] = self.words_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BusinessUnitId') is not None:
            self.business_unit_id = m.get('BusinessUnitId')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Words') is not None:
            self.words_shrink = m.get('Words')

        return self

