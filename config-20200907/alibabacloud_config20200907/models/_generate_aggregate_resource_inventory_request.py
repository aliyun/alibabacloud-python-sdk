# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GenerateAggregateResourceInventoryRequest(DaraModel):
    def __init__(
        self,
        account_ids: str = None,
        aggregator_id: str = None,
        regions: str = None,
        resource_deleted: int = None,
        resource_types: str = None,
    ):
        # The IDs of member accounts in the account group. Separate multiple member account IDs with commas (,).
        self.account_ids = account_ids
        # The ID of the account group.
        # 
        # This parameter is required.
        self.aggregator_id = aggregator_id
        # The IDs of the regions to which the resources belong. Separate multiple region IDs with commas (,).
        self.regions = regions
        # Indicates whether the resource is deleted. Valid values:
        # 
        # *   1 (default): The resource is retained.
        # *   0: The resource is deleted.
        self.resource_deleted = resource_deleted
        # The resource types. Separate multiple resource types with commas (,).
        self.resource_types = resource_types

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_ids is not None:
            result['AccountIds'] = self.account_ids

        if self.aggregator_id is not None:
            result['AggregatorId'] = self.aggregator_id

        if self.regions is not None:
            result['Regions'] = self.regions

        if self.resource_deleted is not None:
            result['ResourceDeleted'] = self.resource_deleted

        if self.resource_types is not None:
            result['ResourceTypes'] = self.resource_types

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountIds') is not None:
            self.account_ids = m.get('AccountIds')

        if m.get('AggregatorId') is not None:
            self.aggregator_id = m.get('AggregatorId')

        if m.get('Regions') is not None:
            self.regions = m.get('Regions')

        if m.get('ResourceDeleted') is not None:
            self.resource_deleted = m.get('ResourceDeleted')

        if m.get('ResourceTypes') is not None:
            self.resource_types = m.get('ResourceTypes')

        return self

