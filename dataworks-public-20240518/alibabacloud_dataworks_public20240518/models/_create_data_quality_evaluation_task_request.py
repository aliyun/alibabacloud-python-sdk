# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataworks_public20240518 import models as main_models
from darabonba.model import DaraModel

class CreateDataQualityEvaluationTaskRequest(DaraModel):
    def __init__(
        self,
        data_quality_rules: List[main_models.CreateDataQualityEvaluationTaskRequestDataQualityRules] = None,
        data_source_id: int = None,
        description: str = None,
        hooks: List[main_models.CreateDataQualityEvaluationTaskRequestHooks] = None,
        name: str = None,
        notifications: main_models.CreateDataQualityEvaluationTaskRequestNotifications = None,
        project_id: int = None,
        runtime_conf: str = None,
        target: main_models.CreateDataQualityEvaluationTaskRequestTarget = None,
        trigger: main_models.CreateDataQualityEvaluationTaskRequestTrigger = None,
    ):
        # The list of data quality rules associated with the data quality monitor. If DataQualityRule.Id is specified, the rule corresponding to that ID is associated with the newly created quality monitor. If not specified, a new rule is created from the other fields and associated with the newly created quality monitor.
        self.data_quality_rules = data_quality_rules
        # The ID of the data source. You can call [ListDataSources](https://help.aliyun.com/document_detail/211431.html) to obtain the ID of the data source.
        # 
        # This parameter is required.
        self.data_source_id = data_source_id
        # The description of the quality monitoring task.
        self.description = description
        # The hook settings.
        self.hooks = hooks
        # The name of the quality monitoring task.
        # 
        # This parameter is required.
        self.name = name
        # The notification subscription configuration.
        self.notifications = notifications
        # The ID of the DataWorks workspace. You can log on to the [DataWorks console](https://workbench.data.aliyun.com/console) and go to the Workspace Management page to obtain the ID.
        # 
        # This parameter specifies the DataWorks workspace used by this API call.
        # 
        # This parameter is required.
        self.project_id = project_id
        # The extended configuration, a JSON-formatted string. This setting takes effect only for EMR-type data quality monitors.
        # - queue: The YARN queue used when running EMR data quality validation. The default is the queue configured for the current project.
        # - sqlEngine: The SQL engine used when running EMR data validation.
        #     + HIVE_SQL
        #     + SPARK_SQL
        self.runtime_conf = runtime_conf
        # The data quality monitoring object.
        # 
        # This parameter is required.
        self.target = target
        # The trigger configuration of the data quality validation task.
        self.trigger = trigger

    def validate(self):
        if self.data_quality_rules:
            for v1 in self.data_quality_rules:
                 if v1:
                    v1.validate()
        if self.hooks:
            for v1 in self.hooks:
                 if v1:
                    v1.validate()
        if self.notifications:
            self.notifications.validate()
        if self.target:
            self.target.validate()
        if self.trigger:
            self.trigger.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DataQualityRules'] = []
        if self.data_quality_rules is not None:
            for k1 in self.data_quality_rules:
                result['DataQualityRules'].append(k1.to_map() if k1 else None)

        if self.data_source_id is not None:
            result['DataSourceId'] = self.data_source_id

        if self.description is not None:
            result['Description'] = self.description

        result['Hooks'] = []
        if self.hooks is not None:
            for k1 in self.hooks:
                result['Hooks'].append(k1.to_map() if k1 else None)

        if self.name is not None:
            result['Name'] = self.name

        if self.notifications is not None:
            result['Notifications'] = self.notifications.to_map()

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.runtime_conf is not None:
            result['RuntimeConf'] = self.runtime_conf

        if self.target is not None:
            result['Target'] = self.target.to_map()

        if self.trigger is not None:
            result['Trigger'] = self.trigger.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_quality_rules = []
        if m.get('DataQualityRules') is not None:
            for k1 in m.get('DataQualityRules'):
                temp_model = main_models.CreateDataQualityEvaluationTaskRequestDataQualityRules()
                self.data_quality_rules.append(temp_model.from_map(k1))

        if m.get('DataSourceId') is not None:
            self.data_source_id = m.get('DataSourceId')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        self.hooks = []
        if m.get('Hooks') is not None:
            for k1 in m.get('Hooks'):
                temp_model = main_models.CreateDataQualityEvaluationTaskRequestHooks()
                self.hooks.append(temp_model.from_map(k1))

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Notifications') is not None:
            temp_model = main_models.CreateDataQualityEvaluationTaskRequestNotifications()
            self.notifications = temp_model.from_map(m.get('Notifications'))

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('RuntimeConf') is not None:
            self.runtime_conf = m.get('RuntimeConf')

        if m.get('Target') is not None:
            temp_model = main_models.CreateDataQualityEvaluationTaskRequestTarget()
            self.target = temp_model.from_map(m.get('Target'))

        if m.get('Trigger') is not None:
            temp_model = main_models.CreateDataQualityEvaluationTaskRequestTrigger()
            self.trigger = temp_model.from_map(m.get('Trigger'))

        return self

