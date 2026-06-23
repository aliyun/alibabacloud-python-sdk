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
        # 质量校验任务分页查询结果
        self.paging_info = paging_info
        # API请求ID
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
        # 质量校验任务
        self.data_quality_evaluation_tasks = data_quality_evaluation_tasks
        # 页码
        self.page_number = page_number
        # 页大小
        self.page_size = page_size
        # 总条数
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
        # 数据质量校验任务描述，最长65535个字符
        self.description = description
        # 数据质量校验任务实例生命周期中的回调设置，目前只支持一个阻塞调度任务的Hook
        self.hooks = hooks
        # 数据质量校验任务ID
        self.id = id
        # 数据质量校验任务名称，数字、英文字母、汉字、半角全角标点符号组合，最长255个字符。
        self.name = name
        # 告警配置
        self.notifications = notifications
        # DataWorks工作空间ID
        self.project_id = project_id
        # 使用数据源时的一些设置，目前只支持指定EMR的yarn队列、采集EMR表时SQL引擎指定为SPARK_SQL|KYUUBI|PRESTO_SQL|HIVE_SQL
        self.runtime_conf = runtime_conf
        # 数据质量校验任务的监控对象
        self.target = target
        # 数据质量校验任务的触发配置
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
        # type=ByScheduledTaskInstance时生效
        # ,具体指明哪些调度节点的实例执行成功后可以触发
        self.task_ids = task_ids
        # 何种事件可以触发质量校验任务执行
        # 
        # - ByScheduledTaskInstance：调度实例运行成功
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
        # 表类型的数据集，表所属的数据库类型
        # - maxcompute
        # - emr
        # - cdh
        # - hologres
        # - analyticdb_for_postgresql
        # - analyticdb_for_mysql
        # - starrocks
        self.database_type = database_type
        # 分区表的分区设置
        self.partition_spec = partition_spec
        # 表在数据地图中的唯一ID
        self.table_guid = table_guid
        # 监控对象类型
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
        # Notification触发条件
        self.condition = condition
        # 具体的告警设置
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
        # 告警方式配置
        self.notification_channels = notification_channels
        # 告警接收人配置
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
        # 扩展信息，格式为 json，例如钉钉机器人支持 at 所有人
        self.extension = extension
        # 告警接收人类型
        # - AliUid - 阿里云账号Uid
        # - WebhookUrl - 自定义 webhook URL
        # - DingdingUrl - 钉钉机器人Url
        # - FeishuUrl - 飞书机器人Url
        # - WeixinUrl - 企微机器人Url
        self.receiver_type = receiver_type
        # 告警接收人具体值
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
        # 告警方式
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
        # Hook触发条件
        self.condition = condition
        # 后续处理动作类型
        # - BlockTaskInstance：阻塞DataWorks任务实例执行
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

