# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_wyota20210420 import models as main_models
from darabonba.model import DaraModel

class SendOpsMessageToTerminalsResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: List[main_models.SendOpsMessageToTerminalsResponseBodyData] = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
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

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

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
                temp_model = main_models.SendOpsMessageToTerminalsResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class SendOpsMessageToTerminalsResponseBodyData(DaraModel):
    def __init__(
        self,
        fail_reason: str = None,
        result: str = None,
        serial_number: str = None,
        success: bool = None,
        uuid: str = None,
    ):
        self.fail_reason = fail_reason
        self.result = result
        self.serial_number = serial_number
        self.success = success
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.fail_reason is not None:
            result['FailReason'] = self.fail_reason

        if self.result is not None:
            result['Result'] = self.result

        if self.serial_number is not None:
            result['SerialNumber'] = self.serial_number

        if self.success is not None:
            result['Success'] = self.success

        if self.uuid is not None:
            result['Uuid'] = self.uuid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FailReason') is not None:
            self.fail_reason = m.get('FailReason')

        if m.get('Result') is not None:
            self.result = m.get('Result')

        if m.get('SerialNumber') is not None:
            self.serial_number = m.get('SerialNumber')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')

        return self

