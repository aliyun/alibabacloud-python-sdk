# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cms20190101 import models as main_models
from darabonba.model import DaraModel

class ModifyMetricRuleBlackListRequest(DaraModel):
    def __init__(
        self,
        category: str = None,
        effective_time: str = None,
        enable_end_time: str = None,
        enable_start_time: str = None,
        id: str = None,
        instances: List[str] = None,
        metrics: List[main_models.ModifyMetricRuleBlackListRequestMetrics] = None,
        name: str = None,
        namespace: str = None,
        region_id: str = None,
        scope_type: str = None,
        scope_value: str = None,
    ):
        # The category of the Alibaba Cloud service. For example, Redis has categories such as `kvstore_standard` (Standard Edition), `kvstore_sharding` (Cluster Edition), and `kvstore_splitrw` (Read/Write Splitting Edition).
        # 
        # This parameter is required.
        self.category = category
        # The effective period of the alert blacklist policy. The implications of the settings for this parameter are as follows:
        # 
        # - If you do not configure the settings for this parameter, the alert blacklist policy is permanently valid.
        # 
        # - If you configure the settings for this parameter, the blacklist policy is valid only within the specified time range. The following examples show two formats for this parameter:
        #     - `03:00-04:59`: The alert blacklist policy is valid from 03:00 to 05:00 (excluding 05:00) local time.
        #     - `03:00-04:59 UTC+0700`: The alert blacklist policy is valid from 03:00 to 05:00 (excluding 05:00) UTC+7.
        self.effective_time = effective_time
        # The end timestamp of the effective period for the alert blacklist policy.
        # 
        # Unit: milliseconds.
        self.enable_end_time = enable_end_time
        # The start timestamp of the effective period for the alert blacklist policy.
        # 
        # Unit: milliseconds.
        self.enable_start_time = enable_start_time
        # The ID of the alert blacklist policy.
        # 
        # For more information about how to obtain the ID of an alert blacklist policy, see [DescribeMetricRuleBlackList](https://help.aliyun.com/document_detail/457257.html).
        # 
        # This parameter is required.
        self.id = id
        # The list of instances of the specified Alibaba Cloud service in the alert blacklist policy.
        # 
        # This parameter is required.
        self.instances = instances
        # The monitoring metrics of the instances.
        # 
        # - If you do not configure the settings for this parameter, the alert blacklist policy applies to all monitoring metrics of the specified Alibaba Cloud service.
        # 
        # - If you configure the settings for this parameter, the blacklist policy applies only to the current monitoring metrics.
        self.metrics = metrics
        # The name of the alert blacklist policy.
        # 
        # This parameter is required.
        self.name = name
        # The data namespace of the cloud service.
        # 
        # For more information about the namespaces of cloud services, see [Cloud service monitoring metrics](https://help.aliyun.com/document_detail/163515.html).
        # 
        # This parameter is required.
        self.namespace = namespace
        self.region_id = region_id
        # The effective scope of the alert blacklist policy. Valid values:
        # 
        # - USER: The alert blacklist policy takes effect only within the current Alibaba Cloud account.
        # 
        # - GROUP (default): The alert blacklist policy takes effect within the specified application group. You must specify an application group.
        #   For more information about how to obtain the ID of an application group, see [DescribeMonitorGroups](https://help.aliyun.com/document_detail/115032.html).
        self.scope_type = scope_type
        # The list of application group IDs.
        # 
        # > This parameter is required only when `ScopeType` is set to `GROUP`.
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

        if self.id is not None:
            result['Id'] = self.id

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

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Instances') is not None:
            self.instances = m.get('Instances')

        self.metrics = []
        if m.get('Metrics') is not None:
            for k1 in m.get('Metrics'):
                temp_model = main_models.ModifyMetricRuleBlackListRequestMetrics()
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

class ModifyMetricRuleBlackListRequestMetrics(DaraModel):
    def __init__(
        self,
        metric_name: str = None,
        resource: str = None,
    ):
        # The name of the monitoring metrics.
        # 
        # Valid values of N: 1 to 10.
        # 
        # This parameter is required.
        self.metric_name = metric_name
        # The extended dimension information of the instance. For example, `{"device":"C:"}` indicates that the blacklist policy applies to all C drives of the ECS instance of the Alibaba Cloud service.
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

