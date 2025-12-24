# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecs20140526 import models as main_models
from darabonba.model import DaraModel

class DescribeDiagnosticMetricSetsResponseBody(DaraModel):
    def __init__(
        self,
        metric_sets: List[main_models.DescribeDiagnosticMetricSetsResponseBodyMetricSets] = None,
        next_token: str = None,
        request_id: str = None,
    ):
        # The diagnostic metric sets.
        self.metric_sets = metric_sets
        # A pagination token. It can be used in the next request to retrieve a new page of results.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.metric_sets:
            for v1 in self.metric_sets:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['MetricSets'] = []
        if self.metric_sets is not None:
            for k1 in self.metric_sets:
                result['MetricSets'].append(k1.to_map() if k1 else None)

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.metric_sets = []
        if m.get('MetricSets') is not None:
            for k1 in m.get('MetricSets'):
                temp_model = main_models.DescribeDiagnosticMetricSetsResponseBodyMetricSets()
                self.metric_sets.append(temp_model.from_map(k1))

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeDiagnosticMetricSetsResponseBodyMetricSets(DaraModel):
    def __init__(
        self,
        description: str = None,
        metric_ids: List[str] = None,
        metric_set_id: str = None,
        metric_set_name: str = None,
        resource_type: str = None,
        type: str = None,
    ):
        # The description of the diagnostic metric set.
        self.description = description
        # The IDs of the diagnostic metrics.
        self.metric_ids = metric_ids
        # The ID of the diagnostic metric set.
        self.metric_set_id = metric_set_id
        # The name of the diagnostic metric set.
        self.metric_set_name = metric_set_name
        # The resource type supported by the diagnostic metric set.
        self.resource_type = resource_type
        # The type of the diagnostic metric set. Valid values:
        # 
        # *   User: user-defined diagnostic metric set
        # *   Common: common diagnostic metric set
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.metric_ids is not None:
            result['MetricIds'] = self.metric_ids

        if self.metric_set_id is not None:
            result['MetricSetId'] = self.metric_set_id

        if self.metric_set_name is not None:
            result['MetricSetName'] = self.metric_set_name

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('MetricIds') is not None:
            self.metric_ids = m.get('MetricIds')

        if m.get('MetricSetId') is not None:
            self.metric_set_id = m.get('MetricSetId')

        if m.get('MetricSetName') is not None:
            self.metric_set_name = m.get('MetricSetName')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

