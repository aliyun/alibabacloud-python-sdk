# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aiccs20191015 import models as main_models
from darabonba.model import DaraModel

class ListRobotParamsResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: List[main_models.ListRobotParamsResponseBodyData] = None,
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
                temp_model = main_models.ListRobotParamsResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListRobotParamsResponseBodyData(DaraModel):
    def __init__(
        self,
        is_empty: int = None,
        param_code: str = None,
        param_name: str = None,
    ):
        self.is_empty = is_empty
        self.param_code = param_code
        self.param_name = param_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.is_empty is not None:
            result['IsEmpty'] = self.is_empty

        if self.param_code is not None:
            result['ParamCode'] = self.param_code

        if self.param_name is not None:
            result['ParamName'] = self.param_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsEmpty') is not None:
            self.is_empty = m.get('IsEmpty')

        if m.get('ParamCode') is not None:
            self.param_code = m.get('ParamCode')

        if m.get('ParamName') is not None:
            self.param_name = m.get('ParamName')

        return self

