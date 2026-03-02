# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_amqp20190901 import models as main_models
from darabonba.model import DaraModel

class GetAckInfoOfMessageResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: List[main_models.GetAckInfoOfMessageResponseBodyData] = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success

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

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.GetAckInfoOfMessageResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetAckInfoOfMessageResponseBodyData(DaraModel):
    def __init__(
        self,
        ack_error_info: str = None,
        ack_result: str = None,
        action: str = None,
        code: str = None,
        property: Dict[str, Any] = None,
        time_stamp: str = None,
    ):
        self.ack_error_info = ack_error_info
        self.ack_result = ack_result
        self.action = action
        self.code = code
        self.property = property
        self.time_stamp = time_stamp

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ack_error_info is not None:
            result['AckErrorInfo'] = self.ack_error_info

        if self.ack_result is not None:
            result['AckResult'] = self.ack_result

        if self.action is not None:
            result['Action'] = self.action

        if self.code is not None:
            result['Code'] = self.code

        if self.property is not None:
            result['Property'] = self.property

        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AckErrorInfo') is not None:
            self.ack_error_info = m.get('AckErrorInfo')

        if m.get('AckResult') is not None:
            self.ack_result = m.get('AckResult')

        if m.get('Action') is not None:
            self.action = m.get('Action')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Property') is not None:
            self.property = m.get('Property')

        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')

        return self

