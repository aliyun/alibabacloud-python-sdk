# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_winnexo20260512 import models as main_models
from darabonba.model import DaraModel

class GetKnowledgeBaseSmartIndexConfigurationResponseBody(DaraModel):
    def __init__(
        self,
        artifacts: main_models.GetKnowledgeBaseSmartIndexConfigurationResponseBodyArtifacts = None,
        billing_id: str = None,
        code: str = None,
        directory_id: str = None,
        enabled: bool = None,
        last_error: str = None,
        last_success_task_id: str = None,
        lifecycle: str = None,
        message: str = None,
        request_id: str = None,
        revision: int = None,
        schedule: main_models.GetKnowledgeBaseSmartIndexConfigurationResponseBodySchedule = None,
        target_dir_id: str = None,
        task: main_models.GetKnowledgeBaseSmartIndexConfigurationResponseBodyTask = None,
    ):
        # 已发布产物引用
        self.artifacts = artifacts
        # 当前或最近任务账单标识
        self.billing_id = billing_id
        # 业务状态码：成功为 200，失败为后端错误码（ERR.* / InvalidParameter.*）
        self.code = code
        # 企业知识库根目录业务 ID
        self.directory_id = directory_id
        # 是否开启 LLM Wiki 智能索引
        self.enabled = enabled
        # 最近一次配置或扫描错误
        self.last_error = last_error
        # 最近成功任务标识
        self.last_success_task_id = last_success_task_id
        # 配置生命周期：DISABLED、ENABLED 或 DISABLING
        self.lifecycle = lifecycle
        # 错误描述，成功时为 success
        self.message = message
        # 请求追踪 ID
        self.request_id = request_id
        # 配置版本；更新时作为 expectedRevision 提交
        self.revision = revision
        # 自动执行计划
        self.schedule = schedule
        # 智能索引产物目录业务 ID
        self.target_dir_id = target_dir_id
        # 当前或最近任务状态
        self.task = task

    def validate(self):
        if self.artifacts:
            self.artifacts.validate()
        if self.schedule:
            self.schedule.validate()
        if self.task:
            self.task.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.artifacts is not None:
            result['artifacts'] = self.artifacts.to_map()

        if self.billing_id is not None:
            result['billingId'] = self.billing_id

        if self.code is not None:
            result['code'] = self.code

        if self.directory_id is not None:
            result['directoryId'] = self.directory_id

        if self.enabled is not None:
            result['enabled'] = self.enabled

        if self.last_error is not None:
            result['lastError'] = self.last_error

        if self.last_success_task_id is not None:
            result['lastSuccessTaskId'] = self.last_success_task_id

        if self.lifecycle is not None:
            result['lifecycle'] = self.lifecycle

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.revision is not None:
            result['revision'] = self.revision

        if self.schedule is not None:
            result['schedule'] = self.schedule.to_map()

        if self.target_dir_id is not None:
            result['targetDirId'] = self.target_dir_id

        if self.task is not None:
            result['task'] = self.task.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('artifacts') is not None:
            temp_model = main_models.GetKnowledgeBaseSmartIndexConfigurationResponseBodyArtifacts()
            self.artifacts = temp_model.from_map(m.get('artifacts'))

        if m.get('billingId') is not None:
            self.billing_id = m.get('billingId')

        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('directoryId') is not None:
            self.directory_id = m.get('directoryId')

        if m.get('enabled') is not None:
            self.enabled = m.get('enabled')

        if m.get('lastError') is not None:
            self.last_error = m.get('lastError')

        if m.get('lastSuccessTaskId') is not None:
            self.last_success_task_id = m.get('lastSuccessTaskId')

        if m.get('lifecycle') is not None:
            self.lifecycle = m.get('lifecycle')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('revision') is not None:
            self.revision = m.get('revision')

        if m.get('schedule') is not None:
            temp_model = main_models.GetKnowledgeBaseSmartIndexConfigurationResponseBodySchedule()
            self.schedule = temp_model.from_map(m.get('schedule'))

        if m.get('targetDirId') is not None:
            self.target_dir_id = m.get('targetDirId')

        if m.get('task') is not None:
            temp_model = main_models.GetKnowledgeBaseSmartIndexConfigurationResponseBodyTask()
            self.task = temp_model.from_map(m.get('task'))

        return self

