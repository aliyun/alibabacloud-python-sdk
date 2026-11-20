# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dyplsapi20170525 import models as main_models
from darabonba.model import DaraModel

class GetXDefaultConfigResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        data: main_models.GetXDefaultConfigResponseBodyData = None,
        message: str = None,
        success: bool = None,
    ):
        # The details about the access denial.
        self.access_denied_detail = access_denied_detail
        # The response status code. Valid values:
        # 
        # - 0000: Success.
        # 
        # - Other values: Failure.
        self.code = code
        # The default configurations of the work number.
        self.data = data
        # The response message.
        self.message = message
        # Indicates whether the request is successful. Valid values:
        # 
        # - true: The request is successful.
        # 
        # - false: The request fails.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail

        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.GetXDefaultConfigResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetXDefaultConfigResponseBodyData(DaraModel):
    def __init__(
        self,
        call_ability: str = None,
        gnflag: str = None,
        reach_json: List[main_models.GetXDefaultConfigResponseBodyDataReachJson] = None,
        sequence_call: List[main_models.GetXDefaultConfigResponseBodyDataSequenceCall] = None,
        sequence_end_time: str = None,
        sequence_start_time: str = None,
        sms_ability: str = None,
        sms_sign_mode: str = None,
    ):
        # The status of the call capability. Valid values: 0: disabled. 1: enabled.
        self.call_ability = call_ability
        # Specifies whether to pass through the caller ID to display the real caller. Valid values: 00: non-passthrough. The work number is displayed when calls are made to each other. 10: passthrough. When Customer A is the caller, the caller ID displayed to Employee B is the number of Customer A. When Employee B is the caller, the caller ID displayed to Customer A is the work number. Default value: 00.
        self.gnflag = gnflag
        # The enterprise business card rule control parameters.
        self.reach_json = reach_json
        # The sequential ringing control parameters.
        self.sequence_call = sequence_call
        # The end time of sequential ringing. Format: HH:mm:ss, such as 18:00:00.
        self.sequence_end_time = sequence_end_time
        # The start time of sequential ringing. Format: HH:mm:ss, such as 09:00:00.
        self.sequence_start_time = sequence_start_time
        # The status of the SMS feature. Valid values: 0: disabled. 1: enabled.
        self.sms_ability = sms_ability
        # Specifies whether to pass through the caller ID to display the real caller. Valid values: 00: non-passthrough. The work number is displayed when calls are made to each other. 10: passthrough. When Customer A is the caller, the caller ID displayed to Employee B is the number of Customer A. When Employee B is the caller, the caller ID displayed to Customer A is the work number. Default value: 00.
        self.sms_sign_mode = sms_sign_mode

    def validate(self):
        if self.reach_json:
            for v1 in self.reach_json:
                 if v1:
                    v1.validate()
        if self.sequence_call:
            for v1 in self.sequence_call:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.call_ability is not None:
            result['CallAbility'] = self.call_ability

        if self.gnflag is not None:
            result['GNFlag'] = self.gnflag

        result['ReachJson'] = []
        if self.reach_json is not None:
            for k1 in self.reach_json:
                result['ReachJson'].append(k1.to_map() if k1 else None)

        result['SequenceCall'] = []
        if self.sequence_call is not None:
            for k1 in self.sequence_call:
                result['SequenceCall'].append(k1.to_map() if k1 else None)

        if self.sequence_end_time is not None:
            result['SequenceEndTime'] = self.sequence_end_time

        if self.sequence_start_time is not None:
            result['SequenceStartTime'] = self.sequence_start_time

        if self.sms_ability is not None:
            result['SmsAbility'] = self.sms_ability

        if self.sms_sign_mode is not None:
            result['SmsSignMode'] = self.sms_sign_mode

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CallAbility') is not None:
            self.call_ability = m.get('CallAbility')

        if m.get('GNFlag') is not None:
            self.gnflag = m.get('GNFlag')

        self.reach_json = []
        if m.get('ReachJson') is not None:
            for k1 in m.get('ReachJson'):
                temp_model = main_models.GetXDefaultConfigResponseBodyDataReachJson()
                self.reach_json.append(temp_model.from_map(k1))

        self.sequence_call = []
        if m.get('SequenceCall') is not None:
            for k1 in m.get('SequenceCall'):
                temp_model = main_models.GetXDefaultConfigResponseBodyDataSequenceCall()
                self.sequence_call.append(temp_model.from_map(k1))

        if m.get('SequenceEndTime') is not None:
            self.sequence_end_time = m.get('SequenceEndTime')

        if m.get('SequenceStartTime') is not None:
            self.sequence_start_time = m.get('SequenceStartTime')

        if m.get('SmsAbility') is not None:
            self.sms_ability = m.get('SmsAbility')

        if m.get('SmsSignMode') is not None:
            self.sms_sign_mode = m.get('SmsSignMode')

        return self

