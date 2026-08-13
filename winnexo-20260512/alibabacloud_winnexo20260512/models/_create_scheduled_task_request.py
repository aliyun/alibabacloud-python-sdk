# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_winnexo20260512 import models as main_models
from darabonba.model import DaraModel

class CreateScheduledTaskRequest(DaraModel):
    def __init__(
        self,
        collaboration_group_id: str = None,
        description: List[main_models.CreateScheduledTaskRequestDescription] = None,
        digital_employee_name: List[str] = None,
        is_open: bool = None,
        model: str = None,
        name: str = None,
        segments: List[main_models.CreateScheduledTaskRequestSegments] = None,
        task_detail: main_models.CreateScheduledTaskRequestTaskDetail = None,
        tenant_id: str = None,
        trigger_config: main_models.CreateScheduledTaskRequestTriggerConfig = None,
    ):
        # 所属协作群组 ID（如 cg_101）；传入时创建群空间任务（调用者需为有效群成员），为空创建个人任务
        self.collaboration_group_id = collaboration_group_id
        self.description = description
        # 数字员工名称列表
        self.digital_employee_name = digital_employee_name
        # 是否公开访问
        self.is_open = is_open
        # 执行模型档位，不传默认 standard
        self.model = model
        # 文件名
        # 
        # This parameter is required.
        self.name = name
        self.segments = segments
        self.task_detail = task_detail
        # 租户ID，公共参数，缺省时使用调用方默认租户
        self.tenant_id = tenant_id
        self.trigger_config = trigger_config

    def validate(self):
        if self.description:
            for v1 in self.description:
                 if v1:
                    v1.validate()
        if self.segments:
            for v1 in self.segments:
                 if v1:
                    v1.validate()
        if self.task_detail:
            self.task_detail.validate()
        if self.trigger_config:
            self.trigger_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.collaboration_group_id is not None:
            result['collaborationGroupId'] = self.collaboration_group_id

        result['description'] = []
        if self.description is not None:
            for k1 in self.description:
                result['description'].append(k1.to_map() if k1 else None)

        if self.digital_employee_name is not None:
            result['digitalEmployeeName'] = self.digital_employee_name

        if self.is_open is not None:
            result['isOpen'] = self.is_open

        if self.model is not None:
            result['model'] = self.model

        if self.name is not None:
            result['name'] = self.name

        result['segments'] = []
        if self.segments is not None:
            for k1 in self.segments:
                result['segments'].append(k1.to_map() if k1 else None)

        if self.task_detail is not None:
            result['taskDetail'] = self.task_detail.to_map()

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        if self.trigger_config is not None:
            result['triggerConfig'] = self.trigger_config.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('collaborationGroupId') is not None:
            self.collaboration_group_id = m.get('collaborationGroupId')

        self.description = []
        if m.get('description') is not None:
            for k1 in m.get('description'):
                temp_model = main_models.CreateScheduledTaskRequestDescription()
                self.description.append(temp_model.from_map(k1))

        if m.get('digitalEmployeeName') is not None:
            self.digital_employee_name = m.get('digitalEmployeeName')

        if m.get('isOpen') is not None:
            self.is_open = m.get('isOpen')

        if m.get('model') is not None:
            self.model = m.get('model')

        if m.get('name') is not None:
            self.name = m.get('name')

        self.segments = []
        if m.get('segments') is not None:
            for k1 in m.get('segments'):
                temp_model = main_models.CreateScheduledTaskRequestSegments()
                self.segments.append(temp_model.from_map(k1))

        if m.get('taskDetail') is not None:
            temp_model = main_models.CreateScheduledTaskRequestTaskDetail()
            self.task_detail = temp_model.from_map(m.get('taskDetail'))

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        if m.get('triggerConfig') is not None:
            temp_model = main_models.CreateScheduledTaskRequestTriggerConfig()
            self.trigger_config = temp_model.from_map(m.get('triggerConfig'))

        return self

