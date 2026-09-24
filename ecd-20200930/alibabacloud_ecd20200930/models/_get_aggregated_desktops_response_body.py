# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

from alibabacloud_ecd20200930 import models as main_models
from darabonba.model import DaraModel

class GetAggregatedDesktopsResponseBody(DaraModel):
    def __init__(
        self,
        aggregations: main_models.GetAggregatedDesktopsResponseBodyAggregations = None,
        request_id: str = None,
    ):
        # The list of aggregation field information.
        # >Notice: When you use an aggregate query, only aggregation results are returned. The list of matched metadata is not returned.
        self.aggregations = aggregations
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.aggregations:
            self.aggregations.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.aggregations is not None:
            result['Aggregations'] = self.aggregations.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Aggregations') is not None:
            temp_model = main_models.GetAggregatedDesktopsResponseBodyAggregations()
            self.aggregations = temp_model.from_map(m.get('Aggregations'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetAggregatedDesktopsResponseBodyAggregations(DaraModel):
    def __init__(
        self,
        desktop_aggregation: List[Dict[str, str]] = None,
    ):
        # The aggregation results.
        self.desktop_aggregation = desktop_aggregation

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.desktop_aggregation is not None:
            result['DesktopAggregation'] = self.desktop_aggregation

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DesktopAggregation') is not None:
            self.desktop_aggregation = m.get('DesktopAggregation')

        return self