class GetXDefaultConfigResponseBodyDataSequenceCall(DaraModel):
    def __init__(
        self,
        sequence_call_no_play_code: str = None,
        sequence_called_no: str = None,
        sequence_called_play_code: str = None,
    ):
        # The play code for the sequential ringing prompt tone. The format is the same as callNoPlayCode.
        self.sequence_call_no_play_code = sequence_call_no_play_code
        # The callee number for sequential ringing.
        self.sequence_called_no = sequence_called_no
        # The play code for the caller and callee after the call is connected. The format is the same as calledPlayCode.
        self.sequence_called_play_code = sequence_called_play_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.sequence_call_no_play_code is not None:
            result['SequenceCallNoPlayCode'] = self.sequence_call_no_play_code

        if self.sequence_called_no is not None:
            result['SequenceCalledNo'] = self.sequence_called_no

        if self.sequence_called_play_code is not None:
            result['SequenceCalledPlayCode'] = self.sequence_called_play_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SequenceCallNoPlayCode') is not None:
            self.sequence_call_no_play_code = m.get('SequenceCallNoPlayCode')

        if m.get('SequenceCalledNo') is not None:
            self.sequence_called_no = m.get('SequenceCalledNo')

        if m.get('SequenceCalledPlayCode') is not None:
            self.sequence_called_play_code = m.get('SequenceCalledPlayCode')

        return self

class GetXDefaultConfigResponseBodyDataReachJson(DaraModel):
    def __init__(
        self,
        call_dir: str = None,
        call_status: str = None,
        receive_dir: str = None,
        rule_id: str = None,
        rule_name: str = None,
        rule_type: str = None,
        temp_id: str = None,
    ):
        # The call direction. Valid values: 1: Employee B calls Customer A. 2: Customer A calls Employee B.
        self.call_dir = call_dir
        # The call status. Valid values: 1: ringing. 2: before connection. 3: after connection. 4: call ended. 5: connected. 6: not connected.
        self.call_status = call_status
        # The receive direction. Valid values: 1: caller. 2: callee.
        self.receive_dir = receive_dir
        # The rule ID.
        self.rule_id = rule_id
        # The rule name.
        self.rule_name = rule_name
        # The rule type. Valid values: 1: enterprise business card - SMS. 2: enterprise business card - flash SMS. 3: enterprise business card - video. 4: enterprise business card - audio.
        self.rule_type = rule_type
        # The template ID.
        self.temp_id = temp_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.call_dir is not None:
            result['CallDir'] = self.call_dir

        if self.call_status is not None:
            result['CallStatus'] = self.call_status

        if self.receive_dir is not None:
            result['ReceiveDir'] = self.receive_dir

        if self.rule_id is not None:
            result['RuleId'] = self.rule_id

        if self.rule_name is not None:
            result['RuleName'] = self.rule_name

        if self.rule_type is not None:
            result['RuleType'] = self.rule_type

        if self.temp_id is not None:
            result['TempId'] = self.temp_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CallDir') is not None:
            self.call_dir = m.get('CallDir')

        if m.get('CallStatus') is not None:
            self.call_status = m.get('CallStatus')

        if m.get('ReceiveDir') is not None:
            self.receive_dir = m.get('ReceiveDir')

        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')

        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')

        if m.get('RuleType') is not None:
            self.rule_type = m.get('RuleType')

        if m.get('TempId') is not None:
            self.temp_id = m.get('TempId')

        return self

