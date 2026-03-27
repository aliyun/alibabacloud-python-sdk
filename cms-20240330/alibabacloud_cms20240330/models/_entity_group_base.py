# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cms20240330 import models as main_models
from darabonba.model import DaraModel

class EntityGroupBase(DaraModel):
    def __init__(
        self,
        description: str = None,
        entity_group_id: str = None,
        entity_group_name: str = None,
        entity_queries: List[main_models.EntityGroupBaseEntityQueries] = None,
        entity_rules: main_models.EntityDiscoverRule = None,
        region_id: str = None,
        user_id: str = None,
        workspace: str = None,
    ):
        self.description = description
        self.entity_group_id = entity_group_id
        self.entity_group_name = entity_group_name
        self.entity_queries = entity_queries
        self.entity_rules = entity_rules
        self.region_id = region_id
        self.user_id = user_id
        self.workspace = workspace

    def validate(self):
        if self.entity_queries:
            for v1 in self.entity_queries:
                 if v1:
                    v1.validate()
        if self.entity_rules:
            self.entity_rules.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['description'] = self.description

        if self.entity_group_id is not None:
            result['entityGroupId'] = self.entity_group_id

        if self.entity_group_name is not None:
            result['entityGroupName'] = self.entity_group_name

        result['entityQueries'] = []
        if self.entity_queries is not None:
            for k1 in self.entity_queries:
                result['entityQueries'].append(k1.to_map() if k1 else None)

        if self.entity_rules is not None:
            result['entityRules'] = self.entity_rules.to_map()

        if self.region_id is not None:
            result['regionId'] = self.region_id

        if self.user_id is not None:
            result['userId'] = self.user_id

        if self.workspace is not None:
            result['workspace'] = self.workspace

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('entityGroupId') is not None:
            self.entity_group_id = m.get('entityGroupId')

        if m.get('entityGroupName') is not None:
            self.entity_group_name = m.get('entityGroupName')

        self.entity_queries = []
        if m.get('entityQueries') is not None:
            for k1 in m.get('entityQueries'):
                temp_model = main_models.EntityGroupBaseEntityQueries()
                self.entity_queries.append(temp_model.from_map(k1))

        if m.get('entityRules') is not None:
            temp_model = main_models.EntityDiscoverRule()
            self.entity_rules = temp_model.from_map(m.get('entityRules'))

        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')

        if m.get('userId') is not None:
            self.user_id = m.get('userId')

        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')

        return self

class EntityGroupBaseEntityQueries(DaraModel):
    def __init__(
        self,
        entity_type: str = None,
        spl: str = None,
    ):
        self.entity_type = entity_type
        self.spl = spl

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.entity_type is not None:
            result['entityType'] = self.entity_type

        if self.spl is not None:
            result['spl'] = self.spl

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('entityType') is not None:
            self.entity_type = m.get('entityType')

        if m.get('spl') is not None:
            self.spl = m.get('spl')

        return self

