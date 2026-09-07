# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_arms20190808 import models as main_models
from darabonba.model import DaraModel

class CreateOrUpdateAlertRuleResponseBody(DaraModel):
    def __init__(
        self,
        alert_rule: main_models.CreateOrUpdateAlertRuleResponseBodyAlertRule = None,
        request_id: str = None,
    ):
        # The alert rule object.
        self.alert_rule = alert_rule
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.alert_rule:
            self.alert_rule.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alert_rule is not None:
            result['AlertRule'] = self.alert_rule.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlertRule') is not None:
            temp_model = main_models.CreateOrUpdateAlertRuleResponseBodyAlertRule()
            self.alert_rule = temp_model.from_map(m.get('AlertRule'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class CreateOrUpdateAlertRuleResponseBodyAlertRule(DaraModel):
    def __init__(
        self,
        alert_check_type: str = None,
        alert_group: int = None,
        alert_id: int = None,
        alert_name: str = None,
        alert_rule_content: main_models.CreateOrUpdateAlertRuleResponseBodyAlertRuleAlertRuleContent = None,
        alert_status: str = None,
        alert_type: str = None,
        annotations: List[main_models.CreateOrUpdateAlertRuleResponseBodyAlertRuleAnnotations] = None,
        auto_add_new_application: bool = None,
        cluster_id: str = None,
        created_time: int = None,
        duration: str = None,
        extend: str = None,
        filters: main_models.CreateOrUpdateAlertRuleResponseBodyAlertRuleFilters = None,
        labels: List[main_models.CreateOrUpdateAlertRuleResponseBodyAlertRuleLabels] = None,
        level: str = None,
        message: str = None,
        metrics_type: str = None,
        notify_mode: str = None,
        notify_strategy: str = None,
        pids: List[str] = None,
        prom_ql: str = None,
        region_id: str = None,
        tags: List[main_models.CreateOrUpdateAlertRuleResponseBodyAlertRuleTags] = None,
        updated_time: int = None,
        user_id: str = None,
    ):
        # The check type of the Prometheus alert rule.
        # 
        # - `STATIC`: The alert is triggered based on a static threshold.
        # 
        # - `CUSTOM`: The alert is triggered based on a custom PromQL expression.
        self.alert_check_type = alert_check_type
        # The alert group for the Prometheus alert rule.
        # 
        # - `-1`: Custom PromQL
        # 
        # - `1`: Kubernetes Workloads
        # 
        # - `15`: Kubernetes Nodes
        self.alert_group = alert_group
        # The ID of the alert rule.
        self.alert_id = alert_id
        # The name of the alert rule.
        self.alert_name = alert_name
        # The content of the alert rule. This applies to application monitoring and browser monitoring.
        self.alert_rule_content = alert_rule_content
        # The status of the alert rule.
        # 
        # - `RUNNING`: The alert rule is running.
        # 
        # - `STOPPED`: The alert rule is stopped.
        # 
        # - `PAUSED`: The alert rule is paused.
        # 
        # > The `PAUSED` status indicates that the system has automatically suspended the alert rule due to an abnormality. This can happen if the alert rule generates too many distinct time series or its associated cluster is deleted.
        self.alert_status = alert_status
        # The type of the alert rule. Valid values:
        # 
        # - `APPLICATION_MONITORING_ALERT_RULE`: an alert rule for application monitoring.
        # 
        # - `BROWSER_MONITORING_ALERT_RULE`: an alert rule for browser monitoring.
        # 
        # - `PROMETHEUS_MONITORING_ALERT_RULE`: an alert rule for Prometheus monitoring.
        self.alert_type = alert_type
        # The annotations of the Prometheus alert rule.
        self.annotations = annotations
        # Indicates whether newly created applications are automatically added to the alert rule. This applies to application monitoring and browser monitoring rules.
        # 
        # - `true`: Enabled
        # 
        # - `false`: Disabled
        self.auto_add_new_application = auto_add_new_application
        # The ID of the cluster that is associated with the Prometheus alert rule.
        self.cluster_id = cluster_id
        # The UNIX timestamp, in milliseconds, when the alert rule was created.
        self.created_time = created_time
        # The duration, in minutes, for which a condition must be true before an alert is triggered. This applies only to Prometheus alert rules.
        self.duration = duration
        # The extended fields, returned as a JSON string.
        self.extend = extend
        # The filters of the alert rule. This applies to application monitoring or browser monitoring.
        self.filters = filters
        # The labels of the Prometheus alert rule.
        self.labels = labels
        # The severity level of the Prometheus alert rule.
        # 
        # - `P1`: Critical. Indicates major issues that affect core business availability and can have severe consequences.
        # 
        # - `P2`: Warning. Indicates issues that impact system availability but have a limited scope.
        # 
        # - `P3`: Info. Indicates potential issues or alerts from less critical services.
        # 
        # - `P4`: Low priority. Indicates informational alerts that do not affect services.
        # 
        # - `Default`: The default level used when no specific severity is required.
        self.level = level
        # The message of the Prometheus alert rule.
        self.message = message
        # The metric type of the alert rule. This applies to application monitoring and browser monitoring.
        self.metrics_type = metrics_type
        # The notification mode.
        self.notify_mode = notify_mode
        # The notification policy.
        self.notify_strategy = notify_strategy
        # The PIDs of the applications associated with the alert rule. This applies to application monitoring and browser monitoring rules.
        self.pids = pids
        # The PromQL expression for the Prometheus alert rule.
        self.prom_ql = prom_ql
        # The region ID.
        self.region_id = region_id
        # The tags that are added to the alert rule.
        self.tags = tags
        # The UNIX timestamp, in milliseconds, when the alert rule was last updated.
        self.updated_time = updated_time
        # The user ID.
        self.user_id = user_id

    def validate(self):
        if self.alert_rule_content:
            self.alert_rule_content.validate()
        if self.annotations:
            for v1 in self.annotations:
                 if v1:
                    v1.validate()
        if self.filters:
            self.filters.validate()
        if self.labels:
            for v1 in self.labels:
                 if v1:
                    v1.validate()
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alert_check_type is not None:
            result['AlertCheckType'] = self.alert_check_type

        if self.alert_group is not None:
            result['AlertGroup'] = self.alert_group

        if self.alert_id is not None:
            result['AlertId'] = self.alert_id

        if self.alert_name is not None:
            result['AlertName'] = self.alert_name

        if self.alert_rule_content is not None:
            result['AlertRuleContent'] = self.alert_rule_content.to_map()

        if self.alert_status is not None:
            result['AlertStatus'] = self.alert_status

        if self.alert_type is not None:
            result['AlertType'] = self.alert_type

        result['Annotations'] = []
        if self.annotations is not None:
            for k1 in self.annotations:
                result['Annotations'].append(k1.to_map() if k1 else None)

        if self.auto_add_new_application is not None:
            result['AutoAddNewApplication'] = self.auto_add_new_application

        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.created_time is not None:
            result['CreatedTime'] = self.created_time

        if self.duration is not None:
            result['Duration'] = self.duration

        if self.extend is not None:
            result['Extend'] = self.extend

        if self.filters is not None:
            result['Filters'] = self.filters.to_map()

        result['Labels'] = []
        if self.labels is not None:
            for k1 in self.labels:
                result['Labels'].append(k1.to_map() if k1 else None)

        if self.level is not None:
            result['Level'] = self.level

        if self.message is not None:
            result['Message'] = self.message

        if self.metrics_type is not None:
            result['MetricsType'] = self.metrics_type

        if self.notify_mode is not None:
            result['NotifyMode'] = self.notify_mode

        if self.notify_strategy is not None:
            result['NotifyStrategy'] = self.notify_strategy

        if self.pids is not None:
            result['Pids'] = self.pids

        if self.prom_ql is not None:
            result['PromQL'] = self.prom_ql

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        if self.updated_time is not None:
            result['UpdatedTime'] = self.updated_time

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlertCheckType') is not None:
            self.alert_check_type = m.get('AlertCheckType')

        if m.get('AlertGroup') is not None:
            self.alert_group = m.get('AlertGroup')

        if m.get('AlertId') is not None:
            self.alert_id = m.get('AlertId')

        if m.get('AlertName') is not None:
            self.alert_name = m.get('AlertName')

        if m.get('AlertRuleContent') is not None:
            temp_model = main_models.CreateOrUpdateAlertRuleResponseBodyAlertRuleAlertRuleContent()
            self.alert_rule_content = temp_model.from_map(m.get('AlertRuleContent'))

        if m.get('AlertStatus') is not None:
            self.alert_status = m.get('AlertStatus')

        if m.get('AlertType') is not None:
            self.alert_type = m.get('AlertType')

        self.annotations = []
        if m.get('Annotations') is not None:
            for k1 in m.get('Annotations'):
                temp_model = main_models.CreateOrUpdateAlertRuleResponseBodyAlertRuleAnnotations()
                self.annotations.append(temp_model.from_map(k1))

        if m.get('AutoAddNewApplication') is not None:
            self.auto_add_new_application = m.get('AutoAddNewApplication')

        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')

        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        if m.get('Extend') is not None:
            self.extend = m.get('Extend')

        if m.get('Filters') is not None:
            temp_model = main_models.CreateOrUpdateAlertRuleResponseBodyAlertRuleFilters()
            self.filters = temp_model.from_map(m.get('Filters'))

        self.labels = []
        if m.get('Labels') is not None:
            for k1 in m.get('Labels'):
                temp_model = main_models.CreateOrUpdateAlertRuleResponseBodyAlertRuleLabels()
                self.labels.append(temp_model.from_map(k1))

        if m.get('Level') is not None:
            self.level = m.get('Level')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('MetricsType') is not None:
            self.metrics_type = m.get('MetricsType')

        if m.get('NotifyMode') is not None:
            self.notify_mode = m.get('NotifyMode')

        if m.get('NotifyStrategy') is not None:
            self.notify_strategy = m.get('NotifyStrategy')

        if m.get('Pids') is not None:
            self.pids = m.get('Pids')

        if m.get('PromQL') is not None:
            self.prom_ql = m.get('PromQL')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.CreateOrUpdateAlertRuleResponseBodyAlertRuleTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('UpdatedTime') is not None:
            self.updated_time = m.get('UpdatedTime')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

class CreateOrUpdateAlertRuleResponseBodyAlertRuleTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key.
        self.key = key
        # The tag value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class CreateOrUpdateAlertRuleResponseBodyAlertRuleLabels(DaraModel):
    def __init__(
        self,
        name: str = None,
        value: str = None,
    ):
        # The label key.
        self.name = name
        # The label value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class CreateOrUpdateAlertRuleResponseBodyAlertRuleFilters(DaraModel):
    def __init__(
        self,
        custom_slsfilters: List[main_models.CreateOrUpdateAlertRuleResponseBodyAlertRuleFiltersCustomSLSFilters] = None,
        custom_slsgroup_by_dimensions: List[str] = None,
        custom_slswheres: List[str] = None,
        dim_filters: List[main_models.CreateOrUpdateAlertRuleResponseBodyAlertRuleFiltersDimFilters] = None,
    ):
        # The custom filter conditions for the browser monitoring alert rule.
        self.custom_slsfilters = custom_slsfilters
        # The aggregation dimensions.
        self.custom_slsgroup_by_dimensions = custom_slsgroup_by_dimensions
        # The configured filter conditions.
        self.custom_slswheres = custom_slswheres
        # The filter conditions of the alert rule. This applies to application monitoring or browser monitoring.
        self.dim_filters = dim_filters

    def validate(self):
        if self.custom_slsfilters:
            for v1 in self.custom_slsfilters:
                 if v1:
                    v1.validate()
        if self.dim_filters:
            for v1 in self.dim_filters:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['CustomSLSFilters'] = []
        if self.custom_slsfilters is not None:
            for k1 in self.custom_slsfilters:
                result['CustomSLSFilters'].append(k1.to_map() if k1 else None)

        if self.custom_slsgroup_by_dimensions is not None:
            result['CustomSLSGroupByDimensions'] = self.custom_slsgroup_by_dimensions

        if self.custom_slswheres is not None:
            result['CustomSLSWheres'] = self.custom_slswheres

        result['DimFilters'] = []
        if self.dim_filters is not None:
            for k1 in self.dim_filters:
                result['DimFilters'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.custom_slsfilters = []
        if m.get('CustomSLSFilters') is not None:
            for k1 in m.get('CustomSLSFilters'):
                temp_model = main_models.CreateOrUpdateAlertRuleResponseBodyAlertRuleFiltersCustomSLSFilters()
                self.custom_slsfilters.append(temp_model.from_map(k1))

        if m.get('CustomSLSGroupByDimensions') is not None:
            self.custom_slsgroup_by_dimensions = m.get('CustomSLSGroupByDimensions')

        if m.get('CustomSLSWheres') is not None:
            self.custom_slswheres = m.get('CustomSLSWheres')

        self.dim_filters = []
        if m.get('DimFilters') is not None:
            for k1 in m.get('DimFilters'):
                temp_model = main_models.CreateOrUpdateAlertRuleResponseBodyAlertRuleFiltersDimFilters()
                self.dim_filters.append(temp_model.from_map(k1))

        return self

class CreateOrUpdateAlertRuleResponseBodyAlertRuleFiltersDimFilters(DaraModel):
    def __init__(
        self,
        filter_key: str = None,
        filter_opt: str = None,
        filter_values: List[str] = None,
    ):
        # The key of the filter condition.
        self.filter_key = filter_key
        # The operator for the filter condition.
        self.filter_opt = filter_opt
        # The values for the filter condition.
        self.filter_values = filter_values

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.filter_key is not None:
            result['FilterKey'] = self.filter_key

        if self.filter_opt is not None:
            result['FilterOpt'] = self.filter_opt

        if self.filter_values is not None:
            result['FilterValues'] = self.filter_values

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FilterKey') is not None:
            self.filter_key = m.get('FilterKey')

        if m.get('FilterOpt') is not None:
            self.filter_opt = m.get('FilterOpt')

        if m.get('FilterValues') is not None:
            self.filter_values = m.get('FilterValues')

        return self

class CreateOrUpdateAlertRuleResponseBodyAlertRuleFiltersCustomSLSFilters(DaraModel):
    def __init__(
        self,
        key: str = None,
        opt: str = None,
        show: bool = None,
        t: str = None,
        value: str = None,
    ):
        # The key of the filter condition.
        self.key = key
        # The operator for the filter condition.
        # 
        # - `=`: equals
        # 
        # - `not`: not equal to
        self.opt = opt
        # Indicates whether the filter condition is displayed on the console.
        self.show = show
        # Used exclusively to distinguish between log types in browser monitoring. This parameter does not apply to other filter conditions.
        self.t = t
        # The value for the filter condition.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.opt is not None:
            result['Opt'] = self.opt

        if self.show is not None:
            result['Show'] = self.show

        if self.t is not None:
            result['T'] = self.t

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Opt') is not None:
            self.opt = m.get('Opt')

        if m.get('Show') is not None:
            self.show = m.get('Show')

        if m.get('T') is not None:
            self.t = m.get('T')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class CreateOrUpdateAlertRuleResponseBodyAlertRuleAnnotations(DaraModel):
    def __init__(
        self,
        name: str = None,
        value: str = None,
    ):
        # The annotation key.
        self.name = name
        # The annotation value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class CreateOrUpdateAlertRuleResponseBodyAlertRuleAlertRuleContent(DaraModel):
    def __init__(
        self,
        alert_rule_items: List[main_models.CreateOrUpdateAlertRuleResponseBodyAlertRuleAlertRuleContentAlertRuleItems] = None,
        condition: str = None,
    ):
        # The alert conditions. This applies to application monitoring and browser monitoring alert rules.
        self.alert_rule_items = alert_rule_items
        # The logical operator for combining multiple alert conditions. This applies to application monitoring and browser monitoring.
        # 
        # - `OR`: The alert is triggered if any condition is met.
        # 
        # - `AND`: The alert is triggered only if all conditions are met.
        self.condition = condition

    def validate(self):
        if self.alert_rule_items:
            for v1 in self.alert_rule_items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AlertRuleItems'] = []
        if self.alert_rule_items is not None:
            for k1 in self.alert_rule_items:
                result['AlertRuleItems'].append(k1.to_map() if k1 else None)

        if self.condition is not None:
            result['Condition'] = self.condition

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.alert_rule_items = []
        if m.get('AlertRuleItems') is not None:
            for k1 in m.get('AlertRuleItems'):
                temp_model = main_models.CreateOrUpdateAlertRuleResponseBodyAlertRuleAlertRuleContentAlertRuleItems()
                self.alert_rule_items.append(temp_model.from_map(k1))

        if m.get('Condition') is not None:
            self.condition = m.get('Condition')

        return self

class CreateOrUpdateAlertRuleResponseBodyAlertRuleAlertRuleContentAlertRuleItems(DaraModel):
    def __init__(
        self,
        aggregate: str = None,
        metric_key: str = None,
        n: float = None,
        operator: str = None,
        value: str = None,
    ):
        # The aggregation method for the alert condition.
        # 
        # - `AVG`: average
        # 
        # - `SUM`: sum
        # 
        # - `MAX`: maximum
        # 
        # - `MIN`: minimum
        self.aggregate = aggregate
        # The metric that is evaluated by the alert condition.
        self.metric_key = metric_key
        # The duration of the time window, in minutes, for evaluating the alert condition.
        self.n = n
        # The operator used to compare the aggregated metric value with the threshold.
        # 
        # - `CURRENT_GTE`: greater than or equal to
        # 
        # - `CURRENT_LTE`: less than or equal to
        # 
        # - `PREVIOUS_UP`: period-over-period increase percentage
        # 
        # - `PREVIOUS_DOWN`: period-over-period decrease percentage
        # 
        # - `HOH_UP`: hour-over-hour increase percentage
        # 
        # - `HOH_DOWN`: hour-over-hour decrease percentage
        # 
        # - `DOD_UP`: day-over-day increase percentage
        # 
        # - `DOD_DOWN`: day-over-day decrease percentage
        self.operator = operator
        # The threshold for the alert condition.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.aggregate is not None:
            result['Aggregate'] = self.aggregate

        if self.metric_key is not None:
            result['MetricKey'] = self.metric_key

        if self.n is not None:
            result['N'] = self.n

        if self.operator is not None:
            result['Operator'] = self.operator

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Aggregate') is not None:
            self.aggregate = m.get('Aggregate')

        if m.get('MetricKey') is not None:
            self.metric_key = m.get('MetricKey')

        if m.get('N') is not None:
            self.n = m.get('N')

        if m.get('Operator') is not None:
            self.operator = m.get('Operator')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

