# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_btripopen20220520 import models as main_models
from darabonba.model import DaraModel

class InvoiceRuleSaveRequest(DaraModel):
    def __init__(
        self,
        all_employe: bool = None,
        entities: List[main_models.InvoiceRuleSaveRequestEntities] = None,
        scope: int = None,
        third_part_id: str = None,
    ):
        self.all_employe = all_employe
        self.entities = entities
        self.scope = scope
        # This parameter is required.
        self.third_part_id = third_part_id

    def validate(self):
        if self.entities:
            for v1 in self.entities:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.all_employe is not None:
            result['all_employe'] = self.all_employe

        result['entities'] = []
        if self.entities is not None:
            for k1 in self.entities:
                result['entities'].append(k1.to_map() if k1 else None)

        if self.scope is not None:
            result['scope'] = self.scope

        if self.third_part_id is not None:
            result['third_part_id'] = self.third_part_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('all_employe') is not None:
            self.all_employe = m.get('all_employe')

        self.entities = []
        if m.get('entities') is not None:
            for k1 in m.get('entities'):
                temp_model = main_models.InvoiceRuleSaveRequestEntities()
                self.entities.append(temp_model.from_map(k1))

        if m.get('scope') is not None:
            self.scope = m.get('scope')

        if m.get('third_part_id') is not None:
            self.third_part_id = m.get('third_part_id')

        return self

class InvoiceRuleSaveRequestEntities(DaraModel):
    def __init__(
        self,
        id: str = None,
        name: str = None,
        type: int = None,
    ):
        self.id = id
        self.name = name
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['id'] = self.id

        if self.name is not None:
            result['name'] = self.name

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

