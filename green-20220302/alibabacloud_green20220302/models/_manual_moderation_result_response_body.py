# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_green20220302 import models as main_models
from darabonba.model import DaraModel

class ManualModerationResultResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: main_models.ManualModerationResultResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        # Error code.
        self.code = code
        # Returned data.
        self.data = data
        # Error message
        self.message = message
        # ID of the request
        self.request_id = request_id

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.ManualModerationResultResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ManualModerationResultResponseBodyData(DaraModel):
    def __init__(
        self,
        data_id: str = None,
        result: List[main_models.ManualModerationResultResponseBodyDataResult] = None,
        risk_level: str = None,
        task_id: str = None,
    ):
        # The value of dataId passed during the API request. This field will not be present if it was not provided during the request.
        self.data_id = data_id
        # Detailed label results.
        self.result = result
        # Risk level, returned based on the set high and low risk scores. Possible values include:
        # 
        # - high: High risk
        #  
        # - low: Low risk
        # 
        #  - none: No risk detected
        self.risk_level = risk_level
        # Task ID
        self.task_id = task_id

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
        if self.data_id is not None:
            result['DataId'] = self.data_id

        result['Result'] = []
        if self.result is not None:
            for k1 in self.result:
                result['Result'].append(k1.to_map() if k1 else None)

        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')

        self.result = []
        if m.get('Result') is not None:
            for k1 in m.get('Result'):
                temp_model = main_models.ManualModerationResultResponseBodyDataResult()
                self.result.append(temp_model.from_map(k1))

        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        return self

class ManualModerationResultResponseBodyDataResult(DaraModel):
    def __init__(
        self,
        description: str = None,
        label: str = None,
    ):
        # Label description
        self.description = description
        # Risk label
        self.label = label

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.label is not None:
            result['Label'] = self.label

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Label') is not None:
            self.label = m.get('Label')

        return self

