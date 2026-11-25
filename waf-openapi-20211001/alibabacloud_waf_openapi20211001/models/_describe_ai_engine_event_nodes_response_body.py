# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_waf_openapi20211001 import models as main_models
from darabonba.model import DaraModel

class DescribeAiEngineEventNodesResponseBody(DaraModel):
    def __init__(
        self,
        items: List[main_models.DescribeAiEngineEventNodesResponseBodyItems] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The list of nodes.
        self.items = items
        # The number of entries to return on each page in a paging query. Valid values: 1 to 20. Default value: 20.
        self.max_results = max_results
        # The pagination token that is used to query the next page. If a next page exists, this field returns a value.
        # > If this parameter returns a value, a next page exists. You can use the returned **NextToken** as a request parameter to obtain the data on the next page until no value is returned, which indicates that all data is obtained.
        self.next_token = next_token
        # The ID of the request.
        self.request_id = request_id
        # The total number of nodes for the event.
        self.total_count = total_count

    def validate(self):
        if self.items:
            for v1 in self.items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['Items'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('Items') is not None:
            for k1 in m.get('Items'):
                temp_model = main_models.DescribeAiEngineEventNodesResponseBodyItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeAiEngineEventNodesResponseBodyItems(DaraModel):
    def __init__(
        self,
        node_detail: str = None,
        node_id: str = None,
        node_name: str = None,
        node_summary: str = None,
        node_tag: str = None,
        occurred_at: int = None,
    ):
        # The details of the node in the specified language. The details are in Markdown format.
        self.node_detail = node_detail
        # The node ID.
        self.node_id = node_id
        # The name of the node in the specified language.
        self.node_name = node_name
        # The summary of the node in the specified language.
        self.node_summary = node_summary
        # The node tag. Valid values:
        # 
        # - **bypass**: Suspected bypass.
        # 
        # - **protect**: Mitigated.
        # 
        # - **attempt**: Reconnaissance and probing.
        self.node_tag = node_tag
        # The time when the node occurred. The time is in the UNIX timestamp format. Unit: milliseconds.
        self.occurred_at = occurred_at

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.node_detail is not None:
            result['NodeDetail'] = self.node_detail

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        if self.node_name is not None:
            result['NodeName'] = self.node_name

        if self.node_summary is not None:
            result['NodeSummary'] = self.node_summary

        if self.node_tag is not None:
            result['NodeTag'] = self.node_tag

        if self.occurred_at is not None:
            result['OccurredAt'] = self.occurred_at

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NodeDetail') is not None:
            self.node_detail = m.get('NodeDetail')

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        if m.get('NodeName') is not None:
            self.node_name = m.get('NodeName')

        if m.get('NodeSummary') is not None:
            self.node_summary = m.get('NodeSummary')

        if m.get('NodeTag') is not None:
            self.node_tag = m.get('NodeTag')

        if m.get('OccurredAt') is not None:
            self.occurred_at = m.get('OccurredAt')

        return self

