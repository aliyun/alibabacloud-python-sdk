# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sae20190506 import models as main_models
from darabonba.model import DaraModel

class ListStaticsQueryResponse(DaraModel):
    def __init__(
        self,
        length: int = None,
        sort: str = None,
        statics: List[main_models.StaticsInfo] = None,
    ):
        self.length = length
        self.sort = sort
        self.statics = statics

    def validate(self):
        if self.statics:
            for v1 in self.statics:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.length is not None:
            result['length'] = self.length

        if self.sort is not None:
            result['sort'] = self.sort

        result['statics'] = []
        if self.statics is not None:
            for k1 in self.statics:
                result['statics'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('length') is not None:
            self.length = m.get('length')

        if m.get('sort') is not None:
            self.sort = m.get('sort')

        self.statics = []
        if m.get('statics') is not None:
            for k1 in m.get('statics'):
                temp_model = main_models.StaticsInfo()
                self.statics.append(temp_model.from_map(k1))

        return self

