# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_resourcecenter20221201 import models as main_models
from darabonba.model import DaraModel

class ListMultiAccountResourceRelationshipsRequest(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        region_id: str = None,
        related_resource_filter: List[main_models.ListMultiAccountResourceRelationshipsRequestRelatedResourceFilter] = None,
        resource_id: str = None,
        resource_type: str = None,
        scope: str = None,
    ):
        self.max_results = max_results
        self.next_token = next_token
        # This parameter is required.
        self.region_id = region_id
        self.related_resource_filter = related_resource_filter
        # This parameter is required.
        self.resource_id = resource_id
        # This parameter is required.
        self.resource_type = resource_type
        # This parameter is required.
        self.scope = scope

    def validate(self):
        if self.related_resource_filter:
            for v1 in self.related_resource_filter:
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

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        result['RelatedResourceFilter'] = []
        if self.related_resource_filter is not None:
            for k1 in self.related_resource_filter:
                result['RelatedResourceFilter'].append(k1.to_map() if k1 else None)

        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.scope is not None:
            result['Scope'] = self.scope

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        self.related_resource_filter = []
        if m.get('RelatedResourceFilter') is not None:
            for k1 in m.get('RelatedResourceFilter'):
                temp_model = main_models.ListMultiAccountResourceRelationshipsRequestRelatedResourceFilter()
                self.related_resource_filter.append(temp_model.from_map(k1))

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('Scope') is not None:
            self.scope = m.get('Scope')

        return self

class ListMultiAccountResourceRelationshipsRequestRelatedResourceFilter(DaraModel):
    def __init__(
        self,
        key: str = None,
        match_type: str = None,
        value: List[str] = None,
    ):
        self.key = key
        self.match_type = match_type
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

        if self.match_type is not None:
            result['MatchType'] = self.match_type

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('MatchType') is not None:
            self.match_type = m.get('MatchType')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

