# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aiccs20230516 import models as main_models
from darabonba.model import DaraModel

class AddBlacklistResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        model: main_models.AddBlacklistResponseBodyModel = None,
        request_id: str = None,
        success: str = None,
        timestamp: int = None,
    ):
        self.code = code
        self.message = message
        self.model = model
        self.request_id = request_id
        self.success = success
        self.timestamp = timestamp

    def validate(self):
        if self.model:
            self.model.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.message is not None:
            result['Message'] = self.message

        if self.model is not None:
            result['Model'] = self.model.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('Model') is not None:
            temp_model = main_models.AddBlacklistResponseBodyModel()
            self.model = temp_model.from_map(m.get('Model'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')

        return self

class AddBlacklistResponseBodyModel(DaraModel):
    def __init__(
        self,
        un_handle_numbers: List[str] = None,
    ):
        # 错误手机号
        self.un_handle_numbers = un_handle_numbers

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.un_handle_numbers is not None:
            result['UnHandleNumbers'] = self.un_handle_numbers

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UnHandleNumbers') is not None:
            self.un_handle_numbers = m.get('UnHandleNumbers')

        return self

