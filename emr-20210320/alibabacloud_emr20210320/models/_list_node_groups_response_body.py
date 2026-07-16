# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_emr20210320 import models as main_models
from darabonba.model import DaraModel

class ListNodeGroupsResponseBody(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        node_groups: List[main_models.NodeGroup] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The maximum number of entries returned for the request.
        self.max_results = max_results
        # The token to retrieve the next page of results. An empty value indicates that all results have been returned.
        self.next_token = next_token
        # An array of node groups.
        self.node_groups = node_groups
        # The request ID.
        self.request_id = request_id
        # The total number of entries that match the query conditions.
        self.total_count = total_count

    def validate(self):
        if self.node_groups:
            for v1 in self.node_groups:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        result['NodeGroups'] = []
        if self.node_groups is not None:
            for k1 in self.node_groups:
                result['NodeGroups'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        self.node_groups = []
        if m.get('NodeGroups') is not None:
            for k1 in m.get('NodeGroups'):
                temp_model = main_models.NodeGroup()
                self.node_groups.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

