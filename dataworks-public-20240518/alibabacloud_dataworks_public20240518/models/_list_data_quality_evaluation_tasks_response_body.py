# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataworks_public20240518 import models as main_models
from darabonba.model import DaraModel

class ListDataQualityEvaluationTasksResponseBody(DaraModel):
    def __init__(
        self,
        paging_info: main_models.ListDataQualityEvaluationTasksResponseBodyPagingInfo = None,
        request_id: str = None,
    ):
        # The paged query result of quality evaluation nodes.
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
            temp_model = main_models.ListDataQualityEvaluationTasksResponseBodyPagingInfo()
            self.paging_info = temp_model.from_map(m.get('PagingInfo'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListDataQualityEvaluationTasksResponseBodyPagingInfo(DaraModel):
    def __init__(
        self,
        data_quality_evaluation_tasks: List[main_models.ListDataQualityEvaluationTasksResponseBodyPagingInfoDataQualityEvaluationTasks] = None,
        page_number: str = None,
        page_size: str = None,
        total_count: str = None,
    ):
        # The quality evaluation tasks.
        self.data_quality_evaluation_tasks = data_quality_evaluation_tasks
        # The page number.
        self.page_number = page_number
        # The page size.
        self.page_size = page_size
        # The total number of records.
        self.total_count = total_count

    def validate(self):
        if self.data_quality_evaluation_tasks:
            for v1 in self.data_quality_evaluation_tasks:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DataQualityEvaluationTasks'] = []
        if self.data_quality_evaluation_tasks is not None:
            for k1 in self.data_quality_evaluation_tasks:
                result['DataQualityEvaluationTasks'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_quality_evaluation_tasks = []
        if m.get('DataQualityEvaluationTasks') is not None:
            for k1 in m.get('DataQualityEvaluationTasks'):
                temp_model = main_models.ListDataQualityEvaluationTasksResponseBodyPagingInfoDataQualityEvaluationTasks()
                self.data_quality_evaluation_tasks.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListDataQualityEvaluationTasksResponseBodyPagingInfoDataQualityEvaluationTasks(DaraModel):
    def __init__(
        self,
        data_source_id: int = None,
        description: str = None,
        hooks: List[main_models.ListDataQualityEvaluationTasksResponseBodyPagingInfoDataQualityEvaluationTasksHooks] = None,
        id: int = None,
        name: str = None,
        notifications: main_models.ListDataQualityEvaluationTasksResponseBodyPagingInfoDataQualityEvaluationTasksNotifications = None,
        project_id: int = None,
        runtime_conf: str = None,
        target: main_models.ListDataQualityEvaluationTasksResponseBodyPagingInfoDataQualityEvaluationTasksTarget = None,
        trigger: main_models.ListDataQualityEvaluationTasksResponseBodyPagingInfoDataQualityEvaluationTasksTrigger = None,
    ):
        self.data_source_id = data_source_id
        # The description of the data quality evaluation task. The description can be up to 65,535 characters in length.
        self.description = description
        # The callback settings during the epoch of data quality evaluation task instances. Currently, only one hook that blocks a scheduling node instance is supported.
        self.hooks = hooks
        # The ID of the data quality evaluation task.
        self.id = id
        # The name of the data quality evaluation task. The name can contain digits, letters, Chinese characters, and half-width or full-width punctuation marks. The name can be up to 255 characters in length.
        self.name = name
        # The alert configuration.
        self.notifications = notifications
        # The DataWorks workspace ID.
        self.project_id = project_id
        # The runtime settings for data sources. Currently, only specifying the EMR YARN queue and the SQL engine for collecting EMR tables is supported. Valid SQL engine values: SPARK_SQL, KYUUBI, PRESTO_SQL, and HIVE_SQL.
        self.runtime_conf = runtime_conf
        # The monitored object of the data quality evaluation task.
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
                temp_model = main_models.ListDataQualityEvaluationTasksResponseBodyPagingInfoDataQualityEvaluationTasksHooks()
                self.hooks.append(temp_model.from_map(k1))

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Notifications') is not None:
            temp_model = main_models.ListDataQualityEvaluationTasksResponseBodyPagingInfoDataQualityEvaluationTasksNotifications()
            self.notifications = temp_model.from_map(m.get('Notifications'))

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('RuntimeConf') is not None:
            self.runtime_conf = m.get('RuntimeConf')

        if m.get('Target') is not None:
            temp_model = main_models.ListDataQualityEvaluationTasksResponseBodyPagingInfoDataQualityEvaluationTasksTarget()
            self.target = temp_model.from_map(m.get('Target'))

        if m.get('Trigger') is not None:
            temp_model = main_models.ListDataQualityEvaluationTasksResponseBodyPagingInfoDataQualityEvaluationTasksTrigger()
            self.trigger = temp_model.from_map(m.get('Trigger'))

        return self

class ListDataQualityEvaluationTasksResponseBodyPagingInfoDataQualityEvaluationTasksTrigger(DaraModel):
    def __init__(
        self,
        task_ids: List[int] = None,
        type: str = None,
    ):
        # This parameter takes effect when type is set to ByScheduledTaskInstance. Specifies the scheduled node IDs whose successful instance execution can trigger the task.
        self.task_ids = task_ids
        # The type of event that triggers the quality evaluation task. Valid values:
        # 
        # - ByScheduledTaskInstance: Triggered when a scheduled node instance runs successfully.
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

class ListDataQualityEvaluationTasksResponseBodyPagingInfoDataQualityEvaluationTasksTarget(DaraModel):
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
        # The unique ID of the table in DataWorks Data Map.
        self.table_guid = table_guid
        # The monitored object type. Valid values:
        # 
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

class ListDataQualityEvaluationTasksResponseBodyPagingInfoDataQualityEvaluationTasksNotifications(DaraModel):
    def __init__(
        self,
        condition: str = None,
        notifications: List[main_models.ListDataQualityEvaluationTasksResponseBodyPagingInfoDataQualityEvaluationTasksNotificationsNotifications] = None,
    ):
        # The cause that triggers the notification.
        self.condition = condition
        # The alert settings.
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
                temp_model = main_models.ListDataQualityEvaluationTasksResponseBodyPagingInfoDataQualityEvaluationTasksNotificationsNotifications()
                self.notifications.append(temp_model.from_map(k1))

        return self

class ListDataQualityEvaluationTasksResponseBodyPagingInfoDataQualityEvaluationTasksNotificationsNotifications(DaraModel):
    def __init__(
        self,
        notification_channels: List[main_models.ListDataQualityEvaluationTasksResponseBodyPagingInfoDataQualityEvaluationTasksNotificationsNotificationsNotificationChannels] = None,
        notification_receivers: List[main_models.ListDataQualityEvaluationTasksResponseBodyPagingInfoDataQualityEvaluationTasksNotificationsNotificationsNotificationReceivers] = None,
    ):
        # The alert channel configurations.
        self.notification_channels = notification_channels
        # The alert recipient configurations.
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
                temp_model = main_models.ListDataQualityEvaluationTasksResponseBodyPagingInfoDataQualityEvaluationTasksNotificationsNotificationsNotificationChannels()
                self.notification_channels.append(temp_model.from_map(k1))

        self.notification_receivers = []
        if m.get('NotificationReceivers') is not None:
            for k1 in m.get('NotificationReceivers'):
                temp_model = main_models.ListDataQualityEvaluationTasksResponseBodyPagingInfoDataQualityEvaluationTasksNotificationsNotificationsNotificationReceivers()
                self.notification_receivers.append(temp_model.from_map(k1))

        return self

class ListDataQualityEvaluationTasksResponseBodyPagingInfoDataQualityEvaluationTasksNotificationsNotificationsNotificationReceivers(DaraModel):
    def __init__(
        self,
        extension: str = None,
        receiver_type: str = None,
        receiver_values: List[str] = None,
    ):
        # The extension information in JSON format. For example, DingTalk chatbots support mentioning all members.
        self.extension = extension
        # The type of the alert recipient. Valid values:
        # - AliUid: Alibaba Cloud account UID.
        # - WebhookUrl: custom webhook URL.
        # - DingdingUrl: DingTalk chatbot URL.
        # - FeishuUrl: Lark chatbot URL.
        # - WeixinUrl: WeCom chatbot URL.
        self.receiver_type = receiver_type
        # The specific values of the alert recipients.
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

class ListDataQualityEvaluationTasksResponseBodyPagingInfoDataQualityEvaluationTasksNotificationsNotificationsNotificationChannels(DaraModel):
    def __init__(
        self,
        channels: List[str] = None,
    ):
        # The alert channel.
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

class ListDataQualityEvaluationTasksResponseBodyPagingInfoDataQualityEvaluationTasksHooks(DaraModel):
    def __init__(
        self,
        condition: str = None,
        type: str = None,
    ):
        # The cause that triggers the hook.
        self.condition = condition
        # The type of the follow-up action. Valid values:
        # - BlockTaskInstance: Blocks the execution of a DataWorks node instance.
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

