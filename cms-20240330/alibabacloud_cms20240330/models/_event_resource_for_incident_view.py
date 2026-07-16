# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class EventResourceForIncidentView(DaraModel):
    def __init__(
        self,
        domain: str = None,
        entity_id: str = None,
        entity_type: str = None,
        probs: str = None,
        tags: str = None,
    ):
        # The domain of the resource type.
        self.domain = domain
        # The entity ID.
        self.entity_id = entity_id
        # The entity type.
        self.entity_type = entity_type
        # The string that describes the properties of the resource.
        self.probs = probs
        # The tags.
        self.tags = tags

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

        if self.probs is not None:
            result['probs'] = self.probs

        if self.tags is not None:
            result['tags'] = self.tags

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('domain') is not None:
            self.domain = m.get('domain')

        if m.get('entityId') is not None:
            self.entity_id = m.get('entityId')

        if m.get('entityType') is not None:
            self.entity_type = m.get('entityType')

        if m.get('probs') is not None:
            self.probs = m.get('probs')

        if m.get('tags') is not None:
            self.tags = m.get('tags')

        return self

