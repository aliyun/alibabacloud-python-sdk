# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetAggregateResourceCountsGroupByResourceTypeRequest(DaraModel):
    def __init__(
        self,
        aggregator_id: str = None,
        folder_id: str = None,
        region: str = None,
        resource_account_id: int = None,
        resource_owner_id: int = None,
    ):
        # This parameter is required.
        self.aggregator_id = aggregator_id
        self.folder_id = folder_id
        self.region = region
        self.resource_account_id = resource_account_id
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.aggregator_id is not None:
            result['AggregatorId'] = self.aggregator_id

        if self.folder_id is not None:
            result['FolderId'] = self.folder_id

        if self.region is not None:
            result['Region'] = self.region

        if self.resource_account_id is not None:
            result['ResourceAccountId'] = self.resource_account_id

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AggregatorId') is not None:
            self.aggregator_id = m.get('AggregatorId')

        if m.get('FolderId') is not None:
            self.folder_id = m.get('FolderId')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('ResourceAccountId') is not None:
            self.resource_account_id = m.get('ResourceAccountId')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        return self

