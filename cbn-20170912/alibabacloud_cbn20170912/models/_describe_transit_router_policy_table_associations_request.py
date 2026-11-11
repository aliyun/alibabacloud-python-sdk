# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cbn20170912 import models as main_models
from darabonba.model import DaraModel

class DescribeTransitRouterPolicyTableAssociationsRequest(DaraModel):
    def __init__(
        self,
        filter: List[main_models.DescribeTransitRouterPolicyTableAssociationsRequestFilter] = None,
        max_results: int = None,
        next_token: str = None,
    ):
        # The filter conditions. You can specify up to five filter conditions at a time.
        self.filter = filter
        # The number of entries to return per page. Valid values: 1 to 100.
        self.max_results = max_results
        # The token for the next query. Valid values:
        # 
        # - If **NextToken** is empty, no subsequent query is available.
        # - If a value is returned for **NextToken**, the value is the token for the next query.
        self.next_token = next_token

    def validate(self):
        if self.filter:
            for v1 in self.filter:
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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.filter = []
        if m.get('Filter') is not None:
            for k1 in m.get('Filter'):
                temp_model = main_models.DescribeTransitRouterPolicyTableAssociationsRequestFilter()
                self.filter.append(temp_model.from_map(k1))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        return self

class DescribeTransitRouterPolicyTableAssociationsRequestFilter(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: List[str] = None,
    ):
        # The filter condition. Valid values:
        # 
        # - **PolicyTableId**: the policy routing table ID.
        # - **AttachmentId**: the network connectivity instance ID.
        # - **AssociationId**: the policy routing table associate relationship instance ID.
        # 
        # By default, multiple filter conditions are connected by the **AND** logical operator. A result is returned only when all filter conditions are met.
        # 
        # You can specify up to five filter conditions at a time.
        self.key = key
        # The value of the filter condition.
        # 
        # Specify the filter value based on the **Key** parameter. You can specify multiple filter values for a single **Key**. Multiple filter values are connected by the **OR** logical operator. A result is returned when any of the filter values is met.
        # 
        # You can specify up to five filter values for a single filter condition.
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

