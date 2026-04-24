# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

from alibabacloud_cms20240330 import models as main_models
from darabonba.model import DaraModel

class DescribeMetricMetaListResponseBody(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        resources: List[main_models.DescribeMetricMetaListResponseBodyResources] = None,
        total_count: int = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        # Id of the request
        self.request_id = request_id
        self.resources = resources
        self.total_count = total_count

    def validate(self):
        if self.resources:
            for v1 in self.resources:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['pageNumber'] = self.page_number

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.request_id is not None:
            result['requestId'] = self.request_id

        result['resources'] = []
        if self.resources is not None:
            for k1 in self.resources:
                result['resources'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['totalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        self.resources = []
        if m.get('resources') is not None:
            for k1 in m.get('resources'):
                temp_model = main_models.DescribeMetricMetaListResponseBodyResources()
                self.resources.append(temp_model.from_map(k1))

        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')

        return self

class DescribeMetricMetaListResponseBodyResources(DaraModel):
    def __init__(
        self,
        description: str = None,
        dimension_description: List[main_models.DescribeMetricMetaListResponseBodyResourcesDimensionDescription] = None,
        dimensions: List[str] = None,
        labels: Dict[str, str] = None,
        metric_name: str = None,
        namespace: str = None,
        periods: str = None,
        statistics: str = None,
        type: str = None,
        unit: str = None,
    ):
        self.description = description
        self.dimension_description = dimension_description
        self.dimensions = dimensions
        self.labels = labels
        self.metric_name = metric_name
        self.namespace = namespace
        self.periods = periods
        self.statistics = statistics
        self.type = type
        self.unit = unit

    def validate(self):
        if self.dimension_description:
            for v1 in self.dimension_description:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['description'] = self.description

        result['dimensionDescription'] = []
        if self.dimension_description is not None:
            for k1 in self.dimension_description:
                result['dimensionDescription'].append(k1.to_map() if k1 else None)

        if self.dimensions is not None:
            result['dimensions'] = self.dimensions

        if self.labels is not None:
            result['labels'] = self.labels

        if self.metric_name is not None:
            result['metricName'] = self.metric_name

        if self.namespace is not None:
            result['namespace'] = self.namespace

        if self.periods is not None:
            result['periods'] = self.periods

        if self.statistics is not None:
            result['statistics'] = self.statistics

        if self.type is not None:
            result['type'] = self.type

        if self.unit is not None:
            result['unit'] = self.unit

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')

        self.dimension_description = []
        if m.get('dimensionDescription') is not None:
            for k1 in m.get('dimensionDescription'):
                temp_model = main_models.DescribeMetricMetaListResponseBodyResourcesDimensionDescription()
                self.dimension_description.append(temp_model.from_map(k1))

        if m.get('dimensions') is not None:
            self.dimensions = m.get('dimensions')

        if m.get('labels') is not None:
            self.labels = m.get('labels')

        if m.get('metricName') is not None:
            self.metric_name = m.get('metricName')

        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')

        if m.get('periods') is not None:
            self.periods = m.get('periods')

        if m.get('statistics') is not None:
            self.statistics = m.get('statistics')

        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('unit') is not None:
            self.unit = m.get('unit')

        return self

class DescribeMetricMetaListResponseBodyResourcesDimensionDescription(DaraModel):
    def __init__(
        self,
        name: str = None,
    ):
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')

        return self

