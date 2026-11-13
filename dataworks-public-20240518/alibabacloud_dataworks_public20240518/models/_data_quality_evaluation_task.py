# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataworks_public20240518 import models as main_models
from darabonba.model import DaraModel

class DataQualityEvaluationTask(DaraModel):
    def __init__(
        self,
        data_source_id: int = None,
        description: str = None,
        hooks: List[main_models.DataQualityEvaluationTaskHooks] = None,
        id: int = None,
        name: str = None,
        notifications: List[main_models.DataQualityEvaluationTaskNotifications] = None,
        project_id: int = None,
        runtime_conf: str = None,
        target: main_models.DataQualityEvaluationTaskTarget = None,
        tenant_id: int = None,
        trigger: main_models.DataQualityEvaluationTaskTrigger = None,
    ):
        # The ID of the data source used to execute the data quality check task.
        self.data_source_id = data_source_id
        # The description of the data quality check task. The description can be up to 65,535 characters in length.
        self.description = description
        # The callback settings for the lifecycle of the data quality check task instance. Currently, only one hook that blocks the scheduled task is supported.
        self.hooks = hooks
        # The ID of the data quality check task.
        self.id = id
        # The name of the data quality check task. The name can contain digits, letters, Chinese characters, and half-width or full-width punctuation marks, and can be up to 255 characters in length.
        self.name = name
        # The notification subscription configuration of the data quality check task.
        self.notifications = notifications
        # The ID of the DataWorks workspace.
        self.project_id = project_id
        # The runtime configuration for using the data source. Currently, you can only specify the YARN queue for EMR and set the SQL engine to SPARK_SQL, KYUUBI, PRESTO_SQL, or HIVE_SQL when collecting EMR tables.
        self.runtime_conf = runtime_conf
        # The monitored object of the data quality check task.
        self.target = target
        # The ID of the DataWorks tenant.
        self.tenant_id = tenant_id
        # The trigger configuration of the data quality check task.
        self.trigger = trigger

    def validate(self):
        if self.hooks:
            for v1 in self.hooks:
                 if v1:
                    v1.validate()
        if self.notifications:
            for v1 in self.notifications:
                 if v1:
                    v1.validate()
        if self.target:
            self.target.validate()
        if self.trigger:
            self.trigger.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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

        result['Notifications'] = []
        if self.notifications is not None:
            for k1 in self.notifications:
                result['Notifications'].append(k1.to_map() if k1 else None)

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.runtime_conf is not None:
            result['RuntimeConf'] = self.runtime_conf

        if self.target is not None:
            result['Target'] = self.target.to_map()

        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id

        if self.trigger is not None:
            result['Trigger'] = self.trigger.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataSourceId') is not None:
            self.data_source_id = m.get('DataSourceId')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        self.hooks = []
        if m.get('Hooks') is not None:
            for k1 in m.get('Hooks'):
                temp_model = main_models.DataQualityEvaluationTaskHooks()
                self.hooks.append(temp_model.from_map(k1))

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        self.notifications = []
        if m.get('Notifications') is not None:
            for k1 in m.get('Notifications'):
                temp_model = main_models.DataQualityEvaluationTaskNotifications()
                self.notifications.append(temp_model.from_map(k1))

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('RuntimeConf') is not None:
            self.runtime_conf = m.get('RuntimeConf')

        if m.get('Target') is not None:
            temp_model = main_models.DataQualityEvaluationTaskTarget()
            self.target = temp_model.from_map(m.get('Target'))

        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')

        if m.get('Trigger') is not None:
            temp_model = main_models.DataQualityEvaluationTaskTrigger()
            self.trigger = temp_model.from_map(m.get('Trigger'))

        return self

class DataQualityEvaluationTaskTrigger(DaraModel):
    def __init__(
        self,
        task_ids: List[int] = None,
        type: str = None,
    ):
        # The IDs of the scheduled nodes whose successful instance execution triggers the data quality check task. This parameter takes effect only when Type is set to ByScheduledTaskInstance.
        self.task_ids = task_ids
        # The event that triggers the execution of the data quality check task. Valid values:
        # - ByScheduledTaskInstance: A scheduled instance completes successfully.
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

class DataQualityEvaluationTaskTarget(DaraModel):
    def __init__(
        self,
        database_type: str = None,
        partition_spec: str = None,
        table_guid: str = None,
        type: str = None,
    ):
        # The database type of the table dataset. Valid values:
        # - maxcompute
        # - emr
        # - cdh
        # - hologres
        # - analyticdb_for_postgresql
        # - analyticdb_for_mysql
        # - starrocks
        self.database_type = database_type
        # The partition settings of the partitioned table.
        self.partition_spec = partition_spec
        # The unique ID of the table in Data Map.
        self.table_guid = table_guid
        # The monitored object type. Valid values:
        # - Table
        self.type = type

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

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatabaseType') is not None:
            self.database_type = m.get('DatabaseType')

        if m.get('PartitionSpec') is not None:
            self.partition_spec = m.get('PartitionSpec')

        if m.get('TableGuid') is not None:
            self.table_guid = m.get('TableGuid')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class DataQualityEvaluationTaskNotifications(DaraModel):
    def __init__(
        self,
        condition: str = None,
        notifications: List[main_models.DataQualityEvaluationTaskNotificationsNotifications] = None,
    ):
        # The trigger condition of the alert.
        self.condition = condition
        # The specific notification settings.
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
                temp_model = main_models.DataQualityEvaluationTaskNotificationsNotifications()
                self.notifications.append(temp_model.from_map(k1))

        return self

class DataQualityEvaluationTaskNotificationsNotifications(DaraModel):
    def __init__(
        self,
        notification_channels: List[main_models.DataQualityEvaluationTaskNotificationsNotificationsNotificationChannels] = None,
        notification_receivers: List[main_models.DataQualityEvaluationTaskNotificationsNotificationsNotificationReceivers] = None,
    ):
        # The notification method.
        self.notification_channels = notification_channels
        # The settings of the alert recipients.
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
                temp_model = main_models.DataQualityEvaluationTaskNotificationsNotificationsNotificationChannels()
                self.notification_channels.append(temp_model.from_map(k1))

        self.notification_receivers = []
        if m.get('NotificationReceivers') is not None:
            for k1 in m.get('NotificationReceivers'):
                temp_model = main_models.DataQualityEvaluationTaskNotificationsNotificationsNotificationReceivers()
                self.notification_receivers.append(temp_model.from_map(k1))

        return self

class DataQualityEvaluationTaskNotificationsNotificationsNotificationReceivers(DaraModel):
    def __init__(
        self,
        extension: str = None,
        receiver_type: str = None,
        receiver_values: List[str] = None,
    ):
        # The extension information in JSON format. For example, DingTalk chatbots support mentioning all members.
        self.extension = extension
        # The type of the alert recipient.
        self.receiver_type = receiver_type
        # The alert recipient values.
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

class DataQualityEvaluationTaskNotificationsNotificationsNotificationChannels(DaraModel):
    def __init__(
        self,
        channels: List[str] = None,
    ):
        # The notification method.
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

class DataQualityEvaluationTaskHooks(DaraModel):
    def __init__(
        self,
        condition: str = None,
        type: str = None,
    ):
        # The trigger condition of the hook.
        self.condition = condition
        # The type of the subsequent action. Valid values:
        # - BlockTaskInstance: Blocks the execution of the DataWorks task instance.
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

