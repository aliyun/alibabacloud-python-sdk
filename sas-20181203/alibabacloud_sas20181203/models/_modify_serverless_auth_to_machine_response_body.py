# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class ModifyServerlessAuthToMachineResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.ModifyServerlessAuthToMachineResponseBodyData = None,
        request_id: str = None,
    ):
        # Details of the returned data.
        self.data = data
        # 本次调用请求的ID，是由阿里云为该请求生成的唯一标识符，可用于排查和定位问题。
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.ModifyServerlessAuthToMachineResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ModifyServerlessAuthToMachineResponseBodyData(DaraModel):
    def __init__(
        self,
        result_code: int = None,
    ):
        # Result code. Values:
        # - **0**: Success
        # - **1**: Parameter error
        self.result_code = result_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.result_code is not None:
            result['ResultCode'] = self.result_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResultCode') is not None:
            self.result_code = m.get('ResultCode')

        return self

