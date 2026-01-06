# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListProtectedResourcesRequest(DaraModel):
    def __init__(
        self,
        created_by_product: str = None,
        max_results: int = None,
        next_token: str = None,
        resource_id: str = None,
        skip: int = None,
        source_type: str = None,
    ):
        self.created_by_product = created_by_product
        self.max_results = max_results
        self.next_token = next_token
        self.resource_id = resource_id
        self.skip = skip
        self.source_type = source_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.created_by_product is not None:
            result['CreatedByProduct'] = self.created_by_product

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        if self.skip is not None:
            result['Skip'] = self.skip

        if self.source_type is not None:
            result['SourceType'] = self.source_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatedByProduct') is not None:
            self.created_by_product = m.get('CreatedByProduct')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('Skip') is not None:
            self.skip = m.get('Skip')

        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')

        return self

