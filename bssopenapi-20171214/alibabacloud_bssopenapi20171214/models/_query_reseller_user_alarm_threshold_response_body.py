# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_bssopenapi20171214 import models as main_models
from darabonba.model import DaraModel

class QueryResellerUserAlarmThresholdResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        count: int = None,
        data: List[main_models.QueryResellerUserAlarmThresholdResponseBodyData] = None,
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

        if self.count is not None:
            result['Count'] = self.count

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

        if m.get('Count') is not None:
            self.count = m.get('Count')

        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.QueryResellerUserAlarmThresholdResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class QueryResellerUserAlarmThresholdResponseBodyData(DaraModel):
    def __init__(
        self,
        denominator: int = None,
        numerator: int = None,
        threshold_amount: str = None,
        threshold_type: int = None,
    ):
        self.denominator = denominator
        self.numerator = numerator
        self.threshold_amount = threshold_amount
        self.threshold_type = threshold_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.denominator is not None:
            result['Denominator'] = self.denominator

        if self.numerator is not None:
            result['Numerator'] = self.numerator

        if self.threshold_amount is not None:
            result['ThresholdAmount'] = self.threshold_amount

        if self.threshold_type is not None:
            result['ThresholdType'] = self.threshold_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Denominator') is not None:
            self.denominator = m.get('Denominator')

        if m.get('Numerator') is not None:
            self.numerator = m.get('Numerator')

        if m.get('ThresholdAmount') is not None:
            self.threshold_amount = m.get('ThresholdAmount')

        if m.get('ThresholdType') is not None:
            self.threshold_type = m.get('ThresholdType')

        return self

