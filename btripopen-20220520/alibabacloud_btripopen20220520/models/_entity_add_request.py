# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_btripopen20220520 import models as main_models
from darabonba.model import DaraModel

class EntityAddRequest(DaraModel):
    def __init__(
        self,
        entity_dolist: List[main_models.EntityAddRequestEntityDOList] = None,
        thirdpart_id: str = None,
    ):
        self.entity_dolist = entity_dolist
        # This parameter is required.
        self.thirdpart_id = thirdpart_id

    def validate(self):
        if self.entity_dolist:
            for v1 in self.entity_dolist:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['entity_d_o_list'] = []
        if self.entity_dolist is not None:
            for k1 in self.entity_dolist:
                result['entity_d_o_list'].append(k1.to_map() if k1 else None)

        if self.thirdpart_id is not None:
            result['thirdpart_id'] = self.thirdpart_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.entity_dolist = []
        if m.get('entity_d_o_list') is not None:
            for k1 in m.get('entity_d_o_list'):
                temp_model = main_models.EntityAddRequestEntityDOList()
                self.entity_dolist.append(temp_model.from_map(k1))

        if m.get('thirdpart_id') is not None:
            self.thirdpart_id = m.get('thirdpart_id')

        return self

class EntityAddRequestEntityDOList(DaraModel):
    def __init__(
        self,
        entity_id: str = None,
        entity_type: str = None,
    ):
        self.entity_id = entity_id
        self.entity_type = entity_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.entity_id is not None:
            result['entity_id'] = self.entity_id

        if self.entity_type is not None:
            result['entity_type'] = self.entity_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('entity_id') is not None:
            self.entity_id = m.get('entity_id')

        if m.get('entity_type') is not None:
            self.entity_type = m.get('entity_type')

        return self

