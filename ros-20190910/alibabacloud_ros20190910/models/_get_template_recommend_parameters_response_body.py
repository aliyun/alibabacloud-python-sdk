# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ros20190910 import models as main_models
from darabonba.model import DaraModel

class GetTemplateRecommendParametersResponseBody(DaraModel):
    def __init__(
        self,
        recommend_parameter_values: List[main_models.GetTemplateRecommendParametersResponseBodyRecommendParameterValues] = None,
        request_id: str = None,
    ):
        self.recommend_parameter_values = recommend_parameter_values
        self.request_id = request_id

    def validate(self):
        if self.recommend_parameter_values:
            for v1 in self.recommend_parameter_values:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['RecommendParameterValues'] = []
        if self.recommend_parameter_values is not None:
            for k1 in self.recommend_parameter_values:
                result['RecommendParameterValues'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.recommend_parameter_values = []
        if m.get('RecommendParameterValues') is not None:
            for k1 in m.get('RecommendParameterValues'):
                temp_model = main_models.GetTemplateRecommendParametersResponseBodyRecommendParameterValues()
                self.recommend_parameter_values.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetTemplateRecommendParametersResponseBodyRecommendParameterValues(DaraModel):
    def __init__(
        self,
        parameter_key: str = None,
        recommend_value: str = None,
    ):
        self.parameter_key = parameter_key
        self.recommend_value = recommend_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.parameter_key is not None:
            result['ParameterKey'] = self.parameter_key

        if self.recommend_value is not None:
            result['RecommendValue'] = self.recommend_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ParameterKey') is not None:
            self.parameter_key = m.get('ParameterKey')

        if m.get('RecommendValue') is not None:
            self.recommend_value = m.get('RecommendValue')

        return self

