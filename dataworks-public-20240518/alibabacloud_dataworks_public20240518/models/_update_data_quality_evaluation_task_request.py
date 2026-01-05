# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataworks_public20240518 import models as main_models
from darabonba.model import DaraModel

class UpdateDataQualityEvaluationTaskRequest(DaraModel):
    def __init__(
        self,
        data_quality_rules: List[main_models.UpdateDataQualityEvaluationTaskRequestDataQualityRules] = None,
        data_source_id: int = None,
        description: str = None,
        hooks: List[main_models.UpdateDataQualityEvaluationTaskRequestHooks] = None,
        id: int = None,
        name: str = None,
        notifications: main_models.UpdateDataQualityEvaluationTaskRequestNotifications = None,
        project_id: int = None,
        runtime_conf: str = None,
        target: main_models.UpdateDataQualityEvaluationTaskRequestTarget = None,
        trigger: main_models.UpdateDataQualityEvaluationTaskRequestTrigger = None,
    ):
        # The list of monitoring rules that are associated with the monitor.
        self.data_quality_rules = data_quality_rules
        # The data source ID. You can call the [ListDataSources](https://help.aliyun.com/document_detail/211431.html) operation to query the ID.
        self.data_source_id = data_source_id
        # The description of the monitor.
        self.description = description
        # The hook.
        self.hooks = hooks
        # The ID of the monitor.
        # 
        # This parameter is required.
        self.id = id
        # The name of the monitor.
        self.name = name
        # The configurations of alert notifications.
        self.notifications = notifications
        # The ID of the DataWorks workspace.
        # 
        # This parameter is required.
        self.project_id = project_id
        # The extended configurations in JSON-formatted strings. You can use this parameter only for monitors that are used to monitor the quality of E-MapReduce (EMR) data.
        # 
        # *   queue: The Yarn queue used when a monitor checks the quality of EMR data. By default, the queue configured for the current workspace is used.
        # 
        # *   sqlEngine: The SQL engine used when a monitor checks the quality of EMR data.
        # 
        #     *   HIVE_SQL
        #     *   SPARK_SQL
        self.runtime_conf = runtime_conf
        # The monitored object of the data quality monitoring task.
        self.target = target
        # The trigger configuration of the monitor.
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

        if self.id is not None:
            result['Id'] = self.id

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
                temp_model = main_models.UpdateDataQualityEvaluationTaskRequestDataQualityRules()
                self.data_quality_rules.append(temp_model.from_map(k1))

        if m.get('DataSourceId') is not None:
            self.data_source_id = m.get('DataSourceId')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        self.hooks = []
        if m.get('Hooks') is not None:
            for k1 in m.get('Hooks'):
                temp_model = main_models.UpdateDataQualityEvaluationTaskRequestHooks()
                self.hooks.append(temp_model.from_map(k1))

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Notifications') is not None:
            temp_model = main_models.UpdateDataQualityEvaluationTaskRequestNotifications()
            self.notifications = temp_model.from_map(m.get('Notifications'))

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('RuntimeConf') is not None:
            self.runtime_conf = m.get('RuntimeConf')

        if m.get('Target') is not None:
            temp_model = main_models.UpdateDataQualityEvaluationTaskRequestTarget()
            self.target = temp_model.from_map(m.get('Target'))

        if m.get('Trigger') is not None:
            temp_model = main_models.UpdateDataQualityEvaluationTaskRequestTrigger()
            self.trigger = temp_model.from_map(m.get('Trigger'))

        return self

class UpdateDataQualityEvaluationTaskRequestTrigger(DaraModel):
    def __init__(
        self,
        task_ids: List[int] = None,
        type: str = None,
    ):
        # The IDs of scheduling tasks. This parameter is valid only if you set Type to ByScheduledTaskInstance.
        self.task_ids = task_ids
        # The trigger type of the monitor. Valid values:
        # 
        # *   ByScheduledTaskInstance: The monitor is triggered by the associated scheduling tasks.
        # *   ByManual: The monitor is manually triggered.
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

class UpdateDataQualityEvaluationTaskRequestTarget(DaraModel):
    def __init__(
        self,
        database_type: str = None,
        partition_spec: str = None,
        table_guid: str = None,
    ):
        # The type of the database to which the table belongs. Valid values:
        # 
        # *   maxcompute
        # *   hologres
        # *   cdh
        # *   analyticdb_for_mysql
        # *   starrocks
        # *   emr
        # *   analyticdb_for_postgresql
        self.database_type = database_type
        # The configuration of the partitioned table.
        self.partition_spec = partition_spec
        # The ID of the table in Data Map.
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

