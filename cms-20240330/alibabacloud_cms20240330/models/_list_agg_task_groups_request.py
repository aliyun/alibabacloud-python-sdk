# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cms20240330 import models as main_models
from darabonba.model import DaraModel

class ListAggTaskGroupsRequest(DaraModel):
    def __init__(
        self,
        filter_agg_task_group_ids: str = None,
        filter_agg_task_group_names: str = None,
        max_results: int = None,
        next_token: str = None,
        query: str = None,
        status: str = None,
        tags: List[main_models.ListAggTaskGroupsRequestTags] = None,
        target_prometheus_id: str = None,
    ):
        # A list of aggregation task group IDs. The value must be a string that can be parsed as a JSON array.
        self.filter_agg_task_group_ids = filter_agg_task_group_ids
        # A list of aggregation task group names. The value must be a string that can be parsed as a JSON array.
        self.filter_agg_task_group_names = filter_agg_task_group_names
        # The maximum number of entries to return on each page.
        self.max_results = max_results
        # The token that is used to retrieve the next page of results.
        self.next_token = next_token
        # The name to search for. Fuzzy search is supported.
        self.query = query
        # The status of the aggregation task group. Valid values are \\`Running\\` and \\`Stopped\\`. The default value is \\`Running\\`.
        self.status = status
        # The tags of the resource group.
        self.tags = tags
        # The ID of the target Prometheus instance for the aggregation task group.
        self.target_prometheus_id = target_prometheus_id

    def validate(self):
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.filter_agg_task_group_ids is not None:
            result['filterAggTaskGroupIds'] = self.filter_agg_task_group_ids

        if self.filter_agg_task_group_names is not None:
            result['filterAggTaskGroupNames'] = self.filter_agg_task_group_names

        if self.max_results is not None:
            result['maxResults'] = self.max_results

        if self.next_token is not None:
            result['nextToken'] = self.next_token

        if self.query is not None:
            result['query'] = self.query

        if self.status is not None:
            result['status'] = self.status

        result['tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['tags'].append(k1.to_map() if k1 else None)

        if self.target_prometheus_id is not None:
            result['targetPrometheusId'] = self.target_prometheus_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('filterAggTaskGroupIds') is not None:
            self.filter_agg_task_group_ids = m.get('filterAggTaskGroupIds')

        if m.get('filterAggTaskGroupNames') is not None:
            self.filter_agg_task_group_names = m.get('filterAggTaskGroupNames')

        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        if m.get('query') is not None:
            self.query = m.get('query')

        if m.get('status') is not None:
            self.status = m.get('status')

        self.tags = []
        if m.get('tags') is not None:
            for k1 in m.get('tags'):
                temp_model = main_models.ListAggTaskGroupsRequestTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('targetPrometheusId') is not None:
            self.target_prometheus_id = m.get('targetPrometheusId')

        return self

class ListAggTaskGroupsRequestTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of the resource group tag.
        self.key = key
        # The value of the resource group tag.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['key'] = self.key

        if self.value is not None:
            result['value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')

        if m.get('value') is not None:
            self.value = m.get('value')

        return self