class CreateDataQualityEvaluationTaskRequestTrigger(DaraModel):
    def __init__(
        self,
        task_ids: List[int] = None,
        type: str = None,
    ):
        # The list of scheduling task IDs. This parameter is valid when Type is set to ByScheduledTaskInstance.
        self.task_ids = task_ids
        # The trigger type of the quality monitoring task. Valid values:
        # - ByManual: triggered manually. This is the default value.
        # - ByScheduledTaskInstance: triggered by an associated scheduling task.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.task_ids is not None:
            result['TaskIds'] = self.task_ids

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TaskIds') is not None:
            self.task_ids = m.get('TaskIds')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class CreateDataQualityEvaluationTaskRequestTarget(DaraModel):
    def __init__(
        self,
        database_type: str = None,
        partition_spec: str = None,
        table_guid: str = None,
    ):
        # The type of the database to which the table belongs. Valid values:
        # - maxcompute
        # - hologres
        # - cdh
        # - analyticdb_for_mysql
        # - starrocks
        # - emr
        # - analyticdb_for_postgresql
        # 
        # This parameter is required.
        self.database_type = database_type
        # The partition settings of the partitioned table.
        self.partition_spec = partition_spec
        # The unique ID of the table in Data Map.
        # 
        # This parameter is required.
        self.table_guid = table_guid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.database_type is not None:
            result['DatabaseType'] = self.database_type

        if self.partition_spec is not None:
            result['PartitionSpec'] = self.partition_spec

        if self.table_guid is not None:
            result['TableGuid'] = self.table_guid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatabaseType') is not None:
            self.database_type = m.get('DatabaseType')

        if m.get('PartitionSpec') is not None:
            self.partition_spec = m.get('PartitionSpec')

        if m.get('TableGuid') is not None:
            self.table_guid = m.get('TableGuid')

        return self

