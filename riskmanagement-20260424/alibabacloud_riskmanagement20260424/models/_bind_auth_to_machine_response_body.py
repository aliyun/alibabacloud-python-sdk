# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_riskmanagement20260424 import models as main_models
from darabonba.model import DaraModel

class BindAuthToMachineResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.BindAuthToMachineResponseBodyData = None,
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
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

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

        if m.get('Data') is not None:
            temp_model = main_models.BindAuthToMachineResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class BindAuthToMachineResponseBodyData(DaraModel):
    def __init__(
        self,
        body: main_models.BindAuthToMachineResponseBodyDataBody = None,
    ):
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.body is not None:
            result['Body'] = self.body.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Body') is not None:
            temp_model = main_models.BindAuthToMachineResponseBodyDataBody()
            self.body = temp_model.from_map(m.get('Body'))

        return self

class BindAuthToMachineResponseBodyDataBody(DaraModel):
    def __init__(
        self,
        bind_count: int = None,
        insufficient_core_count: int = None,
        insufficient_ecs_count: int = None,
        request_id: str = None,
        result_code: int = None,
        un_bind_count: int = None,
    ):
        self.bind_count = bind_count
        self.insufficient_core_count = insufficient_core_count
        self.insufficient_ecs_count = insufficient_ecs_count
        self.request_id = request_id
        self.result_code = result_code
        self.un_bind_count = un_bind_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bind_count is not None:
            result['BindCount'] = self.bind_count

        if self.insufficient_core_count is not None:
            result['InsufficientCoreCount'] = self.insufficient_core_count

        if self.insufficient_ecs_count is not None:
            result['InsufficientEcsCount'] = self.insufficient_ecs_count

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.result_code is not None:
            result['ResultCode'] = self.result_code

        if self.un_bind_count is not None:
            result['UnBindCount'] = self.un_bind_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BindCount') is not None:
            self.bind_count = m.get('BindCount')

        if m.get('InsufficientCoreCount') is not None:
            self.insufficient_core_count = m.get('InsufficientCoreCount')

        if m.get('InsufficientEcsCount') is not None:
            self.insufficient_ecs_count = m.get('InsufficientEcsCount')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResultCode') is not None:
            self.result_code = m.get('ResultCode')

        if m.get('UnBindCount') is not None:
            self.un_bind_count = m.get('UnBindCount')

        return self

