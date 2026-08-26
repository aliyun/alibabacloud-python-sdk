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
        # The Prometheus instance ID. Required when type is PROMETHEUS or VIRTUAL_PROMETHEUS. Ignored for other types.
        self.instance_id = instance_id
        # The raw V1 datasource JSON string returned as a fallback when type is UNKNOWN and read-path parsing fails. When the frontend detects that this field is not empty, display it as read-only.
        self.legacy_raw = legacy_raw
        # Returned when type is UNKNOWN. Indicates that this rule cannot be edited through the new API. Submit a ticket to contact the CloudMonitor team.
        self.legacy_type = legacy_type
        # The namespace. Optional when type is VIRTUAL_PROMETHEUS. Identifies the namespace to which the virtual Prometheus instance belongs.
        self.namespace = namespace
        # The Alibaba Cloud service category. Optional when type is CLOUD_MONITORING. Returns unknown when the source lacks this information.
        self.product_category = product_category
        # The Simple Log Service (SLS) project name. Required when type is SLS. All stores share the same project.
        self.project = project
        # The region ID. Optional for PROMETHEUS, VIRTUAL_PROMETHEUS, UMODEL, APM, XTRACE, EBPF, RUM, and SLS types. Defaults to the region of the rule or gateway. Not used for CLOUD_MONITORING. Use AlertRuleV2.regionId instead for CLOUD_MONITORING.
        self.region_id = region_id
        # The list of SLS stores. Used when type is SLS. At least one store is required. Each store contains store and storeType fields. The project and regionId fields have been moved to the top level. The deprecated fields with the same names that remain in stores return a 400 error if used in write paths.
        self.stores = stores
        # The tenant ID. Optional when type is VIRTUAL_PROMETHEUS. Identifies the tenant to which the virtual Prometheus instance belongs.
        self.tenant_id = tenant_id
        # The data source type. Valid values and associated fields: PROMETHEUS (instanceId required; regionId optional). VIRTUAL_PROMETHEUS (instanceId required; regionId, namespace, and tenantId optional). UMODEL (regionId optional; other fields are carried in queryConfig/conditionConfig). APM (regionId optional). XTRACE (regionId optional). EBPF (regionId optional). RUM (regionId optional). CLOUD_MONITORING (regionId and productCategory optional). SLS (project and stores required). UNKNOWN (read-only fallback; do not use in write paths). Non-enumerated values (such as CMS_BASIC_DS/SLS_DS) are prohibited and the backend returns an Invalidtype 400 error.
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

