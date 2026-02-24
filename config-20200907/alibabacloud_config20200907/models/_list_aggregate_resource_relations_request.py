# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListAggregateResourceRelationsRequest(DaraModel):
    def __init__(
        self,
        aggregator_id: str = None,
        max_results: int = None,
        next_token: str = None,
        region: str = None,
        relation_type: str = None,
        resource_account_id: int = None,
        resource_id: str = None,
        resource_type: str = None,
        target_resource_id: str = None,
        target_resource_type: str = None,
    ):
        # This parameter is required.
        self.aggregator_id = aggregator_id
        self.max_results = max_results
        self.next_token = next_token
        # This parameter is required.
        self.region = region
        self.relation_type = relation_type
        # This parameter is required.
        self.resource_account_id = resource_account_id
        # This parameter is required.
        self.resource_id = resource_id
        # This parameter is required.
        self.resource_type = resource_type
        self.target_resource_id = target_resource_id
        self.target_resource_type = target_resource_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.aggregator_id is not None:
            result['AggregatorId'] = self.aggregator_id

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.region is not None:
            result['Region'] = self.region

        if self.relation_type is not None:
            result['RelationType'] = self.relation_type

        if self.resource_account_id is not None:
            result['ResourceAccountId'] = self.resource_account_id

        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.target_resource_id is not None:
            result['TargetResourceId'] = self.target_resource_id

        if self.target_resource_type is not None:
            result['TargetResourceType'] = self.target_resource_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AggregatorId') is not None:
            self.aggregator_id = m.get('AggregatorId')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('RelationType') is not None:
            self.relation_type = m.get('RelationType')

        if m.get('ResourceAccountId') is not None:
            self.resource_account_id = m.get('ResourceAccountId')

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('TargetResourceId') is not None:
            self.target_resource_id = m.get('TargetResourceId')

        if m.get('TargetResourceType') is not None:
            self.target_resource_type = m.get('TargetResourceType')

        return self

