# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataworks_public20240518 import models as main_models
from darabonba.model import DaraModel

class GetDataQualityEvaluationTaskResponseBody(DaraModel):
    def __init__(
        self,
        data_quality_evaluation_task: main_models.GetDataQualityEvaluationTaskResponseBodyDataQualityEvaluationTask = None,
        request_id: str = None,
    ):
        # The details of the monitor.
        self.data_quality_evaluation_task = data_quality_evaluation_task
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.data_quality_evaluation_task:
            self.data_quality_evaluation_task.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_quality_evaluation_task is not None:
            result['DataQualityEvaluationTask'] = self.data_quality_evaluation_task.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataQualityEvaluationTask') is not None:
            temp_model = main_models.GetDataQualityEvaluationTaskResponseBodyDataQualityEvaluationTask()
            self.data_quality_evaluation_task = temp_model.from_map(m.get('DataQualityEvaluationTask'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetDataQualityEvaluationTaskResponseBodyDataQualityEvaluationTask(DaraModel):
    def __init__(
        self,
        data_source_id: int = None,
        description: str = None,
        hooks: List[main_models.GetDataQualityEvaluationTaskResponseBodyDataQualityEvaluationTaskHooks] = None,
        id: int = None,
        name: str = None,
        notifications: main_models.GetDataQualityEvaluationTaskResponseBodyDataQualityEvaluationTaskNotifications = None,
        project_id: int = None,
        runtime_conf: str = None,
        target: main_models.GetDataQualityEvaluationTaskResponseBodyDataQualityEvaluationTaskTarget = None,
        trigger: main_models.GetDataQualityEvaluationTaskResponseBodyDataQualityEvaluationTaskTrigger = None,
    ):
        # The ID of the data source used for the monitor.
        self.data_source_id = data_source_id
        # The description of the monitor.
        self.description = description
        # The hook.
        self.hooks = hooks
        # The ID of the data quality monitor.
        self.id = id
        # The name of the monitor.
        # 
        # This parameter is required.
        self.name = name
        # The configurations of alert notifications.
        self.notifications = notifications
        # The workspace ID.
        self.project_id = project_id
        # Extended configuration, JSON-formatted string, takes effect only for EMR-type data quality monitoring.
        # 
        # - queue: the yarn queue used when performing EMR data quality verification. The default queue is the queue configured for this project.
        # - sqlEngine: SQL engine used when performing EMR data verification
        #     - HIVE_ SQL
        #     - SPARK_ SQL
        self.runtime_conf = runtime_conf
        # The monitored object of the monitor.
        self.target = target
        # The trigger configuration of the monitor.
        self.trigger = trigger

    def validate(self):
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
        if m.get('DataSourceId') is not None:
            self.data_source_id = m.get('DataSourceId')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        self.hooks = []
        if m.get('Hooks') is not None:
            for k1 in m.get('Hooks'):
                temp_model = main_models.GetDataQualityEvaluationTaskResponseBodyDataQualityEvaluationTaskHooks()
                self.hooks.append(temp_model.from_map(k1))

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Notifications') is not None:
            temp_model = main_models.GetDataQualityEvaluationTaskResponseBodyDataQualityEvaluationTaskNotifications()
            self.notifications = temp_model.from_map(m.get('Notifications'))

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('RuntimeConf') is not None:
            self.runtime_conf = m.get('RuntimeConf')

        if m.get('Target') is not None:
            temp_model = main_models.GetDataQualityEvaluationTaskResponseBodyDataQualityEvaluationTaskTarget()
            self.target = temp_model.from_map(m.get('Target'))

        if m.get('Trigger') is not None:
            temp_model = main_models.GetDataQualityEvaluationTaskResponseBodyDataQualityEvaluationTaskTrigger()
            self.trigger = temp_model.from_map(m.get('Trigger'))

        return self

class GetDataQualityEvaluationTaskResponseBodyDataQualityEvaluationTaskTrigger(DaraModel):
    def __init__(
        self,
        task_ids: List[int] = None,
        type: str = None,
    ):
        # The IDs of scheduling tasks. This parameter is valid only if you set Type to ByScheduledTaskInstance.
        self.task_ids = task_ids
        # The trigger type of the monitor. Valid values:
        # 
        # *   ByManual: The monitor is manually triggered.
        # *   ByScheduledTaskInstance: The monitor is triggered by associated scheduling tasks.
        # *   ByQualityNode: The monitor is triggered by created data quality monitoring nodes.
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

class GetDataQualityEvaluationTaskResponseBodyDataQualityEvaluationTaskTarget(DaraModel):
    def __init__(
        self,
        database_type: str = None,
        partition_spec: str = None,
        table_guid: str = None,
        type: str = None,
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
        # Data quality monitoring partition range settings.
        self.partition_spec = partition_spec
        # The ID of the table in Data Map.
        self.table_guid = table_guid
        # The type of the monitoring object.
        # 
        # - Table: Table.
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

class GetDataQualityEvaluationTaskResponseBodyDataQualityEvaluationTaskNotifications(DaraModel):
    def __init__(
        self,
        condition: str = None,
        notifications: List[main_models.GetDataQualityEvaluationTaskResponseBodyDataQualityEvaluationTaskNotificationsNotifications] = None,
    ):
        # The notification trigger condition. When this condition is met, the alert notification is triggered. Only two conditional expressions are supported:
        # 
        # *   Specify only one group of rule strength type and rule check status, such as `${severity} == "High" AND ${status} == "Critical"`. In this expression, the hook trigger condition is met if severity is High and status is Critical.
        # *   Specify multiple groups of rule strength types and rule check status, such as `(${severity} == "High"AND ${status} == "Critical") OR (${severity} == "Normal" AND ${status} == "Critical") OR (${severity} == "Normal" AND ${status} == "Error")`. In this expression, the hook trigger condition is met if severity is High and status is Critical, severity is Normal and status is Critical, or severity is Normal and status is Error. The enumeration of severity in a conditional expression is the same as the enumeration of severity in DataQualityRule. The enumeration of status in a conditional expression is the same as the enumeration of status in DataQualityResult.
        self.condition = condition
        # The configurations of alert notifications.
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
                temp_model = main_models.GetDataQualityEvaluationTaskResponseBodyDataQualityEvaluationTaskNotificationsNotifications()
                self.notifications.append(temp_model.from_map(k1))

        return self

class GetDataQualityEvaluationTaskResponseBodyDataQualityEvaluationTaskNotificationsNotifications(DaraModel):
    def __init__(
        self,
        notification_channels: List[main_models.GetDataQualityEvaluationTaskResponseBodyDataQualityEvaluationTaskNotificationsNotificationsNotificationChannels] = None,
        notification_receivers: List[main_models.GetDataQualityEvaluationTaskResponseBodyDataQualityEvaluationTaskNotificationsNotificationsNotificationReceivers] = None,
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
                temp_model = main_models.GetDataQualityEvaluationTaskResponseBodyDataQualityEvaluationTaskNotificationsNotificationsNotificationChannels()
                self.notification_channels.append(temp_model.from_map(k1))

        self.notification_receivers = []
        if m.get('NotificationReceivers') is not None:
            for k1 in m.get('NotificationReceivers'):
                temp_model = main_models.GetDataQualityEvaluationTaskResponseBodyDataQualityEvaluationTaskNotificationsNotificationsNotificationReceivers()
                self.notification_receivers.append(temp_model.from_map(k1))

        return self

class GetDataQualityEvaluationTaskResponseBodyDataQualityEvaluationTaskNotificationsNotificationsNotificationReceivers(DaraModel):
    def __init__(
        self,
        extension: str = None,
        receiver_type: str = None,
        receiver_values: List[str] = None,
    ):
        # The extended information.
        self.extension = extension
        # The additional parameters that are required when alerts are sent. The parameters are JSON-formatted strings. The following keys are supported:
        # 
        # *   atAll: specifies that all members in a group are mentioned when alerts are sent by using DingTalk. This parameter is valid only if you set ReceiverType to DingdingUrl.
        # 
        # Valid values:
        # 
        # *   WebhookUrl
        # *   FeishuUrl
        # *   DingdingUrl
        # *   WeixinUrl
        # *   AliUid
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

class GetDataQualityEvaluationTaskResponseBodyDataQualityEvaluationTaskNotificationsNotificationsNotificationChannels(DaraModel):
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

class GetDataQualityEvaluationTaskResponseBodyDataQualityEvaluationTaskHooks(DaraModel):
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
        # The hook type. Only one hook type is supported.
        # 
        # *   BlockTaskInstance: Blocks the running of scheduling tasks. A monitor is triggered by scheduling tasks. After a monitor finishes running, the monitor determines whether to block the running of scheduling tasks based on the hook condition.
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

