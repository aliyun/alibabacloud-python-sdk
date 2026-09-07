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
        # The check type for a Prometheus monitoring alert rule.
        # 
        # - `STATIC`: A static threshold. The **MetricsKey** parameter is required. For more information, see the description of the **MetricsKey** parameter below.
        # 
        # - `CUSTOM`: A custom PromQL query. The **PromQL**, **Duration**, and **Message** parameters are required.
        self.alert_check_type = alert_check_type
        # The alert group ID for the Prometheus alert rule. Valid values:
        # 
        # - `-1`: Custom PromQL
        # 
        # - `1`: Kubernetes workloads
        # 
        # - `15`: Kubernetes nodes
        self.alert_group = alert_group
        # The ID of the alert rule.
        # 
        # - Omit this parameter to create a new alert rule.
        # 
        # - Specify an ID to modify an existing alert rule.
        self.alert_id = alert_id
        # The alert rule name.
        # 
        # This parameter is required.
        self.alert_name = alert_name
        # The alert pipeline configuration. Used for compatibility with legacy alert rules.
        self.alert_piplines = alert_piplines
        # The content of the alert rule for application monitoring or browser monitoring. The following is a template for the **AlertRuleContent** parameter. For a description of the fields in the template, see the supplementary information below this table.
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
        # > The available fields for **AlertRuleItems.MetricKey** depend on the **MetricsType** value. For information about the metric types supported by application monitoring and browser monitoring and their corresponding alert rule fields, see the supplementary information below this table.
        self.alert_rule_content = alert_rule_content
        # The status of the alert rule. Valid values:
        # 
        # - `RUNNING`: The alert rule is running. (Default)
        # 
        # - `STOPPED`: The alert rule is stopped.
        self.alert_status = alert_status
        # The type of the alert rule. Valid values:
        # 
        # - `APPLICATION_MONITORING_ALERT_RULE`: For application monitoring.
        # 
        # - `BROWSER_MONITORING_ALERT_RULE`: For browser monitoring.
        # 
        # - `PROMETHEUS_MONITORING_ALERT_RULE`: For Prometheus monitoring.
        # 
        # - `XTRACE_MONITORING_ALERT_RULE`: For Tracing Analysis (OpenTelemetry edition).
        # 
        # - `EBPF_MONITORING_ALERT_RULE`: For eBPF monitoring.
        # 
        # - `RUM_MONITORING_ALERT_RULE`: For real user monitoring (RUM).
        # 
        # This parameter is required.
        self.alert_type = alert_type
        # Annotations to add to the Prometheus alert rule. Specify as a JSON string representing an array of objects, each with Name and Value keys.
        self.annotations = annotations
        # Determines whether to automatically apply this alert rule to new applications. This applies only to application monitoring and browser monitoring rules.
        # 
        # - `true`: enables the feature.
        # 
        # - `false`: disables the feature.
        self.auto_add_new_application = auto_add_new_application
        # The configuration for automatically adding applications to an application monitoring alert rule. Specify this parameter as a JSON string with the following fields:
        # 
        # - `autoAddMatchType`: The matching method. Can be `REGULAR` (matches the regular expression) or `NOT_REGULAR` (does not match the regular expression).
        # 
        #   Match type: Regular expression match (REGULAR) / Not a regular expression match (NOT_REGULAR)
        # 
        # - `autoAddMatchExp`: The regular expression.
        self.auto_add_target_config = auto_add_target_config
        # The check interval for the Prometheus alert rule.
        self.check_cycle = check_cycle
        # The cluster ID for the Prometheus monitoring alert rule.
        self.cluster_id = cluster_id
        # The data configuration. The dataRevision field specifies how to handle missing metric data.
        # 
        # - `0`: Fills the data with 0.
        # 
        # - `1`: Fills the data with 1.
        # 
        # - `2`: Fills the data with null. This is the default and does not trigger an alert.
        self.data_config = data_config
        # The period, in minutes, that a condition must be true before a Prometheus alert is triggered. Valid values: 0 to 1440.
        self.duration = duration
        # The filters for an application monitoring or browser monitoring alert rule.
        # Specify this parameter as a JSON string in the following format:
        # 
        # ```
        # "DimFilters": [ 
        # { 
        #  "FilterOpt": "ALL",
        #  "FilterValues": [],         // The filter value.
        #  "FilterKey": "rootIp"     // The filter key.
        # }
        # ]
        # ```
        # 
        # Valid values for **FilterOpt**:
        # 
        # - `STATIC`: Matches a fixed dimension value.
        # 
        # - `ALL`: Iterates over all dimension values. Note: This option is not supported for range detection.
        # 
        # - `DISABLE`: Aggregates all dimension values by summing them.
        self.filters = filters
        # Labels to add to the Prometheus alert rule. Specify as a JSON string representing an array of objects, each with Name and Value keys.
        self.labels = labels
        # The severity level for the Prometheus alert rule.
        # 
        # - `P1`: Critical. For major issues that affect core business availability with a wide impact and severe consequences.
        # 
        # - `P2`: Warning. For issues that cause partial service failures or affect system availability with a limited scope.
        # 
        # - `P3`: Info. For potential issues or alerts from non-critical services.
        # 
        # - `P4`: Low priority. Used for informational alerts that require attention but do not affect services.
        # 
        # - `Default`: The default level, used when no specific severity is required.
        self.level = level
        # Application tags used to filter applications in application monitoring alert rules.
        self.mark_tags = mark_tags
        # The alert message for the Prometheus alert rule.
        self.message = message
        # The alert metric. This parameter is required for Prometheus alert rules when **AlertCheckType** is **STATIC**.
        # 
        # > The available alert metrics vary based on the value of **AlertGroup**. For information about the mapping between **AlertGroup** and **MetricsKey**, see the supplementary information below this table.
        self.metrics_key = metrics_key
        # The alert metric type for application monitoring or browser monitoring alert rules. For more information, see the table below.
        self.metrics_type = metrics_type
        # The effective time and notification time. Used for compatibility with legacy alert rules.
        self.notice = notice
        # The notification mode. Valid values:
        # 
        # - `DIRECTED_MODE`: Directed mode.
        # 
        # - `NORMAL_MODE`: Normal mode.
        self.notify_mode = notify_mode
        # The notification policy.
        # 
        # - `null`: Does not associate the alert rule with a notification policy. You can associate them later by creating a notification policy with a matching rule, for example, based on the alert rule\\"s name. When the alert rule is triggered, alert events are sent to the contacts or contact groups specified in the matching notification policy.
        # 
        # - A notification policy ID: Associates the alert rule with a specific notification policy. ARMS automatically adds a matching rule to the policy that uses the alert rule\\"s ID. This ensures that alert events from this rule are always processed by the specified policy.
        self.notify_strategy = notify_strategy
        # The PIDs of applications for an application monitoring or browser monitoring alert rule. Specify as a JSON array of strings.
        self.pids = pids
        # Required for Prometheus alert rules. Used to filter by cloud service. The specified product name must be valid.
        self.product = product
        # The PromQL expression to evaluate.
        self.prom_ql = prom_ql
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The tags to add to the alert rule. These are standard Alibaba Cloud resource tags.
        self.tags = tags
        # The language of the response.
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

