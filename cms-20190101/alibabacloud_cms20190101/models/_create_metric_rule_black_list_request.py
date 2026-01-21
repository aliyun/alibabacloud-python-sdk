# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cms20190101 import models as main_models
from darabonba.model import DaraModel

class CreateMetricRuleBlackListRequest(DaraModel):
    def __init__(
        self,
        category: str = None,
        effective_time: str = None,
        enable_end_time: str = None,
        enable_start_time: str = None,
        instances: List[str] = None,
        metrics: List[main_models.CreateMetricRuleBlackListRequestMetrics] = None,
        name: str = None,
        namespace: str = None,
        region_id: str = None,
        scope_type: str = None,
        scope_value: str = None,
    ):
        # The category of the cloud service. For example, ApsaraDB for Redis includes the following categories: ApsaraDB for Redis (standard architecture), ApsaraDB for Redis (cluster architecture), and ApsaraDB for Redis (read/write splitting architecture). In this case, the valid values of this parameter for ApsaraDB for Redis include `kvstore_standard`, `kvstore_sharding`, and `kvstore_splitrw`.
        # 
        # This parameter is required.
        self.category = category
        # The time range within which the blacklist policy is effective.
        # 
        # *   If you do not configure this parameter, the blacklist policy is permanently effective.
        # 
        # *   If you configure this parameter, the blacklist policy is effective only within the specified time range. Examples:
        # 
        #     *   `03:00-04:59`: The blacklist policy is effective from 03:00 to 05:00 local time. 05:00 local time is excluded.
        #     *   `03:00-04:59 UTC+0700`: The blacklist policy is effective from 03:00 to 05:00 (UTC+7). 05:00 (UTC+7) is excluded.
        self.effective_time = effective_time
        # The timestamp when the blacklist policy expires.
        # 
        # Unit: milliseconds.
        self.enable_end_time = enable_end_time
        # The timestamp when the blacklist policy starts to take effect.
        # 
        # Unit: milliseconds.
        self.enable_start_time = enable_start_time
        # The IDs of the instances that belong to the specified cloud service.
        # 
        # This parameter is required.
        self.instances = instances
        # The metrics of the instance.
        # 
        # *   If you do not configure this parameter, the blacklist policy applies to all metrics of the specified cloud service.
        # *   If you configure this parameter, the blacklist policy applies only to the current metric.
        self.metrics = metrics
        # The name of the blacklist policy.
        # 
        # This parameter is required.
        self.name = name
        # The namespace of the cloud service.
        # 
        # For more information about the namespaces of different cloud services, see [Appendix 1: Metrics](https://help.aliyun.com/document_detail/163515.html).
        # 
        # This parameter is required.
        self.namespace = namespace
        self.region_id = region_id
        # The effective scope of the blacklist policy. Valid values:
        # 
        # *   USER (default): The blacklist policy takes effect only for the current Alibaba Cloud account.
        # *   GROUP: The blacklist policy takes effect only for the specified application group. For information about how to query the IDs of application groups, see [DescribeMonitorGroups](https://help.aliyun.com/document_detail/115032.html).
        self.scope_type = scope_type
        # The ID of the application group. The value of this parameter is a JSON array.
        # 
        # > This parameter must be specified when `ScopeType` is set to `GROUP`.
        self.scope_value = scope_value

    def validate(self):
        if self.metrics:
            for v1 in self.metrics:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category is not None:
            result['Category'] = self.category

        if self.effective_time is not None:
            result['EffectiveTime'] = self.effective_time

        if self.enable_end_time is not None:
            result['EnableEndTime'] = self.enable_end_time

        if self.enable_start_time is not None:
            result['EnableStartTime'] = self.enable_start_time

        if self.instances is not None:
            result['Instances'] = self.instances

        result['Metrics'] = []
        if self.metrics is not None:
            for k1 in self.metrics:
                result['Metrics'].append(k1.to_map() if k1 else None)

        if self.name is not None:
            result['Name'] = self.name

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.scope_type is not None:
            result['ScopeType'] = self.scope_type

        if self.scope_value is not None:
            result['ScopeValue'] = self.scope_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('EffectiveTime') is not None:
            self.effective_time = m.get('EffectiveTime')

        if m.get('EnableEndTime') is not None:
            self.enable_end_time = m.get('EnableEndTime')

        if m.get('EnableStartTime') is not None:
            self.enable_start_time = m.get('EnableStartTime')

        if m.get('Instances') is not None:
            self.instances = m.get('Instances')

        self.metrics = []
        if m.get('Metrics') is not None:
            for k1 in m.get('Metrics'):
                temp_model = main_models.CreateMetricRuleBlackListRequestMetrics()
                self.metrics.append(temp_model.from_map(k1))

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ScopeType') is not None:
            self.scope_type = m.get('ScopeType')

        if m.get('ScopeValue') is not None:
            self.scope_value = m.get('ScopeValue')

        return self

class CreateMetricRuleBlackListRequestMetrics(DaraModel):
    def __init__(
        self,
        metric_name: str = None,
        resource: str = None,
    ):
        # The metric name.
        # 
        # Valid values of N: 1 to 10.
        # 
        # This parameter is required.
        self.metric_name = metric_name
        # The extended dimension of the instance. For example, `{"device":"C:"}` specifies that the blacklist policy is applied to all C disks of the specified Elastic Compute Service (ECS) instance.
        # 
        # Valid values of N: 1 to 10.
        self.resource = resource

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.metric_name is not None:
            result['MetricName'] = self.metric_name

        if self.resource is not None:
            result['Resource'] = self.resource

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MetricName') is not None:
            self.metric_name = m.get('MetricName')

        if m.get('Resource') is not None:
            self.resource = m.get('Resource')

        return self

