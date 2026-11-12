# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ObserveGroupEntitySummary(DaraModel):
    def __init__(
        self,
        entity_category: str = None,
        entity_count: int = None,
        entity_domain: str = None,
        entity_type: str = None,
        main_count: int = None,
        related_count: int = None,
    ):
        # The entity category.
        self.entity_category = entity_category
        # The total count of entities of this type.
        self.entity_count = entity_count
        # The entity domain.
        self.entity_domain = entity_domain
        # The entity type.
        self.entity_type = entity_type
        # The count of primary entities of this type.
        self.main_count = main_count
        # The count of associated child entities of this type.
        self.related_count = related_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.entity_category is not None:
            result['entityCategory'] = self.entity_category

        if self.entity_count is not None:
            result['entityCount'] = self.entity_count

        if self.entity_domain is not None:
            result['entityDomain'] = self.entity_domain

        if self.entity_type is not None:
            result['entityType'] = self.entity_type

        if self.main_count is not None:
            result['mainCount'] = self.main_count

        if self.related_count is not None:
            result['relatedCount'] = self.related_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('entityCategory') is not None:
            self.entity_category = m.get('entityCategory')

        if m.get('entityCount') is not None:
            self.entity_count = m.get('entityCount')

        if m.get('entityDomain') is not None:
            self.entity_domain = m.get('entityDomain')

        if m.get('entityType') is not None:
            self.entity_type = m.get('entityType')

        if m.get('mainCount') is not None:
            self.main_count = m.get('mainCount')

        if m.get('relatedCount') is not None:
            self.related_count = m.get('relatedCount')

        return self

