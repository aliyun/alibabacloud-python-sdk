# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_resourcecenter20221201 import models as main_models
from darabonba.model import DaraModel

class ListResourceRelationshipsResponseBody(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        resource_relationships: List[main_models.ListResourceRelationshipsResponseBodyResourceRelationships] = None,
    ):
        self.max_results = max_results
        self.next_token = next_token
        self.request_id = request_id
        self.resource_relationships = resource_relationships

    def validate(self):
        if self.resource_relationships:
            for v1 in self.resource_relationships:
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

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['ResourceRelationships'] = []
        if self.resource_relationships is not None:
            for k1 in self.resource_relationships:
                result['ResourceRelationships'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.resource_relationships = []
        if m.get('ResourceRelationships') is not None:
            for k1 in m.get('ResourceRelationships'):
                temp_model = main_models.ListResourceRelationshipsResponseBodyResourceRelationships()
                self.resource_relationships.append(temp_model.from_map(k1))

        return self

class ListResourceRelationshipsResponseBodyResourceRelationships(DaraModel):
    def __init__(
        self,
        region_id: str = None,
        related_resource_id: str = None,
        related_resource_region_id: str = None,
        related_resource_type: str = None,
        resource_id: str = None,
        resource_type: str = None,
    ):
        self.region_id = region_id
        self.related_resource_id = related_resource_id
        self.related_resource_region_id = related_resource_region_id
        self.related_resource_type = related_resource_type
        self.resource_id = resource_id
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.related_resource_id is not None:
            result['RelatedResourceId'] = self.related_resource_id

        if self.related_resource_region_id is not None:
            result['RelatedResourceRegionId'] = self.related_resource_region_id

        if self.related_resource_type is not None:
            result['RelatedResourceType'] = self.related_resource_type

        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RelatedResourceId') is not None:
            self.related_resource_id = m.get('RelatedResourceId')

        if m.get('RelatedResourceRegionId') is not None:
            self.related_resource_region_id = m.get('RelatedResourceRegionId')

        if m.get('RelatedResourceType') is not None:
            self.related_resource_type = m.get('RelatedResourceType')

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        return self

