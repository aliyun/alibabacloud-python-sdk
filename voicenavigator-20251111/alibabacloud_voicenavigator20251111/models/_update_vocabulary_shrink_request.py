# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateVocabularyShrinkRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        instance_id: str = None,
        name: str = None,
        vocabulary_id: str = None,
        words_shrink: str = None,
    ):
        self.description = description
        self.instance_id = instance_id
        self.name = name
        self.vocabulary_id = vocabulary_id
        self.words_shrink = words_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.name is not None:
            result['Name'] = self.name

        if self.vocabulary_id is not None:
            result['VocabularyId'] = self.vocabulary_id

        if self.words_shrink is not None:
            result['Words'] = self.words_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('VocabularyId') is not None:
            self.vocabulary_id = m.get('VocabularyId')

        if m.get('Words') is not None:
            self.words_shrink = m.get('Words')

        return self