class CreateScheduledTaskRequestTriggerConfig(DaraModel):
    def __init__(
        self,
        cron: str = None,
        language: str = None,
        push_config: List[main_models.CreateScheduledTaskRequestTriggerConfigPushConfig] = None,
        timezone: str = None,
        trigger_mode: str = None,
    ):
        # Cron 表达式，trigger_mode=scheduled 时必填，如 \"00 09 * * *\"
        self.cron = cron
        # 语言如 zh-CN|en-US，由服务端自动注入
        self.language = language
        # 任务推送频道列表；为空或无启用频道时不推送
        self.push_config = push_config
        # 时区如 Asia/Shanghai，由服务端自动注入
        self.timezone = timezone
        # 触发模式：manual|scheduled
        self.trigger_mode = trigger_mode

    def validate(self):
        if self.push_config:
            for v1 in self.push_config:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cron is not None:
            result['cron'] = self.cron

        if self.language is not None:
            result['language'] = self.language

        result['pushConfig'] = []
        if self.push_config is not None:
            for k1 in self.push_config:
                result['pushConfig'].append(k1.to_map() if k1 else None)

        if self.timezone is not None:
            result['timezone'] = self.timezone

        if self.trigger_mode is not None:
            result['triggerMode'] = self.trigger_mode

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cron') is not None:
            self.cron = m.get('cron')

        if m.get('language') is not None:
            self.language = m.get('language')

        self.push_config = []
        if m.get('pushConfig') is not None:
            for k1 in m.get('pushConfig'):
                temp_model = main_models.CreateScheduledTaskRequestTriggerConfigPushConfig()
                self.push_config.append(temp_model.from_map(k1))

        if m.get('timezone') is not None:
            self.timezone = m.get('timezone')

        if m.get('triggerMode') is not None:
            self.trigger_mode = m.get('triggerMode')

        return self

class CreateScheduledTaskRequestTriggerConfigPushConfig(DaraModel):
    def __init__(
        self,
        channel_type: str = None,
        content_scope: str = None,
        delivery_method: str = None,
        enabled: bool = None,
        file_format: str = None,
        operating_object_name: str = None,
        receiver_type: str = None,
    ):
        # 推送渠道
        self.channel_type = channel_type
        # 推送内容范围，默认 all_replies
        self.content_scope = content_scope
        # 推送方式，默认 channel_bot
        self.delivery_method = delivery_method
        # 是否推送该频道，默认关闭
        self.enabled = enabled
        # 产出文件推送格式，默认 file
        self.file_format = file_format
        # 发送机器人所属数字员工，必传且不可为空
        self.operating_object_name = operating_object_name
        # 接收人，当前仅支持 self
        self.receiver_type = receiver_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.channel_type is not None:
            result['channelType'] = self.channel_type

        if self.content_scope is not None:
            result['contentScope'] = self.content_scope

        if self.delivery_method is not None:
            result['deliveryMethod'] = self.delivery_method

        if self.enabled is not None:
            result['enabled'] = self.enabled

        if self.file_format is not None:
            result['fileFormat'] = self.file_format

        if self.operating_object_name is not None:
            result['operatingObjectName'] = self.operating_object_name

        if self.receiver_type is not None:
            result['receiverType'] = self.receiver_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('channelType') is not None:
            self.channel_type = m.get('channelType')

        if m.get('contentScope') is not None:
            self.content_scope = m.get('contentScope')

        if m.get('deliveryMethod') is not None:
            self.delivery_method = m.get('deliveryMethod')

        if m.get('enabled') is not None:
            self.enabled = m.get('enabled')

        if m.get('fileFormat') is not None:
            self.file_format = m.get('fileFormat')

        if m.get('operatingObjectName') is not None:
            self.operating_object_name = m.get('operatingObjectName')

        if m.get('receiverType') is not None:
            self.receiver_type = m.get('receiverType')

        return self

