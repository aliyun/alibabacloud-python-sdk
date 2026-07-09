# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_agentloop20260520 import models as main_models
from darabonba.model import DaraModel

class ListEvaluatorsResponseBody(DaraModel):
    def __init__(
        self,
        evaluators: List[main_models.ListEvaluatorsResponseBodyEvaluators] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total: int = None,
    ):
        # The list of evaluator summaries.
        self.evaluators = evaluators
        # The number of entries per page used in this request.
        self.max_results = max_results
        # The pagination token for the next page.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The total number of evaluators that match the filter conditions.
        self.total = total

    def validate(self):
        if self.evaluators:
            for v1 in self.evaluators:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['evaluators'] = []
        if self.evaluators is not None:
            for k1 in self.evaluators:
                result['evaluators'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['maxResults'] = self.max_results

        if self.next_token is not None:
            result['nextToken'] = self.next_token

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.total is not None:
            result['total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.evaluators = []
        if m.get('evaluators') is not None:
            for k1 in m.get('evaluators'):
                temp_model = main_models.ListEvaluatorsResponseBodyEvaluators()
                self.evaluators.append(temp_model.from_map(k1))

        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('total') is not None:
            self.total = m.get('total')

        return self

class ListEvaluatorsResponseBodyEvaluators(DaraModel):
    def __init__(
        self,
        annotations: List[str] = None,
        created_at: int = None,
        description: str = None,
        display_name: str = None,
        latest_version: str = None,
        metric_name: str = None,
        name: str = None,
        properties: Dict[str, Any] = None,
        type: str = None,
        updated_at: int = None,
    ):
        # The list of annotations.
        self.annotations = annotations
        # The creation time, in seconds-level UNIX timestamp.
        self.created_at = created_at
        # The evaluator description.
        self.description = description
        # The display name.
        self.display_name = display_name
        # The latest version number.
        self.latest_version = latest_version
        # The metric name.
        self.metric_name = metric_name
        # The evaluator name.
        self.name = name
        # The evaluator properties.
        self.properties = properties
        # The evaluator type.
        self.type = type
        # The update time, in seconds-level UNIX timestamp.
        self.updated_at = updated_at

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.annotations is not None:
            result['annotations'] = self.annotations

        if self.created_at is not None:
            result['createdAt'] = self.created_at

        if self.description is not None:
            result['description'] = self.description

        if self.display_name is not None:
            result['displayName'] = self.display_name

        if self.latest_version is not None:
            result['latestVersion'] = self.latest_version

        if self.metric_name is not None:
            result['metricName'] = self.metric_name

        if self.name is not None:
            result['name'] = self.name

        if self.properties is not None:
            result['properties'] = self.properties

        if self.type is not None:
            result['type'] = self.type

        if self.updated_at is not None:
            result['updatedAt'] = self.updated_at

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('annotations') is not None:
            self.annotations = m.get('annotations')

        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('displayName') is not None:
            self.display_name = m.get('displayName')

        if m.get('latestVersion') is not None:
            self.latest_version = m.get('latestVersion')

        if m.get('metricName') is not None:
            self.metric_name = m.get('metricName')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('properties') is not None:
            self.properties = m.get('properties')

        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('updatedAt') is not None:
            self.updated_at = m.get('updatedAt')

        return self

