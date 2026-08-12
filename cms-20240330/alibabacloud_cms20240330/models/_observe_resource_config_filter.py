# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_cms20240330 import models as main_models
from darabonba.model import DaraModel

class ObserveResourceConfigFilter(DaraModel):
    def __init__(
        self,
        entity_domain: main_models.QueryAlertRulesEntityDomainFilter = None,
        entity_type: main_models.QueryAlertRulesEntityTypeFilter = None,
        namespace: main_models.QueryAlertRulesNamespaceFilter = None,
        product_category: main_models.QueryAlertRulesProductCategoryFilter = None,
        relation_type: main_models.QueryAlertRulesRelationTypeFilter = None,
        resources: main_models.QueryAlertRulesResourcesFilter = None,
    ):
        # The UModel resource domain filter (exact match).
        self.entity_domain = entity_domain
        # The UModel entity type filter (set inclusion/exclusion).
        self.entity_type = entity_type
        # The CloudMonitor namespace filter (exact match).
        self.namespace = namespace
        # The CloudMonitor product category filter (exact match).
        self.product_category = product_category
        # The relationship type filter (set inclusion/exclusion): ALL/UMODEL_ENTITY/CLOUD_INSTANCE/GROUP_V1/GROUP_V2/TAG.
        self.relation_type = relation_type
        # The resources filter (contains uses OR matching; notContains excludes all).
        self.resources = resources

    def validate(self):
        if self.entity_domain:
            self.entity_domain.validate()
        if self.entity_type:
            self.entity_type.validate()
        if self.namespace:
            self.namespace.validate()
        if self.product_category:
            self.product_category.validate()
        if self.relation_type:
            self.relation_type.validate()
        if self.resources:
            self.resources.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.entity_domain is not None:
            result['entityDomain'] = self.entity_domain.to_map()

        if self.entity_type is not None:
            result['entityType'] = self.entity_type.to_map()

        if self.namespace is not None:
            result['namespace'] = self.namespace.to_map()

        if self.product_category is not None:
            result['productCategory'] = self.product_category.to_map()

        if self.relation_type is not None:
            result['relationType'] = self.relation_type.to_map()

        if self.resources is not None:
            result['resources'] = self.resources.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('entityDomain') is not None:
            temp_model = main_models.QueryAlertRulesEntityDomainFilter()
            self.entity_domain = temp_model.from_map(m.get('entityDomain'))

        if m.get('entityType') is not None:
            temp_model = main_models.QueryAlertRulesEntityTypeFilter()
            self.entity_type = temp_model.from_map(m.get('entityType'))

        if m.get('namespace') is not None:
            temp_model = main_models.QueryAlertRulesNamespaceFilter()
            self.namespace = temp_model.from_map(m.get('namespace'))

        if m.get('productCategory') is not None:
            temp_model = main_models.QueryAlertRulesProductCategoryFilter()
            self.product_category = temp_model.from_map(m.get('productCategory'))

        if m.get('relationType') is not None:
            temp_model = main_models.QueryAlertRulesRelationTypeFilter()
            self.relation_type = temp_model.from_map(m.get('relationType'))

        if m.get('resources') is not None:
            temp_model = main_models.QueryAlertRulesResourcesFilter()
            self.resources = temp_model.from_map(m.get('resources'))

        return self

