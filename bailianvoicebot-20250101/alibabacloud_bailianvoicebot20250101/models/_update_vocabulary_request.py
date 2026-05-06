# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from darabonba.model import DaraModel

class UpdateVocabularyRequest(DaraModel):
    def __init__(
        self,
        business_unit_id: str = None,
        description: str = None,
        name: str = None,
        vocabulary_id: str = None,
        words: Dict[str, str] = None,
    ):
        self.business_unit_id = business_unit_id
        self.description = description
        self.name = name
        self.vocabulary_id = vocabulary_id
        self.words = words

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

        if self.vocabulary_id is not None:
            result['VocabularyId'] = self.vocabulary_id

        if self.words is not None:
            result['Words'] = self.words

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BusinessUnitId') is not None:
            self.business_unit_id = m.get('BusinessUnitId')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('VocabularyId') is not None:
            self.vocabulary_id = m.get('VocabularyId')

        if m.get('Words') is not None:
            self.words = m.get('Words')

        return self

