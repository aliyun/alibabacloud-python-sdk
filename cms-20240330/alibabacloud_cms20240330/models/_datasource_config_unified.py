# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cms20240330 import models as main_models
from darabonba.model import DaraModel

class DatasourceConfigUnified(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        legacy_raw: str = None,
        legacy_type: str = None,
        namespace: str = None,
        product_category: str = None,
        project: str = None,
        region_id: str = None,
        stores: List[main_models.Stores] = None,
        tenant_id: str = None,
        type: str = None,
    ):
        # The Prometheus instance ID. This field is used when type is PROMETHEUS.
        self.instance_id = instance_id
        # The original V1 datasource JSON string returned as a fallback when type is UNKNOWN and read path parsing fails. The frontend displays this field as read-only when it is not empty.
        self.legacy_raw = legacy_raw
        # The legacy type, which is returned when type is UNKNOWN to indicate that this rule cannot be edited by using the new API. Submit a ticket to contact the CloudMonitor team.
        self.legacy_type = legacy_type
        # The namespace. This field is optional when type is VIRTUAL_PROMETHEUS and identifies the namespace to which the virtual Prometheus instance belongs.
        self.namespace = namespace
        # The cloud service category. This field is optional when type is CLOUD_MONITORING. Outputs unknown when this information is missing from the source.
        self.product_category = product_category
        # The Simple Log Service project name. This field is required when type is SLS, and all stores share the same project.
        self.project = project
        # The region ID. This field is optional for all types and defaults to the rule or gateway region.
        self.region_id = region_id
        # The Simple Log Service store list. This field is used when type is SLS and requires at least one store. Each store includes store and storeType. The project and regionId fields are moved to the top level. The fields with the same names remaining in Stores are deprecated and return 400 in the write path.
        self.stores = stores
        # The tenant ID. This field is optional when type is VIRTUAL_PROMETHEUS and identifies the tenant to which the virtual Prometheus instance belongs.
        self.tenant_id = tenant_id
        # The data source type.
        # 
        # This parameter is required.
        self.type = type

    def validate(self):
        if self.stores:
            for v1 in self.stores:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id

        if self.legacy_raw is not None:
            result['legacyRaw'] = self.legacy_raw

        if self.legacy_type is not None:
            result['legacyType'] = self.legacy_type

        if self.namespace is not None:
            result['namespace'] = self.namespace

        if self.product_category is not None:
            result['productCategory'] = self.product_category

        if self.project is not None:
            result['project'] = self.project

        if self.region_id is not None:
            result['regionId'] = self.region_id

        result['stores'] = []
        if self.stores is not None:
            for k1 in self.stores:
                result['stores'].append(k1.to_map() if k1 else None)

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')

        if m.get('legacyRaw') is not None:
            self.legacy_raw = m.get('legacyRaw')

        if m.get('legacyType') is not None:
            self.legacy_type = m.get('legacyType')

        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')

        if m.get('productCategory') is not None:
            self.product_category = m.get('productCategory')

        if m.get('project') is not None:
            self.project = m.get('project')

        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')

        self.stores = []
        if m.get('stores') is not None:
            for k1 in m.get('stores'):
                temp_model = main_models.Stores()
                self.stores.append(temp_model.from_map(k1))

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

