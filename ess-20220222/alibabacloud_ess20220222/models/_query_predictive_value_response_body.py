# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ess20220222 import models as main_models
from darabonba.model import DaraModel

class QueryPredictiveValueResponseBody(DaraModel):
    def __init__(
        self,
        predictive_values: main_models.QueryPredictiveValueResponseBodyPredictiveValues = None,
        request_id: str = None,
    ):
        self.predictive_values = predictive_values
        self.request_id = request_id

    def validate(self):
        if self.predictive_values:
            self.predictive_values.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.predictive_values is not None:
            result['PredictiveValues'] = self.predictive_values.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PredictiveValues') is not None:
            temp_model = main_models.QueryPredictiveValueResponseBodyPredictiveValues()
            self.predictive_values = temp_model.from_map(m.get('PredictiveValues'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class QueryPredictiveValueResponseBodyPredictiveValues(DaraModel):
    def __init__(
        self,
        predictive_value: List[main_models.QueryPredictiveValueResponseBodyPredictiveValuesPredictiveValue] = None,
    ):
        self.predictive_value = predictive_value

    def validate(self):
        if self.predictive_value:
            for v1 in self.predictive_value:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['PredictiveValue'] = []
        if self.predictive_value is not None:
            for k1 in self.predictive_value:
                result['PredictiveValue'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.predictive_value = []
        if m.get('PredictiveValue') is not None:
            for k1 in m.get('PredictiveValue'):
                temp_model = main_models.QueryPredictiveValueResponseBodyPredictiveValuesPredictiveValue()
                self.predictive_value.append(temp_model.from_map(k1))

        return self

class QueryPredictiveValueResponseBodyPredictiveValuesPredictiveValue(DaraModel):
    def __init__(
        self,
        time: str = None,
        value: int = None,
    ):
        self.time = time
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.time is not None:
            result['Time'] = self.time

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Time') is not None:
            self.time = m.get('Time')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

