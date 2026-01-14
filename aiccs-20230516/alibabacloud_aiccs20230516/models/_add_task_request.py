# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aiccs20230516 import models as main_models
from darabonba.model import DaraModel

class AddTaskRequest(DaraModel):
    def __init__(
        self,
        call_time_list: List[main_models.AddTaskRequestCallTimeList] = None,
        callback_url: str = None,
        flash_sms_template_id: int = None,
        flash_sms_type: int = None,
        max_concurrency: int = None,
        name: str = None,
        owner_id: int = None,
        play_sleep_val: int = None,
        play_times: int = None,
        recall_type: int = None,
        record_path: str = None,
        repeat_count: int = None,
        repeat_interval: int = None,
        repeat_reason: List[str] = None,
        repeat_times: List[str] = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        send_sms_plan: List[main_models.AddTaskRequestSendSmsPlan] = None,
        start_time: str = None,
        task_type: int = None,
        template_id: int = None,
        template_type: int = None,
    ):
        # 外呼时间
        self.call_time_list = call_time_list
        # 回调地址
        self.callback_url = callback_url
        # 当发送闪信配置为1时，闪信模板ID必填
        self.flash_sms_template_id = flash_sms_template_id
        # 发送闪信配置
        self.flash_sms_type = flash_sms_type
        # 并发数
        self.max_concurrency = max_concurrency
        # 任务名称
        # 
        # This parameter is required.
        self.name = name
        self.owner_id = owner_id
        # 播放间隔时长
        self.play_sleep_val = play_sleep_val
        # 录音播放次数
        self.play_times = play_times
        # 重呼配置
        self.recall_type = recall_type
        # 录音地址
        self.record_path = record_path
        # 重呼次数
        self.repeat_count = repeat_count
        # 重呼间隔
        self.repeat_interval = repeat_interval
        # 重呼条件
        self.repeat_reason = repeat_reason
        # 重呼时间
        self.repeat_times = repeat_times
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # 短信发送规则
        self.send_sms_plan = send_sms_plan
        # 任务启动日期
        self.start_time = start_time
        # 任务类型
        # 
        # This parameter is required.
        self.task_type = task_type
        # 话术模板ID
        self.template_id = template_id
        # 话术模板类型
        self.template_type = template_type

    def validate(self):
        if self.call_time_list:
            for v1 in self.call_time_list:
                 if v1:
                    v1.validate()
        if self.send_sms_plan:
            for v1 in self.send_sms_plan:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['CallTimeList'] = []
        if self.call_time_list is not None:
            for k1 in self.call_time_list:
                result['CallTimeList'].append(k1.to_map() if k1 else None)

        if self.callback_url is not None:
            result['CallbackUrl'] = self.callback_url

        if self.flash_sms_template_id is not None:
            result['FlashSmsTemplateId'] = self.flash_sms_template_id

        if self.flash_sms_type is not None:
            result['FlashSmsType'] = self.flash_sms_type

        if self.max_concurrency is not None:
            result['MaxConcurrency'] = self.max_concurrency

        if self.name is not None:
            result['Name'] = self.name

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.play_sleep_val is not None:
            result['PlaySleepVal'] = self.play_sleep_val

        if self.play_times is not None:
            result['PlayTimes'] = self.play_times

        if self.recall_type is not None:
            result['RecallType'] = self.recall_type

        if self.record_path is not None:
            result['RecordPath'] = self.record_path

        if self.repeat_count is not None:
            result['RepeatCount'] = self.repeat_count

        if self.repeat_interval is not None:
            result['RepeatInterval'] = self.repeat_interval

        if self.repeat_reason is not None:
            result['RepeatReason'] = self.repeat_reason

        if self.repeat_times is not None:
            result['RepeatTimes'] = self.repeat_times

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        result['SendSmsPlan'] = []
        if self.send_sms_plan is not None:
            for k1 in self.send_sms_plan:
                result['SendSmsPlan'].append(k1.to_map() if k1 else None)

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.task_type is not None:
            result['TaskType'] = self.task_type

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        if self.template_type is not None:
            result['TemplateType'] = self.template_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.call_time_list = []
        if m.get('CallTimeList') is not None:
            for k1 in m.get('CallTimeList'):
                temp_model = main_models.AddTaskRequestCallTimeList()
                self.call_time_list.append(temp_model.from_map(k1))

        if m.get('CallbackUrl') is not None:
            self.callback_url = m.get('CallbackUrl')

        if m.get('FlashSmsTemplateId') is not None:
            self.flash_sms_template_id = m.get('FlashSmsTemplateId')

        if m.get('FlashSmsType') is not None:
            self.flash_sms_type = m.get('FlashSmsType')

        if m.get('MaxConcurrency') is not None:
            self.max_concurrency = m.get('MaxConcurrency')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PlaySleepVal') is not None:
            self.play_sleep_val = m.get('PlaySleepVal')

        if m.get('PlayTimes') is not None:
            self.play_times = m.get('PlayTimes')

        if m.get('RecallType') is not None:
            self.recall_type = m.get('RecallType')

        if m.get('RecordPath') is not None:
            self.record_path = m.get('RecordPath')

        if m.get('RepeatCount') is not None:
            self.repeat_count = m.get('RepeatCount')

        if m.get('RepeatInterval') is not None:
            self.repeat_interval = m.get('RepeatInterval')

        if m.get('RepeatReason') is not None:
            self.repeat_reason = m.get('RepeatReason')

        if m.get('RepeatTimes') is not None:
            self.repeat_times = m.get('RepeatTimes')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        self.send_sms_plan = []
        if m.get('SendSmsPlan') is not None:
            for k1 in m.get('SendSmsPlan'):
                temp_model = main_models.AddTaskRequestSendSmsPlan()
                self.send_sms_plan.append(temp_model.from_map(k1))

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')

        return self

class AddTaskRequestSendSmsPlan(DaraModel):
    def __init__(
        self,
        intent_tags: List[str] = None,
        sms_template_id: int = None,
    ):
        # 意向标签
        self.intent_tags = intent_tags
        # 短信模板ID
        self.sms_template_id = sms_template_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.intent_tags is not None:
            result['IntentTags'] = self.intent_tags

        if self.sms_template_id is not None:
            result['SmsTemplateId'] = self.sms_template_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IntentTags') is not None:
            self.intent_tags = m.get('IntentTags')

        if m.get('SmsTemplateId') is not None:
            self.sms_template_id = m.get('SmsTemplateId')

        return self

class AddTaskRequestCallTimeList(DaraModel):
    def __init__(
        self,
        call_time: List[str] = None,
    ):
        self.call_time = call_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.call_time is not None:
            result['CallTime'] = self.call_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CallTime') is not None:
            self.call_time = m.get('CallTime')

        return self

