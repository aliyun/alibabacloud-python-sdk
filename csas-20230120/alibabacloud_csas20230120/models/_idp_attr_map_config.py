# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_csas20230120 import models as main_models
from darabonba.model import DaraModel

class IdpAttrMapConfig(DaraModel):
    def __init__(
        self,
        map_items: List[main_models.IdpAttrMapConfigItem] = None,
    ):
        self.map_items = map_items

    def validate(self):
        if self.map_items:
            for v1 in self.map_items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['MapItems'] = []
        if self.map_items is not None:
            for k1 in self.map_items:
                result['MapItems'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.map_items = []
        if m.get('MapItems') is not None:
            for k1 in m.get('MapItems'):
                temp_model = main_models.IdpAttrMapConfigItem()
                self.map_items.append(temp_model.from_map(k1))

        return self

