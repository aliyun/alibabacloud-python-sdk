# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aiccs20230516 import models as main_models
from darabonba.model import DaraModel

class TaskListResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: int = None,
        message: str = None,
        model: List[main_models.TaskListResponseBodyModel] = None,
        request_id: str = None,
        success: bool = None,
        timestamp: int = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.code = code
        self.message = message
        self.model = model
        self.request_id = request_id
        self.success = success
        self.timestamp = timestamp

    def validate(self):
        if self.model:
            for v1 in self.model:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail

        if self.code is not None:
            result['Code'] = self.code

        if self.message is not None:
            result['Message'] = self.message

        result['Model'] = []
        if self.model is not None:
            for k1 in self.model:
                result['Model'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        self.model = []
        if m.get('Model') is not None:
            for k1 in m.get('Model'):
                temp_model = main_models.TaskListResponseBodyModel()
                self.model.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')

        return self

class TaskListResponseBodyModel(DaraModel):
    def __init__(
        self,
        allow_call_time: str = None,
        allow_call_time_format: str = None,
        allow_day_of_week: str = None,
        call_type: int = None,
        create_time: str = None,
        flash_sms_template_id: int = None,
        flash_sms_template_name: str = None,
        flash_sms_type: int = None,
        import_time: str = None,
        intent_tags: List[main_models.TaskListResponseBodyModelIntentTags] = None,
        invalid_re_call: int = None,
        last_call_time: str = None,
        max_concurrency: int = None,
        personality_tags: List[str] = None,
        priority: int = None,
        properties: str = None,
        recall_type: int = None,
        send_sms: int = None,
        sms_name: str = None,
        status: int = None,
        task_id: int = None,
        task_name: str = None,
        template_id: str = None,
        template_name: str = None,
    ):
        # 外呼时间段
        self.allow_call_time = allow_call_time
        # 外呼时间段格式化
        self.allow_call_time_format = allow_call_time_format
        # 外呼时间
        self.allow_day_of_week = allow_day_of_week
        # 外呼类型
        self.call_type = call_type
        # 创建时间
        self.create_time = create_time
        # 闪信模板id
        self.flash_sms_template_id = flash_sms_template_id
        # 闪信模板名称
        self.flash_sms_template_name = flash_sms_template_name
        # 发送闪信配置，可选0，1；0表示否，1表示是
        self.flash_sms_type = flash_sms_type
        # 最近导入时间
        self.import_time = import_time
        # 意向标签列表
        self.intent_tags = intent_tags
        # 接通重呼次数
        self.invalid_re_call = invalid_re_call
        # 最后外呼时间
        self.last_call_time = last_call_time
        # 最大并发数
        self.max_concurrency = max_concurrency
        # 个性标签列表
        self.personality_tags = personality_tags
        # 优先任务
        self.priority = priority
        # 任务所需参数
        self.properties = properties
        # 自动重呼
        self.recall_type = recall_type
        # 发送短信
        self.send_sms = send_sms
        # 短信模板
        self.sms_name = sms_name
        # 任务状态
        self.status = status
        # 任务ID
        self.task_id = task_id
        # 任务名称
        self.task_name = task_name
        # 话术模板Id
        self.template_id = template_id
        # 话术模板名称
        self.template_name = template_name

    def validate(self):
        if self.intent_tags:
            for v1 in self.intent_tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.allow_call_time is not None:
            result['AllowCallTime'] = self.allow_call_time

        if self.allow_call_time_format is not None:
            result['AllowCallTimeFormat'] = self.allow_call_time_format

        if self.allow_day_of_week is not None:
            result['AllowDayOfWeek'] = self.allow_day_of_week

        if self.call_type is not None:
            result['CallType'] = self.call_type

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.flash_sms_template_id is not None:
            result['FlashSmsTemplateId'] = self.flash_sms_template_id

        if self.flash_sms_template_name is not None:
            result['FlashSmsTemplateName'] = self.flash_sms_template_name

        if self.flash_sms_type is not None:
            result['FlashSmsType'] = self.flash_sms_type

        if self.import_time is not None:
            result['ImportTime'] = self.import_time

        result['IntentTags'] = []
        if self.intent_tags is not None:
            for k1 in self.intent_tags:
                result['IntentTags'].append(k1.to_map() if k1 else None)

        if self.invalid_re_call is not None:
            result['InvalidReCall'] = self.invalid_re_call

        if self.last_call_time is not None:
            result['LastCallTime'] = self.last_call_time

        if self.max_concurrency is not None:
            result['MaxConcurrency'] = self.max_concurrency

        if self.personality_tags is not None:
            result['PersonalityTags'] = self.personality_tags

        if self.priority is not None:
            result['Priority'] = self.priority

        if self.properties is not None:
            result['Properties'] = self.properties

        if self.recall_type is not None:
            result['RecallType'] = self.recall_type

        if self.send_sms is not None:
            result['SendSms'] = self.send_sms

        if self.sms_name is not None:
            result['SmsName'] = self.sms_name

        if self.status is not None:
            result['Status'] = self.status

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.task_name is not None:
            result['TaskName'] = self.task_name

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        if self.template_name is not None:
            result['TemplateName'] = self.template_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllowCallTime') is not None:
            self.allow_call_time = m.get('AllowCallTime')

        if m.get('AllowCallTimeFormat') is not None:
            self.allow_call_time_format = m.get('AllowCallTimeFormat')

        if m.get('AllowDayOfWeek') is not None:
            self.allow_day_of_week = m.get('AllowDayOfWeek')

        if m.get('CallType') is not None:
            self.call_type = m.get('CallType')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('FlashSmsTemplateId') is not None:
            self.flash_sms_template_id = m.get('FlashSmsTemplateId')

        if m.get('FlashSmsTemplateName') is not None:
            self.flash_sms_template_name = m.get('FlashSmsTemplateName')

        if m.get('FlashSmsType') is not None:
            self.flash_sms_type = m.get('FlashSmsType')

        if m.get('ImportTime') is not None:
            self.import_time = m.get('ImportTime')

        self.intent_tags = []
        if m.get('IntentTags') is not None:
            for k1 in m.get('IntentTags'):
                temp_model = main_models.TaskListResponseBodyModelIntentTags()
                self.intent_tags.append(temp_model.from_map(k1))

        if m.get('InvalidReCall') is not None:
            self.invalid_re_call = m.get('InvalidReCall')

        if m.get('LastCallTime') is not None:
            self.last_call_time = m.get('LastCallTime')

        if m.get('MaxConcurrency') is not None:
            self.max_concurrency = m.get('MaxConcurrency')

        if m.get('PersonalityTags') is not None:
            self.personality_tags = m.get('PersonalityTags')

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        if m.get('Properties') is not None:
            self.properties = m.get('Properties')

        if m.get('RecallType') is not None:
            self.recall_type = m.get('RecallType')

        if m.get('SendSms') is not None:
            self.send_sms = m.get('SendSms')

        if m.get('SmsName') is not None:
            self.sms_name = m.get('SmsName')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')

        return self

class TaskListResponseBodyModelIntentTags(DaraModel):
    def __init__(
        self,
        intent_description: str = None,
        intent_tag: str = None,
    ):
        # 意向标签描述
        self.intent_description = intent_description
        # 意向标签ID
        self.intent_tag = intent_tag

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.intent_description is not None:
            result['IntentDescription'] = self.intent_description

        if self.intent_tag is not None:
            result['IntentTag'] = self.intent_tag

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IntentDescription') is not None:
            self.intent_description = m.get('IntentDescription')

        if m.get('IntentTag') is not None:
            self.intent_tag = m.get('IntentTag')

        return self

