# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any, List

from alibabacloud_aligenieip_1_0 import models as main_models
from darabonba.model import DaraModel

class CreateHotelAlarmResponseBody(DaraModel):
    def __init__(
        self,
        extentions: Dict[str, Any] = None,
        message: str = None,
        request_id: str = None,
        result: List[main_models.CreateHotelAlarmResponseBodyResult] = None,
        status_code: int = None,
    ):
        self.extentions = extentions
        self.message = message
        self.request_id = request_id
        self.result = result
        self.status_code = status_code

    def validate(self):
        if self.result:
            for v1 in self.result:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.extentions is not None:
            result['Extentions'] = self.extentions

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Result'] = []
        if self.result is not None:
            for k1 in self.result:
                result['Result'].append(k1.to_map() if k1 else None)

        if self.status_code is not None:
            result['StatusCode'] = self.status_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Extentions') is not None:
            self.extentions = m.get('Extentions')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.result = []
        if m.get('Result') is not None:
            for k1 in m.get('Result'):
                temp_model = main_models.CreateHotelAlarmResponseBodyResult()
                self.result.append(temp_model.from_map(k1))

        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')

        return self

class CreateHotelAlarmResponseBodyResult(DaraModel):
    def __init__(
        self,
        alarm_id: int = None,
        device_open_id: str = None,
        fail_msg: str = None,
        room_no: str = None,
        user_open_id: str = None,
    ):
        self.alarm_id = alarm_id
        self.device_open_id = device_open_id
        self.fail_msg = fail_msg
        self.room_no = room_no
        self.user_open_id = user_open_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alarm_id is not None:
            result['AlarmId'] = self.alarm_id

        if self.device_open_id is not None:
            result['DeviceOpenId'] = self.device_open_id

        if self.fail_msg is not None:
            result['FailMsg'] = self.fail_msg

        if self.room_no is not None:
            result['RoomNo'] = self.room_no

        if self.user_open_id is not None:
            result['UserOpenId'] = self.user_open_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlarmId') is not None:
            self.alarm_id = m.get('AlarmId')

        if m.get('DeviceOpenId') is not None:
            self.device_open_id = m.get('DeviceOpenId')

        if m.get('FailMsg') is not None:
            self.fail_msg = m.get('FailMsg')

        if m.get('RoomNo') is not None:
            self.room_no = m.get('RoomNo')

        if m.get('UserOpenId') is not None:
            self.user_open_id = m.get('UserOpenId')

        return self