class CreateDataQualityEvaluationTaskRequestNotifications(DaraModel):
    def __init__(
        self,
        condition: str = None,
        notifications: List[main_models.CreateDataQualityEvaluationTaskRequestNotificationsNotifications] = None,
    ):
        # The trigger condition of the notification. The notification is triggered when this condition is met. Currently only two forms of expressions are supported:
        # 
        # Specify a single combination of rule severity and rule validation status, for example `${severity} == "High" AND ${status} == "Critical"`, which means the condition is met if among the executed rules there exists a rule whose severity is High and whose validation result is Critical.
        # Specify multiple combinations of rule severity and rule validation status, for example `(${severity} == "High" AND ${status} == "Critical") OR (${severity} == "Normal" AND ${status} == "Critical") OR (${severity} == "Normal" AND ${status} == "Error")`, which means the condition is met if among the executed rules there exists a rule whose severity is High and validation result is Critical, or a rule whose severity is Normal and validation result is Critical, or a rule whose severity is Normal and validation result is Error. The enumeration of severity in the expression is the same as severity in DataQualityRule, and the enumeration of status is the same as status in DataQualityResult.
        self.condition = condition
        # The notification settings.
        self.notifications = notifications

    def validate(self):
        if self.notifications:
            for v1 in self.notifications:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.condition is not None:
            result['Condition'] = self.condition

        result['Notifications'] = []
        if self.notifications is not None:
            for k1 in self.notifications:
                result['Notifications'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Condition') is not None:
            self.condition = m.get('Condition')

        self.notifications = []
        if m.get('Notifications') is not None:
            for k1 in m.get('Notifications'):
                temp_model = main_models.CreateDataQualityEvaluationTaskRequestNotificationsNotifications()
                self.notifications.append(temp_model.from_map(k1))

        return self

class CreateDataQualityEvaluationTaskRequestNotificationsNotifications(DaraModel):
    def __init__(
        self,
        notification_channels: List[main_models.CreateDataQualityEvaluationTaskRequestNotificationsNotificationsNotificationChannels] = None,
        notification_receivers: List[main_models.CreateDataQualityEvaluationTaskRequestNotificationsNotificationsNotificationReceivers] = None,
    ):
        # The notification methods.
        self.notification_channels = notification_channels
        # The alert recipient settings.
        self.notification_receivers = notification_receivers

    def validate(self):
        if self.notification_channels:
            for v1 in self.notification_channels:
                 if v1:
                    v1.validate()
        if self.notification_receivers:
            for v1 in self.notification_receivers:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['NotificationChannels'] = []
        if self.notification_channels is not None:
            for k1 in self.notification_channels:
                result['NotificationChannels'].append(k1.to_map() if k1 else None)

        result['NotificationReceivers'] = []
        if self.notification_receivers is not None:
            for k1 in self.notification_receivers:
                result['NotificationReceivers'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.notification_channels = []
        if m.get('NotificationChannels') is not None:
            for k1 in m.get('NotificationChannels'):
                temp_model = main_models.CreateDataQualityEvaluationTaskRequestNotificationsNotificationsNotificationChannels()
                self.notification_channels.append(temp_model.from_map(k1))

        self.notification_receivers = []
        if m.get('NotificationReceivers') is not None:
            for k1 in m.get('NotificationReceivers'):
                temp_model = main_models.CreateDataQualityEvaluationTaskRequestNotificationsNotificationsNotificationReceivers()
                self.notification_receivers.append(temp_model.from_map(k1))

        return self

class CreateDataQualityEvaluationTaskRequestNotificationsNotificationsNotificationReceivers(DaraModel):
    def __init__(
        self,
        extension: str = None,
        receiver_type: str = None,
        receiver_values: List[str] = None,
    ):
        # Additional parameters used when sending alerts, in JSON format. Supported keys:
        # - atAll: whether to mention all members (@all) in the group when sending a DingTalk alert. This key takes effect when ReceiverType is set to DingdingUrl.
        self.extension = extension
        # The type of the alert recipient. Valid values:
        # - WebhookUrl: a custom webhook URL.
        # - FeishuUrl: a Lark (Feishu) alert URL.
        # - DingdingUrl: a DingTalk alert URL.
        # - WeixinUrl: a WeCom (Enterprise WeChat) alert URL.
        # - AliUid: an Alibaba Cloud user ID.
        self.receiver_type = receiver_type
        # The alert recipients.
        self.receiver_values = receiver_values

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.extension is not None:
            result['Extension'] = self.extension

        if self.receiver_type is not None:
            result['ReceiverType'] = self.receiver_type

        if self.receiver_values is not None:
            result['ReceiverValues'] = self.receiver_values

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Extension') is not None:
            self.extension = m.get('Extension')

        if m.get('ReceiverType') is not None:
            self.receiver_type = m.get('ReceiverType')

        if m.get('ReceiverValues') is not None:
            self.receiver_values = m.get('ReceiverValues')

        return self

class CreateDataQualityEvaluationTaskRequestNotificationsNotificationsNotificationChannels(DaraModel):
    def __init__(
        self,
        channels: List[str] = None,
    ):
        # The notification methods.
        self.channels = channels

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.channels is not None:
            result['Channels'] = self.channels

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Channels') is not None:
            self.channels = m.get('Channels')

        return self

class CreateDataQualityEvaluationTaskRequestHooks(DaraModel):
    def __init__(
        self,
        condition: str = None,
        type: str = None,
    ):
        # The trigger condition of the hook. The hook action is triggered when this condition is met. Currently only two forms of expressions are supported:
        # 1. Specify a single combination of rule severity and rule validation status, for example `${severity} == "High" AND ${status} == "Critical"`, which means the condition is met if among the executed rules there exists a rule whose severity is High and whose validation result is Critical.
        # 2. Specify multiple combinations of rule severity and rule validation status, for example `(${severity} == "High" AND ${status} == "Critical") OR (${severity} == "Normal" AND ${status} == "Critical") OR (${severity} == "Normal" AND ${status} == "Error")`, which means the condition is met if among the executed rules there exists a rule whose severity is High and validation result is Critical, or a rule whose severity is Normal and validation result is Critical, or a rule whose severity is Normal and validation result is Error. The enumeration of severity in the expression is the same as severity in DataQualityRule, and the enumeration of status is the same as status in DataQualityResult.
        self.condition = condition
        # The type of the hook. Currently only one type is supported:
        # - BlockTaskInstance: blocks the scheduling task from continuing to run. If the data quality monitor is triggered by a scheduling task, after the monitor finishes running, Hook.Condition is evaluated to determine whether to block the scheduling task from continuing to run.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.condition is not None:
            result['Condition'] = self.condition

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Condition') is not None:
            self.condition = m.get('Condition')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class CreateDataQualityEvaluationTaskRequestDataQualityRules(DaraModel):
    def __init__(
        self,
        checking_config: main_models.CreateDataQualityEvaluationTaskRequestDataQualityRulesCheckingConfig = None,
        description: str = None,
        enabled: bool = None,
        error_handlers: List[main_models.CreateDataQualityEvaluationTaskRequestDataQualityRulesErrorHandlers] = None,
        id: int = None,
        name: str = None,
        sampling_config: main_models.CreateDataQualityEvaluationTaskRequestDataQualityRulesSamplingConfig = None,
        severity: str = None,
        template_code: str = None,
    ):
        # The sample validation settings.
        self.checking_config = checking_config
        # The description of the data quality rule.
        self.description = description
        # Specifies whether the quality rule is enabled.
        self.enabled = enabled
        # The list of error handlers for issues detected by the quality rule validation.
        self.error_handlers = error_handlers
        # The ID of the rule.
        self.id = id
        # The name of the data quality rule.
        self.name = name
        # The parameters required when collecting samples.
        self.sampling_config = sampling_config
        # The business severity level of the rule (corresponding to strong/weak rules in the console). Valid values:
        # - Normal
        # - High
        self.severity = severity
        # The unique identifier of the rule template that the rule references.
        self.template_code = template_code

    def validate(self):
        if self.checking_config:
            self.checking_config.validate()
        if self.error_handlers:
            for v1 in self.error_handlers:
                 if v1:
                    v1.validate()
        if self.sampling_config:
            self.sampling_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.checking_config is not None:
            result['CheckingConfig'] = self.checking_config.to_map()

        if self.description is not None:
            result['Description'] = self.description

        if self.enabled is not None:
            result['Enabled'] = self.enabled

        result['ErrorHandlers'] = []
        if self.error_handlers is not None:
            for k1 in self.error_handlers:
                result['ErrorHandlers'].append(k1.to_map() if k1 else None)

        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        if self.sampling_config is not None:
            result['SamplingConfig'] = self.sampling_config.to_map()

        if self.severity is not None:
            result['Severity'] = self.severity

        if self.template_code is not None:
            result['TemplateCode'] = self.template_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckingConfig') is not None:
            temp_model = main_models.CreateDataQualityEvaluationTaskRequestDataQualityRulesCheckingConfig()
            self.checking_config = temp_model.from_map(m.get('CheckingConfig'))

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')

        self.error_handlers = []
        if m.get('ErrorHandlers') is not None:
            for k1 in m.get('ErrorHandlers'):
                temp_model = main_models.CreateDataQualityEvaluationTaskRequestDataQualityRulesErrorHandlers()
                self.error_handlers.append(temp_model.from_map(k1))

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('SamplingConfig') is not None:
            temp_model = main_models.CreateDataQualityEvaluationTaskRequestDataQualityRulesSamplingConfig()
            self.sampling_config = temp_model.from_map(m.get('SamplingConfig'))

        if m.get('Severity') is not None:
            self.severity = m.get('Severity')

        if m.get('TemplateCode') is not None:
            self.template_code = m.get('TemplateCode')

        return self

class CreateDataQualityEvaluationTaskRequestDataQualityRulesSamplingConfig(DaraModel):
    def __init__(
        self,
        metric: str = None,
        metric_parameters: str = None,
        sampling_filter: str = None,
        setting_config: str = None,
    ):
        # The name of the sampling metric. Valid values:
        # - Count: the number of rows in the table.
        # - Min: the minimum value of the field.
        # - Max: the maximum value of the field.
        # - Avg: the average value of the field.
        # - DistinctCount: the number of distinct values of the field.
        # - DistinctPercent: the ratio of the number of distinct values of the field to the number of rows.
        # - DuplicatedCount: the number of duplicate values of the field.
        # - DuplicatedPercent: the ratio of the number of duplicate values of the field to the number of rows.
        # - TableSize: the size of the table.
        # - NullValueCount: the number of rows in which the field is null.
        # - NullValuePercent: the ratio of rows in which the field is null.
        # - GroupCount: after grouping by the field value, the count of rows for each value.
        # - CountNotIn: the number of rows whose enumeration values do not match.
        # - CountDistinctNotIn: the number of distinct values whose enumeration values do not match.
        # - UserDefinedSql: collect samples using a custom SQL statement.
        self.metric = metric
        # The parameters required when collecting samples.
        self.metric_parameters = metric_parameters
        # An additional filter condition applied during sampling to exclude data that is not of interest. The maximum length is 16,777,215 characters.
        self.sampling_filter = sampling_filter
        # The runtime parameter statements inserted and executed before the sampling statement is executed. The maximum length is 1000 characters. Only MaxCompute is currently supported.
        self.setting_config = setting_config

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.metric is not None:
            result['Metric'] = self.metric

        if self.metric_parameters is not None:
            result['MetricParameters'] = self.metric_parameters

        if self.sampling_filter is not None:
            result['SamplingFilter'] = self.sampling_filter

        if self.setting_config is not None:
            result['SettingConfig'] = self.setting_config

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Metric') is not None:
            self.metric = m.get('Metric')

        if m.get('MetricParameters') is not None:
            self.metric_parameters = m.get('MetricParameters')

        if m.get('SamplingFilter') is not None:
            self.sampling_filter = m.get('SamplingFilter')

        if m.get('SettingConfig') is not None:
            self.setting_config = m.get('SettingConfig')

        return self

class CreateDataQualityEvaluationTaskRequestDataQualityRulesErrorHandlers(DaraModel):
    def __init__(
        self,
        error_data_filter: str = None,
        type: str = None,
    ):
        # For custom SQL rules, the user must specify a SQL statement to filter the problematic data.
        self.error_data_filter = error_data_filter
        # The type of the handler. Valid values:
        # 
        # - SaveErrorData: retains the problematic data.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_data_filter is not None:
            result['ErrorDataFilter'] = self.error_data_filter

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorDataFilter') is not None:
            self.error_data_filter = m.get('ErrorDataFilter')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class CreateDataQualityEvaluationTaskRequestDataQualityRulesCheckingConfig(DaraModel):
    def __init__(
        self,
        referenced_samples_filter: str = None,
        thresholds: main_models.CreateDataQualityEvaluationTaskRequestDataQualityRulesCheckingConfigThresholds = None,
        type: str = None,
    ):
        # For some threshold types, reference samples must be queried and aggregated to derive the threshold used for comparison. This field uses an expression to describe how the reference samples are queried.
        self.referenced_samples_filter = referenced_samples_filter
        # The validation threshold settings.
        self.thresholds = thresholds
        # The method used to compute the threshold. Valid values:
        # 
        # - Fixed
        # - Fluctation
        # - FluctationDiscreate
        # - Auto
        # - Average
        self.type = type

    def validate(self):
        if self.thresholds:
            self.thresholds.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.referenced_samples_filter is not None:
            result['ReferencedSamplesFilter'] = self.referenced_samples_filter

        if self.thresholds is not None:
            result['Thresholds'] = self.thresholds.to_map()

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ReferencedSamplesFilter') is not None:
            self.referenced_samples_filter = m.get('ReferencedSamplesFilter')

        if m.get('Thresholds') is not None:
            temp_model = main_models.CreateDataQualityEvaluationTaskRequestDataQualityRulesCheckingConfigThresholds()
            self.thresholds = temp_model.from_map(m.get('Thresholds'))

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class CreateDataQualityEvaluationTaskRequestDataQualityRulesCheckingConfigThresholds(DaraModel):
    def __init__(
        self,
        critical: main_models.CreateDataQualityEvaluationTaskRequestDataQualityRulesCheckingConfigThresholdsCritical = None,
        expected: main_models.CreateDataQualityEvaluationTaskRequestDataQualityRulesCheckingConfigThresholdsExpected = None,
        warned: main_models.CreateDataQualityEvaluationTaskRequestDataQualityRulesCheckingConfigThresholdsWarned = None,
    ):
        # The threshold settings for the critical warning level.
        self.critical = critical
        # The expected threshold settings.
        self.expected = expected
        # The threshold settings for the normal warning level.
        self.warned = warned

    def validate(self):
        if self.critical:
            self.critical.validate()
        if self.expected:
            self.expected.validate()
        if self.warned:
            self.warned.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.critical is not None:
            result['Critical'] = self.critical.to_map()

        if self.expected is not None:
            result['Expected'] = self.expected.to_map()

        if self.warned is not None:
            result['Warned'] = self.warned.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Critical') is not None:
            temp_model = main_models.CreateDataQualityEvaluationTaskRequestDataQualityRulesCheckingConfigThresholdsCritical()
            self.critical = temp_model.from_map(m.get('Critical'))

        if m.get('Expected') is not None:
            temp_model = main_models.CreateDataQualityEvaluationTaskRequestDataQualityRulesCheckingConfigThresholdsExpected()
            self.expected = temp_model.from_map(m.get('Expected'))

        if m.get('Warned') is not None:
            temp_model = main_models.CreateDataQualityEvaluationTaskRequestDataQualityRulesCheckingConfigThresholdsWarned()
            self.warned = temp_model.from_map(m.get('Warned'))

        return self

class CreateDataQualityEvaluationTaskRequestDataQualityRulesCheckingConfigThresholdsWarned(DaraModel):
    def __init__(
        self,
        expression: str = None,
        operator: str = None,
        value: str = None,
    ):
        # The threshold expression.
        # 
        # Fluctuation-type rules must use expressions to specify the fluctuation threshold. For example:
        # 
        # - Fluctuation increase greater than 0.01: $checkValue > 0.01
        # - Fluctuation decrease greater than 0.01: $checkValue < -0.01
        # - Absolute fluctuation rate: abs($checkValue) > 0.01
        # 
        # Fixed-value rules can also use expressions to configure thresholds. If both are configured, the expression takes precedence over Operator and Value.
        self.expression = expression
        # The comparison operator. Valid values:
        # - \\>
        # - \\>=
        # - <
        # - <=
        # - !=
        # - =
        self.operator = operator
        # The threshold value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.expression is not None:
            result['Expression'] = self.expression

        if self.operator is not None:
            result['Operator'] = self.operator

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Expression') is not None:
            self.expression = m.get('Expression')

        if m.get('Operator') is not None:
            self.operator = m.get('Operator')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class CreateDataQualityEvaluationTaskRequestDataQualityRulesCheckingConfigThresholdsExpected(DaraModel):
    def __init__(
        self,
        expression: str = None,
        operator: str = None,
        value: str = None,
    ):
        # The threshold expression.
        # 
        # Fluctuation-type rules must use expressions to specify the fluctuation threshold. For example:
        # 
        # - Fluctuation increase greater than 0.01: $checkValue > 0.01
        # - Fluctuation decrease greater than 0.01: $checkValue < -0.01
        # - Absolute fluctuation rate: abs($checkValue) > 0.01
        # 
        # Fixed-value rules can also use expressions to configure thresholds. If both are configured, the expression takes precedence over Operator and Value.
        self.expression = expression
        # The comparison operator. Valid values:
        # - \\>
        # - \\>=
        # - <
        # - <=
        # - !=
        # - =
        self.operator = operator
        # The threshold value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.expression is not None:
            result['Expression'] = self.expression

        if self.operator is not None:
            result['Operator'] = self.operator

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Expression') is not None:
            self.expression = m.get('Expression')

        if m.get('Operator') is not None:
            self.operator = m.get('Operator')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class CreateDataQualityEvaluationTaskRequestDataQualityRulesCheckingConfigThresholdsCritical(DaraModel):
    def __init__(
        self,
        expression: str = None,
        operator: str = None,
        value: str = None,
    ):
        # The threshold expression.
        # 
        # Fluctuation-type rules must use expressions to specify the fluctuation threshold. For example:
        # 
        # - Fluctuation increase greater than 0.01: $checkValue > 0.01
        # - Fluctuation decrease greater than 0.01: $checkValue < -0.01
        # - Absolute fluctuation rate: abs($checkValue) > 0.01
        # 
        # Fixed-value rules can also use expressions to configure thresholds. If both are configured, the expression takes precedence over Operator and Value.
        self.expression = expression
        # The comparison operator. Valid values:
        # - \\>
        # - \\>=
        # - <
        # - <=
        # - !=
        # - =
        self.operator = operator
        # The threshold value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.expression is not None:
            result['Expression'] = self.expression

        if self.operator is not None:
            result['Operator'] = self.operator

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Expression') is not None:
            self.expression = m.get('Expression')

        if m.get('Operator') is not None:
            self.operator = m.get('Operator')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

