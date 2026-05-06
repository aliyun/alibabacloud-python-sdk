# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ExportVocabularyShrinkRequest(DaraModel):
    def __init__(
        self,
        business_unit_id: str = None,
        vocabulary_ids_shrink: str = None,
    ):
        self.business_unit_id = business_unit_id
        self.vocabulary_ids_shrink = vocabulary_ids_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.business_unit_id is not None:
            result['BusinessUnitId'] = self.business_unit_id

        if self.vocabulary_ids_shrink is not None:
            result['VocabularyIds'] = self.vocabulary_ids_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BusinessUnitId') is not None:
            self.business_unit_id = m.get('BusinessUnitId')

        if m.get('VocabularyIds') is not None:
            self.vocabulary_ids_shrink = m.get('VocabularyIds')

        return self

