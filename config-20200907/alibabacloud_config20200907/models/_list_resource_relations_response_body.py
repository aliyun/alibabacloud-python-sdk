# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_config20200907 import models as main_models
from darabonba.model import DaraModel

class ListResourceRelationsResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        resource_relations: main_models.ListResourceRelationsResponseBodyResourceRelations = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The result of the relationship.
        self.resource_relations = resource_relations

    def validate(self):
        if self.resource_relations:
            self.resource_relations.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.resource_relations is not None:
            result['ResourceRelations'] = self.resource_relations.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResourceRelations') is not None:
            temp_model = main_models.ListResourceRelationsResponseBodyResourceRelations()
            self.resource_relations = temp_model.from_map(m.get('ResourceRelations'))

        return self

class ListResourceRelationsResponseBodyResourceRelations(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        resource_relation_list: List[main_models.ListResourceRelationsResponseBodyResourceRelationsResourceRelationList] = None,
    ):
        # The maximum number of entries returned on each page.
        self.max_results = max_results
        # The token that was used to initiate the next request.
        self.next_token = next_token
        # An array that contains the relationships.
        self.resource_relation_list = resource_relation_list

    def validate(self):
        if self.resource_relation_list:
            for v1 in self.resource_relation_list:
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

        result['ResourceRelationList'] = []
        if self.resource_relation_list is not None:
            for k1 in self.resource_relation_list:
                result['ResourceRelationList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        self.resource_relation_list = []
        if m.get('ResourceRelationList') is not None:
            for k1 in m.get('ResourceRelationList'):
                temp_model = main_models.ListResourceRelationsResponseBodyResourceRelationsResourceRelationList()
                self.resource_relation_list.append(temp_model.from_map(k1))

        return self

class ListResourceRelationsResponseBodyResourceRelationsResourceRelationList(DaraModel):
    def __init__(
        self,
        account_id: int = None,
        relation_type: str = None,
        source_resource_id: str = None,
        source_resource_region_id: str = None,
        source_resource_type: str = None,
        target_resource_id: str = None,
        target_resource_type: str = None,
    ):
        # The ID of the Alibaba Cloud account to which the resource belongs.
        self.account_id = account_id
        # The type of the relationship between the resource and the object.
        # 
        # Valid values:
        # 
        # *   IsContained: The object is included as part of the resource.
        # *   IsAttachedTo: The object is added to the resource.
        # *   IsAssociatedIn: The object is associated with the resource.
        # *   Contains: The object contains the resource.
        self.relation_type = relation_type
        # The resource ID.
        self.source_resource_id = source_resource_id
        # The ID of the region in which the resource resides.
        self.source_resource_region_id = source_resource_region_id
        # The type of the resource.
        self.source_resource_type = source_resource_type
        # The ID of the associated resource.
        self.target_resource_id = target_resource_id
        # The type of the associated resource.
        self.target_resource_type = target_resource_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_id is not None:
            result['AccountId'] = self.account_id

        if self.relation_type is not None:
            result['RelationType'] = self.relation_type

        if self.source_resource_id is not None:
            result['SourceResourceId'] = self.source_resource_id

        if self.source_resource_region_id is not None:
            result['SourceResourceRegionId'] = self.source_resource_region_id

        if self.source_resource_type is not None:
            result['SourceResourceType'] = self.source_resource_type

        if self.target_resource_id is not None:
            result['TargetResourceId'] = self.target_resource_id

        if self.target_resource_type is not None:
            result['TargetResourceType'] = self.target_resource_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')

        if m.get('RelationType') is not None:
            self.relation_type = m.get('RelationType')

        if m.get('SourceResourceId') is not None:
            self.source_resource_id = m.get('SourceResourceId')

        if m.get('SourceResourceRegionId') is not None:
            self.source_resource_region_id = m.get('SourceResourceRegionId')

        if m.get('SourceResourceType') is not None:
            self.source_resource_type = m.get('SourceResourceType')

        if m.get('TargetResourceId') is not None:
            self.target_resource_id = m.get('TargetResourceId')

        if m.get('TargetResourceType') is not None:
            self.target_resource_type = m.get('TargetResourceType')

        return self

