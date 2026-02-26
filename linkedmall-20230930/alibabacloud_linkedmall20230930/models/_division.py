# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class Division(DaraModel):
    def __init__(
        self,
        division_code: int = None,
        division_level: int = None,
        division_name: str = None,
        parent_id: int = None,
        pinyin: str = None,
    ):
        self.division_code = division_code
        self.division_level = division_level
        self.division_name = division_name
        self.parent_id = parent_id
        self.pinyin = pinyin

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.division_code is not None:
            result['divisionCode'] = self.division_code

        if self.division_level is not None:
            result['divisionLevel'] = self.division_level

        if self.division_name is not None:
            result['divisionName'] = self.division_name

        if self.parent_id is not None:
            result['parentId'] = self.parent_id

        if self.pinyin is not None:
            result['pinyin'] = self.pinyin

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('divisionCode') is not None:
            self.division_code = m.get('divisionCode')

        if m.get('divisionLevel') is not None:
            self.division_level = m.get('divisionLevel')

        if m.get('divisionName') is not None:
            self.division_name = m.get('divisionName')

        if m.get('parentId') is not None:
            self.parent_id = m.get('parentId')

        if m.get('pinyin') is not None:
            self.pinyin = m.get('pinyin')

        return self

