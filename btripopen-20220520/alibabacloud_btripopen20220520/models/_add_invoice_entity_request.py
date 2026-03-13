# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_btripopen20220520 import models as main_models
from darabonba.model import DaraModel

class AddInvoiceEntityRequest(DaraModel):
    def __init__(
        self,
        entities: List[main_models.AddInvoiceEntityRequestEntities] = None,
        third_part_id: str = None,
    ):
        # This parameter is required.
        self.entities = entities
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
        result['entities'] = []
        if self.entities is not None:
            for k1 in self.entities:
                result['entities'].append(k1.to_map() if k1 else None)

        if self.third_part_id is not None:
            result['third_part_id'] = self.third_part_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.entities = []
        if m.get('entities') is not None:
            for k1 in m.get('entities'):
                temp_model = main_models.AddInvoiceEntityRequestEntities()
                self.entities.append(temp_model.from_map(k1))

        if m.get('third_part_id') is not None:
            self.third_part_id = m.get('third_part_id')

        return self

class AddInvoiceEntityRequestEntities(DaraModel):
    def __init__(
        self,
        entity_id: str = None,
        entity_name: str = None,
        entity_type: str = None,
    ):
        # This parameter is required.
        self.entity_id = entity_id
        # This parameter is required.
        self.entity_name = entity_name
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

        if self.entity_name is not None:
            result['entity_name'] = self.entity_name

        if self.entity_type is not None:
            result['entity_type'] = self.entity_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('entity_id') is not None:
            self.entity_id = m.get('entity_id')

        if m.get('entity_name') is not None:
            self.entity_name = m.get('entity_name')

        if m.get('entity_type') is not None:
            self.entity_type = m.get('entity_type')

        return self

