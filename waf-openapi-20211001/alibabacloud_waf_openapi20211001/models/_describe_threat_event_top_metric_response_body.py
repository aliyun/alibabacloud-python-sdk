# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_waf_openapi20211001 import models as main_models
from darabonba.model import DaraModel

class DescribeThreatEventTopMetricResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        top_metrics: List[main_models.DescribeThreatEventTopMetricResponseBodyTopMetrics] = None,
    ):
        self.request_id = request_id
        self.top_metrics = top_metrics

    def validate(self):
        if self.top_metrics:
            for v1 in self.top_metrics:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['TopMetrics'] = []
        if self.top_metrics is not None:
            for k1 in self.top_metrics:
                result['TopMetrics'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.top_metrics = []
        if m.get('TopMetrics') is not None:
            for k1 in m.get('TopMetrics'):
                temp_model = main_models.DescribeThreatEventTopMetricResponseBodyTopMetrics()
                self.top_metrics.append(temp_model.from_map(k1))

        return self

class DescribeThreatEventTopMetricResponseBodyTopMetrics(DaraModel):
    def __init__(
        self,
        cnt: int = None,
        country: str = None,
        region: str = None,
        value: str = None,
    ):
        self.cnt = cnt
        self.country = country
        self.region = region
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cnt is not None:
            result['Cnt'] = self.cnt

        if self.country is not None:
            result['Country'] = self.country

        if self.region is not None:
            result['Region'] = self.region

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cnt') is not None:
            self.cnt = m.get('Cnt')

        if m.get('Country') is not None:
            self.country = m.get('Country')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

