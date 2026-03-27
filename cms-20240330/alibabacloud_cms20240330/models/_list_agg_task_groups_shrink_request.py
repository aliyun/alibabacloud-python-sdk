# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListAggTaskGroupsShrinkRequest(DaraModel):
    def __init__(
        self,
        filter_agg_task_group_ids: str = None,
        filter_agg_task_group_names: str = None,
        max_results: int = None,
        next_token: str = None,
        query: str = None,
        status: str = None,
        tags_shrink: str = None,
        target_prometheus_id: str = None,
    ):
        # List of IDs for the aggregation task groups, which must be JSON parseable.
        self.filter_agg_task_group_ids = filter_agg_task_group_ids
        # List of names for the aggregation task groups, which must be JSON parseable.
        self.filter_agg_task_group_names = filter_agg_task_group_names
        # Maximum number of records to return.
        self.max_results = max_results
        # Query token.
        self.next_token = next_token
        # Name search, supports fuzzy matching.
        self.query = query
        # Status of the aggregation task group, either \\"Running\\" or \\"Stopped\\". Default is Running.
        self.status = status
        # Resource group tags.
        self.tags_shrink = tags_shrink
        # The target Prometheus instance ID for the aggregation task group.
        self.target_prometheus_id = target_prometheus_id

    def validate(self):
        pass

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

        if self.tags_shrink is not None:
            result['tags'] = self.tags_shrink

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

        if m.get('tags') is not None:
            self.tags_shrink = m.get('tags')

        if m.get('targetPrometheusId') is not None:
            self.target_prometheus_id = m.get('targetPrometheusId')

        return self

