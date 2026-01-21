# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cms20190101 import models as main_models
from darabonba.model import DaraModel

class DescribeMetricRuleBlackListResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        describe_metric_rule_black_list: List[main_models.DescribeMetricRuleBlackListResponseBodyDescribeMetricRuleBlackList] = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        total: int = None,
    ):
        # The categories of the Alibaba Cloud service. For example, ApsaraDB for Redis includes the following categories: ApsaraDB for Redis (standard architecture), ApsaraDB for Redis (cluster architecture), and ApsaraDB for Redis (read/write splitting architecture). In this case, the valid values of this parameter for ApsaraDB for Redis include `kvstore_standard`, `kvstore_sharding`, and `kvstore_splitrw`.
        self.code = code
        # The queried blacklist policies.
        self.describe_metric_rule_black_list = describe_metric_rule_black_list
        # The error message.
        self.message = message
        # The namespace of the cloud service.
        self.request_id = request_id
        # The namespace of the cloud service.
        # 
        # For more information about the namespaces of different cloud services, see [Appendix 1: Metrics](https://help.aliyun.com/document_detail/163515.html).
        self.success = success
        # The timestamp when the blacklist policy was created.
        # 
        # Unit: milliseconds.
        self.total = total

    def validate(self):
        if self.describe_metric_rule_black_list:
            for v1 in self.describe_metric_rule_black_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        result['DescribeMetricRuleBlackList'] = []
        if self.describe_metric_rule_black_list is not None:
            for k1 in self.describe_metric_rule_black_list:
                result['DescribeMetricRuleBlackList'].append(k1.to_map() if k1 else None)

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        self.describe_metric_rule_black_list = []
        if m.get('DescribeMetricRuleBlackList') is not None:
            for k1 in m.get('DescribeMetricRuleBlackList'):
                temp_model = main_models.DescribeMetricRuleBlackListResponseBodyDescribeMetricRuleBlackList()
                self.describe_metric_rule_black_list.append(temp_model.from_map(k1))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class DescribeMetricRuleBlackListResponseBodyDescribeMetricRuleBlackList(DaraModel):
    def __init__(
        self,
        category: str = None,
        create_time: str = None,
        effective_time: str = None,
        enable_end_time: int = None,
        enable_start_time: int = None,
        id: str = None,
        instances: List[str] = None,
        is_enable: bool = None,
        metrics: List[main_models.DescribeMetricRuleBlackListResponseBodyDescribeMetricRuleBlackListMetrics] = None,
        name: str = None,
        namespace: str = None,
        scope_type: str = None,
        scope_value: List[str] = None,
        update_time: str = None,
    ):
        # The category of the cloud service. For example, ApsaraDB for Redis includes the following categories: ApsaraDB for Redis (standard architecture), ApsaraDB for Redis (cluster architecture), and ApsaraDB for Redis (read/write splitting architecture). In this case, the valid values of this parameter for ApsaraDB for Redis include `kvstore_standard`, `kvstore_sharding`, and `kvstore_splitrw`.
        self.category = category
        # The timestamp when the blacklist policy was created.
        # 
        # Unit: milliseconds.
        self.create_time = create_time
        # The time range within which the blacklist policy is effective.
        self.effective_time = effective_time
        # The timestamp when the blacklist policy started to take effect.
        # 
        # Unit: milliseconds.
        self.enable_end_time = enable_end_time
        # The timestamp when the blacklist policy expired.
        # 
        # Unit: milliseconds.
        self.enable_start_time = enable_start_time
        # The ID of the blacklist policy.
        self.id = id
        # The IDs of the instances that belong to the specified cloud service.
        self.instances = instances
        # The status of the blacklist policy. Valid values:
        # 
        # *   true: The blacklist policy is enabled.
        # *   false: The blacklist policy is disabled.
        self.is_enable = is_enable
        # The metrics of the instance.
        self.metrics = metrics
        # The name of the blacklist policy.
        self.name = name
        # The namespace of the cloud service.
        self.namespace = namespace
        # The effective scope of the blacklist policy. Valid values:
        # 
        # *   USER: The blacklist policy takes effect only within the current Alibaba Cloud account.
        # *   GROUP: The blacklist policy takes effect only within the specified application group.
        self.scope_type = scope_type
        # The IDs of the application groups.
        self.scope_value = scope_value
        # The timestamp when the blacklist policy was modified.
        # 
        # Unit: milliseconds.
        self.update_time = update_time

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

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

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

        if self.is_enable is not None:
            result['IsEnable'] = self.is_enable

        result['Metrics'] = []
        if self.metrics is not None:
            for k1 in self.metrics:
                result['Metrics'].append(k1.to_map() if k1 else None)

        if self.name is not None:
            result['Name'] = self.name

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        if self.scope_type is not None:
            result['ScopeType'] = self.scope_type

        if self.scope_value is not None:
            result['ScopeValue'] = self.scope_value

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

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

        if m.get('IsEnable') is not None:
            self.is_enable = m.get('IsEnable')

        self.metrics = []
        if m.get('Metrics') is not None:
            for k1 in m.get('Metrics'):
                temp_model = main_models.DescribeMetricRuleBlackListResponseBodyDescribeMetricRuleBlackListMetrics()
                self.metrics.append(temp_model.from_map(k1))

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        if m.get('ScopeType') is not None:
            self.scope_type = m.get('ScopeType')

        if m.get('ScopeValue') is not None:
            self.scope_value = m.get('ScopeValue')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

class DescribeMetricRuleBlackListResponseBodyDescribeMetricRuleBlackListMetrics(DaraModel):
    def __init__(
        self,
        metric_name: str = None,
        resource: str = None,
    ):
        # The metric name.
        self.metric_name = metric_name
        # The extended dimension of the instance. For example, `{"device":"C:"}` specifies that the blacklist policy is applied to all C disks of the specified Elastic Compute Service (ECS) instance.
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

