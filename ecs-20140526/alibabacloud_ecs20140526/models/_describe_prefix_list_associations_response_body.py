# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecs20140526 import models as main_models
from darabonba.model import DaraModel

class DescribePrefixListAssociationsResponseBody(DaraModel):
    def __init__(
        self,
        next_token: str = None,
        prefix_list_associations: main_models.DescribePrefixListAssociationsResponseBodyPrefixListAssociations = None,
        request_id: str = None,
    ):
        # The query token that is returned in this call. If the return value is empty, no more data is returned.
        self.next_token = next_token
        # Details about the resources that are associated with the prefix list.
        self.prefix_list_associations = prefix_list_associations
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.prefix_list_associations:
            self.prefix_list_associations.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.prefix_list_associations is not None:
            result['PrefixListAssociations'] = self.prefix_list_associations.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('PrefixListAssociations') is not None:
            temp_model = main_models.DescribePrefixListAssociationsResponseBodyPrefixListAssociations()
            self.prefix_list_associations = temp_model.from_map(m.get('PrefixListAssociations'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribePrefixListAssociationsResponseBodyPrefixListAssociations(DaraModel):
    def __init__(
        self,
        prefix_list_association: List[main_models.DescribePrefixListAssociationsResponseBodyPrefixListAssociationsPrefixListAssociation] = None,
    ):
        self.prefix_list_association = prefix_list_association

    def validate(self):
        if self.prefix_list_association:
            for v1 in self.prefix_list_association:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['PrefixListAssociation'] = []
        if self.prefix_list_association is not None:
            for k1 in self.prefix_list_association:
                result['PrefixListAssociation'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.prefix_list_association = []
        if m.get('PrefixListAssociation') is not None:
            for k1 in m.get('PrefixListAssociation'):
                temp_model = main_models.DescribePrefixListAssociationsResponseBodyPrefixListAssociationsPrefixListAssociation()
                self.prefix_list_association.append(temp_model.from_map(k1))

        return self

class DescribePrefixListAssociationsResponseBodyPrefixListAssociationsPrefixListAssociation(DaraModel):
    def __init__(
        self,
        resource_id: str = None,
        resource_type: str = None,
    ):
        # The ID of the resource.
        self.resource_id = resource_id
        # The type of the resource.
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        return self

