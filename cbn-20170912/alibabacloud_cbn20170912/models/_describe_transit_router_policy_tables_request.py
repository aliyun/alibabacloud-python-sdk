# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cbn20170912 import models as main_models
from darabonba.model import DaraModel

class DescribeTransitRouterPolicyTablesRequest(DaraModel):
    def __init__(
        self,
        filter: List[main_models.DescribeTransitRouterPolicyTablesRequestFilter] = None,
        max_results: int = None,
        next_token: str = None,
        tag: List[main_models.DescribeTransitRouterPolicyTablesRequestTag] = None,
        transit_router_id: str = None,
    ):
        # The filter conditions. You can specify up to 5 filter conditions at a time.
        self.filter = filter
        # The number of entries to return on each page. Valid values: 1 to 100. Default value: 20.
        self.max_results = max_results
        # The token that is used to retrieve the next page of results. Valid values:
        # 
        # If this is your first query or no next query is to be sent, ignore this parameter.
        # If a next query is to be sent, set the value to the NextToken value that is returned from the last API invocation.
        self.next_token = next_token
        self.tag = tag
        # The ID of the Enterprise Edition transit router.
        self.transit_router_id = transit_router_id

    def validate(self):
        if self.filter:
            for v1 in self.filter:
                 if v1:
                    v1.validate()
        if self.tag:
            for v1 in self.tag:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Filter'] = []
        if self.filter is not None:
            for k1 in self.filter:
                result['Filter'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        if self.transit_router_id is not None:
            result['TransitRouterId'] = self.transit_router_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.filter = []
        if m.get('Filter') is not None:
            for k1 in m.get('Filter'):
                temp_model = main_models.DescribeTransitRouterPolicyTablesRequestFilter()
                self.filter.append(temp_model.from_map(k1))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.DescribeTransitRouterPolicyTablesRequestTag()
                self.tag.append(temp_model.from_map(k1))

        if m.get('TransitRouterId') is not None:
            self.transit_router_id = m.get('TransitRouterId')

        return self

class DescribeTransitRouterPolicyTablesRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class DescribeTransitRouterPolicyTablesRequestFilter(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: List[str] = None,
    ):
        # The filter condition. Valid values:
        # 
        # PolicyTableId: the ID of the Cloud Enterprise Network (CEN) instance.
        # By default, multiple filter conditions are evaluated by using the AND operator. A result is returned only if all filter conditions are met.
        # 
        # You can specify up to 5 filter conditions at a time.
        self.key = key
        # The value of the filter condition.
        # 
        # Specify the value based on the key. You can specify multiple values for a key. Multiple values are evaluated by using the OR operator. If one of the values is met, the filter condition is met.
        # 
        # You can specify up to 5 values for each filter condition.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

