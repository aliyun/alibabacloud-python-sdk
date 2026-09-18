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
        # The UModel entity domain.
        self.entity_domain = entity_domain
        # The UModel entity type.
        self.entity_type = entity_type
        # The CloudMonitor namespace.
        self.namespace = namespace
        # The CloudMonitor product category.
        self.product_category = product_category
        # The relation type. TAG is supported only for alert rules where datasourceConfig.type is set to APM and queryConfig.type is set to APM_MULTI_QUERY. UMODEL_ENTITY does not support writes and is used only for reading existing data.
        self.relation_type = relation_type
        # The list of resources. If relationType is set to ALL, this parameter can be left empty, which indicates all resources. If relationType is set to TAG, this parameter is a list of labels in key=value format (such as ["env=prod", "app=foo"]). This is supported only for APM data sources with APM_MULTI_QUERY.
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

