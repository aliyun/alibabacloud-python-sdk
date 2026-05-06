# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ImportVocabularyRequest(DaraModel):
    def __init__(
        self,
        business_unit_id: str = None,
        file_key: str = None,
    ):
        self.business_unit_id = business_unit_id
        self.file_key = file_key

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.business_unit_id is not None:
            result['BusinessUnitId'] = self.business_unit_id

        if self.file_key is not None:
            result['FileKey'] = self.file_key

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BusinessUnitId') is not None:
            self.business_unit_id = m.get('BusinessUnitId')

        if m.get('FileKey') is not None:
            self.file_key = m.get('FileKey')

        return self

