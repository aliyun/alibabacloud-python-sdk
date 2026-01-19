# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_xtee20210910 import models as main_models
from darabonba.model import DaraModel

class DescribeModelDetailsByIdResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result_object: List[main_models.DescribeModelDetailsByIdResponseBodyResultObject] = None,
    ):
        # Request ID.
        self.request_id = request_id
        # Returned result information
        self.result_object = result_object

    def validate(self):
        if self.result_object:
            for v1 in self.result_object:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['ResultObject'] = []
        if self.result_object is not None:
            for k1 in self.result_object:
                result['ResultObject'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.result_object = []
        if m.get('ResultObject') is not None:
            for k1 in m.get('ResultObject'):
                temp_model = main_models.DescribeModelDetailsByIdResponseBodyResultObject()
                self.result_object.append(temp_model.from_map(k1))

        return self

class DescribeModelDetailsByIdResponseBodyResultObject(DaraModel):
    def __init__(
        self,
        model_effect_evaluation: str = None,
    ):
        # Model prediction result.
        self.model_effect_evaluation = model_effect_evaluation

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.model_effect_evaluation is not None:
            result['modelEffectEvaluation'] = self.model_effect_evaluation

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('modelEffectEvaluation') is not None:
            self.model_effect_evaluation = m.get('modelEffectEvaluation')

        return self