class GetKnowledgeBaseSmartIndexConfigurationResponseBodyTask(DaraModel):
    def __init__(
        self,
        billing_id: str = None,
        billing_status: str = None,
        execution_status: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        last_error: str = None,
        operation: str = None,
        progress: int = None,
        report_status: str = None,
        reused: bool = None,
        task_key: str = None,
        trigger_type: str = None,
        usage_complete: bool = None,
    ):
        # 任务账单标识
        self.billing_id = billing_id
        # 任务计费状态
        self.billing_status = billing_status
        # 任务执行状态
        self.execution_status = execution_status
        # 任务创建时间，ISO 8601 格式
        self.gmt_create = gmt_create
        # 任务更新时间，ISO 8601 格式
        self.gmt_modified = gmt_modified
        # 最近一次任务错误
        self.last_error = last_error
        # 任务操作类型
        self.operation = operation
        # 任务执行进度
        self.progress = progress
        # 任务结果上报状态
        self.report_status = report_status
        # 是否复用已有任务
        self.reused = reused
        # 任务业务标识
        self.task_key = task_key
        # 任务触发类型
        self.trigger_type = trigger_type
        # 用量统计是否完成
        self.usage_complete = usage_complete

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.billing_id is not None:
            result['billingId'] = self.billing_id

        if self.billing_status is not None:
            result['billingStatus'] = self.billing_status

        if self.execution_status is not None:
            result['executionStatus'] = self.execution_status

        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified

        if self.last_error is not None:
            result['lastError'] = self.last_error

        if self.operation is not None:
            result['operation'] = self.operation

        if self.progress is not None:
            result['progress'] = self.progress

        if self.report_status is not None:
            result['reportStatus'] = self.report_status

        if self.reused is not None:
            result['reused'] = self.reused

        if self.task_key is not None:
            result['taskKey'] = self.task_key

        if self.trigger_type is not None:
            result['triggerType'] = self.trigger_type

        if self.usage_complete is not None:
            result['usageComplete'] = self.usage_complete

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('billingId') is not None:
            self.billing_id = m.get('billingId')

        if m.get('billingStatus') is not None:
            self.billing_status = m.get('billingStatus')

        if m.get('executionStatus') is not None:
            self.execution_status = m.get('executionStatus')

        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')

        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')

        if m.get('lastError') is not None:
            self.last_error = m.get('lastError')

        if m.get('operation') is not None:
            self.operation = m.get('operation')

        if m.get('progress') is not None:
            self.progress = m.get('progress')

        if m.get('reportStatus') is not None:
            self.report_status = m.get('reportStatus')

        if m.get('reused') is not None:
            self.reused = m.get('reused')

        if m.get('taskKey') is not None:
            self.task_key = m.get('taskKey')

        if m.get('triggerType') is not None:
            self.trigger_type = m.get('triggerType')

        if m.get('usageComplete') is not None:
            self.usage_complete = m.get('usageComplete')

        return self

class GetKnowledgeBaseSmartIndexConfigurationResponseBodySchedule(DaraModel):
    def __init__(
        self,
        cron_expression: str = None,
        next_run_at: str = None,
        timezone: str = None,
    ):
        # Cron 表达式；空表示手动执行
        self.cron_expression = cron_expression
        # 下次计划执行时间，ISO 8601 格式
        self.next_run_at = next_run_at
        # 计划使用的 IANA 时区
        self.timezone = timezone

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cron_expression is not None:
            result['cronExpression'] = self.cron_expression

        if self.next_run_at is not None:
            result['nextRunAt'] = self.next_run_at

        if self.timezone is not None:
            result['timezone'] = self.timezone

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cronExpression') is not None:
            self.cron_expression = m.get('cronExpression')

        if m.get('nextRunAt') is not None:
            self.next_run_at = m.get('nextRunAt')

        if m.get('timezone') is not None:
            self.timezone = m.get('timezone')

        return self

