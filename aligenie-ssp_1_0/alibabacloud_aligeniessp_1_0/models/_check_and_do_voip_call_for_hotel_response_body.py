# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aligeniessp_1_0 import models as main_models
from darabonba.model import DaraModel

class CheckAndDoVoipCallForHotelResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        result: main_models.CheckAndDoVoipCallForHotelResponseBodyResult = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.result is not None:
            result['Result'] = self.result.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Result') is not None:
            temp_model = main_models.CheckAndDoVoipCallForHotelResponseBodyResult()
            self.result = temp_model.from_map(m.get('Result'))

        return self

class CheckAndDoVoipCallForHotelResponseBodyResult(DaraModel):
    def __init__(
        self,
        device_targets: main_models.CheckAndDoVoipCallForHotelResponseBodyResultDeviceTargets = None,
        is_start_call: bool = None,
        passed: bool = None,
        start_call_result: main_models.CheckAndDoVoipCallForHotelResponseBodyResultStartCallResult = None,
    ):
        self.device_targets = device_targets
        self.is_start_call = is_start_call
        self.passed = passed
        self.start_call_result = start_call_result

    def validate(self):
        if self.device_targets:
            self.device_targets.validate()
        if self.start_call_result:
            self.start_call_result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.device_targets is not None:
            result['DeviceTargets'] = self.device_targets.to_map()

        if self.is_start_call is not None:
            result['IsStartCall'] = self.is_start_call

        if self.passed is not None:
            result['Passed'] = self.passed

        if self.start_call_result is not None:
            result['StartCallResult'] = self.start_call_result.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceTargets') is not None:
            temp_model = main_models.CheckAndDoVoipCallForHotelResponseBodyResultDeviceTargets()
            self.device_targets = temp_model.from_map(m.get('DeviceTargets'))

        if m.get('IsStartCall') is not None:
            self.is_start_call = m.get('IsStartCall')

        if m.get('Passed') is not None:
            self.passed = m.get('Passed')

        if m.get('StartCallResult') is not None:
            temp_model = main_models.CheckAndDoVoipCallForHotelResponseBodyResultStartCallResult()
            self.start_call_result = temp_model.from_map(m.get('StartCallResult'))

        return self

class CheckAndDoVoipCallForHotelResponseBodyResultStartCallResult(DaraModel):
    def __init__(
        self,
        message: str = None,
        ret_code: int = None,
        ret_value: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        self.message = message
        self.ret_code = ret_code
        self.ret_value = ret_value
        self.success = success
        self.trace_id = trace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.message is not None:
            result['Message'] = self.message

        if self.ret_code is not None:
            result['RetCode'] = self.ret_code

        if self.ret_value is not None:
            result['RetValue'] = self.ret_value

        if self.success is not None:
            result['Success'] = self.success

        if self.trace_id is not None:
            result['TraceId'] = self.trace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RetCode') is not None:
            self.ret_code = m.get('RetCode')

        if m.get('RetValue') is not None:
            self.ret_value = m.get('RetValue')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')

        return self

class CheckAndDoVoipCallForHotelResponseBodyResultDeviceTargets(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: List[main_models.CheckAndDoVoipCallForHotelResponseBodyResultDeviceTargetsData] = None,
        msg: str = None,
    ):
        self.code = code
        self.data = data
        self.msg = msg

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.msg is not None:
            result['Msg'] = self.msg

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.CheckAndDoVoipCallForHotelResponseBodyResultDeviceTargetsData()
                self.data.append(temp_model.from_map(k1))

        if m.get('Msg') is not None:
            self.msg = m.get('Msg')

        return self

class CheckAndDoVoipCallForHotelResponseBodyResultDeviceTargetsData(DaraModel):
    def __init__(
        self,
        device_icon: str = None,
        device_name: str = None,
        device_type: str = None,
        online: bool = None,
        uuid: str = None,
    ):
        self.device_icon = device_icon
        self.device_name = device_name
        self.device_type = device_type
        self.online = online
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.device_icon is not None:
            result['DeviceIcon'] = self.device_icon

        if self.device_name is not None:
            result['DeviceName'] = self.device_name

        if self.device_type is not None:
            result['DeviceType'] = self.device_type

        if self.online is not None:
            result['Online'] = self.online

        if self.uuid is not None:
            result['Uuid'] = self.uuid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceIcon') is not None:
            self.device_icon = m.get('DeviceIcon')

        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')

        if m.get('DeviceType') is not None:
            self.device_type = m.get('DeviceType')

        if m.get('Online') is not None:
            self.online = m.get('Online')

        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')

        return self

