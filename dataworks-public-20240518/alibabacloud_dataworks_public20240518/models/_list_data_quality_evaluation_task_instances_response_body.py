# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataworks_public20240518 import models as main_models
from darabonba.model import DaraModel

class ListDataQualityEvaluationTaskInstancesResponseBody(DaraModel):
    def __init__(
        self,
        paging_info: main_models.ListDataQualityEvaluationTaskInstancesResponseBodyPagingInfo = None,
        request_id: str = None,
    ):
        # The pagination query result of quality evaluation task instances.
        self.paging_info = paging_info
        # The API request ID.
        self.request_id = request_id

    def validate(self):
        if self.paging_info:
            self.paging_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.paging_info is not None:
            result['PagingInfo'] = self.paging_info.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PagingInfo') is not None:
            temp_model = main_models.ListDataQualityEvaluationTaskInstancesResponseBodyPagingInfo()
            self.paging_info = temp_model.from_map(m.get('PagingInfo'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListDataQualityEvaluationTaskInstancesResponseBodyPagingInfo(DaraModel):
    def __init__(
        self,
        data_quality_evaluation_task_instances: List[main_models.ListDataQualityEvaluationTaskInstancesResponseBodyPagingInfoDataQualityEvaluationTaskInstances] = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # The successfully triggered TaskInstance.
        self.data_quality_evaluation_task_instances = data_quality_evaluation_task_instances
        # The page number.
        self.page_number = page_number
        # The page size.
        self.page_size = page_size
        # The total number of records.
        self.total_count = total_count

    def validate(self):
        if self.data_quality_evaluation_task_instances:
            for v1 in self.data_quality_evaluation_task_instances:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DataQualityEvaluationTaskInstances'] = []
        if self.data_quality_evaluation_task_instances is not None:
            for k1 in self.data_quality_evaluation_task_instances:
                result['DataQualityEvaluationTaskInstances'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_quality_evaluation_task_instances = []
        if m.get('DataQualityEvaluationTaskInstances') is not None:
            for k1 in m.get('DataQualityEvaluationTaskInstances'):
                temp_model = main_models.ListDataQualityEvaluationTaskInstancesResponseBodyPagingInfoDataQualityEvaluationTaskInstances()
                self.data_quality_evaluation_task_instances.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListDataQualityEvaluationTaskInstancesResponseBodyPagingInfoDataQualityEvaluationTaskInstances(DaraModel):
    def __init__(
        self,
        create_time: int = None,
        finish_time: int = None,
        id: int = None,
        parameters: str = None,
        project_id: int = None,
        status: str = None,
        task: main_models.ListDataQualityEvaluationTaskInstancesResponseBodyPagingInfoDataQualityEvaluationTaskInstancesTask = None,
        trigger_context: str = None,
    ):
        # The creation time of the task instance.
        self.create_time = create_time
        # The end time of the task instance.
        self.finish_time = finish_time
        # The ID of the quality check task instance.
        self.id = id
        # The parameter settings used during the actual runtime.
        self.parameters = parameters
        # The ID of the DataWorks project workspace.
        self.project_id = project_id
        # The current running status.
        # - Running
        # - Error
        # - Passed
        # - Warned
        # - Critical
        self.status = status
        # The snapshot of the data quality evaluation task when the evaluation starts.
        self.task = task
        # The context information when the instance is triggered.
        self.trigger_context = trigger_context

    def validate(self):
        if self.task:
            self.task.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.finish_time is not None:
            result['FinishTime'] = self.finish_time

        if self.id is not None:
            result['Id'] = self.id

        if self.parameters is not None:
            result['Parameters'] = self.parameters

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.status is not None:
            result['Status'] = self.status

        if self.task is not None:
            result['Task'] = self.task.to_map()

        if self.trigger_context is not None:
            result['TriggerContext'] = self.trigger_context

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('FinishTime') is not None:
            self.finish_time = m.get('FinishTime')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Task') is not None:
            temp_model = main_models.ListDataQualityEvaluationTaskInstancesResponseBodyPagingInfoDataQualityEvaluationTaskInstancesTask()
            self.task = temp_model.from_map(m.get('Task'))

        if m.get('TriggerContext') is not None:
            self.trigger_context = m.get('TriggerContext')

        return self

class ListDataQualityEvaluationTaskInstancesResponseBodyPagingInfoDataQualityEvaluationTaskInstancesTask(DaraModel):
    def __init__(
        self,
        description: str = None,
        hooks: List[main_models.ListDataQualityEvaluationTaskInstancesResponseBodyPagingInfoDataQualityEvaluationTaskInstancesTaskHooks] = None,
        id: int = None,
        name: str = None,
        notifications: main_models.ListDataQualityEvaluationTaskInstancesResponseBodyPagingInfoDataQualityEvaluationTaskInstancesTaskNotifications = None,
        project_id: int = None,
        runtime_conf: str = None,
        target: main_models.ListDataQualityEvaluationTaskInstancesResponseBodyPagingInfoDataQualityEvaluationTaskInstancesTaskTarget = None,
        trigger: main_models.ListDataQualityEvaluationTaskInstancesResponseBodyPagingInfoDataQualityEvaluationTaskInstancesTaskTrigger = None,
    ):
        # The description of the quality monitoring task.
        self.description = description
        # The callback settings in the lifecycle of the data quality evaluation task instance. Currently, only one Hook for blocking scheduled tasks is supported.
        self.hooks = hooks
        # The ID of the data quality evaluation task.
        self.id = id
        # The name of the quality monitoring task.
        # 
        # This parameter is required.
        self.name = name
        # The notification subscription configuration.
        self.notifications = notifications
        # The ID of the project workspace.
        self.project_id = project_id
        # Settings used when accessing data sources. Currently, only specifying the YARN queue of EMR and specifying the SQL engine as SPARK_SQL|KYUUBI|PRESTO_SQL|HIVE_SQL when collecting EMR tables are supported.
        self.runtime_conf = runtime_conf
        # The monitoring object of the data quality evaluation task.
        self.target = target
        # The trigger configuration of the data quality evaluation task.
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
        if m.get('Description') is not None:
            self.description = m.get('Description')

        self.hooks = []
        if m.get('Hooks') is not None:
            for k1 in m.get('Hooks'):
                temp_model = main_models.ListDataQualityEvaluationTaskInstancesResponseBodyPagingInfoDataQualityEvaluationTaskInstancesTaskHooks()
                self.hooks.append(temp_model.from_map(k1))

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Notifications') is not None:
            temp_model = main_models.ListDataQualityEvaluationTaskInstancesResponseBodyPagingInfoDataQualityEvaluationTaskInstancesTaskNotifications()
            self.notifications = temp_model.from_map(m.get('Notifications'))

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('RuntimeConf') is not None:
            self.runtime_conf = m.get('RuntimeConf')

        if m.get('Target') is not None:
            temp_model = main_models.ListDataQualityEvaluationTaskInstancesResponseBodyPagingInfoDataQualityEvaluationTaskInstancesTaskTarget()
            self.target = temp_model.from_map(m.get('Target'))

        if m.get('Trigger') is not None:
            temp_model = main_models.ListDataQualityEvaluationTaskInstancesResponseBodyPagingInfoDataQualityEvaluationTaskInstancesTaskTrigger()
            self.trigger = temp_model.from_map(m.get('Trigger'))

        return self

class ListDataQualityEvaluationTaskInstancesResponseBodyPagingInfoDataQualityEvaluationTaskInstancesTaskTrigger(DaraModel):
    def __init__(
        self,
        task_ids: List[int] = None,
        type: str = None,
    ):
        # The IDs of scheduled task nodes.
        self.task_ids = task_ids
        # The type of event that can trigger the execution of the quality evaluation task.
        # - ByScheduledTaskInstance: A scheduled instance runs successfully.
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

class ListDataQualityEvaluationTaskInstancesResponseBodyPagingInfoDataQualityEvaluationTaskInstancesTaskTarget(DaraModel):
    def __init__(
        self,
        database_type: str = None,
        partition_spec: str = None,
        table_guid: str = None,
        type: str = None,
    ):
        # For a dataset of table type, the database type to which the table belongs.
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
        # The type of the monitoring object.
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

class ListDataQualityEvaluationTaskInstancesResponseBodyPagingInfoDataQualityEvaluationTaskInstancesTaskNotifications(DaraModel):
    def __init__(
        self,
        condition: str = None,
        notifications: List[main_models.ListDataQualityEvaluationTaskInstancesResponseBodyPagingInfoDataQualityEvaluationTaskInstancesTaskNotificationsNotifications] = None,
    ):
        # The trigger condition of the notification.
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
                temp_model = main_models.ListDataQualityEvaluationTaskInstancesResponseBodyPagingInfoDataQualityEvaluationTaskInstancesTaskNotificationsNotifications()
                self.notifications.append(temp_model.from_map(k1))

        return self

class ListDataQualityEvaluationTaskInstancesResponseBodyPagingInfoDataQualityEvaluationTaskInstancesTaskNotificationsNotifications(DaraModel):
    def __init__(
        self,
        nofitication_receivers: List[main_models.ListDataQualityEvaluationTaskInstancesResponseBodyPagingInfoDataQualityEvaluationTaskInstancesTaskNotificationsNotificationsNofiticationReceivers] = None,
        notification_channels: List[main_models.ListDataQualityEvaluationTaskInstancesResponseBodyPagingInfoDataQualityEvaluationTaskInstancesTaskNotificationsNotificationsNotificationChannels] = None,
    ):
        # The alert recipient settings.
        self.nofitication_receivers = nofitication_receivers
        # The alert method.
        self.notification_channels = notification_channels

    def validate(self):
        if self.nofitication_receivers:
            for v1 in self.nofitication_receivers:
                 if v1:
                    v1.validate()
        if self.notification_channels:
            for v1 in self.notification_channels:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['NofiticationReceivers'] = []
        if self.nofitication_receivers is not None:
            for k1 in self.nofitication_receivers:
                result['NofiticationReceivers'].append(k1.to_map() if k1 else None)

        result['NotificationChannels'] = []
        if self.notification_channels is not None:
            for k1 in self.notification_channels:
                result['NotificationChannels'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.nofitication_receivers = []
        if m.get('NofiticationReceivers') is not None:
            for k1 in m.get('NofiticationReceivers'):
                temp_model = main_models.ListDataQualityEvaluationTaskInstancesResponseBodyPagingInfoDataQualityEvaluationTaskInstancesTaskNotificationsNotificationsNofiticationReceivers()
                self.nofitication_receivers.append(temp_model.from_map(k1))

        self.notification_channels = []
        if m.get('NotificationChannels') is not None:
            for k1 in m.get('NotificationChannels'):
                temp_model = main_models.ListDataQualityEvaluationTaskInstancesResponseBodyPagingInfoDataQualityEvaluationTaskInstancesTaskNotificationsNotificationsNotificationChannels()
                self.notification_channels.append(temp_model.from_map(k1))

        return self

class ListDataQualityEvaluationTaskInstancesResponseBodyPagingInfoDataQualityEvaluationTaskInstancesTaskNotificationsNotificationsNotificationChannels(DaraModel):
    def __init__(
        self,
        channels: List[str] = None,
    ):
        # The alert method.
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

class ListDataQualityEvaluationTaskInstancesResponseBodyPagingInfoDataQualityEvaluationTaskInstancesTaskNotificationsNotificationsNofiticationReceivers(DaraModel):
    def __init__(
        self,
        extension: str = None,
        receiver_type: str = None,
        receiver_values: List[str] = None,
    ):
        # The extension information, in JSON format. For example, a DingTalk bot supports at-all.
        self.extension = extension
        # The type of the alert recipient.
        # - AliUid - The UID of the Alibaba Cloud account
        # - WebhookUrl - A custom webhook URL
        # - DingdingUrl - The URL of a DingTalk bot
        # - FeishuUrl - The URL of a Lark bot
        # - WeixinUrl - The URL of a WeCom bot
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

class ListDataQualityEvaluationTaskInstancesResponseBodyPagingInfoDataQualityEvaluationTaskInstancesTaskHooks(DaraModel):
    def __init__(
        self,
        condition: str = None,
        type: str = None,
    ):
        # The trigger condition of the Hook.
        self.condition = condition
        # The type of the subsequent processing action.
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

