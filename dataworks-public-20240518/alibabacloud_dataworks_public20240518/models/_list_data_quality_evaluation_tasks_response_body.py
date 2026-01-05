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
        # The pagination information.
        self.paging_info = paging_info
        # The request ID.
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
        # The data quality monitoring tasks.
        self.data_quality_evaluation_tasks = data_quality_evaluation_tasks
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The total number of entries returned.
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
        # The description of the data quality monitoring task. The description can be up to 65,535 characters in length.
        self.description = description
        # The callback configurations of the task during the instance lifecycle. Blocking an auto triggered node is a type of callback event. Only this type is supported.
        self.hooks = hooks
        # The ID of the data quality monitoring task.
        self.id = id
        # The name of the data quality monitoring task. The name can be up to 255 characters in length and can contain digits, letters, and punctuation marks.
        self.name = name
        # The configurations for alert notifications.
        self.notifications = notifications
        # The DataWorks workspace ID.
        self.project_id = project_id
        # The configuration of the data source. The value of the queue field is default, and that of the sqlEngine field can be set to SPARK_SQL, KYUUBI, PRESTO_SQL, or HIVE_SQL. The value default indicates the YARN queue for E-MapReduce (EMR) tasks.
        self.runtime_conf = runtime_conf
        # The monitored object of the task.
        self.target = target
        # The trigger configuration of the task.
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
        # The IDs of the auto triggered nodes of which the instances are successfully run. This parameter takes effect only if the Type parameter is set to ByScheduledTaskInstance.
        self.task_ids = task_ids
        # The trigger condition of the task. Valid values:
        # 
        # *   ByScheduledTaskInstance. The value indicates that the task is triggered when the instance of an auto triggered node is successfully run.
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
        # The type of the database to which the table belongs. Valid values:
        # 
        # *   maxcompute
        # *   emr
        # *   cdh
        # *   hologres
        # *   analyticdb_for_postgresql
        # *   analyticdb_for_mysql
        # *   starrocks
        self.database_type = database_type
        # The configuration of the partitioned table.
        self.partition_spec = partition_spec
        # The ID of the table in Data Map.
        self.table_guid = table_guid
        # The type of the monitored object. Valid values:
        # 
        # *   Table
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
        # The trigger condition of the alert notification.
        self.condition = condition
        # The configurations for the alert notification.
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
        # The alert notification methods.
        self.notification_channels = notification_channels
        # The alert recipients.
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
        # The extended information in the JSON format. For example, the DingTalk chatbot can remind all members in a DingTalk group by using the at sign (@).
        self.extension = extension
        # The type of the alert recipient. Valid values:
        # 
        # *   AliUid: Alibaba Cloud account ID
        # *   WebhookUrl: URL of a custom webhook
        # *   DingdingUrl: DingTalk chatbot URL
        # *   FeishuUrl: Lark chatbot URL
        # *   WeixinUrl: WeCom chatbot URL
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

class ListDataQualityEvaluationTasksResponseBodyPagingInfoDataQualityEvaluationTasksNotificationsNotificationsNotificationChannels(DaraModel):
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

class ListDataQualityEvaluationTasksResponseBodyPagingInfoDataQualityEvaluationTasksHooks(DaraModel):
    def __init__(
        self,
        condition: str = None,
        type: str = None,
    ):
        # The trigger configuration of the callback event.
        self.condition = condition
        # The type of the callback event. Valid values:
        # 
        # *   BlockTaskInstance. The value indicates that an auto triggered node is blocked.
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

