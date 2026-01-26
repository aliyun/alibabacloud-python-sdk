# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_arms20190808 import models as main_models
from darabonba.model import DaraModel

class CreateOrUpdateAlertRuleRequest(DaraModel):
    def __init__(
        self,
        alert_check_type: str = None,
        alert_group: int = None,
        alert_id: int = None,
        alert_name: str = None,
        alert_piplines: str = None,
        alert_rule_content: str = None,
        alert_status: str = None,
        alert_type: str = None,
        annotations: str = None,
        auto_add_new_application: bool = None,
        auto_add_target_config: str = None,
        check_cycle: int = None,
        cluster_id: str = None,
        data_config: str = None,
        duration: int = None,
        filters: str = None,
        labels: str = None,
        level: str = None,
        mark_tags: List[main_models.CreateOrUpdateAlertRuleRequestMarkTags] = None,
        message: str = None,
        metrics_key: str = None,
        metrics_type: str = None,
        notice: str = None,
        notify_mode: str = None,
        notify_strategy: str = None,
        pids: str = None,
        product: str = None,
        prom_ql: str = None,
        region_id: str = None,
        tags: List[main_models.CreateOrUpdateAlertRuleRequestTags] = None,
        aliyun_lang: str = None,
    ):
        # The alert check type of the Prometheus alert rule. Valid values:
        # 
        # *   STATIC: a static threshold value. If you set the parameter to STATIC, you must specify the **MetricsKey** parameter. For more information, see the **Correspondence between AlertGroup and MetricsKey for Prometheus Service** table.
        # *   CUSTOM: a custom PromQL statement. If you set the parameter to CUSTOM, you must specify the **PromQL**, **Duration**, and **Message** parameters to create a Prometheus alert rule.
        self.alert_check_type = alert_check_type
        # The alert contact group ID of the Prometheus alert rule. Valid values:
        # 
        # *   \\-1: custom PromQL
        # *   1: Kubernetes load
        # *   15: Kubernetes node
        self.alert_group = alert_group
        # The ID of the alert rule.
        # 
        # *   If you do not specify this parameter, a new alert rule is created.
        # *   If you specify this parameter, the specified alert rule is modified.
        self.alert_id = alert_id
        # The name of the alert rule.
        # 
        # This parameter is required.
        self.alert_name = alert_name
        # The configuration of the alert sending channel. This parameter is used to be compatible with the old version of the rule.
        self.alert_piplines = alert_piplines
        # The content of the Application Monitoring or Browser Monitoring alert rule. The following code provides an example of the **AlertRuleContent** parameter. For more information about the meaning of each field, see the supplementary description.
        # 
        # ```json
        # { 
        #     "Condition": "OR",
        #      "AlertRuleItems": [
        #              { "Operator": "CURRENT_LTE",
        #                  "MetricKey": "appstat.jvm.threadcount",
        #                  "Value": 1000,
        #                  "Aggregate": "AVG",
        #                   "N": 10,
        #                   "Tolerability": 169
        #             } 
        #        ]  
        #   }
        # ```
        # 
        # >  The filter conditions specified by the **AlertRuleItems.MetricKey** field depends on the value of the **MetricsType** parameter. For more information about the types of metrics supported by Application Monitoring and Browser Monitoring and the alert rule fields corresponding to each metric, see the supplementary description.
        self.alert_rule_content = alert_rule_content
        # The status of the alert rule. Valid values:
        # 
        # *   RUNNING (default)
        # *   STOPPED
        self.alert_status = alert_status
        # The type of the alert rule. Valid values:
        # 
        # *   APPLICATION_MONITORING_ALERT_RULE: an alert rule for Application Monitoring.
        # *   BROWSER_MONITORING_ALERT_RULE: an alert rule for Browser Monitoring.
        # *   PROMETHEUS_MONITORING_ALERT_RULE: an alert rule for Managed Service for Prometheus.
        # *   XTRACE_MONITORING_ALERT_RULE: an alert rule for Managed Service for OpenTelemetry.
        # *   EBPF_MONITORING_ALERT_RULE: an alert rule for Application Monitoring eBPF Edition.
        # *   RUM_MONITORING_ALERT_RULE: an alert rule for Real User Monitoring.
        # 
        # Valid values:
        # 
        # *   PROMETHEUS_MONITORING_ALERT_RULE
        # *   APPLICATION_MONITORING_ALERT_RULE
        # *   BROWSER_MONITORING_ALERT_RULE
        # *   prometheus monitoring alert
        # *   application monitoring alert
        # *   browser monitoring alert
        # *   XTRACE_MONITORING_ALERT_RULE
        # *   EBPF_MONITORING_ALERT_RULE
        # *   RUM_MONITORING_ALERT_RULE
        # 
        # This parameter is required.
        self.alert_type = alert_type
        # The annotations of the Prometheus alert rule.
        self.annotations = annotations
        # Specifies whether to apply the alert rule to new applications that are created in Application Monitoring or Browser Monitoring. Valid values:
        # 
        # *   `true`: enables the health check feature.
        # *   `false`: disables the automatic backup feature.
        self.auto_add_new_application = auto_add_new_application
        # The configurations that are automatically appended to monitor the application based on the specified alert rule.
        # 
        # *   autoAddMatchType:
        # 
        #     the matching mode. Valid values: REGULAR and NOT_REGULAR.
        # 
        # *   autoAddMatchExp: the regular expression
        self.auto_add_target_config = auto_add_target_config
        # The interval for checking the alerts in Managed Service for Prometheus.
        self.check_cycle = check_cycle
        # The ID of the monitored cluster.
        self.cluster_id = cluster_id
        # Data Configuration. The dataRevision field specifies the data repair method when there is no data for the metric.
        # 
        # - Fill with zero: 0
        # - Fill with one: 1
        # - Fill with null: 2 (default, does not trigger an alarm)
        self.data_config = data_config
        # The duration of the Prometheus alert rule, in minutes, in the range of [0,1440].
        self.duration = duration
        # The filter conditions of the Application Monitoring or Browser Monitoring alert rule. Format:
        # 
        #     "DimFilters": [ 
        #     { 
        #      "FilterOpt": "ALL",
        #     "FilterValues": [],         //The value of the filter condition.
        #     "FilterKey": "rootIp"     //The key of the filter condition.
        #     }
        #     ]
        # 
        # Valid values of **FilterOpt**:
        # 
        # *   STATIC: matches the value of the specified dimension.
        # *   ALL: traverses all dimension values. Dynamic thresholds do not support traversal.
        # *   DISABLE: aggregates the values of all dimensions.
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
        # Application Tags. Used for application monitoring alert rules, to filter applications associated with alert rules.
        self.mark_tags = mark_tags
        # The alert message of the Prometheus alert rule.
        self.message = message
        # The alert metrics. If you set the **AlertCheckType** parameter to **STATIC** when you create a Prometheus alert rule, you must specify the **MetricsKey** parameter.
        # 
        # > Alert metrics vary depending on the value of the **AlertGroup** parameter. For more information about the correspondence between **AlertGroup** and **MetricsKey**, see the supplementary description.
        self.metrics_key = metrics_key
        # The metric type of the Application Monitoring or Browser Monitoring alert rule. For more information, see the following table.
        self.metrics_type = metrics_type
        # The effective time and notification time. This parameter is used to be compatible with the old version of the rule.
        self.notice = notice
        # The notification mode. You can specify normal mode or simple mode.
        # 
        # *   DIRECTED_MODE
        # *   NORMAL_MODE
        self.notify_mode = notify_mode
        # The notification policy.
        # 
        # *   If you set this parameter to null, no notification policy is specified. After you create an alert rule, you can create a notification policy and specify match rules and match conditions. For example, you can specify the name of the alert rule as the match condition. When the alert rule is triggered, an alert event is generated and an alert notification is sent to the contacts or contact groups that are specified in the notification policy.
        # *   To specify a notification policy, set this parameter to the ID of the notification policy. Application Real-Time Monitoring Service (ARMS) automatically adds a match rule to the notification policy and specifies the ID of the alert rule as the match condition. The name of the alert rule is also displayed. This way, the alert events that are generated based on the alert rule can be matched by the specified notification policy.
        self.notify_strategy = notify_strategy
        # The process ID (PID) that is associated with the Application Monitoring or Browser Monitoring alert rule.
        self.pids = pids
        # The product code. If you specify this parameter when you create a Prometheus alert rule, the backend checks whether the product exists.
        self.product = product
        # The PromQL statement of the Prometheus alert rule.
        self.prom_ql = prom_ql
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The list of tags.
        self.tags = tags
        self.aliyun_lang = aliyun_lang

    def validate(self):
        if self.mark_tags:
            for v1 in self.mark_tags:
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

        if self.alert_piplines is not None:
            result['AlertPiplines'] = self.alert_piplines

        if self.alert_rule_content is not None:
            result['AlertRuleContent'] = self.alert_rule_content

        if self.alert_status is not None:
            result['AlertStatus'] = self.alert_status

        if self.alert_type is not None:
            result['AlertType'] = self.alert_type

        if self.annotations is not None:
            result['Annotations'] = self.annotations

        if self.auto_add_new_application is not None:
            result['AutoAddNewApplication'] = self.auto_add_new_application

        if self.auto_add_target_config is not None:
            result['AutoAddTargetConfig'] = self.auto_add_target_config

        if self.check_cycle is not None:
            result['CheckCycle'] = self.check_cycle

        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.data_config is not None:
            result['DataConfig'] = self.data_config

        if self.duration is not None:
            result['Duration'] = self.duration

        if self.filters is not None:
            result['Filters'] = self.filters

        if self.labels is not None:
            result['Labels'] = self.labels

        if self.level is not None:
            result['Level'] = self.level

        result['MarkTags'] = []
        if self.mark_tags is not None:
            for k1 in self.mark_tags:
                result['MarkTags'].append(k1.to_map() if k1 else None)

        if self.message is not None:
            result['Message'] = self.message

        if self.metrics_key is not None:
            result['MetricsKey'] = self.metrics_key

        if self.metrics_type is not None:
            result['MetricsType'] = self.metrics_type

        if self.notice is not None:
            result['Notice'] = self.notice

        if self.notify_mode is not None:
            result['NotifyMode'] = self.notify_mode

        if self.notify_strategy is not None:
            result['NotifyStrategy'] = self.notify_strategy

        if self.pids is not None:
            result['Pids'] = self.pids

        if self.product is not None:
            result['Product'] = self.product

        if self.prom_ql is not None:
            result['PromQL'] = self.prom_ql

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        if self.aliyun_lang is not None:
            result['aliyunLang'] = self.aliyun_lang

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

        if m.get('AlertPiplines') is not None:
            self.alert_piplines = m.get('AlertPiplines')

        if m.get('AlertRuleContent') is not None:
            self.alert_rule_content = m.get('AlertRuleContent')

        if m.get('AlertStatus') is not None:
            self.alert_status = m.get('AlertStatus')

        if m.get('AlertType') is not None:
            self.alert_type = m.get('AlertType')

        if m.get('Annotations') is not None:
            self.annotations = m.get('Annotations')

        if m.get('AutoAddNewApplication') is not None:
            self.auto_add_new_application = m.get('AutoAddNewApplication')

        if m.get('AutoAddTargetConfig') is not None:
            self.auto_add_target_config = m.get('AutoAddTargetConfig')

        if m.get('CheckCycle') is not None:
            self.check_cycle = m.get('CheckCycle')

        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('DataConfig') is not None:
            self.data_config = m.get('DataConfig')

        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        if m.get('Filters') is not None:
            self.filters = m.get('Filters')

        if m.get('Labels') is not None:
            self.labels = m.get('Labels')

        if m.get('Level') is not None:
            self.level = m.get('Level')

        self.mark_tags = []
        if m.get('MarkTags') is not None:
            for k1 in m.get('MarkTags'):
                temp_model = main_models.CreateOrUpdateAlertRuleRequestMarkTags()
                self.mark_tags.append(temp_model.from_map(k1))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('MetricsKey') is not None:
            self.metrics_key = m.get('MetricsKey')

        if m.get('MetricsType') is not None:
            self.metrics_type = m.get('MetricsType')

        if m.get('Notice') is not None:
            self.notice = m.get('Notice')

        if m.get('NotifyMode') is not None:
            self.notify_mode = m.get('NotifyMode')

        if m.get('NotifyStrategy') is not None:
            self.notify_strategy = m.get('NotifyStrategy')

        if m.get('Pids') is not None:
            self.pids = m.get('Pids')

        if m.get('Product') is not None:
            self.product = m.get('Product')

        if m.get('PromQL') is not None:
            self.prom_ql = m.get('PromQL')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.CreateOrUpdateAlertRuleRequestTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('aliyunLang') is not None:
            self.aliyun_lang = m.get('aliyunLang')

        return self

class CreateOrUpdateAlertRuleRequestTags(DaraModel):
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

class CreateOrUpdateAlertRuleRequestMarkTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The Tag Key.
        self.key = key
        # The Tag Value.
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

