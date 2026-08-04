# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_account_crm20160606 import models as main_models
from darabonba.model import DaraModel

class QueryEnumConfigByTypeResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.QueryEnumConfigByTypeResponseBodyData = None,
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
            temp_model = main_models.QueryEnumConfigByTypeResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class QueryEnumConfigByTypeResponseBodyData(DaraModel):
    def __init__(
        self,
        enum_config: List[main_models.QueryEnumConfigByTypeResponseBodyDataEnumConfig] = None,
    ):
        self.enum_config = enum_config

    def validate(self):
        if self.enum_config:
            for v1 in self.enum_config:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['EnumConfig'] = []
        if self.enum_config is not None:
            for k1 in self.enum_config:
                result['EnumConfig'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.enum_config = []
        if m.get('EnumConfig') is not None:
            for k1 in m.get('EnumConfig'):
                temp_model = main_models.QueryEnumConfigByTypeResponseBodyDataEnumConfig()
                self.enum_config.append(temp_model.from_map(k1))

        return self

class QueryEnumConfigByTypeResponseBodyDataEnumConfig(DaraModel):
    def __init__(
        self,
        enum_name: str = None,
        enum_value: str = None,
    ):
        self.enum_name = enum_name
        self.enum_value = enum_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enum_name is not None:
            result['enumName'] = self.enum_name

        if self.enum_value is not None:
            result['enumValue'] = self.enum_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('enumName') is not None:
            self.enum_name = m.get('enumName')

        if m.get('enumValue') is not None:
            self.enum_value = m.get('enumValue')

        return self

