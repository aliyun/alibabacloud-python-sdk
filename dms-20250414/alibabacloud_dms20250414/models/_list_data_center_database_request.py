# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListDataCenterDatabaseRequest(DaraModel):
    def __init__(
        self,
        call_from: str = None,
        dms_unit: str = None,
        import_type: str = None,
        language: str = None,
        search_key: str = None,
    ):
        self.call_from = call_from
        self.dms_unit = dms_unit
        self.import_type = import_type
        self.language = language
        self.search_key = search_key

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.call_from is not None:
            result['CallFrom'] = self.call_from

        if self.dms_unit is not None:
            result['DmsUnit'] = self.dms_unit

        if self.import_type is not None:
            result['ImportType'] = self.import_type

        if self.language is not None:
            result['Language'] = self.language

        if self.search_key is not None:
            result['SearchKey'] = self.search_key

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CallFrom') is not None:
            self.call_from = m.get('CallFrom')

        if m.get('DmsUnit') is not None:
            self.dms_unit = m.get('DmsUnit')

        if m.get('ImportType') is not None:
            self.import_type = m.get('ImportType')

        if m.get('Language') is not None:
            self.language = m.get('Language')

        if m.get('SearchKey') is not None:
            self.search_key = m.get('SearchKey')

        return self

