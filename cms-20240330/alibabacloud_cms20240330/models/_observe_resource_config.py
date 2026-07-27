# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ObserveResourceConfig(DaraModel):
    def __init__(
        self,
        entity_domain: str = None,
        entity_type: str = None,
        namespace: str = None,
        product_category: str = None,
        relation_type: str = None,
        resources: List[str] = None,
    ):
        self.entity_domain = entity_domain
        self.entity_type = entity_type
        self.namespace = namespace
        self.product_category = product_category
        self.relation_type = relation_type
        self.resources = resources

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.entity_domain is not None:
            result['entityDomain'] = self.entity_domain

        if self.entity_type is not None:
            result['entityType'] = self.entity_type

        if self.namespace is not None:
            result['namespace'] = self.namespace

        if self.product_category is not None:
            result['productCategory'] = self.product_category

        if self.relation_type is not None:
            result['relationType'] = self.relation_type

        if self.resources is not None:
            result['resources'] = self.resources

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('entityDomain') is not None:
            self.entity_domain = m.get('entityDomain')

        if m.get('entityType') is not None:
            self.entity_type = m.get('entityType')

        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')

        if m.get('productCategory') is not None:
            self.product_category = m.get('productCategory')

        if m.get('relationType') is not None:
            self.relation_type = m.get('relationType')

        if m.get('resources') is not None:
            self.resources = m.get('resources')

        return self

