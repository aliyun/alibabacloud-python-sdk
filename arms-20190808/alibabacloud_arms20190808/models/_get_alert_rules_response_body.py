# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_arms20190808 import models as main_models
from darabonba.model import DaraModel

class GetAlertRulesResponseBody(DaraModel):
    def __init__(
        self,
        page_bean: main_models.GetAlertRulesResponseBodyPageBean = None,
        request_id: str = None,
    ):
        # The returned pages.
        self.page_bean = page_bean
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.page_bean:
            self.page_bean.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_bean is not None:
            result['PageBean'] = self.page_bean.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageBean') is not None:
            temp_model = main_models.GetAlertRulesResponseBodyPageBean()
            self.page_bean = temp_model.from_map(m.get('PageBean'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetAlertRulesResponseBodyPageBean(DaraModel):
    def __init__(
        self,
        alert_rules: List[main_models.GetAlertRulesResponseBodyPageBeanAlertRules] = None,
        page: int = None,
        size: int = None,
        total: int = None,
    ):
        # The alert rules.
        self.alert_rules = alert_rules
        # The number of pages returned.
        self.page = page
        # The number of alert rules returned per page.
        self.size = size
        # The total number of queried alert rules.
        self.total = total

    def validate(self):
        if self.alert_rules:
            for v1 in self.alert_rules:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AlertRules'] = []
        if self.alert_rules is not None:
            for k1 in self.alert_rules:
                result['AlertRules'].append(k1.to_map() if k1 else None)

        if self.page is not None:
            result['Page'] = self.page

        if self.size is not None:
            result['Size'] = self.size

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.alert_rules = []
        if m.get('AlertRules') is not None:
            for k1 in m.get('AlertRules'):
                temp_model = main_models.GetAlertRulesResponseBodyPageBeanAlertRules()
                self.alert_rules.append(temp_model.from_map(k1))

        if m.get('Page') is not None:
            self.page = m.get('Page')

        if m.get('Size') is not None:
            self.size = m.get('Size')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class GetAlertRulesResponseBodyPageBeanAlertRules(DaraModel):
    def __init__(
        self,
        alert_check_type: str = None,
        alert_group: int = None,
        alert_id: int = None,
        alert_name: str = None,
        alert_rule_content: main_models.GetAlertRulesResponseBodyPageBeanAlertRulesAlertRuleContent = None,
        alert_status: str = None,
        alert_type: str = None,
        annotations: List[main_models.GetAlertRulesResponseBodyPageBeanAlertRulesAnnotations] = None,
        auto_add_new_application: bool = None,
        cluster_id: str = None,
        created_time: int = None,
        duration: str = None,
        extend: str = None,
        filters: main_models.GetAlertRulesResponseBodyPageBeanAlertRulesFilters = None,
        labels: List[main_models.GetAlertRulesResponseBodyPageBeanAlertRulesLabels] = None,
        level: str = None,
        message: str = None,
        metrics_type: str = None,
        notify_strategy: str = None,
        pids: List[str] = None,
        prom_ql: str = None,
        region_id: str = None,
        tags: List[main_models.GetAlertRulesResponseBodyPageBeanAlertRulesTags] = None,
        updated_time: int = None,
        user_id: str = None,
    ):
        # The alert check type of the Prometheus alert rule.
        # 
        # *   STATIC: static threshold
        # *   CUSTOM: custom PromQL
        self.alert_check_type = alert_check_type
        # The alert contact group ID of the Prometheus alert rule.
        # 
        # *   \\-1: custom PromQL
        # *   1: Kubernetes load
        # *   15: Kubernetes node
        self.alert_group = alert_group
        # The alert rule ID.
        self.alert_id = alert_id
        # The name of the alert rule.
        self.alert_name = alert_name
        # The content of the Application Monitoring or Browser Monitoring alert rule.
        self.alert_rule_content = alert_rule_content
        # The status of the alert rule. Valid values:
        # 
        # *   RUNNING
        # *   STOPPED
        # *   PAUSED
        # 
        # >  The PAUSED state indicates that the alert rule is abnormal and has been suspended. This may be because the specified threshold value is excessively large, or the associated cluster has been deleted.
        self.alert_status = alert_status
        # The type of the alert rule. Valid values:
        # 
        # *   APPLICATION_MONITORING_ALERT_RULE: alert rule for Application Monitoring
        # *   BROWSER_MONITORING_ALERT_RULE: alert rule for Browser Monitoring
        # *   PROMETHEUS_MONITORING_ALERT_RULE: Prometheus alert rule
        self.alert_type = alert_type
        # The annotations of the Prometheus alert rule.
        self.annotations = annotations
        # Indicates whether the alert rule is applied to new applications that are created in Application Monitoring or Browser Monitoring. Valid values:
        # 
        # *   `true`: yes
        # *   `false`: no
        self.auto_add_new_application = auto_add_new_application
        # The cluster ID of the Prometheus alert rule.
        self.cluster_id = cluster_id
        # The time when the alert rule was created. The value is a timestamp. Unit: milliseconds.
        self.created_time = created_time
        # The duration of the Prometheus alert rule.
        self.duration = duration
        # The extended fields.
        # 
        # >  For existing Application Monitoring alert rules, the fields contain information such as contacts, alert template, and notification content.
        self.extend = extend
        # The filter conditions of the Application Monitoring or Browser Monitoring alert rule.
        self.filters = filters
        # The tags of the Prometheus alert rule.
        self.labels = labels
        # The severity level of the Prometheus alert rule.
        # 
        # *   P1: Alert notifications are sent for major issues that affect the availability of core business, have a huge impact, and may lead to serious consequences.
        # *   P2: Alert notifications are sent for service errors that affect the system availability with relatively limited impact.
        # *   P3: Alert notifications are sent for issues that may cause service errors or negative effects, or alert notifications for services that are relatively less important.
        # *   P4: Alert notifications are sent for low-priority issues that do not affect your business.
        # *   Default: Alert notifications are sent regardless of alert levels.
        self.level = level
        # The alert message of the Prometheus alert rule.
        self.message = message
        # The metric type of the Application Monitoring or Browser Monitoring alert rule.
        self.metrics_type = metrics_type
        # The name of the notification policy.
        self.notify_strategy = notify_strategy
        # The process ID (PID) of the application to which the Application Monitoring or Browser Monitoring alert rule is applied.
        self.pids = pids
        # The PromQL statement of the Prometheus alert rule.
        self.prom_ql = prom_ql
        # The region ID.
        self.region_id = region_id
        # The tags of the alert rule.
        self.tags = tags
        # The time when the alert rule was updated. The value is a timestamp. Unit: milliseconds.
        self.updated_time = updated_time
        # The ID of the Alibaba Cloud account.
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
            temp_model = main_models.GetAlertRulesResponseBodyPageBeanAlertRulesAlertRuleContent()
            self.alert_rule_content = temp_model.from_map(m.get('AlertRuleContent'))

        if m.get('AlertStatus') is not None:
            self.alert_status = m.get('AlertStatus')

        if m.get('AlertType') is not None:
            self.alert_type = m.get('AlertType')

        self.annotations = []
        if m.get('Annotations') is not None:
            for k1 in m.get('Annotations'):
                temp_model = main_models.GetAlertRulesResponseBodyPageBeanAlertRulesAnnotations()
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
            temp_model = main_models.GetAlertRulesResponseBodyPageBeanAlertRulesFilters()
            self.filters = temp_model.from_map(m.get('Filters'))

        self.labels = []
        if m.get('Labels') is not None:
            for k1 in m.get('Labels'):
                temp_model = main_models.GetAlertRulesResponseBodyPageBeanAlertRulesLabels()
                self.labels.append(temp_model.from_map(k1))

        if m.get('Level') is not None:
            self.level = m.get('Level')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('MetricsType') is not None:
            self.metrics_type = m.get('MetricsType')

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
                temp_model = main_models.GetAlertRulesResponseBodyPageBeanAlertRulesTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('UpdatedTime') is not None:
            self.updated_time = m.get('UpdatedTime')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

class GetAlertRulesResponseBodyPageBeanAlertRulesTags(DaraModel):
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

class GetAlertRulesResponseBodyPageBeanAlertRulesLabels(DaraModel):
    def __init__(
        self,
        name: str = None,
        value: str = None,
    ):
        # The tag key.
        self.name = name
        # The tag value.
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

class GetAlertRulesResponseBodyPageBeanAlertRulesFilters(DaraModel):
    def __init__(
        self,
        custom_slsfilters: List[main_models.GetAlertRulesResponseBodyPageBeanAlertRulesFiltersCustomSLSFilters] = None,
        custom_slsgroup_by_dimensions: List[str] = None,
        custom_slswheres: List[str] = None,
        dim_filters: List[main_models.GetAlertRulesResponseBodyPageBeanAlertRulesFiltersDimFilters] = None,
    ):
        # The custom filter condition of the Browser Monitoring alert rule.
        self.custom_slsfilters = custom_slsfilters
        # The information about the aggregation dimension.
        self.custom_slsgroup_by_dimensions = custom_slsgroup_by_dimensions
        # The details of the custom filter condition.
        self.custom_slswheres = custom_slswheres
        # The information about each filter condition of the Application Monitoring or Browser Monitoring alert rule.
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
                temp_model = main_models.GetAlertRulesResponseBodyPageBeanAlertRulesFiltersCustomSLSFilters()
                self.custom_slsfilters.append(temp_model.from_map(k1))

        if m.get('CustomSLSGroupByDimensions') is not None:
            self.custom_slsgroup_by_dimensions = m.get('CustomSLSGroupByDimensions')

        if m.get('CustomSLSWheres') is not None:
            self.custom_slswheres = m.get('CustomSLSWheres')

        self.dim_filters = []
        if m.get('DimFilters') is not None:
            for k1 in m.get('DimFilters'):
                temp_model = main_models.GetAlertRulesResponseBodyPageBeanAlertRulesFiltersDimFilters()
                self.dim_filters.append(temp_model.from_map(k1))

        return self

class GetAlertRulesResponseBodyPageBeanAlertRulesFiltersDimFilters(DaraModel):
    def __init__(
        self,
        filter_key: str = None,
        filter_opt: str = None,
        filter_values: List[str] = None,
    ):
        # The key of the filter condition.
        self.filter_key = filter_key
        # The logical operator of the filter condition.
        self.filter_opt = filter_opt
        # The details of the filter condition.
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

class GetAlertRulesResponseBodyPageBeanAlertRulesFiltersCustomSLSFilters(DaraModel):
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
        # The logical operator of the filter condition. Valid values:
        # 
        # *   \\=: equal to
        # *   not: not equal to
        self.opt = opt
        # Indicates whether this filter condition is displayed on the frontend.
        self.show = show
        # The log type of Browser Monitoring. This field is not included in other filter conditions.
        self.t = t
        # The value of the filter condition.
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

class GetAlertRulesResponseBodyPageBeanAlertRulesAnnotations(DaraModel):
    def __init__(
        self,
        name: str = None,
        value: str = None,
    ):
        # The key of the annotation.
        self.name = name
        # The value of the annotation.
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

class GetAlertRulesResponseBodyPageBeanAlertRulesAlertRuleContent(DaraModel):
    def __init__(
        self,
        alert_rule_items: List[main_models.GetAlertRulesResponseBodyPageBeanAlertRulesAlertRuleContentAlertRuleItems] = None,
        condition: str = None,
    ):
        # The trigger conditions of the Application Monitoring or Browser Monitoring alert rule.
        self.alert_rule_items = alert_rule_items
        # The relationship between multiple alert conditions specified for the Application Monitoring or Browser Monitoring alert rule. Valid values:
        # 
        # *   OR: The alert rule is triggered if one of the conditions is met.
        # *   AND: The alert rule is triggered if all the conditions are met.
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
                temp_model = main_models.GetAlertRulesResponseBodyPageBeanAlertRulesAlertRuleContentAlertRuleItems()
                self.alert_rule_items.append(temp_model.from_map(k1))

        if m.get('Condition') is not None:
            self.condition = m.get('Condition')

        return self

class GetAlertRulesResponseBodyPageBeanAlertRulesAlertRuleContentAlertRuleItems(DaraModel):
    def __init__(
        self,
        aggregate: str = None,
        metric_key: str = None,
        n: int = None,
        operator: str = None,
        value: str = None,
    ):
        # The aggregation method of the alert condition. Valid values:
        # 
        # *   AVG: calculates the average value
        # *   SUM: calculates the total value
        # *   MAX: selects the maximum value
        # *   MIN: selects the minimum value
        self.aggregate = aggregate
        # The metric of the alert condition.
        self.metric_key = metric_key
        # The last N minutes.
        self.n = n
        # The operator that is used to compare the metric value with the threshold. Valid values:
        # 
        # *   CURRENT_GTE: greater than or equal to
        # *   CURRENT_LTE: less than or equal to
        # *   PREVIOUS_UP: increase in percentage compared with the previous period
        # *   PREVIOUS_DOWN: decrease in percentage compared with the previous period
        # *   HOH_UP: increase in percentage compared with the same period in the previous hour
        # *   HOH_DOWN: decrease in percentage compared with the same period in the previous hour
        # *   DOD_UP: increase in percentage compared with the same period in the previous day
        # *   DOD_DOWN: decrease in percentage compared with the same period in the previous day
        self.operator = operator
        # The threshold of the alert condition.
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

