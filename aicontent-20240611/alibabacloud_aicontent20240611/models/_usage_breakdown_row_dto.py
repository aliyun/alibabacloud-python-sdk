# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aicontent20240611 import models as main_models
from darabonba.model import DaraModel

class UsageBreakdownRowDTO(DaraModel):
    def __init__(
        self,
        client_id: int = None,
        client_name: str = None,
        metrics: List[main_models.MetricKVPairDTO] = None,
        model_code: str = None,
        model_id: int = None,
        model_name: str = None,
        model_type: str = None,
        summary_time: int = None,
    ):
        self.client_id = client_id
        self.client_name = client_name
        self.metrics = metrics
        self.model_code = model_code
        self.model_id = model_id
        self.model_name = model_name
        self.model_type = model_type
        self.summary_time = summary_time

    def validate(self):
        if self.metrics:
            for v1 in self.metrics:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_id is not None:
            result['clientId'] = self.client_id

        if self.client_name is not None:
            result['clientName'] = self.client_name

        result['metrics'] = []
        if self.metrics is not None:
            for k1 in self.metrics:
                result['metrics'].append(k1.to_map() if k1 else None)

        if self.model_code is not None:
            result['modelCode'] = self.model_code

        if self.model_id is not None:
            result['modelId'] = self.model_id

        if self.model_name is not None:
            result['modelName'] = self.model_name

        if self.model_type is not None:
            result['modelType'] = self.model_type

        if self.summary_time is not None:
            result['summaryTime'] = self.summary_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clientId') is not None:
            self.client_id = m.get('clientId')

        if m.get('clientName') is not None:
            self.client_name = m.get('clientName')

        self.metrics = []
        if m.get('metrics') is not None:
            for k1 in m.get('metrics'):
                temp_model = main_models.MetricKVPairDTO()
                self.metrics.append(temp_model.from_map(k1))

        if m.get('modelCode') is not None:
            self.model_code = m.get('modelCode')

        if m.get('modelId') is not None:
            self.model_id = m.get('modelId')

        if m.get('modelName') is not None:
            self.model_name = m.get('modelName')

        if m.get('modelType') is not None:
            self.model_type = m.get('modelType')

        if m.get('summaryTime') is not None:
            self.summary_time = m.get('summaryTime')

        return self

