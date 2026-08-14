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
        product_category: str = None,
        project: str = None,
        region_id: str = None,
        stores: List[main_models.Stores] = None,
        type: str = None,
    ):
        # The Prometheus instance ID (required when type=PROMETHEUS; ignored for other types).
        self.instance_id = instance_id
        # The original V1 datasource JSON string returned as a fallback when type=UNKNOWN and the read path fails to parse the datasource. If the frontend detects that this field is not empty, display it as read-only.
        self.legacy_raw = legacy_raw
        # Returned when type=UNKNOWN, indicating that this rule cannot be edited through the new API. Submit a ticket to contact the CloudMonitor team.
        self.legacy_type = legacy_type
        # The Alibaba Cloud service category (optional when type=CLOUD_MONITORING). If the source does not contain this information, the value unknown is returned.
        self.product_category = product_category
        # The Simple Log Service project name (required when type=SLS; all stores share the same project).
        self.project = project
        # The region ID (optional for PROMETHEUS / UMODEL / APM / SLS types; defaults to the same region as the rule or gateway. CLOUD_MONITORING does not use this field; use AlertRuleV2.regionId instead).
        self.region_id = region_id
        # The list of Simple Log Service stores (used when type=SLS; at least one store is required). Each store contains store and storeType fields. The project and regionId fields have been moved to the top level. The deprecated fields with the same names that remain in stores cause a 400 error if used in write paths.
        self.stores = stores
        # The datasource type. Valid values: PROMETHEUS (instanceId is required; regionId is optional). UMODEL (regionId is optional; other settings are carried in queryConfig/conditionConfig). APM (regionId is optional). CLOUD_MONITORING (regionId and productCategory are optional). UNKNOWN (read-only fallback; do not use in write paths). Do not use non-enumerated values (such as CMS_BASIC_DS or SLS_DS). The backend returns an Invalidtype 400 error.
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

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