class GetKnowledgeBaseSmartIndexConfigurationResponseBodyArtifacts(DaraModel):
    def __init__(
        self,
        knowledge_insights: main_models.GetKnowledgeBaseSmartIndexConfigurationResponseBodyArtifactsKnowledgeInsights = None,
        topic_cards: main_models.GetKnowledgeBaseSmartIndexConfigurationResponseBodyArtifactsTopicCards = None,
        topic_graph: main_models.GetKnowledgeBaseSmartIndexConfigurationResponseBodyArtifactsTopicGraph = None,
        topic_overview: main_models.GetKnowledgeBaseSmartIndexConfigurationResponseBodyArtifactsTopicOverview = None,
    ):
        # 知识洞察
        self.knowledge_insights = knowledge_insights
        # 主题卡片目录
        self.topic_cards = topic_cards
        # 主题关系图
        self.topic_graph = topic_graph
        # 主题概览
        self.topic_overview = topic_overview

    def validate(self):
        if self.knowledge_insights:
            self.knowledge_insights.validate()
        if self.topic_cards:
            self.topic_cards.validate()
        if self.topic_graph:
            self.topic_graph.validate()
        if self.topic_overview:
            self.topic_overview.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.knowledge_insights is not None:
            result['knowledgeInsights'] = self.knowledge_insights.to_map()

        if self.topic_cards is not None:
            result['topicCards'] = self.topic_cards.to_map()

        if self.topic_graph is not None:
            result['topicGraph'] = self.topic_graph.to_map()

        if self.topic_overview is not None:
            result['topicOverview'] = self.topic_overview.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('knowledgeInsights') is not None:
            temp_model = main_models.GetKnowledgeBaseSmartIndexConfigurationResponseBodyArtifactsKnowledgeInsights()
            self.knowledge_insights = temp_model.from_map(m.get('knowledgeInsights'))

        if m.get('topicCards') is not None:
            temp_model = main_models.GetKnowledgeBaseSmartIndexConfigurationResponseBodyArtifactsTopicCards()
            self.topic_cards = temp_model.from_map(m.get('topicCards'))

        if m.get('topicGraph') is not None:
            temp_model = main_models.GetKnowledgeBaseSmartIndexConfigurationResponseBodyArtifactsTopicGraph()
            self.topic_graph = temp_model.from_map(m.get('topicGraph'))

        if m.get('topicOverview') is not None:
            temp_model = main_models.GetKnowledgeBaseSmartIndexConfigurationResponseBodyArtifactsTopicOverview()
            self.topic_overview = temp_model.from_map(m.get('topicOverview'))

        return self

class GetKnowledgeBaseSmartIndexConfigurationResponseBodyArtifactsTopicOverview(DaraModel):
    def __init__(
        self,
        source_id: str = None,
    ):
        # 产物资源业务 ID
        self.source_id = source_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.source_id is not None:
            result['sourceId'] = self.source_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('sourceId') is not None:
            self.source_id = m.get('sourceId')

        return self

class GetKnowledgeBaseSmartIndexConfigurationResponseBodyArtifactsTopicGraph(DaraModel):
    def __init__(
        self,
        source_id: str = None,
    ):
        # 产物资源业务 ID
        self.source_id = source_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.source_id is not None:
            result['sourceId'] = self.source_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('sourceId') is not None:
            self.source_id = m.get('sourceId')

        return self

class GetKnowledgeBaseSmartIndexConfigurationResponseBodyArtifactsTopicCards(DaraModel):
    def __init__(
        self,
        directory_id: str = None,
    ):
        # 产物目录业务 ID
        self.directory_id = directory_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.directory_id is not None:
            result['directoryId'] = self.directory_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('directoryId') is not None:
            self.directory_id = m.get('directoryId')

        return self

class GetKnowledgeBaseSmartIndexConfigurationResponseBodyArtifactsKnowledgeInsights(DaraModel):
    def __init__(
        self,
        source_id: str = None,
    ):
        # 产物资源业务 ID
        self.source_id = source_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.source_id is not None:
            result['sourceId'] = self.source_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('sourceId') is not None:
            self.source_id = m.get('sourceId')

        return self

