# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_btripopen20220520 import models as main_models
from darabonba.model import DaraModel

class TravelStandardRelateDeleteRequest(DaraModel):
    def __init__(
        self,
        from_group: bool = None,
        remove_list: List[main_models.TravelStandardRelateDeleteRequestRemoveList] = None,
        rule_id: int = None,
    ):
        self.from_group = from_group
        self.remove_list = remove_list
        # This parameter is required.
        self.rule_id = rule_id

    def validate(self):
        if self.remove_list:
            for v1 in self.remove_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.from_group is not None:
            result['from_group'] = self.from_group

        result['remove_list'] = []
        if self.remove_list is not None:
            for k1 in self.remove_list:
                result['remove_list'].append(k1.to_map() if k1 else None)

        if self.rule_id is not None:
            result['rule_id'] = self.rule_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('from_group') is not None:
            self.from_group = m.get('from_group')

        self.remove_list = []
        if m.get('remove_list') is not None:
            for k1 in m.get('remove_list'):
                temp_model = main_models.TravelStandardRelateDeleteRequestRemoveList()
                self.remove_list.append(temp_model.from_map(k1))

        if m.get('rule_id') is not None:
            self.rule_id = m.get('rule_id')

        return self

class TravelStandardRelateDeleteRequestRemoveList(DaraModel):
    def __init__(
        self,
        entity_id: str = None,
        entity_type: str = None,
    ):
        # This parameter is required.
        self.entity_id = entity_id
        # This parameter is required.
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