class UpdateDataQualityEvaluationTaskRequestNotifications(DaraModel):
    def __init__(
        self,
        condition: str = None,
        notifications: List[main_models.UpdateDataQualityEvaluationTaskRequestNotificationsNotifications] = None,
    ):
        # The notification trigger condition. When this condition is met, the alert notification is triggered. Only two conditional expressions are supported:
        # 
        # *   Specify only one group of rule strength type and rule check status, such as `${severity} == "High" AND ${status} == "Critical"`. In this expression, the hook trigger condition is met if severity is High and status is Critical.
        # *   Specify multiple groups of rule strength types and rule check status, such as `(${severity} == "High" AND ${status} == "Critical") OR (${severity} == "Normal" AND ${status} == "Critical") OR (${severity} == "Normal" AND ${status} == "Error")`. In this expression, the hook trigger condition is met if severity is High and status is Critical, severity is Normal and status is Critical, or severity is Normal and status is Error. The enumeration of severity in a conditional expression is the same as the enumeration of severity in DataQualityRule. The enumeration of status in a conditional expression is the same as the enumeration of status in DataQualityResult.
        self.condition = condition
        # The configurations of the alert notification.
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
                temp_model = main_models.UpdateDataQualityEvaluationTaskRequestNotificationsNotifications()
                self.notifications.append(temp_model.from_map(k1))

        return self

class UpdateDataQualityEvaluationTaskRequestNotificationsNotifications(DaraModel):
    def __init__(
        self,
        notification_channels: List[main_models.UpdateDataQualityEvaluationTaskRequestNotificationsNotificationsNotificationChannels] = None,
        notification_receivers: List[main_models.UpdateDataQualityEvaluationTaskRequestNotificationsNotificationsNotificationReceivers] = None,
    ):
        # The alert notification methods.
        self.notification_channels = notification_channels
        # The configurations of alert recipients.
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
                temp_model = main_models.UpdateDataQualityEvaluationTaskRequestNotificationsNotificationsNotificationChannels()
                self.notification_channels.append(temp_model.from_map(k1))

        self.notification_receivers = []
        if m.get('NotificationReceivers') is not None:
            for k1 in m.get('NotificationReceivers'):
                temp_model = main_models.UpdateDataQualityEvaluationTaskRequestNotificationsNotificationsNotificationReceivers()
                self.notification_receivers.append(temp_model.from_map(k1))

        return self

class UpdateDataQualityEvaluationTaskRequestNotificationsNotificationsNotificationReceivers(DaraModel):
    def __init__(
        self,
        extension: str = None,
        receiver_type: str = None,
        receiver_values: List[str] = None,
    ):
        # The additional parameters that are required when alerts are sent. The parameters are JSON-formatted strings. The following keys are supported:
        # 
        # *   atAll: specifies that all members in a group are mentioned when alerts are sent by using DingTalk. This parameter is valid only if you set ReceiverType to DingdingUrl.
        self.extension = extension
        # The type of the alert recipient.
        # 
        # Valid values:
        # 
        # *   WebhookUrl
        # *   FeishuUrl
        # *   DingdingUrl
        # *   WeixinUrl
        # *   AliUid
        self.receiver_type = receiver_type
        # The alert recipient.
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

class UpdateDataQualityEvaluationTaskRequestNotificationsNotificationsNotificationChannels(DaraModel):
    def __init__(
        self,
        channels: List[str] = None,
    ):
        # The alert notification methods.
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

class UpdateDataQualityEvaluationTaskRequestHooks(DaraModel):
    def __init__(
        self,
        condition: str = None,
        type: str = None,
    ):
        # The hook trigger condition. When this condition is met, the hook action is triggered. Only two conditional expressions are supported:
        # 
        # *   Specify only one group of rule strength type and rule check status, such as `${severity} == "High" AND ${status} == "Critical"`. In this expression, the hook trigger condition is met if severity is High and status is Critical.
        # *   Specify multiple groups of rule strength types and rule check status, such as `(${severity} == "High" AND ${status} == "Critical") OR (${severity} == "Normal" AND ${status} == "Critical") OR (${severity} == "Normal" AND ${status} == "Error")`. In this expression, the hook trigger condition is met if severity is High and status is Critical, severity is Normal and status is Critical, or severity is Normal and status is Error. The enumeration of severity in a conditional expression is the same as the enumeration of severity in DataQualityRule. The enumeration of status in a conditional expression is the same as the enumeration of status in DataQualityResult.
        self.condition = condition
        # The hook type. Valid values:
        # 
        # *   BlockTaskInstance: Blocks the running of scheduling tasks.
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