class CreateScheduledTaskRequestTaskDetail(DaraModel):
    def __init__(
        self,
        related_objects: List[main_models.CreateScheduledTaskRequestTaskDetailRelatedObjects] = None,
        related_semantics: List[main_models.CreateScheduledTaskRequestTaskDetailRelatedSemantics] = None,
        related_skills: List[main_models.CreateScheduledTaskRequestTaskDetailRelatedSkills] = None,
        task_understand: str = None,
    ):
        self.related_objects = related_objects
        self.related_semantics = related_semantics
        self.related_skills = related_skills
        # LLM 润色后的任务理解描述
        self.task_understand = task_understand

    def validate(self):
        if self.related_objects:
            for v1 in self.related_objects:
                 if v1:
                    v1.validate()
        if self.related_semantics:
            for v1 in self.related_semantics:
                 if v1:
                    v1.validate()
        if self.related_skills:
            for v1 in self.related_skills:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['relatedObjects'] = []
        if self.related_objects is not None:
            for k1 in self.related_objects:
                result['relatedObjects'].append(k1.to_map() if k1 else None)

        result['relatedSemantics'] = []
        if self.related_semantics is not None:
            for k1 in self.related_semantics:
                result['relatedSemantics'].append(k1.to_map() if k1 else None)

        result['relatedSkills'] = []
        if self.related_skills is not None:
            for k1 in self.related_skills:
                result['relatedSkills'].append(k1.to_map() if k1 else None)

        if self.task_understand is not None:
            result['taskUnderstand'] = self.task_understand

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.related_objects = []
        if m.get('relatedObjects') is not None:
            for k1 in m.get('relatedObjects'):
                temp_model = main_models.CreateScheduledTaskRequestTaskDetailRelatedObjects()
                self.related_objects.append(temp_model.from_map(k1))

        self.related_semantics = []
        if m.get('relatedSemantics') is not None:
            for k1 in m.get('relatedSemantics'):
                temp_model = main_models.CreateScheduledTaskRequestTaskDetailRelatedSemantics()
                self.related_semantics.append(temp_model.from_map(k1))

        self.related_skills = []
        if m.get('relatedSkills') is not None:
            for k1 in m.get('relatedSkills'):
                temp_model = main_models.CreateScheduledTaskRequestTaskDetailRelatedSkills()
                self.related_skills.append(temp_model.from_map(k1))

        if m.get('taskUnderstand') is not None:
            self.task_understand = m.get('taskUnderstand')

        return self

class CreateScheduledTaskRequestTaskDetailRelatedSkills(DaraModel):
    def __init__(
        self,
        display_name: str = None,
        name: str = None,
        skill_code: str = None,
        source_ids: List[str] = None,
    ):
        # 技能展示名称
        self.display_name = display_name
        # 文件名
        self.name = name
        # 技能代码
        self.skill_code = skill_code
        # sourceIds
        self.source_ids = source_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.display_name is not None:
            result['displayName'] = self.display_name

        if self.name is not None:
            result['name'] = self.name

        if self.skill_code is not None:
            result['skillCode'] = self.skill_code

        if self.source_ids is not None:
            result['sourceIds'] = self.source_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('displayName') is not None:
            self.display_name = m.get('displayName')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('skillCode') is not None:
            self.skill_code = m.get('skillCode')

        if m.get('sourceIds') is not None:
            self.source_ids = m.get('sourceIds')

        return self

class CreateScheduledTaskRequestTaskDetailRelatedSemantics(DaraModel):
    def __init__(
        self,
        attributes: str = None,
        entity: str = None,
    ):
        # 语义属性（JSON 字符串），用于语义检索时过滤
        self.attributes = attributes
        # 语义实体名，如客户/机会
        self.entity = entity

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.attributes is not None:
            result['attributes'] = self.attributes

        if self.entity is not None:
            result['entity'] = self.entity

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('attributes') is not None:
            self.attributes = m.get('attributes')

        if m.get('entity') is not None:
            self.entity = m.get('entity')

        return self

