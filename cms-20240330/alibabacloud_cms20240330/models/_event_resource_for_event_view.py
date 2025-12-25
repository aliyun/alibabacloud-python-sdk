# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from alibabacloud_cms20240330 import models as main_models
from darabonba.model import DaraModel

class EventResourceForEventView(DaraModel):
    def __init__(
        self,
        entity: main_models.EventResourceForEventViewEntity = None,
        tags: Dict[str, Any] = None,
    ):
        self.entity = entity
        self.tags = tags

    def validate(self):
        if self.entity:
            self.entity.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.entity is not None:
            result['entity'] = self.entity.to_map()

        if self.tags is not None:
            result['tags'] = self.tags

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('entity') is not None:
            temp_model = main_models.EventResourceForEventViewEntity()
            self.entity = temp_model.from_map(m.get('entity'))

        if m.get('tags') is not None:
            self.tags = m.get('tags')

        return self

class EventResourceForEventViewEntity(DaraModel):
    def __init__(
        self,
        domain: str = None,
        entity_id: str = None,
        entity_type: str = None,
        prop: Dict[str, Any] = None,
    ):
        self.domain = domain
        self.entity_id = entity_id
        self.entity_type = entity_type
        self.prop = prop

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain is not None:
            result['domain'] = self.domain

        if self.entity_id is not None:
            result['entityId'] = self.entity_id

        if self.entity_type is not None:
            result['entityType'] = self.entity_type

        if self.prop is not None:
            result['prop'] = self.prop

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('domain') is not None:
            self.domain = m.get('domain')

        if m.get('entityId') is not None:
            self.entity_id = m.get('entityId')

        if m.get('entityType') is not None:
            self.entity_type = m.get('entityType')

        if m.get('prop') is not None:
            self.prop = m.get('prop')

        return self