class UpdateDataQualityEvaluationTaskRequestDataQualityRules(DaraModel):
    def __init__(
        self,
        checking_config: main_models.UpdateDataQualityEvaluationTaskRequestDataQualityRulesCheckingConfig = None,
        description: str = None,
        enabled: bool = None,
        error_handlers: List[main_models.UpdateDataQualityEvaluationTaskRequestDataQualityRulesErrorHandlers] = None,
        id: int = None,
        name: str = None,
        sampling_config: main_models.UpdateDataQualityEvaluationTaskRequestDataQualityRulesSamplingConfig = None,
        severity: str = None,
        template_code: str = None,
    ):
        # The check settings for sample data.
        self.checking_config = checking_config
        # The description of the rule.
        self.description = description
        # Specifies whether to enable the rule.
        self.enabled = enabled
        # The operations that you can perform after the rule-based check fails.
        self.error_handlers = error_handlers
        # The rule ID. You can call the [ListQualityRules](https://help.aliyun.com/document_detail/173995.html) operation to query the ID of the monitoring rule.
        self.id = id
        # The name of the monitoring rule.
        self.name = name
        # The parameters required for sampling.
        self.sampling_config = sampling_config
        # The strength of the rule. Valid values:
        # 
        # *   Normal
        # *   High
        self.severity = severity
        # The ID of the template used by the rule.
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
            temp_model = main_models.UpdateDataQualityEvaluationTaskRequestDataQualityRulesCheckingConfig()
            self.checking_config = temp_model.from_map(m.get('CheckingConfig'))

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')

        self.error_handlers = []
        if m.get('ErrorHandlers') is not None:
            for k1 in m.get('ErrorHandlers'):
                temp_model = main_models.UpdateDataQualityEvaluationTaskRequestDataQualityRulesErrorHandlers()
                self.error_handlers.append(temp_model.from_map(k1))

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('SamplingConfig') is not None:
            temp_model = main_models.UpdateDataQualityEvaluationTaskRequestDataQualityRulesSamplingConfig()
            self.sampling_config = temp_model.from_map(m.get('SamplingConfig'))

        if m.get('Severity') is not None:
            self.severity = m.get('Severity')

        if m.get('TemplateCode') is not None:
            self.template_code = m.get('TemplateCode')

        return self

class UpdateDataQualityEvaluationTaskRequestDataQualityRulesSamplingConfig(DaraModel):
    def __init__(
        self,
        metric: str = None,
        metric_parameters: str = None,
        sampling_filter: str = None,
        setting_config: str = None,
    ):
        # The metrics used for sampling. Valid values:
        # 
        # *   Count: the number of rows in the table.
        # *   Min: the minimum value of the field.
        # *   Max: the maximum value of the field.
        # *   Avg: the average value of the field.
        # *   DistinctCount: the number of unique values of the field after deduplication.
        # *   DistinctPercent: the proportion of the number of unique values of the field after deduplication to the number of rows in the table.
        # *   DuplicatedCount: the number of duplicated values of the field.
        # *   DuplicatedPercent: the proportion of the number of duplicated values of the field to the number of rows in the table.
        # *   TableSize: the table size.
        # *   NullValueCount: the number of rows in which the field value is null.
        # *   NullValuePercent: the proportion of the number of rows in which the field value is null to the number of rows in the table.
        # *   GroupCount: the field value and the number of rows for each field value.
        # *   CountNotIn: the number of rows in which the field values are different from the referenced values that you specified in the rule.
        # *   CountDistinctNotIn: the number of unique values that are different from the referenced values that you specified in the rule after deduplication.
        # *   UserDefinedSql: specifies that data is sampled by executing custom SQL statements.
        self.metric = metric
        # The parameters required for sampling.
        self.metric_parameters = metric_parameters
        # The statements that are used to filter unnecessary data during sampling. The statements can be up to 16,777,215 characters in length.
        self.sampling_filter = sampling_filter
        # The statements that are used to configure the parameters required for sampling before you execute the sampling statements. The statements can be up to 1,000 characters in length. Only the MaxCompute database is supported.
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

class UpdateDataQualityEvaluationTaskRequestDataQualityRulesErrorHandlers(DaraModel):
    def __init__(
        self,
        error_data_filter: str = None,
        type: str = None,
    ):
        # The SQL statement that is used to filter failed tasks. If you define the rule by using custom SQL statements, you must specify an SQL statement to filter failed tasks.
        self.error_data_filter = error_data_filter
        # The type of the operation. Valid values:
        # 
        # *   SaveErrorData
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

