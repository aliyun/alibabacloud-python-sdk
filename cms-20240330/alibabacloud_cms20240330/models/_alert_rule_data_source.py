# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cms20240330 import models as main_models
from darabonba.model import DaraModel

class AlertRuleDataSource(DaraModel):
    def __init__(
        self,
        app_type: str = None,
        ds_list: List[main_models.AlertRuleDataSourceDsList] = None,
        instance_id: str = None,
        namespace: str = None,
        region_id: str = None,
        tenant_id: str = None,
        type: str = None,
    ):
        # Applicable data source type: APM_DS.
        # Application type: 
        # 
        # - apm.
        self.app_type = app_type
        # Applicable data source type: SLS_MULTI_DS.
        # List of sub-data sources.
        self.ds_list = ds_list
        # Applicable data source type: PROMETHEUS_DS.
        # Prometheus instance ID.
        self.instance_id = instance_id
        # Applicable data source type: ENTERPRISE_DS.
        # Name of the enterprise cloud monitoring metric repository.
        self.namespace = namespace
        # Applicable data source types: APM_DS, PROMETHEUS_DS.
        # The regionId to which the data source belongs.
        self.region_id = region_id
        self.tenant_id = tenant_id
        # Data source type.
        # Valid values:
        # - PROMETHEUS_DS: Prometheus data source.
        # - SLS_MULTI_DS: SLS data source.
        # - APM_DS: Application monitoring data source.
        # - CMS_BASIC_DS: Basic cloud monitoring data source.
        # - ENTERPRISE_DS: Enterprise cloud monitoring data source.
        # 
        # This parameter is required.
        self.type = type

    def validate(self):
        if self.ds_list:
            for v1 in self.ds_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_type is not None:
            result['appType'] = self.app_type

        result['dsList'] = []
        if self.ds_list is not None:
            for k1 in self.ds_list:
                result['dsList'].append(k1.to_map() if k1 else None)

        if self.instance_id is not None:
            result['instanceId'] = self.instance_id

        if self.namespace is not None:
            result['namespace'] = self.namespace

        if self.region_id is not None:
            result['regionId'] = self.region_id

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appType') is not None:
            self.app_type = m.get('appType')

        self.ds_list = []
        if m.get('dsList') is not None:
            for k1 in m.get('dsList'):
                temp_model = main_models.AlertRuleDataSourceDsList()
                self.ds_list.append(temp_model.from_map(k1))

        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')

        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')

        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

class AlertRuleDataSourceDsList(DaraModel):
    def __init__(
        self,
        project: str = None,
        region_id: str = None,
        store: str = None,
        type: str = None,
    ):
        # SLS project
        self.project = project
        # The region where the SLS project is located.
        self.region_id = region_id
        # LogStore/MetricStore name.
        self.store = store
        # Type of SLS data sub-source:
        # 
        # - SLS_LOG_DS: LogStore data source.
        # - SLS_METRIC_DS: MetricStore data source.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.project is not None:
            result['project'] = self.project

        if self.region_id is not None:
            result['regionId'] = self.region_id

        if self.store is not None:
            result['store'] = self.store

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('project') is not None:
            self.project = m.get('project')

        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')

        if m.get('store') is not None:
            self.store = m.get('store')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

