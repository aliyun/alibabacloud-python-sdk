# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class BatchRobotSmartCallRequest(DaraModel):
    def __init__(
        self,
        called_number: str = None,
        called_show_number: str = None,
        corp_name: str = None,
        dialog_id: str = None,
        early_media_asr: bool = None,
        is_self_line: bool = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        schedule_call: bool = None,
        schedule_time: int = None,
        task_name: str = None,
        tts_param: str = None,
        tts_param_head: str = None,
    ):
        # The called number. Only mobile phone numbers in the Chinese mainland are supported.
        # 
        # You can set up to 1,000 called numbers and separate the numbers with commas (,).
        # 
        # This parameter is required.
        self.called_number = called_number
        # The number displayed to called parties, which must be a number you purchased. You can view the numbers you purchased in the [Voice Messaging Service console](https://dyvms.console.aliyun.com/dyvms.htm#/number/normal).
        # 
        # You can set up to 100 numbers and separate the numbers with commas (,).
        # 
        # This parameter is required.
        self.called_show_number = called_show_number
        # The company name, which must be the same as the **company name** specified on the [qualification management page](https://dyvms.console.aliyun.com/dyvms.htm#/corp/normal).
        # 
        # > This parameter is optional if **isSelfLine** is set to **true**.
        self.corp_name = corp_name
        # The ID of the robot or communication script that is used to initiate a call.
        # 
        # You can obtain the **communication script ID** from the [Communication script management](https://dyvms.console.aliyun.com/dyvms.htm#/smart-call/saas/robot/list) page.
        # 
        # This parameter is required.
        self.dialog_id = dialog_id
        # The speech recognition identifier of early media. The default value is **false**, which means that the speech recognition identifier of early media is not enabled.
        # 
        # Set the parameter to **true** if you want to enable the speech recognition identifier of early media.
        self.early_media_asr = early_media_asr
        # Specifies whether to call the self-managed line. Default value: **false**.
        self.is_self_line = is_self_line
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # Specifies whether the call is scheduled. If you set this parameter to **true**, the **ScheduleTime** parameter is required.
        self.schedule_call = schedule_call
        # The preset call time. This value is a UNIX timestamp. Unit: milliseconds.
        # 
        # >  This parameter is required only when **ScheduleCall** is set to **true**.
        self.schedule_time = schedule_time
        # The task name. The task name can be up to 30 characters in length.
        # 
        # This parameter is required.
        self.task_name = task_name
        # The variable value of the TTS template, in the JSON format.
        # 
        # The variable value must correspond to a number. The TtsParam parameter must be used together with the TtsParamHead parameter.
        self.tts_param = tts_param
        # The call tasks with variables, in the JSON format.
        # 
        # The parameter value is a list of variable names. The TtsParamHead parameter must be used together with the TtsParam parameter.
        self.tts_param_head = tts_param_head

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.called_number is not None:
            result['CalledNumber'] = self.called_number

        if self.called_show_number is not None:
            result['CalledShowNumber'] = self.called_show_number

        if self.corp_name is not None:
            result['CorpName'] = self.corp_name

        if self.dialog_id is not None:
            result['DialogId'] = self.dialog_id

        if self.early_media_asr is not None:
            result['EarlyMediaAsr'] = self.early_media_asr

        if self.is_self_line is not None:
            result['IsSelfLine'] = self.is_self_line

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.schedule_call is not None:
            result['ScheduleCall'] = self.schedule_call

        if self.schedule_time is not None:
            result['ScheduleTime'] = self.schedule_time

        if self.task_name is not None:
            result['TaskName'] = self.task_name

        if self.tts_param is not None:
            result['TtsParam'] = self.tts_param

        if self.tts_param_head is not None:
            result['TtsParamHead'] = self.tts_param_head

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CalledNumber') is not None:
            self.called_number = m.get('CalledNumber')

        if m.get('CalledShowNumber') is not None:
            self.called_show_number = m.get('CalledShowNumber')

        if m.get('CorpName') is not None:
            self.corp_name = m.get('CorpName')

        if m.get('DialogId') is not None:
            self.dialog_id = m.get('DialogId')

        if m.get('EarlyMediaAsr') is not None:
            self.early_media_asr = m.get('EarlyMediaAsr')

        if m.get('IsSelfLine') is not None:
            self.is_self_line = m.get('IsSelfLine')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('ScheduleCall') is not None:
            self.schedule_call = m.get('ScheduleCall')

        if m.get('ScheduleTime') is not None:
            self.schedule_time = m.get('ScheduleTime')

        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')

        if m.get('TtsParam') is not None:
            self.tts_param = m.get('TtsParam')

        if m.get('TtsParamHead') is not None:
            self.tts_param_head = m.get('TtsParamHead')

        return self