class CreateScheduledTaskRequestTaskDetailRelatedObjects(DaraModel):
    def __init__(
        self,
        mention_type: str = None,
        name: str = None,
        object_id: str = None,
        object_type: str = None,
    ):
        # 提及类型，如 objects
        self.mention_type = mention_type
        # 文件名
        self.name = name
        # 对象 ID（@指定时有值）
        self.object_id = object_id
        # 对象类型，如 customer、company
        self.object_type = object_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.mention_type is not None:
            result['mentionType'] = self.mention_type

        if self.name is not None:
            result['name'] = self.name

        if self.object_id is not None:
            result['objectId'] = self.object_id

        if self.object_type is not None:
            result['objectType'] = self.object_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('mentionType') is not None:
            self.mention_type = m.get('mentionType')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('objectId') is not None:
            self.object_id = m.get('objectId')

        if m.get('objectType') is not None:
            self.object_type = m.get('objectType')

        return self

class CreateScheduledTaskRequestSegments(DaraModel):
    def __init__(
        self,
        content: str = None,
        enabled: bool = None,
        name: str = None,
        object_id: str = None,
        object_type: str = None,
        skill_code: str = None,
        type: str = None,
    ):
        # 文本内容，type=text 时必填
        self.content = content
        # 功能开关，type=web_search 时可选
        self.enabled = enabled
        # 文件名
        self.name = name
        # 对象 ID，type=mention 时有值
        self.object_id = object_id
        # 对象类型如 customer，type=mention 时有值
        self.object_type = object_type
        # 技能编码，type=skill 时有值
        self.skill_code = skill_code
        # 元素类型：text|web_search|mention|skill
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['content'] = self.content

        if self.enabled is not None:
            result['enabled'] = self.enabled

        if self.name is not None:
            result['name'] = self.name

        if self.object_id is not None:
            result['objectId'] = self.object_id

        if self.object_type is not None:
            result['objectType'] = self.object_type

        if self.skill_code is not None:
            result['skillCode'] = self.skill_code

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')

        if m.get('enabled') is not None:
            self.enabled = m.get('enabled')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('objectId') is not None:
            self.object_id = m.get('objectId')

        if m.get('objectType') is not None:
            self.object_type = m.get('objectType')

        if m.get('skillCode') is not None:
            self.skill_code = m.get('skillCode')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

class CreateScheduledTaskRequestDescription(DaraModel):
    def __init__(
        self,
        content: str = None,
        enabled: bool = None,
        name: str = None,
        object_id: str = None,
        object_type: str = None,
        skill_code: str = None,
        type: str = None,
    ):
        # 文本内容，type=text 时必填
        self.content = content
        # 功能开关，type=web_search 时可选
        self.enabled = enabled
        # 文件名
        self.name = name
        # 对象 ID，type=mention 时有值
        self.object_id = object_id
        # 对象类型如 customer，type=mention 时有值
        self.object_type = object_type
        # 技能编码，type=skill 时有值
        self.skill_code = skill_code
        # 元素类型：text|web_search|mention|skill
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['content'] = self.content

        if self.enabled is not None:
            result['enabled'] = self.enabled

        if self.name is not None:
            result['name'] = self.name

        if self.object_id is not None:
            result['objectId'] = self.object_id

        if self.object_type is not None:
            result['objectType'] = self.object_type

        if self.skill_code is not None:
            result['skillCode'] = self.skill_code

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')

        if m.get('enabled') is not None:
            self.enabled = m.get('enabled')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('objectId') is not None:
            self.object_id = m.get('objectId')

        if m.get('objectType') is not None:
            self.object_type = m.get('objectType')

        if m.get('skillCode') is not None:
            self.skill_code = m.get('skillCode')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

