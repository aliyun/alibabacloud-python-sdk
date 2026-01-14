# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class EditTaskShrinkRequest(DaraModel):
    def __init__(
        self,
        call_time_list_shrink: str = None,
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
        repeat_reason_shrink: str = None,
        repeat_times_shrink: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        send_sms_plan_shrink: str = None,
        status: int = None,
        task_id: int = None,
        template_id: int = None,
        template_type: int = None,
    ):
        # 外呼时间
        self.call_time_list_shrink = call_time_list_shrink
        # 回调地址
        self.callback_url = callback_url
        # 当发送闪信配置为1时，闪信模板ID必填
        self.flash_sms_template_id = flash_sms_template_id
        # 发送闪信配置,默认为0,0不发送闪信.1发送闪信
        self.flash_sms_type = flash_sms_type
        # 并发数
        self.max_concurrency = max_concurrency
        # 任务名称
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
        self.repeat_reason_shrink = repeat_reason_shrink
        # 重呼时间
        self.repeat_times_shrink = repeat_times_shrink
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # 短信发送规则
        self.send_sms_plan_shrink = send_sms_plan_shrink
        # 任务状态
        self.status = status
        # 任务id
        # 
        # This parameter is required.
        self.task_id = task_id
        # 话术模板ID
        self.template_id = template_id
        # 话术模板类型
        self.template_type = template_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.call_time_list_shrink is not None:
            result['CallTimeList'] = self.call_time_list_shrink

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

        if self.repeat_reason_shrink is not None:
            result['RepeatReason'] = self.repeat_reason_shrink

        if self.repeat_times_shrink is not None:
            result['RepeatTimes'] = self.repeat_times_shrink

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.send_sms_plan_shrink is not None:
            result['SendSmsPlan'] = self.send_sms_plan_shrink

        if self.status is not None:
            result['Status'] = self.status

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        if self.template_type is not None:
            result['TemplateType'] = self.template_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CallTimeList') is not None:
            self.call_time_list_shrink = m.get('CallTimeList')

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
            self.repeat_reason_shrink = m.get('RepeatReason')

        if m.get('RepeatTimes') is not None:
            self.repeat_times_shrink = m.get('RepeatTimes')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('SendSmsPlan') is not None:
            self.send_sms_plan_shrink = m.get('SendSmsPlan')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')

        return self

