# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_qualitycheck20190115 import models as main_models
from darabonba.model import DaraModel

class ListWarningStrategyConfigResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        count: int = None,
        data: main_models.ListWarningStrategyConfigResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.count = count
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

        if self.count is not None:
            result['Count'] = self.count

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

        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('Data') is not None:
            temp_model = main_models.ListWarningStrategyConfigResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListWarningStrategyConfigResponseBodyData(DaraModel):
    def __init__(
        self,
        data: List[main_models.ListWarningStrategyConfigResponseBodyDataData] = None,
    ):
        self.data = data

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
        result['data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['data'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('data') is not None:
            for k1 in m.get('data'):
                temp_model = main_models.ListWarningStrategyConfigResponseBodyDataData()
                self.data.append(temp_model.from_map(k1))

        return self

class ListWarningStrategyConfigResponseBodyDataData(DaraModel):
    def __init__(
        self,
        id: int = None,
        interval_time: int = None,
        lambda_: str = None,
        level: int = None,
        max_number: int = None,
        name: str = None,
    ):
        self.id = id
        self.interval_time = interval_time
        self.lambda_ = lambda_
        self.level = level
        self.max_number = max_number
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.interval_time is not None:
            result['IntervalTime'] = self.interval_time

        if self.lambda_ is not None:
            result['Lambda'] = self.lambda_

        if self.level is not None:
            result['Level'] = self.level

        if self.max_number is not None:
            result['MaxNumber'] = self.max_number

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('IntervalTime') is not None:
            self.interval_time = m.get('IntervalTime')

        if m.get('Lambda') is not None:
            self.lambda_ = m.get('Lambda')

        if m.get('Level') is not None:
            self.level = m.get('Level')

        if m.get('MaxNumber') is not None:
            self.max_number = m.get('MaxNumber')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

