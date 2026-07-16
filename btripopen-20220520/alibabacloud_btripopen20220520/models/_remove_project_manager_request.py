# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_btripopen20220520 import models as main_models
from darabonba.model import DaraModel

class RemoveProjectManagerRequest(DaraModel):
    def __init__(
        self,
        org_entities: List[main_models.RemoveProjectManagerRequestOrgEntities] = None,
        out_project_id: str = None,
        project_id: int = None,
        remove_all: bool = None,
    ):
        self.org_entities = org_entities
        self.out_project_id = out_project_id
        self.project_id = project_id
        self.remove_all = remove_all

    def validate(self):
        if self.org_entities:
            for v1 in self.org_entities:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['org_entities'] = []
        if self.org_entities is not None:
            for k1 in self.org_entities:
                result['org_entities'].append(k1.to_map() if k1 else None)

        if self.out_project_id is not None:
            result['out_project_id'] = self.out_project_id

        if self.project_id is not None:
            result['project_id'] = self.project_id

        if self.remove_all is not None:
            result['remove_all'] = self.remove_all

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.org_entities = []
        if m.get('org_entities') is not None:
            for k1 in m.get('org_entities'):
                temp_model = main_models.RemoveProjectManagerRequestOrgEntities()
                self.org_entities.append(temp_model.from_map(k1))

        if m.get('out_project_id') is not None:
            self.out_project_id = m.get('out_project_id')

        if m.get('project_id') is not None:
            self.project_id = m.get('project_id')

        if m.get('remove_all') is not None:
            self.remove_all = m.get('remove_all')

        return self

class RemoveProjectManagerRequestOrgEntities(DaraModel):
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