class UpdateDataQualityEvaluationTaskRequestDataQualityRulesCheckingConfig(DaraModel):
    def __init__(
        self,
        referenced_samples_filter: str = None,
        thresholds: main_models.UpdateDataQualityEvaluationTaskRequestDataQualityRulesCheckingConfigThresholds = None,
        type: str = None,
    ):
        # The method that is used to query the referenced samples. To obtain specific types of thresholds, you must query reference values. In this example, an expression is used to specify the query method of referenced samples.
        self.referenced_samples_filter = referenced_samples_filter
        # The threshold settings.
        self.thresholds = thresholds
        # The threshold calculation method. Valid values:
        # 
        # *   Fluctation
        # *   Auto
        # *   FluctationDiscreate
        # *   Average
        # *   Fixed
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
            temp_model = main_models.UpdateDataQualityEvaluationTaskRequestDataQualityRulesCheckingConfigThresholds()
            self.thresholds = temp_model.from_map(m.get('Thresholds'))

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class UpdateDataQualityEvaluationTaskRequestDataQualityRulesCheckingConfigThresholds(DaraModel):
    def __init__(
        self,
        critical: main_models.UpdateDataQualityEvaluationTaskRequestDataQualityRulesCheckingConfigThresholdsCritical = None,
        expected: main_models.UpdateDataQualityEvaluationTaskRequestDataQualityRulesCheckingConfigThresholdsExpected = None,
        warned: main_models.UpdateDataQualityEvaluationTaskRequestDataQualityRulesCheckingConfigThresholdsWarned = None,
    ):
        # The threshold settings for critical alerts.
        self.critical = critical
        # The expected threshold setting.
        self.expected = expected
        # The threshold settings for normal alerts.
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
            temp_model = main_models.UpdateDataQualityEvaluationTaskRequestDataQualityRulesCheckingConfigThresholdsCritical()
            self.critical = temp_model.from_map(m.get('Critical'))

        if m.get('Expected') is not None:
            temp_model = main_models.UpdateDataQualityEvaluationTaskRequestDataQualityRulesCheckingConfigThresholdsExpected()
            self.expected = temp_model.from_map(m.get('Expected'))

        if m.get('Warned') is not None:
            temp_model = main_models.UpdateDataQualityEvaluationTaskRequestDataQualityRulesCheckingConfigThresholdsWarned()
            self.warned = temp_model.from_map(m.get('Warned'))

        return self

class UpdateDataQualityEvaluationTaskRequestDataQualityRulesCheckingConfigThresholdsWarned(DaraModel):
    def __init__(
        self,
        expression: str = None,
        operator: str = None,
        value: str = None,
    ):
        # The threshold expression.
        # 
        # If the template specified by the TemplateCode parameter is about fluctuation, you must use an expression to represent the threshold for fluctuation. Examples:
        # 
        # *   $checkValue > 0.01
        # *   $checkValue < -0.01
        # *   abs($checkValue) > 0.01
        # 
        # If the template specified by the TemplateCode parameter is about fixed value, you can also use an expression to represent the threshold. If you configure the Expression, Operator, and Value parameters for the threshold at the same time, the Expression parameter takes precedence over the Operator and Value parameters.
        self.expression = expression
        # The comparison operator. Valid values:
        # 
        # *   \\>
        # *   \\>=
        # *   <
        # *   <=
        # *   !=
        # *   \\=
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

class UpdateDataQualityEvaluationTaskRequestDataQualityRulesCheckingConfigThresholdsExpected(DaraModel):
    def __init__(
        self,
        expression: str = None,
        operator: str = None,
        value: str = None,
    ):
        # The threshold expression.
        # 
        # If the template specified by the TemplateCode parameter is about fluctuation, you must use an expression to represent the threshold for fluctuation. Examples:
        # 
        # *   $checkValue > 0.01
        # *   $checkValue < -0.01
        # *   abs($checkValue) > 0.01
        # 
        # If the template specified by the TemplateCode parameter is about fixed value, you can also use an expression to represent the threshold. If you configure the Expression, Operator, and Value parameters for the threshold at the same time, the Expression parameter takes precedence over the Operator and Value parameters.
        self.expression = expression
        # The comparison operator. Valid values:
        # 
        # *   \\>
        # *   \\>=
        # *   <
        # *   <=
        # *   !=
        # *   \\=
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

class UpdateDataQualityEvaluationTaskRequestDataQualityRulesCheckingConfigThresholdsCritical(DaraModel):
    def __init__(
        self,
        expression: str = None,
        operator: str = None,
        value: str = None,
    ):
        # The threshold expression.
        # 
        # If the template specified by the TemplateCode parameter is about fluctuation, you must use an expression to represent the threshold for fluctuation. Examples:
        # 
        # *   $checkValue > 0.01
        # *   $checkValue < -0.01
        # *   abs($checkValue) > 0.01
        # 
        # If the template specified by the TemplateCode parameter is about fixed value, you can also use an expression to represent the threshold. If you configure the Expression, Operator, and Value parameters for the threshold at the same time, the Expression parameter takes precedence over the Operator and Value parameters.
        self.expression = expression
        # The comparison operator. Valid values:
        # 
        # *   \\>
        # *   \\>=
        # *   <
        # *   <=
        # *   !=
        # *   \\=
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

