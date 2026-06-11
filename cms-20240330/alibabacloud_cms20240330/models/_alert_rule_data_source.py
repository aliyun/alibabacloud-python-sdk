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
        # Applies to the APM_DS data source type.
        # 
        # The type of the application. Valid value:
        # 
        # - apm
        self.app_type = app_type
        # Applies to the SLS_MULTI_DS data source type.
        # 
        # A list of sub-data sources.
        self.ds_list = ds_list
        # Applies to the PROMETHEUS_DS data source type.
        # 
        # The ID of the Prometheus instance.
        self.instance_id = instance_id
        # Applies to the ENTERPRISE_DS data source type.
        # 
        # The name of the Hybrid Cloud Monitoring metric repository.
        self.namespace = namespace
        # Applies to the APM_DS and PROMETHEUS_DS data source types.
        # 
        # The ID of the region where the data source is located.
        self.region_id = region_id
        self.tenant_id = tenant_id
        # The data source type.
        # 
        # Valid values:
        # 
        # - PROMETHEUS_DS: A Prometheus data source.
        # 
        # - SLS_MULTI_DS: An SLS data source.
        # 
        # - APM_DS: An Application Monitoring data source.
        # 
        # - CMS_BASIC_DS: A basic Cloud Monitor data source.
        # 
        # - ENTERPRISE_DS: A Hybrid Cloud Monitoring data source.
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
        # The SLS project.
        self.project = project
        # The region where the SLS project is located.
        self.region_id = region_id
        # The name of the LogStore or MetricStore.
        self.store = store
        # The type of the SLS sub-data source. Valid values:
        # 
        # - SLS_LOG_DS: A LogStore data source.
        # 
        # - SLS_METRIC_DS: A MetricStore data source.
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

