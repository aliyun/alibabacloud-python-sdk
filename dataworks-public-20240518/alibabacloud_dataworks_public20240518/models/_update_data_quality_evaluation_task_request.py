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
        # List of data quality rules associated with the data quality monitoring.
        self.data_quality_rules = data_quality_rules
        # Data source ID. You can call [ListDataSources](https://help.aliyun.com/document_detail/211431.html) to obtain the data source ID.
        self.data_source_id = data_source_id
        # Description of the quality monitoring task
        self.description = description
        # Callback settings
        self.hooks = hooks
        # Data quality monitoring ID.
        # 
        # This parameter is required.
        self.id = id
        # Name of the quality monitoring task
        self.name = name
        # Notification subscription configuration
        self.notifications = notifications
        # Workspace ID
        # 
        # This parameter is required.
        self.project_id = project_id
        # Extended configuration. A JSON-formatted string. Takes effect only for EMR-type data quality monitoring.
        # 
        # - queue: The YARN queue used when executing EMR data quality validation. Defaults to the queue configured for the current project.
        # - sqlEngine: The SQL engine used when executing EMR data validation.
        #   + HIVE_SQL
        #   + SPARK_SQL
        self.runtime_conf = runtime_conf
        # Data quality monitoring object
        self.target = target
        # Trigger configuration of the data quality validation task
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
        # List of scheduling task IDs. Valid when Type is ByScheduledTaskInstance.
        self.task_ids = task_ids
        # Trigger type of the quality monitoring task.
        # - ByScheduledTaskInstance: Triggered by an associated scheduling task.
        # - ByManual: Triggered manually.
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
        # Database type to which the table belongs
        # - maxcompute
        # - hologres
        # - cdh
        # - analyticdb_for_mysql
        # - starrocks
        # - emr
        # - analyticdb_for_postgresql
        self.database_type = database_type
        # Partition settings of the partitioned table
        self.partition_spec = partition_spec
        # Unique ID of the table in Data Map
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
        # Notification trigger condition. When this condition is met, a message notification is triggered. Currently, only two types of condition expressions are supported:
        # 
        # - Specify a single group of rule severity type and rule validation status, such as `${severity} == "High" AND ${status} == "Critical"`. This means the condition is met when any executed rule with severity High has a validation result of Critical.
        # - Specify multiple groups of rule severity type and rule validation status, such as `(${severity} == "High" AND ${status} == "Critical") OR (${severity} == "Normal" AND ${status} == "Critical") OR (${severity} == "Normal" AND ${status} == "Error")`. This means the condition is met when any executed rule satisfies one of the following: severity High with validation result Critical, severity Normal with validation result Critical, or severity Normal with validation result Error. The severity enum in the condition expression is consistent with the severity enum in DataQualityRule, and the status enum is consistent with the status in DataQualityResult.
        self.condition = condition
        # Notification settings
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
        # Notification method
        self.notification_channels = notification_channels
        # Alert recipient settings
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
        # Additional parameter settings when sending alerts. JSON format. The supported keys are as follows:
        # 
        # - atAll: Whether to @all members in the group when sending DingTalk alerts. Takes effect when ReceiverType is DingdingUrl.
        self.extension = extension
        # Alert recipient type
        self.receiver_type = receiver_type
        # Alert recipients
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
        # Notification method
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
        # Hook trigger condition. When this condition is met, the hook action is triggered. Currently, only two types of condition expressions are supported:
        # 
        # - Specify a single group of rule severity type and rule validation status, such as `${severity} == "High" AND ${status} == "Critical"`. This means the condition is met when any executed rule with severity High has a validation result of Critical.
        # - Specify multiple groups of rule severity type and rule validation status, such as `(${severity} == "High" AND ${status} == "Critical") OR (${severity} == "Normal" AND ${status} == "Critical") OR (${severity} == "Normal" AND ${status} == "Error")`. This means the condition is met when any executed rule satisfies one of the following: severity High with validation result Critical, severity Normal with validation result Critical, or severity Normal with validation result Error. The severity enum in the condition expression is consistent with the severity enum in DataQualityRule, and the status enum is consistent with the status in DataQualityResult.
        self.condition = condition
        # Hook actions executed after data quality validation completes.
        # 
        # - BlockTaskInstance: Block the scheduling task.
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
        # Sample validation settings
        self.checking_config = checking_config
        # Description of the data quality rule.
        self.description = description
        # Whether the data quality rule is enabled.
        self.enabled = enabled
        # Quality rule validation issue handler
        self.error_handlers = error_handlers
        # ID of the validation rule. You can call the [ListQualityRules](https://help.aliyun.com/document_detail/173995.html) operation to obtain the rule ID.
        self.id = id
        # Name of the data quality rule.
        self.name = name
        # Parameters required for sample collection
        self.sampling_config = sampling_config
        # Severity level of the rule for the business (corresponds to strong/weak rules on the page). Optional enum values:
        # - Normal
        # - High
        self.severity = severity
        # Unique identifier of the rule template referenced by the rule.
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
        # Name of the sampling metric
        # - Count: Number of rows in the table
        # - Min: Minimum value of the field
        # - Max: Maximum value of the field
        # - Avg: Average value of the field
        # - DistinctCount: Number of distinct values of the field
        # - DistinctPercent: Ratio of the number of distinct field values to the total number of rows
        # - DuplicatedCount: Number of duplicate values of the field
        # - DuplicatedPercent: Ratio of the number of duplicate field values to the total number of rows
        # - TableSize: Size of the table
        # - NullValueCount: Number of rows where the field is null
        # - NullValuePercent: Proportion of rows where the field is null
        # - GroupCount: After aggregating by field value, each value and its corresponding number of rows
        # - CountNotIn: Number of rows whose enum values do not match
        # - CountDistinctNotIn: Number of distinct values whose enum values do not match
        # - UserDefinedSql: Sample collection via custom SQL
        self.metric = metric
        # Parameters required for sample collection
        self.metric_parameters = metric_parameters
        # Conditions for further filtering of data not of concern during sampling. Maximum 16777215 characters.
        self.sampling_filter = sampling_filter
        # Runtime parameter setting statements to be inserted and executed before the actual sampling statement. Maximum 1000 characters. Currently only MaxCompute is supported.
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
        # For custom SQL rules, the user must specify the SQL to filter problematic data.
        self.error_data_filter = error_data_filter
        # Handler type:
        # 
        # - SaveErrorData: Retain problematic data
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
        # Some threshold types require querying reference samples and then aggregating their values to derive the comparison threshold. An expression is used here to indicate how the reference samples are queried.
        self.referenced_samples_filter = referenced_samples_filter
        # Validation threshold settings.
        self.thresholds = thresholds
        # Threshold calculation method
        # 
        # - Fluctation: Fluctuation range validation
        # - Auto: Intelligent threshold validation
        # - FluctationDiscreate: Discrete value fluctuation range validation
        # - Average: Mean fluctuation range validation
        # - Fixed: Fixed value validation
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
        # Threshold settings for critical warnings
        self.critical = critical
        # Expected threshold settings
        self.expected = expected
        # Threshold settings for normal warnings
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
        # Threshold expression.
        # 
        # Fluctuation-type rules must use an expression to represent the fluctuation threshold. For example:
        # 
        # - Fluctuation rises above 0.01: $checkValue > 0.01
        # - Fluctuation drops below 0.01: $checkValue < -0.01
        # - Absolute fluctuation rate: abs($checkValue) > 0.01
        # 
        # Fixed-value-type rules can also use an expression to configure the threshold. If both are configured, the expression takes precedence over Operator and Value.
        self.expression = expression
        # Comparison operator
        # - \\>
        # - \\>=
        # - \\<
        # - \\<=
        # - !=
        # - =
        self.operator = operator
        # Threshold value
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
        # Threshold expression.
        # 
        # Fluctuation-type rules must use an expression to represent the fluctuation threshold. For example:
        # 
        # - Fluctuation rises above 0.01: $checkValue > 0.01
        # - Fluctuation drops below 0.01: $checkValue < -0.01
        # - Absolute fluctuation rate: abs($checkValue) > 0.01
        # 
        # Fixed-value-type rules can also use an expression to configure the threshold. If both are configured, the expression takes precedence over Operator and Value.
        self.expression = expression
        # Comparison operator
        # - \\>
        # - \\>=
        # - <
        # - <=
        # - !=
        # - =
        self.operator = operator
        # Threshold value
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
        # Threshold expression.
        # 
        # Fluctuation-type rules must use an expression to represent the fluctuation threshold. For example:
        # 
        # - Fluctuation rises above 0.01: $checkValue > 0.01
        # - Fluctuation drops below 0.01: $checkValue < -0.01
        # - Absolute fluctuation rate: abs($checkValue) > 0.01
        # 
        # Fixed-value-type rules can also use an expression to configure the threshold. If both are configured, the expression takes precedence over Operator and Value.
        self.expression = expression
        # Comparison operator
        # - \\>
        # - \\>=
        # - <
        # - <=
        # - !=
        # - =
        self.operator = operator
        # Threshold value.
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

